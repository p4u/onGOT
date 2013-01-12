<BODY BGCOLOR="#f4eda0">
<?
require("config.inc.php");

$DBlink = mysql_connect($DBhost,$DBuser,$DBpass)
	or die('Could not connect: ' . mysql_error());
mysql_select_db($DBname,$DBlink)
	or die('Could not select database' .  mysql_error());
	
foreach( $Houses as &$h )
	{
	$query="UPDATE barrels SET num='$_POST[$h]' WHERE house='$h'";
	mysql_query($query,$DBlink) 
		or die('Cannot select: ' . mysql_error());
	}
unset($h);
echo "<p>DONE</p>"
?>
<form action="JavaScript:window.close()">
        <p><input type="submit" value="Close"></p>
</form>

</BODY>
