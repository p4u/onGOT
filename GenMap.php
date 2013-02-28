<?php
require("config.inc.php");

function barrels()
	{
	global $Houses;
	global $DBlink;
	global $pipes;
	global $BarrelsLimit;

	echo "<h5>Inserting Barrels...</h5>\n";
	
	foreach( $Houses as &$h )
		{
		$query="SELECT num FROM barrels WHERE house='$h'";
		$result = mysql_query($query,$DBlink) 
			or die('Cannot select: ' . mysql_error());
		
		$barrelsCount = mysql_fetch_array($result, MYSQL_NUM);
		mysql_free_result($result);
		
		if( $barrelsCount[0] >= $BarrelsLimit[0] and $barrelsCount[0] <= $BarrelsLimit[1] ) 
			{
			$cmd = "barrel $h $barrelsCount[0]\n";
			fwrite($pipes[0],$cmd);
			}
		else
			echo "Invalid barrel index: $barrelsCount[0]<br/>\n";
			
		}

	unset($h);
	}

function close()
	{
	global $process;
	global $pipes;
	global $GenMapPy;

	echo "<h5>Clossing process and making image...</h5>\n";

	fwrite($pipes[0],"write $GenMapPy\n");
	fwrite($pipes[0],"exit\n");
	fclose($pipes[0]);

	echo "<b>Process std output:</b>\n";
	echo "<pre>";
	echo stream_get_contents($pipes[1]);
	echo "</pre>\n";
	fclose($pipes[1]);
	
	echo "<b>Process err output:</b>\n";
	echo "<pre>";
	echo stream_get_contents($pipes[2]);
	echo "</pre>\n";

	fclose($pipes[2]);

	proc_close($process);
	}


function rankings()
	{
	global $Houses;
	global $DBlink;
	global $pipes;	
	global $RankingLimit;

	echo "<h5>Inserting Rankings...</h5>\n";

	$RL = $RankingLimit;

	foreach( $Houses as &$h )
		{
		$query="SELECT iron,fiefdoms,court FROM rankings WHERE name='$h'";
		$result = mysql_query($query,$DBlink)
			or die('Cannot select: ' . mysql_error());
		$rank = mysql_fetch_array($result, MYSQL_NUM);
		mysql_free_result($result);

		if( $rank[0] >= $RL[0] and $rank[0] <= $RL[1] ) {	
			$cmd = "power $h IronThrone$rank[0]\n";
			fwrite($pipes[0],$cmd);
			}
		else
			echo "IronThrone $h not valid: $rank[0]<br/>\n";

		if( $rank[1] >= $RL[0] and $rank[1] <= $RL[1] ) {
			$cmd = "power $h Fiefdoms$rank[1]\n";
			fwrite($pipes[0],$cmd);
			}
		else
			echo "Fiefdoms $h not valid: $rank[1]<br/>\n";

		if( $rank[2] >= $RL[0] and $rank[2] <= $RL[1] ) {
			$cmd = "power $h KingsCourt$rank[2]\n";
			fwrite($pipes[0],$cmd);
			}
		else
			echo "KingsCourt $h not valid: $rank[2]<br/>\n";

		}
	
	unset($h);

	}

function shift()
	{
	global $DBlink;
	global $pipes;
	global $ShiftLimit;

	echo "<h5>Inserting Shift...</h5>\n";

	$query="SELECT actshift FROM shift";
	$result = mysql_query($query,$DBlink)
		or die('Cannot select: ' . mysql_error());
	$shift = mysql_fetch_array($result, MYSQL_NUM);
	mysql_free_result($result);

	if ( $shift[0] >= $ShiftLimit[0] and $shift[0] <= $ShiftLimit[1])
		{
		$cmd = "chip Shift Shift$shift[0]\n";
		fwrite($pipes[0],$cmd);
		}
	else
		echo "Invalid shift index: $shift[0]<br/>\n";

	}


function wildling()
	{
	global $DBlink;
	global $pipes;

	echo "<h5>Inserting Wildling strong...</h5>\n";
	$query="SELECT wildlingstrong FROM wildling";
	$result = mysql_query($query,$DBlink)
		or die('Cannot select: ' . mysql_error());
	$wildling = mysql_fetch_array($result, MYSQL_NUM);
	mysql_free_result($result);

	$cmd = "chip Wildling Wildling$wildling[0]\n";
	fwrite($pipes[0],$cmd);
	}

function query($Q)
	{
	/*
	Returns the query results. 
	returnvalue[i][j] -> i for rows, j for fields 
	returnvalue[0][0] is first row first field
	*/
	global $DBlink;
	$row = array();

	$result = mysql_query($Q,$DBlink)
		or die('Cannot select: ' . mysql_error());
	
	$row = mysql_fetch_array($result, MYSQL_NUM);
	$i=0;

	while($row)
		{
		$retquery[$i] = $row;
		$row = mysql_fetch_array($result, MYSQL_NUM);
		$i++;
		}

	mysql_free_result($result);
	
	return $retquery;
	}


function regions()
	{
	global $pipes;

	echo "<h5>Inserting Region icons...</h5>\n";
	
	$regions = query("SELECT name FROM regions");

	foreach( $regions as &$R )
		{
		global $Troops;
		$actReg = $R[0];
		
		$house = query("SELECT house FROM regions where name='$actReg'");
		$house = $house[0][0];
	
		if ($house != "nobody")
			{

			//----------------
			//INSERTING TROOPS
			//----------------
			$tC = 0;
			$troopsArray = $Troops;
			$troopsQuery = $troopsArray[0];
			
			$first = 1;
			foreach ( $troopsArray as &$T ) { if ( ! $first) $troopsQuery = "$troopsQuery,$T"; else $first = 0;  }
			$troops = query("SELECT $troopsQuery FROM regions where name='$actReg'");
			
			foreach( $troops[0] as &$T )
				{
				if( $T > 0 )
					{
					$cmd = "troop $house $actReg $troopsArray[$tC] $T\n";
					fwrite($pipes[0],$cmd);
					}
				$tC++;	
				}

			//---------------
			//INSERTING TOKEN
			//---------------
			$token = query("SELECT power FROM regions WHERE name='$actReg'");
			$token = $token[0][0];
			if($token)
				{
				$cmd = "power $house $actReg\n";
				fwrite($pipes[0],$cmd);
				}

			//---------------
			//INSERTING ORDER
			//---------------
			$order = query("SELECT ord FROM regions WHERE name='$actReg'");
			$order = $order[0][0];
			if ($order != "none")
				{
				if(strstr($order,"March")) {
					$ord = "March";
					$mode = substr($order,5);
					}
				else if(strstr($order,"Support")) {
					$ord = "Support";
					$mode = substr($order,7);
					}
				else if(strstr($order,"Defense")) {
					$ord = "Defense";
					$mode = substr($order,7);
					}
				else if(strstr($order,"Consolide")) {
					$ord = "Consolide";
					$mode = substr($order,9);
					}
				else if(strstr($order,"Raid")) {
					$ord = "Raid";
					$mode = substr($order,4);
					}
	
				$cmd = "order $actReg $ord $mode\n";
				fwrite($pipes[0],$cmd);
				}

			}
		
		}
	unset($R);
	}

$descriptor = array(
	0 => array("pipe", "r"),  
	1 => array("pipe", "w"), 
	2 => array("pipe", "w") 
	);

$cwd = $PythonDir;
$cmd = $PythonExec;
$process = proc_open($cmd, $descriptor, $pipes, $cwd, NULL);

if ( is_resource($process)) 
	{
	echo "<h1>Generate Map</h1>\n";
	$DBlink = mysql_connect($DBhost,$DBuser,$DBpass)
		or die('Could not connect: ' . mysql_error());

	mysql_select_db($DBname,$DBlink)
		or die('Could not select database' .  mysql_error());

	barrels();
	rankings();
	shift();
	wildling();
	regions();
	close();
	echo "<p>[Done]</p>";
	echo "<form action='Map.php'><input type='submit' value='Back'></form>";
	}
?>

