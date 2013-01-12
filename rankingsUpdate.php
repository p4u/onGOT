<BODY BGCOLOR="#f4eda0">
<?php
require("config.inc.php");

$DBlink = mysql_connect($DBhost,$DBuser,$DBpass)
	or die('Could not connect: ' . mysql_error());
mysql_select_db($DBname,$DBlink)
	or die('Could not select database' .  mysql_error());

foreach ($Houses as &$h)
	{
	$iron = $_POST["${h}i"];
	$fief = $_POST["${h}f"];
	$kings = $_POST["${h}k"];

	echo "<p>Inserting $h ... ";
	$query="UPDATE rankings SET iron='$iron',fiefdoms='$fief',court='$kings' ";
	$query=$query . "WHERE name='$h'";
	mysql_query($query,$DBlink) 
		or die('Cannot insert: ' . mysql_error());
	echo "ok</p>";
	}

unset($h);
?>

<form action="JavaScript:window.close()">
        <p><input type="submit" value="Close"></p>
</form>

</BODY>

