/*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

You must create and select the marina database before executing 
the following SQL statements.

  
  YOU MAY NEED TO REFRESH THE SCHEMAS FOR MARINA TO SHOW UP. 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% */
CREATE SCHEMA `marina` ;
Use marina;

CREATE TABLE Boats (
  bid integer,
  bname varchar(50),
  color varchar(25),
  PRIMARY KEY (bid)
);

INSERT INTO Boats (bid, bname, color) VALUES 
(101, 'Interlake', 'blue'),
(102, 'Interlake', 'red'),
(103, 'Clipper', 'green'),
(104, 'Marine', 'red');


CREATE TABLE Sailors (
  sid integer,
  sname varchar(50),
  rating integer,
  age integer,
  PRIMARY KEY (sid)
);

INSERT INTO Sailors (sid, sname, rating, age) VALUES
(22, 'Dustin', 7, 45),
(29, 'Brutus', 1, 33),
(31, 'Lubber', 8, 55.5),
(32, 'Andy', 8, 25.5),
(58, 'Rusty', 10, 35),
(64, 'Horatio', 7, 35),
(71, 'Zorba', 10, 16),
(74, 'Horatio', 9, 35),
(85, 'Art', 3, 25.5),
(95, 'Bob', 3, 63.5);



CREATE TABLE Reserves (
  sid integer,
  bid integer,
  day date,
  PRIMARY KEY (sid,bid,day),
  FOREIGN KEY (bid) REFERENCES Boats (bid),
  FOREIGN KEY (sid) REFERENCES Sailors (sid)
);

INSERT INTO Reserves (sid, bid, day) VALUES
(22, 101, '1998-10-10'),
(64, 101, '1998-09-05'),
(22, 102, '1998-10-10'),
(31, 102, '1998-11-10'),
(64, 102, '1998-09-08'),
(22, 103, '1998-10-08'),
(31, 103, '1998-11-06'),
(74, 103, '1998-09-08'),
(22, 104, '1998-10-07'),
(31, 104, '1998-11-12');