CREATE DATABASE `Running_Route` /*!40100 DEFAULT CHARACTER SET big5 */;
CREATE TABLE `User` (
  `User_ID` int(11) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `token` varchar(45) NOT NULL,
  PRIMARY KEY (`User_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=big5;
CREATE TABLE `Routes` (
  `Route_ID` int(11) NOT NULL,
  `start_point` varchar(45) NOT NULL,
  `mid_point` varchar(45) NOT NULL,
  `route_length` varchar(45) NOT NULL,
  PRIMARY KEY (`Route_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=big5;
CREATE TABLE `Playlist` (
  `Playlist_ID` int(11) NOT NULL,
  `User_ID` int(11) NOT NULL,
  `length` varchar(45) NOT NULL,
  PRIMARY KEY (`Playlist_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=big5;
CREATE TABLE `Cache` (
  `Route_ID` int(11) NOT NULL,
  `route_length` varchar(45) NOT NULL,
  `start_point` varchar(45) NOT NULL,
  `mid_point` varchar(45) NOT NULL,
  PRIMARY KEY (`Route_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=big5;
