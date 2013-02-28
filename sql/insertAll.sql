DROP TABLE IF EXISTS areas;

CREATE TABLE areas(
	id integer NOT NULL auto_increment,
	name char(20), 
	a integer, 
	b integer, 
	c integer, 
	d integer, 
KEY id (id)) AUTO_INCREMENT=1;


INSERT INTO areas(name,a,b,c,d) VALUES('rankings',21,23,1164,253);
INSERT INTO areas(name,a,b,c,d) VALUES('shift',26,275,248,584);
INSERT INTO areas(name,a,b,c,d) VALUES('barrels',267,278,1159,582);
INSERT INTO areas(name,a,b,c,d) VALUES('wildling',382,609,718,705);


DROP TABLE IF EXISTS barrels;

CREATE TABLE barrels(
	id integer NOT NULL auto_increment, 		
	house char(20), 
	num integer default 0, 
	KEY id (id)) 
AUTO_INCREMENT=1;

INSERT INTO barrels(house) VALUES('Stark');
INSERT INTO barrels(house) VALUES('Lannister');
INSERT INTO barrels(house) VALUES('Targaryen');
INSERT INTO barrels(house) VALUES('Greyjoy');
INSERT INTO barrels(house) VALUES('Baratheon');
INSERT INTO barrels(house) VALUES('Tully');
INSERT INTO barrels(house) VALUES('Arryn');
INSERT INTO barrels(house) VALUES('Martell');
INSERT INTO barrels(house) VALUES('Tyrell');

DROP TABLE IF EXISTS rankings;

CREATE TABLE rankings(
    id integer NOT NULL auto_increment,
    name char(20), 
    iron integer default 0,
    fiefdoms integer default 0,
    court integer default 0,
    KEY id (id)) AUTO_INCREMENT=1;

INSERT INTO rankings(name) VALUES('Stark');
INSERT INTO rankings(name) VALUES('Lannister');
INSERT INTO rankings(name) VALUES('Targaryen');
INSERT INTO rankings(name) VALUES('Greyjoy');
INSERT INTO rankings(name) VALUES('Baratheon');
INSERT INTO rankings(name) VALUES('Tully');
INSERT INTO rankings(name) VALUES('Arryn');
INSERT INTO rankings(name) VALUES('Martell');
INSERT INTO rankings(name) VALUES('Tyrell');

DROP TABLE IF EXISTS regionpos;

CREATE TABLE regionpos(
	id integer NOT NULL auto_increment, 
	name char(40), 
	posx integer, 
	posy integer, 
	KEY id (id)) 
AUTO_INCREMENT=1;

INSERT INTO regionpos(name,posx,posy) values('Barrowlands',518, 1335);
INSERT INTO regionpos(name,posx,posy) values('BayOfIce',135, 915);
INSERT INTO regionpos(name,posx,posy) values('Bitterbridge',600, 2322);
INSERT INTO regionpos(name,posx,posy) values('Blackwater',595, 2207);
INSERT INTO regionpos(name,posx,posy) values('BlackwaterBay',877, 2166);
INSERT INTO regionpos(name,posx,posy) values('BlazewaterBay',145, 1468);
INSERT INTO regionpos(name,posx,posy) values('BloodyGate',843, 1930);
INSERT INTO regionpos(name,posx,posy) values('CapeWrath',925, 2480);
INSERT INTO regionpos(name,posx,posy) values('CasterlyRock',292, 1968);
INSERT INTO regionpos(name,posx,posy) values('Castleblack',750, 760);
INSERT INTO regionpos(name,posx,posy) values('CiderHall',456, 2343);
INSERT INTO regionpos(name,posx,posy) values('CrackclawPoint',958, 1988);
INSERT INTO regionpos(name,posx,posy) values('Deepwood',536, 1056);
INSERT INTO regionpos(name,posx,posy) values('DeepwoodPort',472, 982);
INSERT INTO regionpos(name,posx,posy) values('DornishMarches',463, 2488);
INSERT INTO regionpos(name,posx,posy) values('Dragonstone',1072, 2081);
INSERT INTO regionpos(name,posx,posy) values('DragonstonePort',1032, 2200);
INSERT INTO regionpos(name,posx,posy) values('Duskendale',770, 2064);
INSERT INTO regionpos(name,posx,posy) values('EastSummerSea',1036, 2896);
INSERT INTO regionpos(name,posx,posy) values('FlintsFinger',250, 1547);
INSERT INTO regionpos(name,posx,posy) values('GoldenTooth',433, 1973);
INSERT INTO regionpos(name,posx,posy) values('Goldroad',533, 2040);
INSERT INTO regionpos(name,posx,posy) values('GreywaterWatch',414, 1529);
INSERT INTO regionpos(name,posx,posy) values('Gulltown',959, 1892);
INSERT INTO regionpos(name,posx,posy) values('GulltownPort',1058, 1846);
INSERT INTO regionpos(name,posx,posy) values('Harrenhal',635, 2014);
INSERT INTO regionpos(name,posx,posy) values('Highgarden',335, 2363);
INSERT INTO regionpos(name,posx,posy) values('IronmansBay',266, 1656);
INSERT INTO regionpos(name,posx,posy) values('Karhold',930, 977);
INSERT INTO regionpos(name,posx,posy) values('KingsLanding',714, 2219);
INSERT INTO regionpos(name,posx,posy) values('KingsLandingPort',786, 2183);
INSERT INTO regionpos(name,posx,posy) values('Kingsroad',614, 887);
INSERT INTO regionpos(name,posx,posy) values('Kingswood',892, 2273);
INSERT INTO regionpos(name,posx,posy) values('Lannisport',331, 2130);
INSERT INTO regionpos(name,posx,posy) values('LannisportPort',224, 2106);
INSERT INTO regionpos(name,posx,posy) values('Maidenpool',764, 2006);
INSERT INTO regionpos(name,posx,posy) values('MoatCailin',596, 1450);
INSERT INTO regionpos(name,posx,posy) values('Oldtown',262, 2547);
INSERT INTO regionpos(name,posx,posy) values('OldtownPort',179, 2590);
INSERT INTO regionpos(name,posx,posy) values('PrincesPass',494, 2664);
INSERT INTO regionpos(name,posx,posy) values('Pyke',274, 1760);
INSERT INTO regionpos(name,posx,posy) values('PykePort',197, 1826);
INSERT INTO regionpos(name,posx,posy) values('RedwyneStraights',162, 2687);
INSERT INTO regionpos(name,posx,posy) values('Riverrun',545, 1894);
INSERT INTO regionpos(name,posx,posy) values('Roseroad',737, 2357);
INSERT INTO regionpos(name,posx,posy) values('SaltShore',776, 2807);
INSERT INTO regionpos(name,posx,posy) values('SeaOfDorne',824, 2615);
INSERT INTO regionpos(name,posx,posy) values('Seagard',506, 1704);
INSERT INTO regionpos(name,posx,posy) values('SeagardPort',410, 1650);
INSERT INTO regionpos(name,posx,posy) values('SearoadMarches',318, 2197);
INSERT INTO regionpos(name,posx,posy) values('ShipbrfakerBay',1112, 2284);
INSERT INTO regionpos(name,posx,posy) values('Starfall',492, 2754);
INSERT INTO regionpos(name,posx,posy) values('StoneySept',477, 2154);
INSERT INTO regionpos(name,posx,posy) values('StormsEnd',808, 2464);
INSERT INTO regionpos(name,posx,posy) values('SunsetSea',88, 2241);
INSERT INTO regionpos(name,posx,posy) values('Sunspear',898, 2744);
INSERT INTO regionpos(name,posx,posy) values('SunspearPort',1024, 2738);
INSERT INTO regionpos(name,posx,posy) values('Tarth',1026, 2332);
INSERT INTO regionpos(name,posx,posy) values('TheArbor',158, 2783);
INSERT INTO regionpos(name,posx,posy) values('TheBite',796, 1530);
INSERT INTO regionpos(name,posx,posy) values('TheBoneway',614, 2594);
INSERT INTO regionpos(name,posx,posy) values('TheDreadfort',822, 1134);
INSERT INTO regionpos(name,posx,posy) values('TheEyrie',844, 1858);
INSERT INTO regionpos(name,posx,posy) values('TheFingers',818, 1690);
INSERT INTO regionpos(name,posx,posy) values('TheGoldenSound',174, 2020);
INSERT INTO regionpos(name,posx,posy) values('TheMountainsOfTheMoon',716, 1810);
INSERT INTO regionpos(name,posx,posy) values('TheNarrowSea',1085, 1532);
INSERT INTO regionpos(name,posx,posy) values('TheShimeringSea',1061, 1196);
INSERT INTO regionpos(name,posx,posy) values('TheStoneyShore',329, 1271);
INSERT INTO regionpos(name,posx,posy) values('TheTrident',640, 1904);
INSERT INTO regionpos(name,posx,posy) values('TheTwins',630, 1661);
INSERT INTO regionpos(name,posx,posy) values('TheVale',964, 1745);
INSERT INTO regionpos(name,posx,posy) values('ThreeTowers',323, 2705);
INSERT INTO regionpos(name,posx,posy) values('Tumblestone',390, 1885);
INSERT INTO regionpos(name,posx,posy) values('WestSummerSea',212, 2906);
INSERT INTO regionpos(name,posx,posy) values('WidowsWatch',870, 1331);
INSERT INTO regionpos(name,posx,posy) values('Winterfell',612, 1182);
INSERT INTO regionpos(name,posx,posy) values('WhiteHarbor',725, 1337);
INSERT INTO regionpos(name,posx,posy) values('WhiteHarborPort',731, 1452);
INSERT INTO regionpos(name,posx,posy) values('Yronwood',638, 2688);
DROP TABLE IF EXISTS regions;

CREATE TABLE regions(
	id integer NOT NULL auto_increment,
	name char(40) default "none", 
	house char(20) default "nobody",
	horse integer default 0, 
	soldier integer default 0, 
	boat integer default 0, 
	fort integer default 0, 
	siege integer default 0, 
	dragon integer default 0,
	direwolf integer default 0,
	clanman integer default 0,
	mercenary integer default 0,
	archer integer default 0,
	barcoluengo integer default 0,
	bastion integer default 0,
	sperman integer default 0,
	power bool default 0,  
	ord char(20) default "none",
	KEY id (id)) 
AUTO_INCREMENT=1;

INSERT INTO regions(name) values('Barrowlands');
INSERT INTO regions(name) values('BayOfIce');
INSERT INTO regions(name) values('Bitterbridge');
INSERT INTO regions(name) values('Blackwater');
INSERT INTO regions(name) values('BlackwaterBay');
INSERT INTO regions(name) values('BlazewaterBay');
INSERT INTO regions(name) values('BloodyGate');
INSERT INTO regions(name) values('CapeWrath');
INSERT INTO regions(name) values('CasterlyRock');
INSERT INTO regions(name) values('Castleblack');
INSERT INTO regions(name) values('CiderHall');
INSERT INTO regions(name) values('CrackclawPoint');
INSERT INTO regions(name) values('Deepwood');
INSERT INTO regions(name) values('DeepwoodPort');
INSERT INTO regions(name) values('DornishMarches');
INSERT INTO regions(name) values('Dragonstone');
INSERT INTO regions(name) values('DragonstonePort');
INSERT INTO regions(name) values('Duskendale');
INSERT INTO regions(name) values('EastSummerSea');
INSERT INTO regions(name) values('FlintsFinger');
INSERT INTO regions(name) values('GoldenTooth');
INSERT INTO regions(name) values('Goldroad');
INSERT INTO regions(name) values('GreywaterWatch');
INSERT INTO regions(name) values('Gulltown');
INSERT INTO regions(name) values('GulltownPort');
INSERT INTO regions(name) values('Harrenhal');
INSERT INTO regions(name) values('Highgarden');
INSERT INTO regions(name) values('IronmansBay');
INSERT INTO regions(name) values('Karhold');
INSERT INTO regions(name) values('KingsLanding');
INSERT INTO regions(name) values('KingsLandingPort');
INSERT INTO regions(name) values('Kingsroad');
INSERT INTO regions(name) values('Kingswood');
INSERT INTO regions(name) values('Lannisport');
INSERT INTO regions(name) values('LannisportPort');
INSERT INTO regions(name) values('Maidenpool');
INSERT INTO regions(name) values('MoatCailin');
INSERT INTO regions(name) values('Oldtown');
INSERT INTO regions(name) values('OldtownPort');
INSERT INTO regions(name) values('PrincesPass');
INSERT INTO regions(name) values('Pyke');
INSERT INTO regions(name) values('PykePort');
INSERT INTO regions(name) values('RedwyneStraights');
INSERT INTO regions(name) values('Riverrun');
INSERT INTO regions(name) values('Roseroad');
INSERT INTO regions(name) values('SaltShore');
INSERT INTO regions(name) values('SeaOfDorne');
INSERT INTO regions(name) values('Seagard');
INSERT INTO regions(name) values('SeagardPort');
INSERT INTO regions(name) values('SearoadMarches');
INSERT INTO regions(name) values('ShipbrfakerBay');
INSERT INTO regions(name) values('Starfall');
INSERT INTO regions(name) values('StoneySept');
INSERT INTO regions(name) values('StormsEnd');
INSERT INTO regions(name) values('SunsetSea');
INSERT INTO regions(name) values('Sunspear');
INSERT INTO regions(name) values('SunspearPort');
INSERT INTO regions(name) values('Tarth');
INSERT INTO regions(name) values('TheArbor');
INSERT INTO regions(name) values('TheBite');
INSERT INTO regions(name) values('TheBoneway');
INSERT INTO regions(name) values('TheDreadfort');
INSERT INTO regions(name) values('TheEyrie');
INSERT INTO regions(name) values('TheFingers');
INSERT INTO regions(name) values('TheGoldenSound');
INSERT INTO regions(name) values('TheMountainsOfTheMoon');
INSERT INTO regions(name) values('TheNarrowSea');
INSERT INTO regions(name) values('TheShimeringSea');
INSERT INTO regions(name) values('TheStoneyShore');
INSERT INTO regions(name) values('TheTrident');
INSERT INTO regions(name) values('TheTwins');
INSERT INTO regions(name) values('TheVale');
INSERT INTO regions(name) values('ThreeTowers');
INSERT INTO regions(name) values('Tumblestone');
INSERT INTO regions(name) values('WestSummerSea');
INSERT INTO regions(name) values('WidowsWatch');
INSERT INTO regions(name) values('Winterfell');
INSERT INTO regions(name) values('WhiteHarbor');
INSERT INTO regions(name) values('WhiteHarborPort');
INSERT INTO regions(name) values('Yronwood');
DROP TABLE IF EXISTS shift;
CREATE TABLE shift(actshift integer);
INSERT INTO shift(actshift) VALUES('0');

DROP TABLE IF EXISTS wildling;
CREATE TABLE wildling(wildlingstrong integer);
INSERT INTO wildling(wildlingstrong) VALUES('0');

