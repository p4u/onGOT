<HEAD>
<SCRIPT language="JavaScript">
        function getRandom()
        	{
		var ranNum= Math.floor(Math.random()*10+1);
		alert(ranNum);
		}
</SCRIPT>
</HEAD>

<BODY>

<h1>Game of Throns</h3>

<TABLE><TBODY><TR>
<TD><FORM action="GenMap.php">
<INPUT type="submit" value="GenMap">
</FORM></TD>

<TD><FORM action="Instructions.html">
<INPUT type="submit" value="Instructions">
</FORM></TD>

<TD><FORM action="CleanAll.php">
<INPUT type="submit" value="CleanAll">
</FORM></TD>

<TD><FORM>
<INPUT type="button" value="GenRandom" onClick="getRandom()">
</FORM></TD>
</TBODY></TABLE>


<?php
require("config.inc.php");

$DBlink = mysql_connect($DBhost,$DBuser,$DBpass)
	or die('Could not connect: ' . mysql_error());

mysql_select_db($DBname,$DBlink)
	or die('Could not select database' .  mysql_error());

$query = "SELECT name,posx,posy from regionpos";
$result = mysql_query($query,$DBlink) 
	or die('Cannot select: ' . mysql_error());

echo "<img src=\"$GenMap\" usemap=\"#tronosmap\">\n";
echo "\t<map name=\"tronosmap\">\n";

$row = mysql_fetch_array($result, MYSQL_NUM);
while ($row) {
	echo "\t<area shape=\"circle\" coords=\"$row[1],$row[2],20\" href=\"region.php?q=$row[0]\" \n";	
	echo "\t\t onClick=\"window.open(this.href, this.target,'width=250,height=450'); return false;\">\n";
	$row = mysql_fetch_array($result, MYSQL_NUM);
	}

$query = "SELECT name,a,b,c,d from areas";
$result = mysql_query($query,$DBlink)
        or die('Cannot select: ' . mysql_error());

$row = mysql_fetch_array($result, MYSQL_NUM);
while ($row) {
	echo "\t<area shape='rect' coords='$row[1],$row[2],$row[3],$row[4]' href='$row[0].php'\n";
	echo "\t\t onClick=\"window.open(this.href, this.target,'width=350,height=450'); return false;\">\n";
	$row = mysql_fetch_array($result, MYSQL_NUM);
	}

echo "</map>\n";

/*
<img src="MapaBase.jpeg" usemap="#tronosmap">

<map name="tronosmap">
	<area shape="circle" coords="750,760,20" href="region.php?q=Castleblack" 
		onClick="window.open(this.href, this.target, 'width=300,height=450'); return false;"">
</map>
*/
?>
</BODY>
