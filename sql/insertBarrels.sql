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

