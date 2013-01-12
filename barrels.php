<BODY BGCOLOR="#f4eda0">
<?php
require_once("config.inc.php");

echo "<h3>Supply</h3>\n";
echo "<hr>\n";
echo  "<form action='barrelsUpdate.php' method='post'>\n";
echo "<table><tbody>\n";

$DBlink = mysql_connect($DBhost,$DBuser,$DBpass)
	or die('Could not connect: ' . mysql_error());

mysql_select_db($DBname,$DBlink)
	or die('Could not select database' .  mysql_error());

foreach( $Houses as &$h )
	{
	$query = "SELECT num FROM barrels WHERE house='$h'";
	$result = mysql_query($query,$DBlink); 
	$row = mysql_fetch_array($result, MYSQL_NUM);
	mysql_free_result($result);
	
	echo "\t<tr><td><b>$h</b></td>";
	echo "\t\t<td><INPUT type='text' value='$row[0]' name='$h' size='1' maxlength='1'></td>";
	echo "\t</tr>";

	}
unset($h);

echo "</tbody></table>\n";
echo "<p><input type=\"submit\" value=\"Update\"></form></p>\n";

?>
</BODY>

