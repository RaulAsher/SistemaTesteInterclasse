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
-- Dumping data for table `equipes`
--

LOCK TABLES `equipes` WRITE;
/*!40000 ALTER TABLE `equipes` DISABLE KEYS */;
INSERT INTO `equipes` VALUES (104,'Xadrez','3MKTB','Masculino',NULL),(105,'Xadrez','3TDSA','Masculino',NULL),(106,'Xadrez','3TDSA','Masculino',NULL),(107,'Xadrez','3TDSB','Masculino',NULL),(108,'Xadrez','3TDSA','Masculino',NULL),(109,'Xadrez','3TDSB','Masculino',NULL),(110,'Xadrez','3TDSA','Masculino',NULL),(112,'Xadrez','3MKTB','Feminino',NULL),(115,'Xadrez','3TDSB','Masculino',NULL),(116,'Xadrez','3TDSB','Masculino',NULL),(119,'Xadrez','1TDSA','Masculino',NULL),(120,'Xadrez','3TDSB','Feminino',NULL),(122,'Xadrez','3TDSB','Feminino',NULL),(123,'Xadrez','1TDSA','Masculino',NULL),(124,'Xadrez','3TDSB','Feminino',NULL),(125,'Xadrez','2MKTA','Feminino',NULL),(126,'Xadrez','2MKTB','Masculino',NULL),(128,'Xadrez','2MKTB','Feminino',NULL),(129,'Xadrez','2TDSA','Masculino',NULL),(130,'Xadrez','2TDSB','Masculino',NULL),(131,'Xadrez','3MKTA','Feminino',NULL),(132,'Xadrez','2TDSA','Feminino',NULL),(133,'Xadrez','1TDSB','Masculino',NULL),(134,'Xadrez','2TDSA','Feminino',NULL),(135,'Xadrez','3MKTA','Masculino',NULL),(136,'Xadrez','2TDSA','Feminino',NULL),(137,'Xadrez','1TDSB','Masculino',NULL),(138,'Xadrez','1TDSB','Masculino',NULL),(139,'Xadrez','2TDSA','Feminino',NULL),(140,'Xadrez','1TDSB','Masculino',NULL),(141,'Xadrez','3MKTA','Masculino',NULL),(142,'Xadrez','3MKTA','Masculino',NULL),(143,'Xadrez','3MKTA','Masculino',NULL),(144,'Xadrez','3MKTA','Masculino',NULL),(145,'Xadrez','2TDSA','Feminino',NULL),(146,'Handebol','3TDSB','Masculino',NULL),(148,'Futsal','3TDSB','Masculino',NULL),(149,'Handebol','3MKTA','Feminino',NULL),(150,'Handebol','1TDSA','Masculino',NULL),(152,'Futsal','3MKTA','Feminino',NULL),(155,'Vôlei','1TDSA','Feminino',NULL),(156,'Vôlei','3TDSB','Masculino',NULL),(157,'Handebol','3TDSA','Masculino',NULL),(158,'Vôlei','3MKTA','Feminino',NULL),(159,'Futsal','1TDSA','Masculino',NULL),(162,'Handebol','2TDSA','Masculino',NULL),(163,'Vôlei','1TDSA','Masculino',NULL),(164,'Basquete','3MKTA','Feminino',NULL),(165,'Futsal','3TDSA','Masculino',NULL),(167,'Queimada','3MKTA','Misto',NULL),(168,'Vôlei','3TDSA','Masculino',NULL),(169,'Futsal','2TDSA','Masculino',NULL),(171,'Handebol','2MKTA','Masculino',NULL),(172,'Tênis de Mesa','3MKTA','Feminino',NULL),(173,'Queimada','1TDSA','Misto',NULL),(174,'Tênis de Mesa','1TDSA','Masculino',NULL),(175,'Tênis de Mesa','1TDSA','Masculino',NULL),(176,'Tênis de Mesa','1TDSA','Masculino',NULL),(178,'Tênis de Mesa','1TDSA','Masculino',NULL),(179,'Futsal','3MKTA','Masculino',NULL),(180,'Vôlei','2TDSA','Masculino',NULL),(182,'Queimada','3TDSA','Misto',NULL),(183,'Handebol','1TDSB','Masculino',NULL),(184,'Handebol','2MKTA','Feminino',NULL),(185,'Vôlei','3MKTA','Masculino',NULL),(186,'Basquete','3MKTA','Masculino',NULL),(188,'Basquete','2TDSA','Masculino',NULL),(189,'Handebol','2MKTB','Feminino',NULL),(190,'Tênis de Mesa','3MKTA','Masculino',NULL),(193,'Tênis de Mesa','3MKTA','Masculino',NULL),(194,'Futsal','2MKTB','Feminino',NULL),(196,'Futsal','1TDSB','Masculino',NULL),(198,'Futsal','2MKTA','Masculino',NULL),(200,'Queimada','3TDSB','Misto',NULL),(201,'Queimada','2TDSA','Misto',NULL),(203,'Vôlei','1TDSB','Masculino',NULL),(206,'Tênis de Mesa','3TDSB','Masculino',NULL),(207,'Tênis de Mesa','3TDSB','Masculino',NULL),(208,'Tênis de Mesa','2TDSA','Masculino',NULL),(209,'Vôlei','2MKTB','Feminino',NULL),(210,'Tênis de Mesa','3TDSB','Masculino',NULL),(211,'Tênis de Mesa','3TDSB','Masculino',NULL),(212,'Tênis de Mesa','2TDSA','Masculino',NULL),(213,'Basquete','1TDSB','Masculino',NULL),(214,'Tênis de Mesa','2TDSA','Masculino',NULL),(215,'Futsal','2MKTA','Feminino',NULL),(216,'Tênis de Mesa','2TDSA','Masculino',NULL),(218,'Basquete','2MKTB','Feminino',NULL),(220,'Handebol','2TDSA','Feminino',NULL),(222,'Vôlei','2TDSA','Feminino',NULL),(224,'Handebol','3MKTB','Masculino',NULL),(225,'Tênis de Mesa','2TDSA','Feminino',NULL),(226,'Futsal','3MKTB','Masculino',NULL),(227,'Queimada','1TDSB','Misto',NULL),(229,'Vôlei','3MKTB','Masculino',NULL),(231,'Queimada','2MKTB','Misto',NULL),(232,'Basquete','3MKTB','Masculino',NULL),(233,'Tênis de Mesa','1TDSB','Masculino',NULL),(234,'Tênis de Mesa','1TDSB','Masculino',NULL),(235,'Basquete','2MKTB','Masculino',NULL),(237,'Tênis de Mesa','1TDSB','Masculino',NULL),(238,'Tênis de Mesa','1TDSB','Masculino',NULL),(239,'Vôlei','2MKTB','Masculino',NULL),(240,'Queimada','3MKTB','Misto',NULL),(241,'Futsal','2MKTB','Masculino',NULL),(242,'Handebol','2MKTB','Masculino',NULL),(243,'Vôlei','2MKTA','Masculino',NULL),(244,'Basquete','2MKTA','Masculino',NULL),(245,'Queimada','2MKTA','Misto',NULL),(246,'Tênis de Mesa','2MKTA','Masculino',NULL),(247,'Tênis de Mesa','2MKTA','Masculino',NULL),(248,'Tênis de Mesa','2MKTA','Masculino',NULL),(249,'Tênis de Mesa','2MKTA','Masculino',NULL),(250,'Tênis de Mesa','2MKTA','Masculino',NULL),(251,'Tênis de Mesa','2MKTA','Masculino',NULL),(252,'Tênis de Mesa','2MKTA','Masculino',NULL),(253,'Tênis de Mesa','2MKTA','Masculino',NULL),(254,'Vôlei','2MKTA','Feminino',NULL),(255,'Tênis de Mesa','3MKTB','Masculino',NULL),(256,'Tênis de Mesa','3MKTB','Masculino',NULL),(258,'Handebol','3MKTB','Feminino',NULL),(259,'Futsal','3MKTB','Feminino',NULL),(260,'Vôlei','3MKTB','Feminino',NULL),(261,'Basquete','3MKTB','Feminino',NULL),(262,'Handebol','2TDSB','Masculino',NULL),(264,'Vôlei','2TDSB','Masculino',NULL),(265,'Basquete','2TDSB','Masculino',NULL),(266,'Queimada','2TDSB','Misto',NULL),(267,'Tênis de Mesa','2TDSB','Masculino',NULL),(268,'Tênis de Mesa','2TDSB','Masculino',NULL),(269,'Tênis de Mesa','2TDSB','Masculino',NULL),(270,'Tênis de Mesa','2TDSB','Masculino',NULL),(271,'Tênis de Mesa','2TDSB','Masculino',NULL),(272,'Handebol','2TDSB','Feminino',NULL),(273,'Vôlei','2TDSB','Feminino',NULL),(274,'Futsal','2TDSB','Masculino',NULL),(275,'Futsal','1TDSA','Masculino',NULL),(276,'Basquete','3TDSB','Feminino',NULL);
/*!40000 ALTER TABLE `equipes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-12  4:27:57
