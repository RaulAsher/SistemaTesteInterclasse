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
-- Table structure for table `inscricoes_provas_atletismo`
--

DROP TABLE IF EXISTS `inscricoes_provas_atletismo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inscricoes_provas_atletismo` (
  `pk_inscricao` int NOT NULL AUTO_INCREMENT,
  `fk_prova` int NOT NULL,
  `fk_matricula` int NOT NULL,
  `resultado` decimal(10,3) DEFAULT NULL,
  `posicao` int DEFAULT NULL,
  `data_inscricao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`pk_inscricao`),
  UNIQUE KEY `uk_prova_aluno` (`fk_prova`,`fk_matricula`),
  KEY `idx_inscricao_prova` (`fk_prova`),
  KEY `idx_inscricao_aluno` (`fk_matricula`),
  CONSTRAINT `fk_inscricao_aluno` FOREIGN KEY (`fk_matricula`) REFERENCES `alunos` (`pk_matricula`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_inscricao_prova` FOREIGN KEY (`fk_prova`) REFERENCES `provas_atletismo` (`pk_prova`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inscricoes_provas_atletismo`
--

LOCK TABLES `inscricoes_provas_atletismo` WRITE;
/*!40000 ALTER TABLE `inscricoes_provas_atletismo` DISABLE KEYS */;
INSERT INTO `inscricoes_provas_atletismo` VALUES (11,11,3017763,NULL,NULL,'2026-08-26 03:41:19'),(12,11,3032485,NULL,NULL,'2026-08-26 03:41:26'),(16,11,3673740,NULL,NULL,'2026-09-09 03:01:20'),(17,11,3714666,NULL,NULL,'2026-09-09 03:08:11'),(18,11,3242905,NULL,NULL,'2026-09-09 03:08:23'),(19,11,3275800,NULL,NULL,'2026-09-09 03:08:28'),(20,11,2733531,NULL,NULL,'2026-09-09 03:08:33'),(21,1,3673377,NULL,NULL,'2026-09-09 04:52:13'),(22,1,3714666,NULL,NULL,'2026-09-09 04:52:17'),(23,1,3671461,NULL,NULL,'2026-09-09 04:52:22'),(24,1,3672634,NULL,NULL,'2026-09-09 04:52:28'),(25,1,3275800,NULL,NULL,'2026-09-09 04:52:34');
/*!40000 ALTER TABLE `inscricoes_provas_atletismo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-09-09  2:06:43
