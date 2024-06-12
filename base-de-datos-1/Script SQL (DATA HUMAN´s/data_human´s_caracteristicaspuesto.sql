CREATE DATABASE  IF NOT EXISTS `data_human´s` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `data_human´s`;
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
-- Table structure for table `caracteristicaspuesto`
--

DROP TABLE IF EXISTS `caracteristicaspuesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caracteristicaspuesto` (
  `Descripcion` varchar(700) NOT NULL,
  `Condicion/contratacion` varchar(40) DEFAULT NULL,
  `Experiencia` varchar(200) DEFAULT NULL,
  `Excluyente` varchar(200) NOT NULL,
  `Seconsidera` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Descripcion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caracteristicaspuesto`
--

LOCK TABLES `caracteristicaspuesto` WRITE;
/*!40000 ALTER TABLE `caracteristicaspuesto` DISABLE KEYS */;
INSERT INTO `caracteristicaspuesto` VALUES ('Se solicita personal para cubrir puesto de Maestranza, se requiere ser mayor de 18 años, tener secundario completo y residir en la ciudad de Cordoba. Las tareas son de mantenimiento, orden y limpieza, de espacios comunes del edificio, recolección de basura y desinfección, entre otros.','Permanente','Sin experiencia previa','Ser mayor de Edad, Secundario completo, residir en la Ciudad de Cordoba','Conocimiento y manejo, de aspiradoras e hidrolavadoras.');
/*!40000 ALTER TABLE `caracteristicaspuesto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-11 23:00:04
