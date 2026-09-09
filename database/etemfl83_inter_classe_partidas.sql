-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: etemfl83_inter_classe
-- ------------------------------------------------------
-- Server version	8.0.46

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
-- Table structure for table `partidas`
--

DROP TABLE IF EXISTS `partidas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partidas` (
  `pk_partida` int NOT NULL AUTO_INCREMENT,
  `fk_esporte` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `fk_genero` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `fk_equipe_casa` int DEFAULT NULL,
  `fk_equipe_visitante` int DEFAULT NULL,
  `pontos_turma_casa` int DEFAULT NULL,
  `pontos_turma_visitante` int DEFAULT NULL,
  `definida` enum('sim','nao') CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT 'nao',
  `par_re1` int DEFAULT NULL,
  `par_re2` int DEFAULT NULL,
  `etapa` int DEFAULT NULL,
  `pk_partida_mae` int DEFAULT NULL,
  `pk_equipe_vencedora` int DEFAULT NULL,
  `data_hora` datetime DEFAULT NULL,
  PRIMARY KEY (`pk_partida`),
  KEY `fk_esporte` (`fk_esporte`),
  KEY `fk_genero` (`fk_genero`),
  CONSTRAINT `partidas_ibfk_1` FOREIGN KEY (`fk_esporte`) REFERENCES `esportes` (`pk_esporte`),
  CONSTRAINT `partidas_ibfk_2` FOREIGN KEY (`fk_genero`) REFERENCES `classificacao` (`pk_genero`)
) ENGINE=InnoDB AUTO_INCREMENT=1218 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-09-08 23:10:56
