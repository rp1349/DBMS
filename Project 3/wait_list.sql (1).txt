-- Starting point of Wait List database

CREATE DATABASE IF NOT EXISTS wait_list;
USE wait_list;


CREATE TABLE IF NOT EXISTS student (
  netID char(8)  NOT NULL,
  firstname varchar(100)  NOT NULL,
  lastname varchar(100)  NOT NULL,
  class char(10)  NOT NULL,
  graduating varchar(1) NOT NULL,
  PRIMARY KEY (netID)
) ;

INSERT INTO student (netID, firstname, lastname, class, graduating) VALUES
('aec3', 'Amy', 'Cruise', 'junior', 0),
('am2', 'Amy', 'Moosey', 'senior', 1),
('cd911', 'Columbus', 'Dispatch', 'senior', 0),
('eec14', 'Emma', 'Cowden', 'senior', 1),
('hc23', 'Honda', 'Civic', 'junior', 0),
('jjc13', 'John', 'Crank', 'senior', 0),
('la790', 'LA', 'Times', 'senior', 1),
('sd1009', 'Starkville', 'Daily', 'freshman', 0),
('tc987', 'Toyota', 'Camry', 'senior', 0),
('tc1', 'Tom', 'Cruise', 'junior', 0),
('ts12', 'Taylor', 'Swift', 'sophmore', 0),
('ts2', 'Tim', 'Sanders', 'senior', 1),
('bbb55','Bob','Billings', 'junior', 0),
('wp4', 'Washington', 'Post', 'junior', 0);


CREATE TABLE IF NOT EXISTS curriculum (
  major varchar(100)  NOT NULL,
  year varchar(4) NOT NULL,
  PRIMARY KEY (major,year)
) ;

INSERT INTO curriculum (major, year) VALUES
('Computer Science', 2014),
('Computer Science', 2017),
('English', 2016),
('Music Education', 2013),
('Philosophy', 2013),
('English', 2014),
('Software Engineering', 2011),
('Software Engineering', 2017);


CREATE TABLE IF NOT EXISTS choose (
  netID char(8)  NOT NULL,
  major varchar(100)  NOT NULL,
  year varchar(4) NOT NULL,
  PRIMARY KEY (netID,major,year),
  FOREIGN KEY (netID) REFERENCES student (netID),
  FOREIGN KEY (major,year) REFERENCES curriculum (major, year)
) ;

INSERT INTO choose (netID, major, year) VALUES
('aec3', 'Computer Science', 2014),
('am2', 'English', 2016),
('am2', 'Software Engineering', 2011),
('eec14', 'Music Education', 2013),
('hc23', 'Computer Science', 2014),
('jjc13', 'Computer Science', 2014),
('la790', 'Computer Science', 2014),
('sd1009', 'English', 2016),
('tc987', 'Computer Science', 2014),
('tc987', 'Software Engineering', 2011),
('tc1', 'Software Engineering', 2011),
('ts12', 'Music Education', 2013),
('ts12', 'Philosophy', 2013),
('bbb55', 'English', 2014),
('ts2', 'Software Engineering', 2011),
('wp4', 'Computer Science', 2014);


CREATE TABLE IF NOT EXISTS course (
  symbol char(4)  NOT NULL,
  number char(4)  NOT NULL,
  cname varchar(100)  NOT NULL,
  PRIMARY KEY (symbol,number)
) ;

INSERT INTO course (symbol, number, cname) VALUES
('CSE', '1384', 'Intermediate Computer Programming'),
('CSE', '3324', 'DCSP'),
('CSE', '4214', 'Intro SW Eng'),
('CSE', '4503', 'Database'),
('CSE', '4713', 'Programming Languages'),
('ECE', '4713', 'Computer Architecture');


CREATE TABLE IF NOT EXISTS consists (
  major varchar(100)  NOT NULL,
  year varchar(4) NOT NULL,
  symbol char(4)  NOT NULL,
  number char(4)  NOT NULL,
  PRIMARY KEY (major,year,symbol,number),
  FOREIGN KEY (major,year) REFERENCES curriculum (major, year),
  FOREIGN KEY (symbol,number) REFERENCES course (symbol, number)
) ;

INSERT INTO consists (major, year, symbol, number) VALUES
('Computer Science', 2014, 'CSE', '1384'),
('Computer Science', 2014, 'CSE', '3324'),
('Computer Science', 2014, 'CSE', '4713'),
('Computer Science', 2014, 'ECE', '4713'),
('Computer Science', 2017, 'CSE', '1384'),
('Computer Science', 2017, 'CSE', '3324'),
('Computer Science', 2017, 'CSE', '4503'),
('Computer Science', 2017, 'CSE', '4713'),
('Computer Science', 2017, 'ECE', '4713'),
('Software Engineering', 2011, 'CSE', '1384'),
('Software Engineering', 2011, 'CSE', '3324'),
('Software Engineering', 2011, 'CSE', '4214'),
('Software Engineering', 2011, 'CSE', '4503'),
('Software Engineering', 2017, 'CSE', '1384'),
('Software Engineering', 2017, 'CSE', '3324'),
('Software Engineering', 2017, 'CSE', '4214'),
('Software Engineering', 2017, 'CSE', '4503');


CREATE TABLE IF NOT EXISTS location (
  building varchar(100)  NOT NULL,
  room char(5)  NOT NULL,
  capacity integer NOT NULL,
  PRIMARY KEY (building,room)
) ;

INSERT INTO location (building, room, capacity) VALUES
('Butler', '100', 5),
('Butler', '102', 2),
('Butler', '103', 3),
('Old Main', '2830', 6),
('Old Main', '3030', 3);


CREATE TABLE IF NOT EXISTS courseoffering_of (
  symbol char(4)  NOT NULL,
  number char(4)  NOT NULL,
  building varchar(100)  NOT NULL,
  room char(5)  NOT NULL,
  sectionNumber char(2)  NOT NULL,
  PRIMARY KEY (symbol,number,sectionNumber),
  FOREIGN KEY (symbol,number) REFERENCES course (symbol, number),
  FOREIGN KEY (building,room) REFERENCES location (building, room)
) ;

INSERT INTO courseoffering_of (symbol, number, building, room, sectionNumber) VALUES
('CSE', '4503', 'Butler', '100', '01'),
('CSE', '1384', 'Butler', '103', '01'),
('CSE', '1384', 'Butler', '103', '02'),
('ECE', '4713', 'Old Main', '2830', '01');


CREATE TABLE IF NOT EXISTS enrolled (
  netID char(8)  NOT NULL,
  symbol char(4)  NOT NULL,
  number char(4)  NOT NULL,
  sectionNumber char(2)  NOT NULL,
  PRIMARY KEY (netID,symbol,number,sectionNumber),
  FOREIGN KEY (netID) REFERENCES student (netID),
  FOREIGN KEY (symbol,number,sectionNumber) REFERENCES courseoffering_of (symbol, number, sectionNumber)
) ;


INSERT INTO enrolled (netID, symbol, number, sectionNumber) VALUES
('wp4','CSE','1384','01'),
('bbb55','CSE','1384','01'),
('jjc13','CSE','1384','01'),
('jjc13','CSE','4503','01'),
('la790','CSE','4503','01')
;


CREATE TABLE IF NOT EXISTS waitinglist (
  netID char(8)  NOT NULL,
  symbol char(4)  NOT NULL,
  number char(4)  NOT NULL,
  sectionNumber char(2)  NOT NULL,
  since timestamp DEFAULT NULL,
  PRIMARY KEY (netID,symbol,number,sectionNumber),
  FOREIGN KEY (netID) REFERENCES student (netID),
  FOREIGN KEY (symbol,number,sectionNumber) REFERENCES courseoffering_of (symbol, number, sectionNumber)
) ;


INSERT INTO waitinglist (netID, symbol, number, sectionNumber,since) VALUES
('aec3','CSE','1384','02', '2021-10-15 14:00:00'),
('cd911','CSE','1384','01','2021-10-21 01:00:00'),
('hc23','ECE','4713', '01','2021-10-01 08:00:00'),
('wp4','ECE','4713','01','2021-10-13 04:23:00'),
('am2','CSE','4503','01','2021-09-30 09:34:00'),
('ts12','CSE','4503','01','2021-10-10 14:45:00'),
('ts2','CSE','4503','01','2021-09-29 20:32:00'),
 ('ts2','ECE','4713','01','2021-10-10 01:03:00');
