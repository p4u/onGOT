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


