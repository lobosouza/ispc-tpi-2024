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
-- Table structure for table `postulante`
--

DROP TABLE IF EXISTS `postulante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `postulante` (
  `id_postulante` int NOT NULL,
  `Dni` int DEFAULT NULL,
  `Nombre` varchar(45) DEFAULT NULL,
  `Apellido` varchar(45) DEFAULT NULL,
  `Fechanacimiento` date DEFAULT NULL,
  `Residencia` varchar(45) DEFAULT NULL,
  `Nivelacademico` varchar(45) DEFAULT NULL,
  `C.v` varchar(45) DEFAULT NULL,
  `Puestodeseado` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_postulante`),
  UNIQUE KEY `id_POSTULANTE_UNIQUE` (`id_postulante`),
  UNIQUE KEY `D.N.I_UNIQUE` (`Dni`),
  KEY `FK_Residencia_idx` (`Residencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postulante`
--

LOCK TABLES `postulante` WRITE;
/*!40000 ALTER TABLE `postulante` DISABLE KEYS */;
INSERT INTO `postulante` VALUES (1,35871057,'Nicolas','Allende','1992-05-06','Cordoba','Universitarios','Cargado','Cajero'),(2,36692589,'Carlos','Aguirre','1991-02-07','Cordoba','Secundarios','Cargado','Administrativo'),(3,26892569,'Malena','Polanco','1996-10-04','Cordoba','Secundarios','Cargado','Maestranza'),(4,35986352,'Juliana','Salcedo','2000-09-06','Cordoba','Secundarios','Cargado','Vendedor'),(5,39685963,'Vittorio','Arjona','1998-01-26','Cordoba','Secundarios','Cargado','Operario'),(6,41968712,'Matias','Wider','1997-02-21','Cordoba','Secundarios','Cargado','Administrativo'),(7,31569825,'Esperanza','Castro','1996-05-23','Cordoba','Universitarios','Cargado','Vendedor'),(8,35953689,'Juan','Perez','1995-08-09','Cordoba','Universitarios','Cargado','Repositor'),(9,32966884,'Cecilia','Lopez','1993-07-10','Cordoba','Secundarios','Cargado','Vendedor'),(10,33989625,'Maura','Cuneo','1999-12-09','Salta','Secundarios','Cargado','Maestranza'),(11,33695852,'Alicia','Cataneo','2001-03-13','Tucuman','Universitarios','Cargado','Productor'),(12,32696874,'Pablo','Mateos','1992-10-10','Chaco','Secundarios','Cargado','Administrativo'),(13,40693542,'Damian','Cortez','1980-12-05','La Rioja','Secundarios','Cargado','Maestranza'),(14,39521558,'Martin','Joray','1985-12-12','Jujuy','Universitarios','Cargado','Maestranza'),(15,30569820,'Agustina','Sueldo','1993-10-12','Salta','Secundarios','Cargado','Guardia'),(16,35876952,'Lucas','Sousa','1993-06-06','Neuquen','Universitarios','Cargado','Repositor'),(17,38967410,'Ernesto','Palomeque','1992-11-22','Chubut','Secundarios','Cargado','Guardia'),(18,26958741,'Monica','Llance','1995-07-15','Mendoza','Secundarios','Cargado','Vendedor'),(19,35986325,'Paula','Machuca','1996-03-25','Salta','Secundarios','Cargado','Maestranza'),(20,37852159,'Mauricio','Silva','1995-09-08','Catamarca','Universitarios','Cargado','Maestranza');
/*!40000 ALTER TABLE `postulante` ENABLE KEYS */;
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
