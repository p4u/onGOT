<?
$DBhost = "127.0.0.1";
$DBuser = "got_online";
$DBpass = "NedStark";
$DBname = "got_online";

// Original map path
$Map = "map/MapaBase.jpeg";

// Current map path
$GenMap = "map/GameOfThrones.jpeg";

// Output map path relative to python script
$GenMapPy = "../map/GameOfThrones.jpeg";

// File with the sql inserts
$SQLinsertFile = "sql/insertAll.sql";

// File to store the backup
$SQLbackupFile = "sql/backup.sql";

$Houses = array('Stark',
		'Lannister',
		'Baratheon',
		'Targaryen',
		'Greyjoy',
		'Tully',
		'Martell',
		'Tyrell',
		'Arryn');

$PythonDir = "/var/www/ongot/pytronos";
$PythonExec = "./pytronos.py";

$BarrelsLimit = array(0,8);
$ShiftLimit = array(1,14);
$RankingLimit = array(1,9);
$WildlingLimit = array(0,18);

?>
