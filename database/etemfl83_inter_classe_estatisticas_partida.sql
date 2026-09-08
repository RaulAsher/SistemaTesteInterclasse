-- MySQL dump 10.13  Distrib 8.0.46, for Linux (x86_64)
--
-- Host: localhost    Database: etemfl83_inter_classe
-- ------------------------------------------------------
-- Server version	8.0.46-0ubuntu0.24.04.3

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
-- Table structure for table `estatisticas_partida`
--

DROP TABLE IF EXISTS `estatisticas_partida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estatisticas_partida` (
  `fk_partida` int NOT NULL,
  `fk_nome_estatistica` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `valor_time_casa` int DEFAULT NULL,
  `valor_time_visitante` int DEFAULT NULL,
  PRIMARY KEY (`fk_partida`,`fk_nome_estatistica`),
  KEY `fk_nome_estatistica` (`fk_nome_estatistica`),
  CONSTRAINT `estatisticas_partida_ibfk_1` FOREIGN KEY (`fk_partida`) REFERENCES `partidas` (`pk_partida`),
  CONSTRAINT `estatisticas_partida_ibfk_2` FOREIGN KEY (`fk_nome_estatistica`) REFERENCES `tipo_estatistica` (`pk_nome_estatistica`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estatisticas_partida`
--

LOCK TABLES `estatisticas_partida` WRITE;
/*!40000 ALTER TABLE `estatisticas_partida` DISABLE KEYS */;
INSERT INTO `estatisticas_partida` VALUES (67,'Finalizações',7,10),(67,'Gols',7,1),(67,'Passes',1,51),(70,'Arremessos de Três',0,0),(70,'Passes',0,0),(70,'Pontos',1,0),(71,'Eliminações',1,0),(72,'Eliminações',0,0),(74,'Eliminações',0,0),(77,'Sets',0,0),(78,'Sets',3,2),(79,'Sets',0,0),(80,'Sets',1,0),(81,'Sets',4,0),(82,'Sets',0,0),(84,'Finalizações',1,0),(84,'Gols',2,2),(84,'Passes',1,0);
/*!40000 ALTER TABLE `estatisticas_partida` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-12  4:27:55
