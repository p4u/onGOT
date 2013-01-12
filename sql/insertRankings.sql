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

