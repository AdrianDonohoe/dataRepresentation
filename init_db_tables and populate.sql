-- MySQL dump 10.13  Distrib 8.0.19, for Linux (x86_64)
--
-- Host: localhost    Database: datarep
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
-- Table structure for table `states`
--

DROP TABLE IF EXISTS `states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `states` (
  `name` varchar(20) NOT NULL,
  `abv` varchar(2) NOT NULL,
  `ecv` int NOT NULL,
  `tv` int NOT NULL,
  `bv` int NOT NULL,
  `tp` varchar(5) NOT NULL,
  `bp` varchar(5) NOT NULL,
  `stateID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`stateID`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `states`
--

LOCK TABLES `states` WRITE;
/*!40000 ALTER TABLE `states` DISABLE KEYS */;
INSERT INTO `states` VALUES ('Alabama','AL',9,1434159,843473,'62.1','36.5',1),('Alaska','AK',3,189457,153551,'53.1','43.0',2),('Arizona','AZ',11,1661686,1672143,'49.08','49.39',3),('Arkansas','AR',6,759715,423502,'62.4','34.8',4),('California','CA',55,5890353,10957388,'34.96','65.04',5),('Colorado','CO',9,1364202,1803921,'41.9','55.4',6),('Connecticut','CT',7,715567,1080387,'39.2','59.2',7),('Delaware','DE',3,200603,296268,'39.8','58.8',8),('Florida','FL',29,5668731,5297045,'51.2','47.9',9),('Georgia','GA',16,2462857,2475141,'49.88','50.12',10),('Hawaii','HI',4,196864,366130,'34.3','63.7',11),('Idaho','ID',4,554128,287031,'63.8','33.1',12),('Illinois','IL',20,2430860,3443172,'40.6','57.5',13),('Indiana','IN',11,1729446,1241774,'57.0','40.9',14),('Iowa','IA',6,897467,758881,'53.2','44.9',15),('Kansas','KS',6,753370,551199,'56.5','41.3',16),('Kentucky','KY',8,1326347,772223,'62.1','36.2',17),('Louisiana','LA',8,1255776,856034,'58.5','39.9',18),('Maine','ME',3,342325,420588,'43.5','53.4',19),('Maryland','MD',10,967546,1950920,'32.5','65.6',20),('Massachusetts','MA',11,1149614,2319420,'32.4','65.3',21),('Michigan','MI',16,2649537,2807309,'47.8','50.6',22),('District of Columbia','DC',3,18586,317323,'5.4','92.1',23),('Minnesota','MN',10,1483750,1716312,'45.4','52.5',24),('Mississippi','MS',6,756731,539494,'58.38','41.62',25),('Missouri','MO',10,1717601,1252351,'56.7','41.4',26),('Montana','MT',3,343602,244786,'58.40','41.60',27),('Nebraska','NE',4,555509,374169,'58.5','39.4',28),('Nevada','NV',6,669890,703486,'47.7','50.1',29),('New Hampshire','NH',4,365660,424937,'45.5','52.8',30),('New Jersey','NJ',14,1851351,2570675,'41.2','57.2',31),('New Mexico','NM',5,401825,501471,'43.5','54.3',32),('New York','NY',29,2948571,3987255,'41.9','56.6',33),('North Carolina','NC',15,2758775,2684302,'49.9','48.6',34),('North Dakota','ND',3,235595,114902,'65.1','31.8',35),('Ohio','OH',18,3148559,2676916,'53.2','45.2',36),('Oklahoma','OK',7,1020280,503890,'65.4','32.3',37),('Oregon','OR',7,958494,1339643,'40.4','56.5',38),('Pennsylvania','PA',20,3372730,3454715,'49.40','50.60',39),('Rhode Island','RI',4,199830,306192,'38.9','59.6',40),('South Carolina','SC',9,1385103,1091541,'55.1','43.4',41),('South Dakota','SD',3,261043,150471,'61.8','35.6',42),('Tennessee','TN',11,1849820,1139376,'60.7','37.4',43),('Texas','TX',38,5891778,5261055,'52.83','47.17',44),('Utah','UT',6,865140,560282,'58.2','37.7',45),('Vermont','VT',3,112704,242820,'30.7','66.1',46),('Virginia','VA',13,1962612,2413577,'44.0','54.2',47),('Washington','WA',12,1579402,2363988,'39.0','58.4',48),('West Virginia','WV',5,545051,235847,'68.6','29.7',49),('Wisconsin','WI',10,1610151,1630716,'48.83','49.45',50),('Wyoming','WY',3,193559,73491,'69.9','26.6',51);
/*!40000 ALTER TABLE `states` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-04 10:50:41
