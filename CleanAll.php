<?php
require('config.inc.php');

if( $_POST['confirm'] == "yes" ) {
	echo "<h3>Cleaning Map image</h3>\n";

	//Copy original map
	copy($Map,$GenMap);
	
	// Check for mysql connection
	$DBlink = mysql_connect($DBhost,$DBuser,$DBpass)
	    or die('Could not connect: ' . mysql_error());
	
	echo "<h3>Generating backup</h3>\n";
	exec("mysqldump -u ".$DBuser." --password=".$DBpass." ".$DBname." > ".$SQLbackupFile);
	echo "Backup generated <a href='".$SQLbackupFile."'>".$SQLbackupFile."</a>";
	
	echo "<h3>Cleaning database</h3>\n";
	exec("mysql -u ".$DBuser." --password=".$DBpass." ".$DBname." < ".$SQLinsertFile);
	
	echo "<p>[Done]</p>\n";
} else {
	echo "<h3>Clean all confirmation</h3>";
	echo "<p>This will destroy all the current data stored in the database and also the map image. All values will be restored.</p>\n";
	echo "<p>To confirm write yes in the textbox</p>";
	echo "<form method='POST' action='CleanAll.php'><input type='text' name='confirm' size=3><input type='submit' value='remove all data'></form>\n";
}
echo "<form action='Map.php'><input type='submit' value='Back'></form>\n";

?>
