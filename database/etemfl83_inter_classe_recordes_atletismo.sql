-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: etemfl83_inter_classe
-- ------------------------------------------------------
-- Server version	8.0.44

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
-- Table structure for table `recordes_atletismo`
--

DROP TABLE IF EXISTS `recordes_atletismo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recordes_atletismo` (
  `pk_recorde` int NOT NULL AUTO_INCREMENT,
  `fk_prova` int NOT NULL,
  `fk_matricula` int NOT NULL,
  `resultado` decimal(10,3) NOT NULL,
  `data_recorde` date DEFAULT NULL,
  `ano` int DEFAULT NULL,
  PRIMARY KEY (`pk_recorde`),
  KEY `idx_prova` (`fk_prova`),
  KEY `idx_matricula` (`fk_matricula`),
  CONSTRAINT `fk_recorde_aluno` FOREIGN KEY (`fk_matricula`) REFERENCES `alunos` (`pk_matricula`),
  CONSTRAINT `fk_recorde_prova` FOREIGN KEY (`fk_prova`) REFERENCES `provas_atletismo` (`pk_prova`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recordes_atletismo`
--

LOCK TABLES `recordes_atletismo` WRITE;
/*!40000 ALTER TABLE `recordes_atletismo` DISABLE KEYS */;
INSERT INTO `recordes_atletismo` VALUES (1,1,3673377,7.000,'2026-09-09',2026),(2,1,3275800,3.450,'2026-09-09',2026),(3,1,3672634,20.000,'2026-09-09',2026),(4,1,3671461,12.200,'2026-09-09',2026),(5,1,3714666,11.200,'2026-09-09',2026);
/*!40000 ALTER TABLE `recordes_atletismo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-09-09  2:06:42
