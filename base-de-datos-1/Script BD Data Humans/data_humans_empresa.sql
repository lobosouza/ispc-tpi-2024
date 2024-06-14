-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: data_human´s
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `empresa`
--

DROP TABLE IF EXISTS `empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empresa` (
  `Id_empresa` int NOT NULL,
  `Razonsocial` varchar(20) NOT NULL,
  `Cuit` varchar(20) NOT NULL,
  `Rubro` tinytext NOT NULL,
  `Ubicacion` varchar(100) NOT NULL,
  `Cantvacantes` int NOT NULL,
  `Id_vacantes` int NOT NULL,
  PRIMARY KEY (`Id_empresa`),
  UNIQUE KEY `Id_EMPRESA_UNIQUE` (`Id_empresa`),
  UNIQUE KEY `Id_VACANTES_UNIQUE` (`Id_vacantes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresa`
--

LOCK TABLES `empresa` WRITE;
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
INSERT INTO `empresa` VALUES (10001,'Clean is good','30256856256','Limpieza','Cordoba',5,30001),(10002,'Paul Mc Carne','30659875435','Carniceria','Cordoba',2,30002),(10003,'Jueguito','30256874196','Jugueteria','Cordoba',1,30003),(10004,'L cafe','30256874156','Cafeteria','Cordoba',3,30004),(10005,'Ayudin Cool','30269587459','Limpieza','Cordoba',3,30005),(10006,'Desinf-accion','30563982156','Limpieza','Cordoba',5,30006),(10007,'Limpia Door','30526912589','Limpieza','Cordoba',2,30007),(10008,'Aspira Dora','30569871059','Limpieza','Cordoba',3,30008),(10009,'A Todotrapo','30658714569','Limpieza','Cordoba',6,30009),(10010,'Limpiecito','30658971259','Limpieza','Cordoba',4,30010);
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-12  1:25:14
