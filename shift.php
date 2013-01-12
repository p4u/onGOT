<BODY BGCOLOR="#f4eda0">
<?php
require('config.inc.php');

echo "<h3>Shift</h3>\n";
echo "<hr>\n";

echo  "<form action='shiftUpdate.php' method='post'>\n";
echo "<table><tbody>\n";

$DBlink = mysql_connect($DBhost,$DBuser,$DBpass)
	or die('Could not connect: ' . mysql_error());

mysql_select_db($DBname,$DBlink)
	or die('Could not select database' .  mysql_error());

$query="SELECT actshift from shift";
$result = mysql_query($query,$DBlink); 
$row = mysql_fetch_array($result, MYSQL_NUM);
mysql_free_result($result);

echo "\t<tr><td><b>Actual Shift:</b></td>\n";
echo "\t<td><INPUT type='text' size='2' maxlenght='2' name='actshift' value='$row[0]'></td>\n";
echo "</tr></tbody></table>\n";
echo "<p><input type=\"submit\" value=\"Update\"></form></p>\n";

?>
