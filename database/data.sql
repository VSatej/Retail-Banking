-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: xplore
-- ------------------------------------------------------
-- Server version	8.0.20-0ubuntu0.20.04.1

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
-- Table structure for table `Account`
--

DROP TABLE IF EXISTS `Account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Account` (
  `Customer_ID` int NOT NULL,
  `Account_ID` int NOT NULL,
  `Balance` int NOT NULL,
  `CR_Data` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `CR_LDate` datetime DEFAULT NULL,
  `Duration` int NOT NULL DEFAULT '10',
  `Account_Type` varchar(1) NOT NULL,
  PRIMARY KEY (`Account_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Account`
--

LOCK TABLES `Account` WRITE;
/*!40000 ALTER TABLE `Account` DISABLE KEYS */;
INSERT INTO `Account` VALUES (123123123,123122436,50000,'2020-06-17 03:42:47','2030-06-17 00:00:00',10,'C'),(123123123,123123284,50000,'2020-06-16 11:20:32','2030-06-16 00:00:00',10,'C'),(123456789,123456789,10000,'2020-06-16 08:36:29','2030-06-16 00:00:00',10,'C'),(123456789,123458847,4500,'2020-06-16 09:46:20','2030-06-16 00:00:00',10,'S');
/*!40000 ALTER TABLE `Account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AccountStatus`
--

DROP TABLE IF EXISTS `AccountStatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AccountStatus` (
  `Customer_ID` int NOT NULL,
  `Account_ID` int NOT NULL,
  `Account_Type` varchar(20) NOT NULL,
  `Status` varchar(20) NOT NULL,
  `Message` varchar(100) NOT NULL,
  `Last_Updated` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AccountStatus`
--

LOCK TABLES `AccountStatus` WRITE;
/*!40000 ALTER TABLE `AccountStatus` DISABLE KEYS */;
INSERT INTO `AccountStatus` VALUES (123456789,123456789,'S','Removed','Account Removed Successfully','2020-06-15 14:22:53'),(123456789,123456789,'S','Active','Account Created Successfully','2020-06-15 14:24:27'),(123456789,123456789,'S','Removed','Account Removed Successfully','2020-06-15 14:25:44'),(123456789,123456789,'C','Active','Account Created Successfully','2020-06-16 08:36:29'),(123456789,123459925,'S','Active','Account Created Successfully','2020-06-16 09:03:08'),(123456789,123459925,'S','Removed','Account Removed Successfully','2020-06-16 09:45:51'),(123456789,123458847,'S','Active','Account Created Successfully','2020-06-16 09:46:20'),(123123123,123123284,'C','Active','Account Created Successfully','2020-06-16 11:20:32'),(123123123,123122436,'C','Active','Account Created Successfully','2020-06-17 03:42:47');
/*!40000 ALTER TABLE `AccountStatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `SSN_ID` int NOT NULL,
  `Customer_ID` int NOT NULL,
  `Name` varchar(40) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Age` int NOT NULL,
  PRIMARY KEY (`SSN_ID`),
  UNIQUE KEY `Customer_ID` (`Customer_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (123123123,123123123,'Rohan','Bibwewadi,  Pune , Maharashtra',21);
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CustomerStatus`
--

DROP TABLE IF EXISTS `CustomerStatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CustomerStatus` (
  `SSN_ID` int NOT NULL,
  `Customer_ID` int NOT NULL,
  `Status` varchar(20) NOT NULL,
  `Message` varchar(100) DEFAULT NULL,
  `Last_Updated` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CustomerStatus`
--

LOCK TABLES `CustomerStatus` WRITE;
/*!40000 ALTER TABLE `CustomerStatus` DISABLE KEYS */;
INSERT INTO `CustomerStatus` VALUES (123123123,123123123,'Active','Customer Created Successfully','2020-06-16 11:00:11');
/*!40000 ALTER TABLE `CustomerStatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transactions`
--

DROP TABLE IF EXISTS `Transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Transactions` (
  `Account_ID` int NOT NULL,
  `Transaction_ID` int NOT NULL AUTO_INCREMENT,
  `Transaction_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Type` varchar(20) NOT NULL,
  `Amount` int NOT NULL,
  PRIMARY KEY (`Transaction_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transactions`
--

LOCK TABLES `Transactions` WRITE;
/*!40000 ALTER TABLE `Transactions` DISABLE KEYS */;
INSERT INTO `Transactions` VALUES (123122436,1,'2020-06-17 10:11:24','Deposit',10000),(123122436,2,'2020-06-18 09:17:29','Withdraw',30000);
/*!40000 ALTER TABLE `Transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userstore`
--

DROP TABLE IF EXISTS `userstore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userstore` (
  `login` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`login`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userstore`
--

LOCK TABLES `userstore` WRITE;
/*!40000 ALTER TABLE `userstore` DISABLE KEYS */;
INSERT INTO `userstore` VALUES ('Cashier','secret','2020-06-17 05:07:00','Cashier'),('Rohan','RohanPassword','2020-06-13 12:19:42','User'),('User01','qwerty','2020-06-13 12:23:30','User');
/*!40000 ALTER TABLE `userstore` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-18  9:35:28
