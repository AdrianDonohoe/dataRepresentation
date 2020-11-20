-- MySQL dump 10.13  Distrib 8.0.19, for Linux (x86_64)
--
-- Host: localhost    Database: election
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `candidate`
--

DROP TABLE IF EXISTS `candidate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `candidate` (
  `fname` varchar(20) NOT NULL,
  `sname` varchar(20) NOT NULL,
  `candidateID` int NOT NULL AUTO_INCREMENT,
  `party` varchar(20) NOT NULL,
  PRIMARY KEY (`candidateID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `candidate`
--

LOCK TABLES `candidate` WRITE;
/*!40000 ALTER TABLE `candidate` DISABLE KEYS */;
INSERT INTO `candidate` VALUES ('Donald','Trump',1,'Republican'),('Joe','Biden',2,'Democrat');
/*!40000 ALTER TABLE `candidate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `states`
--

DROP TABLE IF EXISTS `states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `states` (
  `name` varchar(20) NOT NULL,
  `abv` varchar(2) NOT NULL,
  `electoral_votes` int NOT NULL,
  `stateID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`stateID`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `states`
--

LOCK TABLES `states` WRITE;
/*!40000 ALTER TABLE `states` DISABLE KEYS */;
INSERT INTO `states` VALUES ('Alabama','AL',9,1),('Alaska','AK',3,2),('Arizona','AZ',11,3),('Arkansas','AR',6,4),('California','CA',55,5),('Colorado','CO',9,6),('Connecticut','CT',7,7),('Delaware','DE',3,8),('Florida','FL',29,9),('Georgia','GA',16,10),('Hawaii','HI',4,11),('Idaho','ID',4,12),('Illinois','IL',20,13),('Indiana','IN',11,14),('Iowa','IA',6,15),('Kansas','KS',6,16),('Kentucky','KY',8,17),('Louisiana','LA',8,18),('Maine','ME',3,19),('Maryland','MD',10,20),('Massachusetts','MA',11,21),('Michigan','MI',16,22),('Minnesota','MN',10,23),('Mississippi','MS',6,24),('Missouri','MO',10,25),('Montana','MT',3,26),('Nebraska','NE',4,27),('Nevada','NV',6,28),('New Hampshire','NH',4,29),('New Jersey','NJ',14,30),('New Mexico','NM',5,31),('New York','NY',29,32),('North Carolina','NC',15,33),('North Dakota','ND',3,34),('Ohio','OH',18,35),('Oklahoma','OK',7,36),('Oregon','OR',7,37),('Pennsylvania','PA',20,38),('Rhode Island','RI',4,39),('South Carolina','SC',9,40),('South Dakota','SD',3,41),('Tennessee','TN',11,42),('Texas','TX',38,43),('Utah','UT',6,44),('Vermont','VT',3,45),('Virginia','VA',13,46),('Washington','WA',12,47),('West Virginia','WV',5,48),('Wisconsin','WI',10,49),('Wyoming','WY',3,50);
/*!40000 ALTER TABLE `states` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `votes`
--

DROP TABLE IF EXISTS `votes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `votes` (
  `votes` int NOT NULL,
  `candidateID` int NOT NULL,
  `stateID` int NOT NULL,
  `percent` int NOT NULL,
  `voteID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`voteID`),
  KEY `stateID` (`stateID`),
  KEY `candidateID` (`candidateID`),
  CONSTRAINT `votes_ibfk_1` FOREIGN KEY (`stateID`) REFERENCES `states` (`stateID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `votes_ibfk_2` FOREIGN KEY (`candidateID`) REFERENCES `candidate` (`candidateID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `votes`
--

LOCK TABLES `votes` WRITE;
/*!40000 ALTER TABLE `votes` DISABLE KEYS */;
/*!40000 ALTER TABLE `votes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'election'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-20 16:03:09
