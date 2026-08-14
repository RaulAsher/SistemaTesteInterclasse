CREATE DATABASE  IF NOT EXISTS `etemfl83_inter_classe` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `etemfl83_inter_classe`;
-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: etemfl83_inter_classe
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
-- Table structure for table `alunos`
--

DROP TABLE IF EXISTS `alunos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alunos` (
  `pk_matricula` int NOT NULL,
  `nome_aluno` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `fk_nome_turma` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `fk_classificacao` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`pk_matricula`),
  KEY `fk_nome_turma` (`fk_nome_turma`),
  CONSTRAINT `alunos_ibfk_1` FOREIGN KEY (`fk_nome_turma`) REFERENCES `turmas` (`pk_nome_turma`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `calendario`
--

DROP TABLE IF EXISTS `calendario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calendario` (
  `pk_evento` int NOT NULL AUTO_INCREMENT,
  `dia_evento` date DEFAULT NULL,
  `fk_partida` int DEFAULT NULL,
  `hora_inicio` time DEFAULT NULL,
  `hora_fim` time DEFAULT NULL,
  PRIMARY KEY (`pk_evento`),
  KEY `fk_partida` (`fk_partida`),
  CONSTRAINT `calendario_ibfk_1` FOREIGN KEY (`fk_partida`) REFERENCES `partidas` (`pk_partida`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `classificacao`
--

DROP TABLE IF EXISTS `classificacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classificacao` (
  `pk_genero` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`pk_genero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `configuracoes`
--

DROP TABLE IF EXISTS `configuracoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `configuracoes` (
  `chave` varchar(50) NOT NULL,
  `valor` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`chave`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `equipes`
--

DROP TABLE IF EXISTS `equipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipes` (
  `pk_equipe` int NOT NULL AUTO_INCREMENT,
  `fk_esporte` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `fk_nome_turma` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `fk_genero` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `nome_equipe` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`pk_equipe`),
  KEY `fk_esporte` (`fk_esporte`),
  KEY `fk_nome_turma` (`fk_nome_turma`),
  KEY `fk_genero` (`fk_genero`),
  CONSTRAINT `equipes_ibfk_1` FOREIGN KEY (`fk_esporte`) REFERENCES `esportes` (`pk_esporte`),
  CONSTRAINT `equipes_ibfk_2` FOREIGN KEY (`fk_nome_turma`) REFERENCES `turmas` (`pk_nome_turma`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `equipes_ibfk_3` FOREIGN KEY (`fk_genero`) REFERENCES `classificacao` (`pk_genero`)
) ENGINE=InnoDB AUTO_INCREMENT=278 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `esportes`
--

DROP TABLE IF EXISTS `esportes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `esportes` (
  `pk_esporte` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `grupo` enum('Coletivo','Individual','Atletismo') COLLATE utf8mb3_unicode_ci NOT NULL,
  `qtd_jogadores` int NOT NULL,
  PRIMARY KEY (`pk_esporte`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `estatisticas_esporte`
--

DROP TABLE IF EXISTS `estatisticas_esporte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estatisticas_esporte` (
  `fk_esporte` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `fk_nome_estatistica` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`fk_esporte`,`fk_nome_estatistica`),
  KEY `fk_nome_estatistica` (`fk_nome_estatistica`),
  CONSTRAINT `estatisticas_esporte_ibfk_1` FOREIGN KEY (`fk_esporte`) REFERENCES `esportes` (`pk_esporte`),
  CONSTRAINT `estatisticas_esporte_ibfk_2` FOREIGN KEY (`fk_nome_estatistica`) REFERENCES `tipo_estatistica` (`pk_nome_estatistica`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `pk_usuario` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `senha` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `nivel` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `fk_nome_turma` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`pk_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `membros_equipe`
--

DROP TABLE IF EXISTS `membros_equipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `membros_equipe` (
  `fk_equipe` int NOT NULL,
  `fk_matricula` int NOT NULL,
  PRIMARY KEY (`fk_equipe`,`fk_matricula`),
  KEY `fk_matricula` (`fk_matricula`),
  CONSTRAINT `membros_equipe_ibfk_1` FOREIGN KEY (`fk_equipe`) REFERENCES `equipes` (`pk_equipe`),
  CONSTRAINT `membros_equipe_ibfk_2` FOREIGN KEY (`fk_matricula`) REFERENCES `alunos` (`pk_matricula`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `modalidades_atletismo`
--

DROP TABLE IF EXISTS `modalidades_atletismo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modalidades_atletismo` (
  `pk_modalidade` int NOT NULL AUTO_INCREMENT,
  `nome_modalidade` varchar(100) NOT NULL,
  `descricao` varchar(255) DEFAULT NULL,
  `ativo` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`pk_modalidade`),
  UNIQUE KEY `uk_nome_modalidade` (`nome_modalidade`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  PRIMARY KEY (`pk_partida`),
  KEY `fk_esporte` (`fk_esporte`),
  KEY `fk_genero` (`fk_genero`),
  CONSTRAINT `partidas_ibfk_1` FOREIGN KEY (`fk_esporte`) REFERENCES `esportes` (`pk_esporte`),
  CONSTRAINT `partidas_ibfk_2` FOREIGN KEY (`fk_genero`) REFERENCES `classificacao` (`pk_genero`)
) ENGINE=InnoDB AUTO_INCREMENT=853 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `provas_atletismo`
--

DROP TABLE IF EXISTS `provas_atletismo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provas_atletismo` (
  `pk_prova` int NOT NULL AUTO_INCREMENT,
  `fk_modalidade` int NOT NULL,
  `fk_genero` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `nome_prova` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `tipo_resultado` enum('tempo','distancia','altura','pontos') COLLATE utf8mb3_unicode_ci NOT NULL,
  `unidade_medida` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `ativo` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`pk_prova`),
  KEY `idx_modalidade` (`fk_modalidade`),
  KEY `idx_genero` (`fk_genero`),
  CONSTRAINT `fk_prova_genero` FOREIGN KEY (`fk_genero`) REFERENCES `classificacao` (`pk_genero`),
  CONSTRAINT `fk_prova_modalidade` FOREIGN KEY (`fk_modalidade`) REFERENCES `modalidades_atletismo` (`pk_modalidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tipo_estatistica`
--

DROP TABLE IF EXISTS `tipo_estatistica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_estatistica` (
  `pk_nome_estatistica` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`pk_nome_estatistica`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `turmas`
--

DROP TABLE IF EXISTS `turmas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `turmas` (
  `pk_nome_turma` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `icone_url` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`pk_nome_turma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-14 19:45:16
