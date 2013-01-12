<BODY BGCOLOR="#f4eda0">
<?php
require("config.inc.php");

echo "<h3>Rankings</h3>\n";
echo "<hr>\n";
echo  "<form action='rankingsUpdate.php' method='post'>\n";

$DBlink = mysql_connect($DBhost,$DBuser,$DBpass)
	or die('Could not connect: ' . mysql_error());

mysql_select_db($DBname,$DBlink)
	or die('Could not select database' .  mysql_error());

echo "<table><tbody align='center'>\n";
echo "<tr><td></td>\n";
echo "<td><p style='font-size: small;'>IronThrone</p></td>\n";
echo "<td><p style='font-size: small;'>Fiefdoms</p></td>\n";
echo "<td><p style='font-size: small;'>KingsCourt</p></td>\n";

foreach ($Houses as &$h)
	{
	$query = "SELECT iron,fiefdoms,court from rankings where name='$h'";
	$result = mysql_query($query,$DBlink) 
	        or die('Cannot select: ' . mysql_error());
	$row = mysql_fetch_array($result, MYSQL_NUM);

	echo "<tr><td><b>$h</b></td>\n";
	echo "\t<td><INPUT type='text' name='${h}i' value='$row[0]' size='1' maxlenght='1'></td>\n";
	echo "\t<td><INPUT type='text' name='${h}f' value='$row[1]' size='1' maxlenght='1'></td>\n";
	echo "\t<td><INPUT type='text' name='${h}k' value='$row[2]' size='1' maxlenght='1'></td>\n";
	echo "</tr>\n";
	}

echo "</tbody></table>\n";
echo "<p><input type=\"submit\" value=\"Update\"></form></p>\n";


?>
</BODY>
