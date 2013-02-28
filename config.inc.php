<?
$DBhost = "127.0.0.1";
$DBuser = "Martin";
$DBpass = "WinterIsComming";
$DBname = "ongot";

// Original map path
$Map = "MapaBase.jpeg";

// Current map path
$GenMap = "../GameOfThrones.jpeg";

// Output map path relative to python script
$GenMapPy = "../../GameOfThrones.jpeg";

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

$Troops = array("Horse","Soldier",
       "Boat","Fort","Siege","Dragon",
       "Direwolf","Clanman","Archer","Mercenary",
       "Barcoluengo","Bastion","Sperman");

$Figures = array("house","power","ord");

$PythonDir = "pytronos";
$PythonExec = "./pytronos.py";

$BarrelsLimit = array(0,8);
$ShiftLimit = array(1,14);
$RankingLimit = array(1,9);
$WildlingLimit = array(0,18);

?>
