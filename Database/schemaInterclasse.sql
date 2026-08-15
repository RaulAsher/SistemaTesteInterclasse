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
-- Dumping data for table `alunos`
--

LOCK TABLES `alunos` WRITE;
/*!40000 ALTER TABLE `alunos` DISABLE KEYS */;
INSERT INTO `alunos` VALUES (2298618,'JOSE DEIVYD BEZERRA DE FRANÇA FILHO','3TDSA','Masculino'),(2733531,'WASHINGTON VITOR DA SILVA PEREIRA','3TDSB','Masculino'),(2734262,'SENI BRYAN DA SILVA PAIXÃO','3TDSA','Masculino'),(2734267,'GEISIANE MAYARA OLIVEIRA SILVA','3MKTA','Feminino'),(2820692,'LARA DÁVILLA DE LIMA MELO','3MKTA','Feminino'),(2849098,'DAYELLY GABRIELLY LUCENA DA SILVA','3TDSB','Feminino'),(3011379,'JOANA CLARA ALMEIDA DIAS DA SILVA','3MKTA','Feminino'),(3017763,'AGUIDA FERNANDA DA SILVA SANTOS','2MKTA','Feminino'),(3017852,'GABRYEL RYAN DA SILVA SANTANA','2TDSA','Masculino'),(3025421,'PEDRO LUCAS SILVA RIBEIRO','1TDSA','Masculino'),(3026104,'LUANNY GABRIELLY FARIAS DA SILVA','2MKTB','Feminino'),(3032485,'LUCAS ARQUILES SANTOS SILVA','2TDSA','Masculino'),(3139436,'LEONARDO MIGUEL SOARES DOS SANTOS','1TDSA','Masculino'),(3142848,'PEDRO AUGUSTO DE ALMEIDA FIGUEIRA','1TDSA','Masculino'),(3148465,'LUCAS FERREIRA DE AMORIM','1TDSA','Masculino'),(3242905,'ALLAN VICTOR SILVA DE ANDRADE','2TDSB','Masculino'),(3252826,'ELOA DA SILVA NEVES','2MKTB','Feminino'),(3265475,'CAUÊ WILLAMS DOS SANTOS DE LIMA','2TDSB','Masculino'),(3275800,'FERNANDO GOMES SOARES DE OLIVEIRA','3TDSA','Masculino'),(3312845,'VITHOR GABRIEL CARDOSO DE AQUINO','3MKTB','Masculino'),(3365192,'IGOR LEANDRO DA SILVA','1TDSB','Masculino'),(3427219,'PEDRO HENRYQUE MARINHO BATISTA DA SILVA','3TDSB','Masculino'),(3431553,'MARIA CLARA MARQUES MOURA','3MKTB','Feminino'),(3599496,'THAYNA KETYLY NUNES ARAUJO','2MKTB','Feminino'),(3643954,'SARAH RAQUELL DUQUE DA SILVA','3MKTB','Feminino'),(3667698,'ANA BEATRIZ DA SILVA NASCIMENTO','3MKTB','Feminino'),(3670459,'HENRY MATHEUS MOURA BARROS','3TDSA','Masculino'),(3670471,'ANA BEATRIZ DA SILVA','3MKTB','Feminino'),(3670494,'IAN VITOR REIS DE LIRA','3MKTB','Masculino'),(3670503,'GUSTAVO ASCENDINO DE SOUZA','3TDSB','Masculino'),(3670508,'JOAO VITOR ZACARIAS DE OLIVEIRA','3TDSB','Masculino'),(3670537,'MILENA DE FREITAS CHAVES MOURA','3MKTA','Feminino'),(3670547,'JULLIA BHEATRIZ DA SILVA QUEIROZ','3MKTA','Feminino'),(3670629,'ALANE RAYSSA SOARES DE LIMA','3MKTA','Feminino'),(3670647,'ELOISA FERREIRA DA SILVA','3MKTB','Feminino'),(3671136,'MARIA CASSIANE GOMES DA SILVA','3MKTA','Feminino'),(3671323,'HADASSA VITORIA RAMOS DE OLIVEIRA','3MKTA','Feminino'),(3671334,'MAYSE GABRYELLE DA SILVA MELO','3TDSA','Feminino'),(3671347,'KETLYN MILENA ALVES DA SILVA','3MKTA','Feminino'),(3671461,'RIQUELME DA SILVA MENEZES','3TDSA','Masculino'),(3671486,'SAMUEL TEIXEIRA CUMARU MENDES DE SOUZA','3TDSB','Masculino'),(3671609,'DAVI NOAH GONCALO SILVA','3TDSB','Masculino'),(3671646,'LYZANDRA THAYS QUIRINO ALVES SILVA','3TDSB','Feminino'),(3671657,'YASMIM SOARES GALINDO DOS SANTOS','3MKTB','Feminino'),(3671660,'JOSE GUSTAVO DA SILVA SANTOS','3TDSA','Masculino'),(3671760,'JOAO PEDRO NASCIMENTO GUALBERTO BEZERRA','3TDSA','Masculino'),(3672614,'JOSE EUDES SANTIAGO MATIAS','3TDSB','Masculino'),(3672624,'RAUL ASHER GONCALVES E SILVA','3TDSB','Masculino'),(3672629,'KAIO RICARDO DA SILVA LIRA','3TDSA','Masculino'),(3672631,'JHENYFFER HELENA VIEIRA DE MELO','3MKTA','Feminino'),(3672634,'PIETRO MICHEL DO NASCIMENTO DA SILVA','3TDSB','Masculino'),(3672640,'MARIA CLARA DA SILVA DE LIMA','3TDSA','Feminino'),(3672644,'RAYANNY VITORIA VIEIRA DO NASCIMENTO','3TDSA','Feminino'),(3672646,'JAMYRES GABRIELA DE FREITAS FERREIRA','3MKTB','Feminino'),(3672649,'MARIA CLARISSA ATAIDE OLIVEIRA','3MKTA','Feminino'),(3672651,'IZABELY BIATRIZ DA SILVA OLIVEIRA','3MKTB','Feminino'),(3672655,'GEOVANNA VITORIA BASILIO DA SILVA','3MKTB','Feminino'),(3672657,'EWENLLY LAIS RODRIGUES BARBOZA','3MKTB','Feminino'),(3672658,'ANNA CAROLYNA LINS PINHEIRO','3MKTB','Feminino'),(3672659,'JENIFFER LINDANCY MARTINS TENORIO','3MKTA','Feminino'),(3672660,'PEDRO ELNATÃ FERREIRA MARTINS','3MKTA','Masculino'),(3672661,'MARIA CLARA SANTOS NASCIMENTO','3MKTA','Feminino'),(3672662,'LAIZ MAYARA SILVA ALVES','3MKTB','Feminino'),(3672709,'EDUARDO ANGELO VICTOR DE JESUS','3TDSA','Masculino'),(3672762,'LUIZ HELENO NETO SERAFIM DA SILVA','3TDSA','Masculino'),(3672783,'LAURA ALICE MENDONCA CORSINO','3MKTA','Feminino'),(3672878,'KARYNE DA SILVA NOGUEIRA','3MKTB','Feminino'),(3672888,'SABRYNNA THALYA FERNANDES DA SILVA','3TDSB','Feminino'),(3672943,'DAFNNE EMILLY VITORIA RODRIGUES DA SILVA','3MKTB','Feminino'),(3673019,'VANESSA KESLA BEZERRA ALCANTARA','3MKTB','Feminino'),(3673042,'ATAIDE JOSE DA SILVA NETO','3TDSB','Masculino'),(3673099,'MATEUS ANTONIO MELO LIRA','3TDSA','Masculino'),(3673159,'DAVI DE MENESES DOS SANTOS','3TDSB','Masculino'),(3673204,'JULIANA GABRIELLE ALVES BEZERRA','3MKTB','Feminino'),(3673228,'GABRIEL GUILHERME DA SILVA','3TDSA','Masculino'),(3673264,'MATHEUS YEHUDI CURSINO DE MELO','3TDSA','Masculino'),(3673282,'DYORGENNES MARCELL DE LIMA PINHEIRO FILHO','3TDSB','Masculino'),(3673285,'LUAN VITOR AFONSO DA SILVA','3TDSA','Masculino'),(3673295,'DAVY HENRIQUE LEITE DE MORAIS','3MKTA','Masculino'),(3673304,'MIGUEL DIAS VALENTIM','3MKTB','Masculino'),(3673377,'EWERTON FERREIRA GOMES DA SILVA','3TDSB','Masculino'),(3673598,'DAVID GABRIEL DA SILVA FLORENCIO','3TDSB','Masculino'),(3673620,'LUAN GABRIEL GOMES DOS SANTOS','3MKTA','Masculino'),(3673740,'GABRIEL HENRIQUE DOS SANTOS ROCHA','3TDSB','Masculino'),(3673810,'MICAEL GERONIMO SILVA','3TDSA','Masculino'),(3673876,'VINICIUS GABRIEL RAMOS MONTEIRO','3TDSB','Masculino'),(3673924,'NATHANAEL DAVI ANTONIO SILVA','3TDSA','Masculino'),(3673950,'DEYVID BERGSON MEDEIROS SANTOS','3TDSA','Masculino'),(3673987,'APHAEL FERREIRA ALVES','3TDSA','Masculino'),(3674110,'CAIQUE VINICIUS DA SILVA SANTOS','3TDSA','Masculino'),(3674376,'CARLOS DANIEL GENESIO DOS SANTOS','3MKTB','Masculino'),(3674449,'GEOVANNA SAMILLY DANIELLY DA SILVA','3MKTA','Feminino'),(3674506,'LARISSA NAYANE DOS SANTOS LIMA','3MKTB','Feminino'),(3674591,'RAFAELA FERNANDES RIBEIRO','3MKTA','Feminino'),(3674638,'EMILY FERNANDA DE OLIVEIRA FREIRE','3MKTA','Feminino'),(3674662,'MARIA GABRIELLA AVELINO DA SILVA','3MKTB','Feminino'),(3674670,'JAIANE SANTOS DA SILVA','3MKTB','Feminino'),(3674684,'GABRIEL FRANCISCO DA SILVA BEZERRA','3MKTA','Masculino'),(3674706,'JULLIA BEATRIZ SANTOS DE LIMA','3MKTB','Feminino'),(3674735,'DAVY RODRIGUES DA SILVA','3MKTA','Masculino'),(3674746,'MIGUEL DE ALMEIDA TABOSA CAVALCANTI','3TDSB','Masculino'),(3674758,'TAYNARA VITORIA FLORENCIO DA SILVA NASCIMENTO','3MKTB','Feminino'),(3674783,'RODRIGO DE SOUZA SILVA JUNIOR','3TDSA','Masculino'),(3674854,'ANA BEATRIZ BEZERRA DE LIMA','3MKTA','Feminino'),(3674860,'EMANUEL ALVES FELICIANO','3MKTA','Masculino'),(3674893,'MARIA ALICE ROSAS MENDES DE HOLANDA','3MKTA','Feminino'),(3674913,'BARBARA BEATRIZ DA SILVA NEVES','3MKTA','Feminino'),(3674932,'JOSE VINICIUS DA SILVA RODRIGUES','3MKTB','Masculino'),(3674953,'MARIA CLARA DE LIMA MELO','3MKTB','Feminino'),(3674972,'ANA LETICIA LOPES SALVADOR','3MKTA','Feminino'),(3674987,'EMYLLE REBECCA SILVA DE FREITAS','3MKTB','Feminino'),(3675022,'JALLYSON HIGOR RAMOS VENTURA','3TDSB','Masculino'),(3675127,'PEDRO VICTOR CORDEIRO DE MELO','3TDSA','Masculino'),(3675144,'HENRY KAUA NEPOMUCENO SOARES','3MKTB','Masculino'),(3675294,'LUCIO EMMANOEL GUEDES BISNETO','3MKTA','Masculino'),(3676328,'EMILY KAMILLY DE MORAIS OLIVEIRA','3TDSA','Feminino'),(3676656,'ANTONY KAUA MENDES DA SILVA COSTA','3TDSA','Masculino'),(3677057,'CAMILLA RAYSSA DE OLIVEIRA SILVA','3TDSA','Feminino'),(3677069,'MARIA CLARA FLORENCIO DE SOUZA','3TDSB','Feminino'),(3677087,'GUSTAVO HENRIQUE DA SILVA NOGUEIRA','3TDSA','Masculino'),(3677165,'EMANUELLY MARIA DE ARAUJO','3MKTA','Feminino'),(3677511,'MARIA VICTORIA TORRES DE MELO','3MKTA','Feminino'),(3677523,'YOHANAN EZEQUIEL OTAVIANO DO PRADO','3MKTA','Masculino'),(3677652,'CAIQUE JOAO DA SILVA','3TDSB','Masculino'),(3677816,'VICTOR MANOEL DA SILVA','3MKTA','Masculino'),(3677817,'RAFAELLA ALVES DA SILVA','3MKTB','Feminino'),(3677819,'INGRIDY WENDY MILANEZ SANTOS','3TDSB','Feminino'),(3714647,'LUIS FERNANDO DA SILVA MOURA','3TDSB','Masculino'),(3714650,'LUAN FELICIANO DE LIMA','3TDSB','Masculino'),(3714651,'DAYANE EMANUELA DA SILVA','3TDSA','Feminino'),(3714653,'JOELTON JONATAS ARAUJO DOS SANTOS','3TDSA','Masculino'),(3714654,'EVELYN CIBELLY FERREIRA DOS SANTOS','3MKTB','Feminino'),(3714656,'JADIELLY BEATRIZ DA SILVA AZEVEDO','3MKTA','Feminino'),(3714660,'VICTOR EDUARDO BEZERRA DE CARVALHO','3TDSA','Masculino'),(3714662,'ANA LUIZA MELO DA ROCHA','3TDSB','Feminino'),(3714664,'MARIA LUIZA BARBOSA DOS SANTOS','3MKTB','Feminino'),(3714666,'WESLEY VICTOR BEZERRA DA SILVA','3TDSB','Masculino'),(3714669,'GABRIEL KAUA DE ANDRADE SANTOS','3TDSA','Masculino'),(3714671,'GRAZIELLE MENEZES DA SILVA','3MKTB','Feminino'),(3714674,'ESTHER VIRGINIA ALVES FERREIRA','3MKTA','Feminino'),(3714677,'DIEGO BELMIRO DE LIMA','3TDSB','Masculino'),(3714683,'VITOR HENRIQUE MENEZES DA SILVA','3TDSB','Masculino'),(3714685,'NATHALY GABRIELLY GALVAO LIMA','3MKTA','Feminino'),(3714704,'ANDREA VITORIA LIMA DA SILVA','3MKTB','Feminino'),(3714708,'MARIA JULIA DOS SANTOS SILVA','3TDSA','Feminino'),(3714709,'PEDRO HENRIQUE BUARQUE DE OLIVEIRA','3TDSA','Masculino'),(3714710,'PEDRO HENRIQUE URBANO DA SILVA MOURA','3TDSB','Masculino'),(3714712,'JOANDERSON MANOEL SILVA','3TDSA','Masculino'),(3714714,'THAIS MARIA FELIX DA SILVA','3MKTA','Feminino'),(3714721,'ALLANA NICOLY DE BARROS SALVADOR','3MKTB','Feminino'),(3721956,'TAYLA CHARLICE DA SILVA','3TDSB','Feminino'),(3721957,'ISABELA VITÓRIA DO NASCIMENTO SILVA','3MKTB','Feminino'),(3722170,'KAUANE VITORIA SILVA','3MKTB','Feminino'),(3722547,'GUSTAVO VALENÇA DA SILVA','3MKTA','Masculino'),(3722548,'ISLA DA SILVA SANTOS','3TDSA','Feminino'),(3722552,'ENZO HENRIQUE DE SOUZA TAVARES','2TDSB','Masculino'),(3722554,'NICOLLY VAZ MIRANDA DA SILVA','3TDSB','Feminino'),(3723815,'HIAGO KAIQUE DOS SANTOS','3TDSB','Masculino'),(3738373,'JOAO PEDRO DA SILVA','2MKTB','Masculino'),(3759022,'LETÍCIA VIRGINYA DA SILVA ARAUJO','2MKTA','Feminino'),(3760069,'ANA LUIZA DE AZEVEDO MATIAS','2MKTA','Feminino'),(3771155,'ISAQUE CIPLISCIANO SILVA','1TDSA','Masculino'),(3786121,'JOSE CAIO MATHEUS VASCONCELOS DA SILVA','1TDSB','Masculino'),(3791715,'LUIZ GUSTAVO DOS SANTOS SILVA','2TDSB','Masculino'),(3804918,'YAGO BRUNO SILVA','2MKTB','Masculino'),(3820730,'ARTHUR MIGUEL FERREIRA SILVA','2TDSA','Masculino'),(3840420,'JOÃO MANOEL ANDRADE SALVADOR DA SILVA','2TDSB','Masculino'),(3867935,'LOUISE ALICE RODRIGUES BARROS','2MKTB','Feminino'),(3867941,'MARIA LUIZA SILVA FERREIRA DE MORAES','2MKTA','Feminino'),(3868068,'RHUAN GUILHERME VITORINO DA SILVA','2TDSB','Masculino'),(3868079,'DEVID FLORENCIO DOS SANTOS','2MKTA','Masculino'),(3868188,'MIKAEL HIAGO DE ANDRADE SILVA','2TDSB','Masculino'),(3868310,'NAILA CORDEIRO DE SOUZA PEIXOTO','2TDSA','Feminino'),(3868330,'JOSE GUILHERME SILVA','2TDSA','Masculino'),(3868382,'SOPHIA VALENTINA ROCHA LIMA DE SOUZA','2TDSA','Feminino'),(3868409,'CECILIA OHANA DOS SANTOS SILVA','2MKTB','Feminino'),(3868475,'ISABELY VITORIA CARDOSO LIMA','2TDSB','Feminino'),(3868531,'DAVID RUBENS FERREIRA DA SILVA','2TDSA','Masculino'),(3868621,'JULIA NERI BALBINO DE LIMA','2MKTB','Feminino'),(3868781,'JOAO VITOR BARBOSA SOUZA','2MKTA','Masculino'),(3868808,'ANA CAROLINA AZEVEDO','2MKTB','Feminino'),(3868831,'ERICK HENRIQUE DA SILVA AGUIAR','2TDSA','Masculino'),(3868849,'SAMUEL BARBOSA DA SILVA','2TDSB','Masculino'),(3868853,'MICHELLE ISABELLE CAMPOS DO NASCIMENTO','2TDSA','Feminino'),(3869619,'GERALDO AGOSTINHO DA SILVA SANTOS','2TDSA','Masculino'),(3869983,'LAURA BEATRIZ GUERRA DA SILVA','2MKTA','Feminino'),(3870014,'JOAO JULIAO DA SILVA FILHO','2MKTB','Masculino'),(3870122,'MARIA CLARA DA SILVA BARROS','2MKTB','Feminino'),(3870134,'ELOISA FARIAS LOPES','2MKTB','Feminino'),(3870199,'LAIS ISABELA BARBOSA VASCONCELOS','2MKTB','Feminino'),(3870239,'FERNANDA SANTOS MEDEIROS','2MKTA','Feminino'),(3870258,'JOAO VITOR PEREIRA DA SILVA','2MKTA','Masculino'),(3870266,'VITORIA RAQUEL DA SILVA','2MKTA','Feminino'),(3870282,'NADYNE FERREIRA DE LIMA','2MKTA','Feminino'),(3870290,'LARA TAVARES NASCIMENTO','2MKTA','Feminino'),(3870404,'LAILA JENNIFER DA SILVA','2MKTA','Feminino'),(3870416,'CARLOS ARTHUR EUSEBIO TEIXEIRA DE CARVALHO','2MKTA','Masculino'),(3870471,'YASMIM MARYANE DA SILVA SANTOS','2MKTB','Feminino'),(3870506,'EYSHILA VITORIA SANTIAGO XAVIER','2MKTB','Feminino'),(3870547,'NATANAEL FELIPE DA SILVA FILHO','2MKTB','Masculino'),(3870746,'RAFAEL RABELO QUEIROZ DE ANDRADE','2MKTA','Masculino'),(3870910,'ALESSA RIBEIRO DE ALMEIDA','2MKTB','Feminino'),(3870956,'DEISY VITORIA PEREIRA DA SILVA','2MKTA','Feminino'),(3870977,'ITHALO GABRIEL DOS ANJOS','2TDSB','Masculino'),(3871043,'MARIA LUIZA FIGUEIROA FORTUNA','2TDSA','Feminino'),(3871052,'ANA ELLAYNNE JULIA SILVA','2TDSB','Feminino'),(3871068,'ELIESER SILVA DE LIMA','2TDSA','Masculino'),(3871080,'LUCAS GABRIEL KAUAM SILVA DO NASCIMENTO','2TDSB','Masculino'),(3871087,'VICTOR MIGUEL RICARDO SILVA','2TDSA','Masculino'),(3871122,'MILENA VITORIA DE CARVALHO','2TDSB','Feminino'),(3871129,'DAVI GONÇALVES MAIA DE AGUIAR','2TDSB','Masculino'),(3871801,'KAUA ALEXANDRE DA SILVA','2TDSA','Masculino'),(3871818,'PAULO DANIEL GUEDES FERREIRA','2TDSB','Masculino'),(3871824,'PEDRO HENRIQUE VERAS ARAGAO FERREIRA','2TDSA','Masculino'),(3871883,'ESTHER MIRIAN RODRIGUES DA SILVA','2TDSB','Feminino'),(3871906,'GUSTAVO JUAN DE LIMA','2TDSA','Masculino'),(3871961,'GUILHERME LIRA DE OLIVEIRA','2TDSB','Masculino'),(3871974,'LUIZ GUSTAVO LIMA PIMENTEL DE ANDRADE','2TDSA','Masculino'),(3872035,'AUREO GUSTAVO SANTOS PIMENTEL','2TDSB','Masculino'),(3872058,'FILIPE PEREIRA DA SILVA','2TDSA','Masculino'),(3872102,'THIERRY VINICIOS EMANOEL PORTELA SILVA','2TDSA','Masculino'),(3872119,'SOFIA DE SOUSA DINIZ','2TDSA','Feminino'),(3872129,'CARLOS HENRIQUE DE SOUSA NOGUEIRA DOS SANTOS','2TDSB','Masculino'),(3872143,'PEDRO VITTOR DA SILVA','2TDSB','Masculino'),(3872150,'LUIZ EDUARDO DA SILVA','2TDSB','Masculino'),(3872227,'LUANA TAVARES DE ANDRADE','2TDSA','Feminino'),(3872239,'VITOR VINNICIUS TORRES SOUZA','2TDSA','Masculino'),(3872561,'LUIZ GUSTAVO MENDONCA MENEZES','2TDSB','Masculino'),(3872578,'DEXTER WOTSON LIMA GOMES','2TDSA','Masculino'),(3872592,'ANA BEATRIZ DOS SANTOS SILVA','2TDSA','Feminino'),(3872605,'LUCAS RIQUELMY LEITE DUTRA','2TDSB','Masculino'),(3872615,'HELOISA PEDROSA DA SILVA','2TDSB','Feminino'),(3872852,'AMANDA GABRIELE DA SILVA SANTOS','2MKTA','Feminino'),(3872858,'MARYA VICTORIA PAULINO DOS SANTOS','2TDSA','Feminino'),(3872874,'LEVI GOMES DE LIRA TAVARES','2TDSB','Masculino'),(3872880,'CAIO ILIDIO DE ASSIS','2MKTA','Masculino'),(3872900,'SIAMARA LETICIA FERREIRA DOS SANTOS','2TDSB','Feminino'),(3872949,'JULIA VITORIA MARTINS MENDES','2MKTB','Feminino'),(3872986,'MAYANE CRISTINA DE SOUZA SANTOS','2MKTA','Feminino'),(3872999,'ANTHONY GABRIEL HONORIO DA SILVA LIMA','2MKTA','Masculino'),(3873035,'PAMELA MAYSA ARAUJO DOS SANTOS','2MKTB','Feminino'),(3873111,'PYETRO GABRIEL DE LIMA NUNES','2TDSA','Masculino'),(3873113,'GUILHERME ROBERTO DE ALMEIDA SATURNINO','2MKTA','Masculino'),(3873130,'NYCOLLAS CAUA ALVES DE LIRA','2TDSB','Masculino'),(3873132,'PEDRO MIGUEL CARLOS VIANA','2MKTA','Masculino'),(3873150,'BRUNO VINICIOS MENDES BELCHIOR','2TDSB','Masculino'),(3873169,'ENIO DE AGUIAR SILVA FILHO','2TDSB','Masculino'),(3873208,'JOAO FELIPE CAVALCANTE DE SIQUEIRA NUNES','2MKTA','Masculino'),(3873229,'ANNA SOPHIA SANTANA DE LIMA','2MKTB','Feminino'),(3873248,'ANA LUISA TEIXEIRA FERREIRA','2MKTB','Feminino'),(3873456,'ISAC DE LIRA SANTOS','2TDSB','Masculino'),(3873496,'MARTA SALES LEOTE CAVACO','2TDSA','Feminino'),(3873512,'MILENA HELOA PEREIRA DA SILVA','2TDSA','Feminino'),(3873565,'RENATO TARSIS DE OLIVEIRA ALMEIDA','2TDSA','Masculino'),(3873653,'NIKOLAS RAPHAEL NARCISO RODRIGUES','2TDSA','Masculino'),(3873671,'MARIANA VITORIA BEZERRA SILVA','2MKTA','Feminino'),(3873815,'VITORIA MELISSA BARBOSA BEZERRA','2MKTB','Feminino'),(3873887,'ANA CAROLINA BARBOZA DA SILVA','2TDSB','Feminino'),(3873910,'MATHEUS DAVI MAZUQUIEL DE LIMA','2TDSB','Masculino'),(3873926,'LIVIA PAULINA VASCONCELOS DE OLIVEIRA','2MKTB','Feminino'),(3873936,'INGRID GISELLY SILVA','2MKTB','Feminino'),(3873938,'ANA CLARA OLIVEIRA VALENCA','2MKTB','Feminino'),(3873954,'ANDRAYDE RHENAN DE LIMA FERNANDES','2MKTB','Masculino'),(3873969,'ANA MAISA BARBOSA DA SILVA','2MKTB','Feminino'),(3873981,'MARIA GEOVANA BEZERRA FERREIRA','2MKTB','Feminino'),(3873991,'LAVINIA CAVALCANTE FERREIRA','2MKTA','Feminino'),(3874087,'JOHN CHRISTIAN NICACIO BARBOSA DA SILVA','2MKTA','Masculino'),(3874655,'CARLOS DAVI ALVES DE SOUZA','2TDSA','Masculino'),(3874656,'STHEFFANY SUELLEN VIEIRA PORTELA OLIVEIRA','2TDSA','Feminino'),(3874657,'LAURA GABRIELLA NASCIMENTO SILVA','2TDSB','Feminino'),(3874670,'MATEUS HENRIQUE FERREIRA BRITO','2MKTB','Masculino'),(3874682,'ANA MONALIZA OLIVEIRA DO VALE','2MKTA','Feminino'),(3874686,'ANA CECILIA SANTOS MARTINEZ','2MKTA','Feminino'),(3874899,'DAVI SANTANA FAUSTINO DA COSTA','2TDSA','Masculino'),(3874929,'PEDRO HENRIQUE SILVA','2TDSB','Masculino'),(3874939,'ARTHUR ANTONIO DOS SANTOS','2TDSB','Masculino'),(3875000,'JOAO MARCELINO DE LIMA NETO','2TDSA','Masculino'),(3875007,'ISABELA TRESSOLDI DE MACEDO','2MKTA','Feminino'),(3875026,'GIOVANNA JUNIELLY FLORENCIO DE OLIVEIRA','2TDSB','Feminino'),(3875037,'EDUARDO NASCIMENTO DE LIMA','2TDSA','Masculino'),(3875048,'ALLANA VITÓRIA BARBOSA DE LIMA','2MKTA','Feminino'),(3875059,'MARIA EDUARDA DA SILVA LIRA','2TDSB','Feminino'),(3875264,'MIGUEL MARCIO MELO DA SILVA','2TDSA','Masculino'),(3875270,'YASMIM GABRIELY DE MELO SILVA','2MKTA','Feminino'),(3875277,'CHRISTIAN GABRIEL SANTOS SILVA','2MKTA','Masculino'),(3875472,'PEDRO HENRIQUE ARAUJO DE MELO','2MKTA','Masculino'),(3875476,'PAULO ERNESTO SOUZA DE AMORIM','2TDSA','Masculino'),(3875478,'EMANUELLA BATISTA DA SILVA','2MKTA','Feminino'),(3875483,'GHENESYS RELRISON CONRADO','2MKTB','Masculino'),(3875593,'JULIA AGNES SANTOS DE FRANCA','2MKTB','Feminino'),(3875595,'EVANDREY GUSTAVO DE LIMA ANDRADE','2MKTA','Masculino'),(3881402,'LUCAS OLIVEIRA LIRA','2TDSA','Masculino'),(3881404,'EMILLY LAVINIA SILVA GOMES','2MKTB','Feminino'),(3881405,'DEIVISON GUSTAVO CUSTODIO DA SILVA','2MKTA','Masculino'),(3881407,'GABRIEL ARAUJO BEZERRA SANTOS','2MKTB','Masculino'),(3881408,'LORRAINY VITÓRIA DOS SANTOS DO NASCIMENTO','2MKTB','Feminino'),(3881410,'ASHLEY HAIUMY DE OLIVEIRA SILVESTRE','2TDSA','Feminino'),(3881412,'JOAO VITOR RODRIGUES DE LIMA','2TDSA','Masculino'),(3881415,'MAISA SABRINA DA SILVA','2TDSB','Feminino'),(3881416,'STEPHANI VITORIA GOMES LOPES','2TDSB','Feminino'),(3881419,'JOSE WILLIAN RAMOS DA SILVA','2TDSA','Masculino'),(3881422,'ANA STELLA FARIAS LIMA RAMOS','2TDSA','Feminino'),(3881423,'ALLANNA BEATRIZ COUTO SILVA','2MKTB','Feminino'),(3881426,'PEDRO FELIPE DO NASCIMENTO MOTA','2MKTB','Masculino'),(3881428,'JOAO VITOR LUIZ DA SILVA','2MKTB','Masculino'),(3881430,'JULIA GRAZIELE SALVINO DE OLIVEIRA','2MKTA','Feminino'),(3881431,'GABRIEL GUIMARAES ALCOFORADO','2TDSB','Masculino'),(3881433,'AMANDA PATRICIA PALHARIM BRITO','2MKTB','Feminino'),(3891324,'LAIS REGINA TENÓRIO DE MELO','2MKTB','Feminino'),(3891799,'JOANA D ARC COSTA DA SILVA','2MKTA','Feminino'),(3892382,'Maria Antonia Bezerra da Silva','2TDSA','Feminino'),(3914526,'OTÁVIO HENRIQUE DA SILVA','1TDSB','Masculino'),(3920150,'GABRIEL ALEXANDRE ESPINDOLA SILVA','1TDSA','Masculino'),(3920938,'HEVERTON RUBENS SILVA','1TDSA','Masculino'),(3921137,'AWINY KETLLIN FLORENCIO DA SILVA','1TDSA','Feminino'),(3936845,'MARIANA VITORIA DA SILVA LOURENCO','1TDSA','Feminino'),(3944723,'José Bruno Marques Oliveira Melo','1TDSA','Masculino'),(3957780,'THALLYSON HENRIQUE MARQUES PEREIRA','1TDSA','Masculino'),(3978054,'PEDRO HENRIQUE LIMA ARAUJO','1TDSA','Masculino'),(3999926,'MIGUEL HENRIQUE SANTOS LIMA','1TDSB','Masculino'),(4000994,'MANUELA DE FREITAS CHAVES MOURA','1TDSA','Feminino'),(4003563,'NATHAN SAMUEL ROGRIGUES TORRES','1TDSA','Masculino'),(4009761,'IGOR VINICIUS FERREIRA CLAUDINO','1TDSA','Masculino'),(4009773,'BRUNO RAFAEL ARAUJO DE QUEIROZ','1TDSB','Masculino'),(4009774,'KETHILYN KAWANY MUNIZ SILVA','1TDSB','Feminino'),(4009775,'AYLA EDUARDA ALENCAR GOMES','1TDSB','Feminino'),(4009776,'ALEXANDRE GALVAO DOS SANTOS COSTA JUNIOR','1TDSB','Masculino'),(4009777,'JOAO MATHEUS DA SILVA ALCANTARA','1TDSB','Masculino'),(4009778,'JANIELLY SOBRAL FERREIRA SOBRINHO','1TDSA','Feminino'),(4009779,'SAMUEL DAVI MEZA SILVA','1TDSB','Masculino'),(4009780,'MARIA CLARA CALMON VILELA DOS SANTOS','1TDSA','Feminino'),(4009787,'LUIS HENRIQUE FARIAS MARQUES','1TDSB','Masculino'),(4009788,'RUBENS ROBERTO QUIXABEIRA DE AZEVEDO SILVA','1TDSA','Masculino'),(4009791,'MATHEUS HENRIQUE DA SILVA NASCIMENTO','1TDSA','Masculino'),(4009792,'AINALLY LAVINIA VENANCIO DE LIMA','1TDSB','Feminino'),(4009793,'PAULO CESAR SANTOS BARROS FILHO','1TDSB','Masculino'),(4009795,'GEOVANA GABRIELEN DA SILVA','1TDSA','Feminino'),(4009796,'JOAO GUILHERME LUIZ DA SILVA','1TDSA','Masculino'),(4009797,'IURI REIS DE LIRA SILVA','1TDSB','Masculino'),(4009798,'ARTUR GUILHERME MENEZES RAMOS','1TDSB','Masculino'),(4009799,'JHONATA SOUZA DE OLIVEIRA','1TDSB','Masculino'),(4009800,'GEAM LUCAS ALVES ALEXANDRE','1TDSA','Masculino'),(4009802,'RAFAELLY FIGUEIROA DE MELO SILVA','1TDSA','Feminino'),(4009828,'RAVI EMANOEL DOS SANTOS SILVA','1TDSA','Masculino'),(4009829,'DEIVIDY ANDERSON DA SILVA','1TDSB','Masculino'),(4009831,'SAULO DAVI CUNHA FIGUEREDO','1TDSA','Masculino'),(4009833,'THYAGO LUIZ DA SILVA GOMES','1TDSB','Masculino'),(4009834,'MIQUEAS ABRAAO SANTOS ALVES SILVA','1TDSA','Masculino'),(4009835,'LUIZ GUSTAVO DE LIMA AURELIANO','1TDSA','Masculino'),(4009836,'NATHALIA ALVES DA SILVA','1TDSB','Feminino'),(4009837,'LUAN VINICIOS SILVA DE OLIVEIRA','1TDSB','Masculino'),(4009838,'ARTHUR JOSE GOMES','1TDSB','Masculino'),(4009840,'MATEUS HENRICK FELICIANO SILVA','1TDSB','Masculino'),(4009841,'NATAN GUILHERME DOS SANTOS SILVA','1TDSA','Masculino'),(4009842,'EDUARDO DA SILVA SANTOS','1TDSA','Masculino'),(4009843,'NYCOLLAS GABRIEL DOS SANTOS SILVA','1TDSA','Masculino'),(4009853,'LUAN MATEUS RODRIGUES BARROS','1TDSA','Masculino'),(4009855,'VIVIANE FABIANA DA SILVA MARQUES','1TDSA','Feminino'),(4009856,'SIWANNE LETICIA DE MELO DA SILVA','1TDSB','Feminino'),(4009857,'LUAN CARLOS VICENTE BARBOSA','1TDSB','Masculino'),(4009859,'ERICK DAVI GALVÃO LIMA','1TDSA','Masculino'),(4009869,'VITORIA GABRIELLY SOARES DA SILVA','1TDSB','Feminino'),(4009870,'SAMUEL MARTINS DA SILVA','1TDSA','Masculino'),(4009871,'PEDRO MIGUEL DE MELO SILVA','1TDSB','Masculino'),(4009872,'CESAR GABRIEL SOUTO DOS SANTOS','1TDSB','Masculino'),(4009879,'ISAAC BRUNO OLIVEIRA DA SILVA','1TDSA','Masculino'),(4009880,'HELENA ALVES RIBEIRO VILA NOVA','1TDSB','Feminino'),(4009881,'HELLEN BEATRIZ SILVA SANTOS','1TDSA','Feminino'),(4009886,'LUCAS RAFAEL DA SILVA GUERRA','1TDSB','Masculino'),(4009891,'NICOLLAS KEVIN DE CARVALHO SILVA','1TDSB','Masculino'),(4009898,'KAYO FELIPE DOS SANTOS LACERDA','1TDSA','Masculino'),(4009907,'PEDRO HENRIQUE BANDEIRA SILVA DE SANTANA','1TDSB','Masculino'),(4009908,'ISAAC WISLLEY SOARES SILVA','1TDSB','Masculino'),(4009909,'TOMAZ HENRIQUE CALUMBI TAVARES','1TDSB','Masculino'),(4009910,'LUIS HENRIQUE DE LIMA','1TDSB','Masculino'),(4009911,'KAROLAYNE ALLANE SILVA','1TDSB','Feminino'),(4009916,'ADRIELLY TAWANE GALINDO DUQUE','1TDSB','Feminino'),(4009920,'EVANDRO HENRIQUE OLIVEIRA AGUIAR DE LIMA','1TDSB','Masculino'),(4009921,'MARIA CLARA DE SOUSA CARDOZO','1TDSB','Feminino'),(4009922,'WALLESCA RAYANE SILVA DE OLIVEIRA','1TDSA','Feminino'),(4009923,'YAN AMBROSIO DE BRITO','1TDSB','Masculino'),(4009924,'ALUIZIO JACINTO LUCENA','1TDSA','Masculino'),(4009925,'MAYSA ELLEN GOMES SILVA','1TDSB','Feminino'),(4039538,'RIANN LAEL BEZERRA DANTAS DE QUEIROZ','1TDSA','Masculino'),(4051268,'Yosef Calinalwan','1TDSB','Masculino'),(4053219,'Larissa Silva Santos','1TDSA','Feminino'),(4064624,'MIGUEL SILVA DE LIMA','1TDSA','Masculino'),(67676767,'Mero Betinha','3TDSA','Masculino');
/*!40000 ALTER TABLE `alunos` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `calendario`
--

LOCK TABLES `calendario` WRITE;
/*!40000 ALTER TABLE `calendario` DISABLE KEYS */;
/*!40000 ALTER TABLE `calendario` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `classificacao`
--

LOCK TABLES `classificacao` WRITE;
/*!40000 ALTER TABLE `classificacao` DISABLE KEYS */;
INSERT INTO `classificacao` VALUES ('Feminino'),('Masculino'),('Misto');
/*!40000 ALTER TABLE `classificacao` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `configuracoes`
--

LOCK TABLES `configuracoes` WRITE;
/*!40000 ALTER TABLE `configuracoes` DISABLE KEYS */;
INSERT INTO `configuracoes` VALUES ('inicio_prazo_edicao_equipes','2026-08-03 22:48:58'),('prazo_edicao_equipes','40');
/*!40000 ALTER TABLE `configuracoes` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `esportes`
--

LOCK TABLES `esportes` WRITE;
/*!40000 ALTER TABLE `esportes` DISABLE KEYS */;
INSERT INTO `esportes` VALUES ('Basquete','Coletivo',10),('Futsal','Coletivo',10),('Handebol','Coletivo',10),('Queimada','Coletivo',10),('Tênis de Mesa','Individual',1),('Vôlei','Coletivo',10),('Xadrez','Individual',1);
/*!40000 ALTER TABLE `esportes` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `estatisticas_esporte`
--

LOCK TABLES `estatisticas_esporte` WRITE;
/*!40000 ALTER TABLE `estatisticas_esporte` DISABLE KEYS */;
INSERT INTO `estatisticas_esporte` VALUES ('Basquete','Arremessos de Três'),('Queimada','Eliminações'),('Futsal','Finalizações'),('Futsal','Gols'),('Basquete','Passes'),('Futsal','Passes'),('Basquete','Pontos'),('Tênis de Mesa','Sets'),('Xadrez','Sets');
/*!40000 ALTER TABLE `estatisticas_esporte` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inscricoes_provas_atletismo`
--

LOCK TABLES `inscricoes_provas_atletismo` WRITE;
/*!40000 ALTER TABLE `inscricoes_provas_atletismo` DISABLE KEYS */;
/*!40000 ALTER TABLE `inscricoes_provas_atletismo` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('adm','adm','Administrador',NULL),('gio@gmail.com','212121','AlunoMonitor','1MKTB'),('Monitor','monitor','AlunoMonitor','3TDSA'),('monitor2','monitor2','AlunoMonitor','2TDSA'),('Pinheiro','123456','Administrador',NULL),('ryan','123','AlunoMonitor','3TDSB'),('teste6','6666666','Administrador',NULL),('testeMetodo','100002','AlunoMonitor','1TDSB');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `membros_equipe`
--

LOCK TABLES `membros_equipe` WRITE;
/*!40000 ALTER TABLE `membros_equipe` DISABLE KEYS */;
INSERT INTO `membros_equipe` VALUES (165,2734262),(149,2734267),(152,2734267),(158,2734267),(164,2734267),(172,2734267),(149,2820692),(152,2820692),(158,2820692),(164,2820692),(276,2849098),(184,3017763),(254,3017763),(150,3139436),(163,3139436),(173,3139436),(175,3142848),(159,3148465),(209,3252826),(130,3265475),(264,3265475),(165,3275800),(182,3275800),(224,3312845),(226,3312845),(229,3312845),(232,3312845),(240,3312845),(146,3427219),(148,3427219),(156,3427219),(200,3427219),(209,3599496),(157,3670459),(168,3670459),(112,3670471),(224,3670494),(226,3670494),(229,3670494),(232,3670494),(240,3670494),(256,3670494),(107,3670508),(149,3670629),(152,3670629),(158,3670629),(164,3670629),(258,3670647),(149,3671136),(152,3671136),(158,3671136),(164,3671136),(131,3671323),(152,3671323),(158,3671323),(164,3671323),(149,3671347),(152,3671347),(158,3671347),(164,3671347),(146,3671486),(148,3671486),(156,3671486),(200,3671486),(109,3671609),(120,3671646),(200,3671646),(276,3671646),(259,3671657),(260,3671657),(261,3671657),(106,3671760),(157,3671760),(168,3671760),(182,3671760),(146,3672624),(156,3672624),(149,3672631),(207,3672634),(182,3672644),(158,3672649),(240,3672658),(258,3672658),(259,3672658),(260,3672658),(261,3672658),(144,3672660),(185,3672660),(186,3672660),(149,3672661),(152,3672661),(158,3672661),(164,3672661),(240,3672662),(258,3672662),(259,3672662),(260,3672662),(261,3672662),(165,3672762),(168,3672762),(276,3672888),(240,3672943),(258,3672943),(261,3672943),(146,3673042),(148,3673042),(156,3673042),(115,3673159),(148,3673159),(258,3673204),(259,3673204),(260,3673204),(261,3673204),(108,3673228),(157,3673228),(168,3673228),(165,3673285),(179,3673295),(185,3673295),(186,3673295),(224,3673304),(226,3673304),(229,3673304),(232,3673304),(240,3673304),(200,3673377),(148,3673598),(167,3673620),(179,3673620),(185,3673620),(186,3673620),(105,3673810),(165,3673924),(168,3673924),(157,3673987),(165,3673987),(168,3673987),(182,3673987),(157,3674110),(224,3674376),(226,3674376),(229,3674376),(232,3674376),(167,3674638),(258,3674662),(259,3674662),(260,3674662),(261,3674662),(258,3674670),(259,3674670),(261,3674670),(143,3674684),(167,3674684),(185,3674684),(179,3674735),(185,3674735),(186,3674735),(141,3674860),(167,3674860),(179,3674860),(185,3674860),(186,3674860),(224,3674932),(226,3674932),(229,3674932),(232,3674932),(240,3674932),(149,3674972),(152,3674972),(158,3674972),(164,3674972),(146,3675022),(148,3675022),(156,3675022),(200,3675022),(157,3675127),(104,3675144),(224,3675144),(226,3675144),(229,3675144),(232,3675144),(240,3675144),(255,3675144),(135,3675294),(167,3675294),(179,3675294),(185,3675294),(186,3675294),(182,3676328),(168,3676656),(182,3677057),(122,3677069),(276,3677069),(157,3677087),(165,3677087),(182,3677087),(167,3677165),(149,3677511),(152,3677511),(158,3677511),(164,3677511),(167,3677523),(179,3677523),(185,3677523),(186,3677523),(116,3677652),(167,3677816),(179,3677816),(185,3677816),(186,3677816),(190,3677816),(276,3677819),(146,3714647),(148,3714647),(182,3714651),(165,3714653),(168,3714653),(182,3714653),(149,3714656),(152,3714656),(164,3714656),(157,3714660),(165,3714660),(168,3714660),(200,3714662),(276,3714662),(146,3714666),(148,3714666),(156,3714666),(200,3714666),(110,3714669),(168,3714669),(146,3714683),(148,3714683),(156,3714683),(200,3714683),(210,3714683),(240,3714704),(258,3714704),(260,3714704),(157,3714709),(146,3714710),(156,3714710),(211,3714710),(157,3714712),(165,3714712),(182,3714712),(167,3714714),(240,3714721),(258,3714721),(259,3714721),(276,3721956),(258,3722170),(261,3722170),(142,3722547),(167,3722547),(179,3722547),(185,3722547),(186,3722547),(193,3722547),(266,3722552),(271,3722552),(274,3722552),(124,3722554),(200,3722554),(276,3722554),(146,3723815),(148,3723815),(156,3723815),(200,3723815),(206,3723815),(184,3759022),(215,3759022),(245,3759022),(254,3759022),(184,3760069),(215,3760069),(231,3804918),(235,3804918),(239,3804918),(241,3804918),(242,3804918),(262,3840420),(265,3840420),(266,3840420),(274,3840420),(189,3867935),(209,3867935),(231,3867935),(184,3867941),(262,3868068),(265,3868068),(266,3868068),(274,3868068),(243,3868079),(244,3868079),(264,3868188),(132,3868310),(201,3868310),(220,3868310),(225,3868310),(209,3868409),(273,3868475),(189,3868621),(194,3868621),(218,3868621),(246,3868781),(162,3868831),(169,3868831),(180,3868831),(188,3868831),(201,3868831),(214,3868831),(162,3869619),(169,3869619),(254,3869983),(231,3870014),(239,3870014),(242,3870014),(209,3870134),(189,3870199),(194,3870199),(209,3870199),(218,3870199),(215,3870239),(254,3870239),(198,3870258),(253,3870258),(171,3870416),(198,3870416),(243,3870416),(244,3870416),(231,3870506),(235,3870547),(239,3870547),(241,3870547),(242,3870547),(198,3870746),(243,3870746),(248,3870746),(262,3870977),(265,3870977),(134,3871043),(220,3871043),(222,3871043),(273,3871052),(266,3871080),(188,3871087),(264,3871129),(274,3871129),(265,3871818),(272,3871883),(273,3871883),(180,3871906),(188,3871906),(201,3871906),(216,3871906),(264,3871961),(274,3871961),(162,3871974),(169,3871974),(180,3871974),(188,3871974),(201,3871974),(180,3872058),(201,3872058),(129,3872102),(136,3872119),(201,3872119),(220,3872119),(264,3872129),(274,3872129),(262,3872143),(264,3872143),(265,3872143),(266,3872143),(274,3872143),(220,3872227),(222,3872227),(162,3872239),(180,3872239),(188,3872239),(201,3872239),(264,3872561),(139,3872592),(201,3872592),(220,3872592),(222,3872592),(262,3872605),(264,3872605),(265,3872605),(274,3872605),(273,3872615),(254,3872852),(262,3872874),(264,3872874),(265,3872874),(266,3872874),(274,3872874),(171,3872880),(198,3872880),(243,3872880),(244,3872880),(245,3872880),(266,3872900),(272,3872900),(273,3872900),(171,3872999),(198,3872999),(252,3872999),(162,3873111),(169,3873111),(180,3873111),(188,3873111),(201,3873111),(243,3873113),(244,3873113),(269,3873130),(171,3873132),(198,3873132),(243,3873132),(244,3873132),(245,3873132),(250,3873132),(265,3873169),(268,3873169),(274,3873169),(171,3873208),(244,3873208),(189,3873229),(209,3873229),(231,3873229),(189,3873248),(194,3873248),(218,3873248),(222,3873496),(220,3873512),(222,3873512),(162,3873653),(169,3873653),(180,3873653),(188,3873653),(208,3873653),(273,3873887),(262,3873910),(265,3873910),(270,3873910),(231,3873926),(209,3873938),(235,3873954),(239,3873954),(241,3873954),(242,3873954),(189,3873969),(194,3873969),(209,3873969),(218,3873969),(231,3873981),(184,3873991),(215,3873991),(245,3873991),(254,3873991),(171,3874087),(198,3874087),(243,3874087),(244,3874087),(245,3874087),(162,3874655),(169,3874655),(188,3874655),(266,3874657),(272,3874657),(273,3874657),(184,3874682),(215,3874682),(254,3874682),(254,3874686),(266,3874929),(262,3874939),(264,3874939),(267,3874939),(162,3875000),(169,3875000),(180,3875000),(188,3875000),(212,3875000),(162,3875037),(169,3875037),(125,3875048),(272,3875059),(273,3875059),(180,3875264),(184,3875270),(215,3875270),(171,3875472),(198,3875472),(243,3875472),(245,3875472),(249,3875472),(169,3875476),(201,3875476),(215,3875478),(245,3875478),(254,3875478),(235,3875483),(239,3875483),(241,3875483),(242,3875483),(231,3875593),(171,3875595),(198,3875595),(243,3875595),(244,3875595),(245,3875595),(251,3875595),(209,3881404),(171,3881405),(198,3881405),(247,3881405),(235,3881407),(239,3881407),(241,3881407),(242,3881407),(189,3881408),(194,3881408),(218,3881408),(231,3881408),(272,3881415),(266,3881416),(272,3881416),(273,3881416),(162,3881419),(169,3881419),(180,3881419),(188,3881419),(145,3881422),(126,3881426),(231,3881426),(235,3881426),(239,3881426),(241,3881426),(242,3881426),(254,3881430),(265,3881431),(128,3881433),(184,3891799),(215,3891799),(220,3892382),(222,3892382),(227,3914526),(155,3921137),(173,3921137),(155,3936845),(163,3957780),(183,3999926),(196,3999926),(119,4003563),(150,4003563),(173,4003563),(275,4009761),(137,4009773),(213,4009773),(227,4009775),(183,4009777),(213,4009777),(155,4009778),(196,4009787),(203,4009787),(275,4009788),(163,4009791),(275,4009791),(183,4009793),(196,4009793),(213,4009793),(155,4009795),(173,4009795),(238,4009797),(183,4009798),(196,4009798),(213,4009798),(227,4009798),(233,4009798),(196,4009799),(163,4009800),(173,4009800),(203,4009833),(234,4009833),(150,4009835),(163,4009835),(227,4009836),(183,4009837),(196,4009837),(213,4009837),(138,4009838),(140,4009840),(183,4009840),(203,4009840),(213,4009840),(159,4009841),(163,4009841),(173,4009841),(174,4009841),(159,4009842),(150,4009843),(159,4009843),(173,4009843),(150,4009853),(159,4009853),(163,4009853),(173,4009853),(196,4009857),(227,4009857),(203,4009872),(178,4009879),(196,4009886),(213,4009886),(227,4009886),(237,4009886),(183,4009891),(196,4009891),(203,4009891),(227,4009907),(183,4009908),(213,4009908),(183,4009909),(196,4009909),(227,4009911),(227,4009916),(203,4009920),(155,4009922),(173,4009922),(133,4009923),(123,4009924),(150,4009924),(159,4009924),(173,4009924),(159,4039538),(176,4039538),(183,4051268),(227,4051268),(155,4053219);
/*!40000 ALTER TABLE `membros_equipe` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modalidades_atletismo`
--

LOCK TABLES `modalidades_atletismo` WRITE;
/*!40000 ALTER TABLE `modalidades_atletismo` DISABLE KEYS */;
INSERT INTO `modalidades_atletismo` VALUES (1,'Corrida','Modalidades de corrida do atletismo',1),(3,'Salto','Modalidades de salto',1),(4,'Arremesso','Modalidades de arremesso',1),(8,'Natação','Esporte olímpico de natação',1);
/*!40000 ALTER TABLE `modalidades_atletismo` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=861 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partidas`
--

LOCK TABLES `partidas` WRITE;
/*!40000 ALTER TABLE `partidas` DISABLE KEYS */;
INSERT INTO `partidas` VALUES (636,'Xadrez','Feminino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,4,NULL,NULL,NULL),(637,'Xadrez','Feminino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,636,NULL,NULL),(638,'Xadrez','Feminino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,636,NULL,NULL),(639,'Xadrez','Feminino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,2,637,NULL,NULL),(640,'Xadrez','Feminino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,2,637,NULL,NULL),(641,'Xadrez','Feminino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,2,638,NULL,NULL),(642,'Xadrez','Feminino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,2,638,NULL,NULL),(643,'Xadrez','Feminino',120,118,NULL,NULL,'nao',NULL,NULL,1,639,NULL,NULL),(644,'Xadrez','Feminino',121,131,NULL,NULL,'nao',NULL,NULL,1,639,NULL,NULL),(645,'Xadrez','Feminino',145,111,NULL,NULL,'nao',NULL,NULL,1,640,NULL,NULL),(646,'Xadrez','Feminino',139,128,NULL,NULL,'nao',NULL,NULL,1,640,NULL,NULL),(647,'Xadrez','Feminino',117,124,NULL,NULL,'nao',NULL,NULL,1,641,NULL,NULL),(648,'Xadrez','Feminino',122,125,NULL,NULL,'nao',NULL,NULL,1,641,NULL,NULL),(649,'Xadrez','Feminino',132,134,NULL,NULL,'nao',NULL,NULL,1,642,NULL,NULL),(650,'Xadrez','Feminino',112,136,NULL,NULL,'nao',NULL,NULL,1,642,NULL,NULL),(651,'Vôlei','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,4,NULL,NULL,NULL),(652,'Vôlei','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,651,NULL,NULL),(653,'Vôlei','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,651,NULL,NULL),(654,'Vôlei','Masculino',163,180,NULL,NULL,'nao',NULL,NULL,2,652,NULL,NULL),(655,'Vôlei','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,2,652,NULL,NULL),(656,'Vôlei','Masculino',156,NULL,NULL,NULL,'nao',NULL,NULL,2,653,NULL,NULL),(657,'Vôlei','Masculino',185,168,NULL,NULL,'nao',NULL,NULL,2,653,NULL,NULL),(658,'Vôlei','Masculino',163,NULL,NULL,NULL,'sim',NULL,NULL,1,654,163,NULL),(659,'Vôlei','Masculino',180,NULL,NULL,NULL,'sim',NULL,NULL,1,654,180,NULL),(660,'Vôlei','Masculino',229,239,NULL,NULL,'nao',NULL,NULL,1,655,NULL,NULL),(661,'Vôlei','Masculino',203,243,NULL,NULL,'nao',NULL,NULL,1,655,NULL,NULL),(662,'Vôlei','Masculino',156,NULL,NULL,NULL,'sim',NULL,NULL,1,656,156,NULL),(663,'Vôlei','Masculino',199,264,NULL,NULL,'nao',NULL,NULL,1,656,NULL,NULL),(664,'Vôlei','Masculino',185,NULL,NULL,NULL,'sim',NULL,NULL,1,657,185,NULL),(665,'Vôlei','Masculino',168,NULL,NULL,NULL,'sim',NULL,NULL,1,657,168,NULL),(666,'Vôlei','Feminino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,4,NULL,NULL,NULL),(667,'Vôlei','Feminino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,666,NULL,NULL),(668,'Vôlei','Feminino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,666,NULL,NULL),(669,'Vôlei','Feminino',228,158,NULL,NULL,'nao',NULL,NULL,2,667,NULL,NULL),(670,'Vôlei','Feminino',222,254,NULL,NULL,'nao',NULL,NULL,2,667,NULL,NULL),(671,'Vôlei','Feminino',NULL,155,NULL,NULL,'nao',NULL,NULL,2,668,NULL,NULL),(672,'Vôlei','Feminino',219,209,NULL,NULL,'nao',NULL,NULL,2,668,NULL,NULL),(673,'Vôlei','Feminino',228,NULL,NULL,NULL,'sim',NULL,NULL,1,669,228,NULL),(674,'Vôlei','Feminino',158,NULL,NULL,NULL,'sim',NULL,NULL,1,669,158,NULL),(675,'Vôlei','Feminino',222,NULL,NULL,NULL,'sim',NULL,NULL,1,670,222,NULL),(676,'Vôlei','Feminino',254,NULL,NULL,NULL,'sim',NULL,NULL,1,670,254,NULL),(677,'Vôlei','Feminino',260,273,NULL,NULL,'nao',NULL,NULL,1,671,NULL,NULL),(678,'Vôlei','Feminino',155,NULL,NULL,NULL,'sim',NULL,NULL,1,671,155,NULL),(679,'Vôlei','Feminino',219,NULL,NULL,NULL,'sim',NULL,NULL,1,672,219,NULL),(680,'Vôlei','Feminino',209,NULL,NULL,NULL,'sim',NULL,NULL,1,672,209,NULL),(681,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,6,NULL,NULL,NULL),(682,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,5,681,NULL,NULL),(683,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,5,681,NULL,NULL),(684,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,4,682,NULL,NULL),(685,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,4,682,NULL,NULL),(686,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,4,683,NULL,NULL),(687,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,4,683,NULL,NULL),(688,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,684,NULL,NULL),(689,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,684,NULL,NULL),(690,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,685,NULL,NULL),(691,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,685,NULL,NULL),(692,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,686,NULL,NULL),(693,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,686,NULL,NULL),(694,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,687,NULL,NULL),(695,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,687,NULL,NULL),(696,'Tênis de Mesa','Masculino',252,174,NULL,NULL,'nao',NULL,NULL,2,688,NULL,NULL),(697,'Tênis de Mesa','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,2,688,NULL,NULL),(698,'Tênis de Mesa','Masculino',NULL,193,NULL,NULL,'nao',NULL,NULL,2,689,NULL,NULL),(699,'Tênis de Mesa','Masculino',207,210,NULL,NULL,'nao',NULL,NULL,2,689,NULL,NULL),(700,'Tênis de Mesa','Masculino',267,247,NULL,NULL,'nao',NULL,NULL,2,690,NULL,NULL),(701,'Tênis de Mesa','Masculino',212,NULL,NULL,NULL,'nao',NULL,NULL,2,690,NULL,NULL),(702,'Tênis de Mesa','Masculino',271,205,NULL,NULL,'nao',NULL,NULL,2,691,NULL,NULL),(703,'Tênis de Mesa','Masculino',206,251,NULL,NULL,'nao',NULL,NULL,2,691,NULL,NULL),(704,'Tênis de Mesa','Masculino',238,178,NULL,NULL,'nao',NULL,NULL,2,692,NULL,NULL),(705,'Tênis de Mesa','Masculino',233,204,NULL,NULL,'nao',NULL,NULL,2,692,NULL,NULL),(706,'Tênis de Mesa','Masculino',214,176,NULL,NULL,'nao',NULL,NULL,2,693,NULL,NULL),(707,'Tênis de Mesa','Masculino',249,208,NULL,NULL,'nao',NULL,NULL,2,693,NULL,NULL),(708,'Tênis de Mesa','Masculino',256,253,NULL,NULL,'nao',NULL,NULL,2,694,NULL,NULL),(709,'Tênis de Mesa','Masculino',250,248,NULL,NULL,'nao',NULL,NULL,2,694,NULL,NULL),(710,'Tênis de Mesa','Masculino',255,270,NULL,NULL,'nao',NULL,NULL,2,695,NULL,NULL),(711,'Tênis de Mesa','Masculino',190,268,NULL,NULL,'nao',NULL,NULL,2,695,NULL,NULL),(712,'Tênis de Mesa','Masculino',252,NULL,NULL,NULL,'sim',NULL,NULL,1,696,252,NULL),(713,'Tênis de Mesa','Masculino',174,NULL,NULL,NULL,'sim',NULL,NULL,1,696,174,NULL),(714,'Tênis de Mesa','Masculino',246,269,NULL,NULL,'nao',NULL,NULL,1,697,NULL,NULL),(715,'Tênis de Mesa','Masculino',234,216,NULL,NULL,'nao',NULL,NULL,1,697,NULL,NULL),(716,'Tênis de Mesa','Masculino',175,237,NULL,NULL,'nao',NULL,NULL,1,698,NULL,NULL),(717,'Tênis de Mesa','Masculino',193,NULL,NULL,NULL,'sim',NULL,NULL,1,698,193,NULL),(718,'Tênis de Mesa','Masculino',207,NULL,NULL,NULL,'sim',NULL,NULL,1,699,207,NULL),(719,'Tênis de Mesa','Masculino',210,NULL,NULL,NULL,'sim',NULL,NULL,1,699,210,NULL),(720,'Tênis de Mesa','Masculino',267,NULL,NULL,NULL,'sim',NULL,NULL,1,700,267,NULL),(721,'Tênis de Mesa','Masculino',247,NULL,NULL,NULL,'sim',NULL,NULL,1,700,247,NULL),(722,'Tênis de Mesa','Masculino',212,NULL,NULL,NULL,'sim',NULL,NULL,1,701,212,NULL),(723,'Tênis de Mesa','Masculino',187,211,NULL,NULL,'nao',NULL,NULL,1,701,NULL,NULL),(724,'Tênis de Mesa','Masculino',271,NULL,NULL,NULL,'sim',NULL,NULL,1,702,271,NULL),(725,'Tênis de Mesa','Masculino',205,NULL,NULL,NULL,'sim',NULL,NULL,1,702,205,NULL),(726,'Tênis de Mesa','Masculino',206,NULL,NULL,NULL,'sim',NULL,NULL,1,703,206,NULL),(727,'Tênis de Mesa','Masculino',251,NULL,NULL,NULL,'sim',NULL,NULL,1,703,251,NULL),(728,'Tênis de Mesa','Masculino',238,NULL,NULL,NULL,'sim',NULL,NULL,1,704,238,NULL),(729,'Tênis de Mesa','Masculino',178,NULL,NULL,NULL,'sim',NULL,NULL,1,704,178,NULL),(730,'Tênis de Mesa','Masculino',233,NULL,NULL,NULL,'sim',NULL,NULL,1,705,233,NULL),(731,'Tênis de Mesa','Masculino',204,NULL,NULL,NULL,'sim',NULL,NULL,1,705,204,NULL),(732,'Tênis de Mesa','Masculino',214,NULL,NULL,NULL,'sim',NULL,NULL,1,706,214,NULL),(733,'Tênis de Mesa','Masculino',176,NULL,NULL,NULL,'sim',NULL,NULL,1,706,176,NULL),(734,'Tênis de Mesa','Masculino',249,NULL,NULL,NULL,'sim',NULL,NULL,1,707,249,NULL),(735,'Tênis de Mesa','Masculino',208,NULL,NULL,NULL,'sim',NULL,NULL,1,707,208,NULL),(736,'Tênis de Mesa','Masculino',256,NULL,NULL,NULL,'sim',NULL,NULL,1,708,256,NULL),(737,'Tênis de Mesa','Masculino',253,NULL,NULL,NULL,'sim',NULL,NULL,1,708,253,NULL),(738,'Tênis de Mesa','Masculino',250,NULL,NULL,NULL,'sim',NULL,NULL,1,709,250,NULL),(739,'Tênis de Mesa','Masculino',248,NULL,NULL,NULL,'sim',NULL,NULL,1,709,248,NULL),(740,'Tênis de Mesa','Masculino',255,NULL,NULL,NULL,'sim',NULL,NULL,1,710,255,NULL),(741,'Tênis de Mesa','Masculino',270,NULL,NULL,NULL,'sim',NULL,NULL,1,710,270,NULL),(742,'Tênis de Mesa','Masculino',190,NULL,NULL,NULL,'sim',NULL,NULL,1,711,190,NULL),(743,'Tênis de Mesa','Masculino',268,NULL,NULL,NULL,'sim',NULL,NULL,1,711,268,NULL),(744,'Tênis de Mesa','Feminino',172,225,NULL,NULL,'nao',NULL,NULL,1,NULL,NULL,NULL),(745,'Queimada','Misto',NULL,NULL,NULL,NULL,'nao',NULL,NULL,4,NULL,NULL,NULL),(746,'Queimada','Misto',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,745,NULL,NULL),(747,'Queimada','Misto',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,745,NULL,NULL),(748,'Queimada','Misto',182,167,NULL,NULL,'nao',NULL,NULL,2,746,NULL,NULL),(749,'Queimada','Misto',173,NULL,NULL,NULL,'nao',NULL,NULL,2,746,NULL,NULL),(750,'Queimada','Misto',NULL,NULL,NULL,NULL,'nao',NULL,NULL,2,747,NULL,NULL),(751,'Queimada','Misto',181,NULL,NULL,NULL,'nao',NULL,NULL,2,747,NULL,NULL),(752,'Queimada','Misto',182,NULL,NULL,NULL,'sim',NULL,NULL,1,748,182,NULL),(753,'Queimada','Misto',167,NULL,NULL,NULL,'sim',NULL,NULL,1,748,167,NULL),(754,'Queimada','Misto',173,NULL,NULL,NULL,'sim',NULL,NULL,1,749,173,NULL),(755,'Queimada','Misto',201,245,NULL,NULL,'nao',NULL,NULL,1,749,NULL,NULL),(756,'Queimada','Misto',200,266,NULL,NULL,'nao',NULL,NULL,1,750,NULL,NULL),(757,'Queimada','Misto',217,240,NULL,NULL,'nao',NULL,NULL,1,750,NULL,NULL),(758,'Queimada','Misto',181,NULL,NULL,NULL,'sim',NULL,NULL,1,751,181,NULL),(759,'Queimada','Misto',227,231,NULL,NULL,'nao',NULL,NULL,1,751,NULL,NULL),(760,'Handebol','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,4,NULL,NULL,NULL),(761,'Handebol','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,760,NULL,NULL),(762,'Handebol','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,760,NULL,NULL),(763,'Handebol','Masculino',NULL,262,NULL,NULL,'nao',NULL,NULL,2,761,NULL,NULL),(764,'Handebol','Masculino',157,183,NULL,NULL,'nao',NULL,NULL,2,761,NULL,NULL),(765,'Handebol','Masculino',150,147,NULL,NULL,'nao',NULL,NULL,2,762,NULL,NULL),(766,'Handebol','Masculino',162,146,NULL,NULL,'nao',NULL,NULL,2,762,NULL,NULL),(767,'Handebol','Masculino',191,224,NULL,NULL,'nao',NULL,NULL,1,763,NULL,NULL),(768,'Handebol','Masculino',171,262,2,3,'sim',NULL,NULL,1,763,262,NULL),(769,'Handebol','Masculino',157,NULL,NULL,NULL,'sim',NULL,NULL,1,764,157,NULL),(770,'Handebol','Masculino',183,242,10,1,'sim',NULL,NULL,1,764,183,NULL),(771,'Handebol','Masculino',150,NULL,NULL,NULL,'sim',NULL,NULL,1,765,150,NULL),(772,'Handebol','Masculino',147,NULL,NULL,NULL,'sim',NULL,NULL,1,765,147,NULL),(773,'Handebol','Masculino',162,NULL,NULL,NULL,'sim',NULL,NULL,1,766,162,NULL),(774,'Handebol','Masculino',146,NULL,NULL,NULL,'sim',NULL,NULL,1,766,146,NULL),(775,'Handebol','Feminino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,NULL,NULL,NULL),(776,'Handebol','Feminino',184,149,NULL,NULL,'nao',NULL,NULL,2,775,NULL,NULL),(777,'Handebol','Feminino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,2,775,NULL,NULL),(778,'Handebol','Feminino',184,258,10,2,'sim',NULL,NULL,1,776,184,NULL),(779,'Handebol','Feminino',149,272,11,3,'sim',NULL,NULL,1,776,149,NULL),(780,'Handebol','Feminino',197,220,NULL,NULL,'nao',NULL,NULL,1,777,NULL,NULL),(781,'Handebol','Feminino',189,221,NULL,NULL,'nao',NULL,NULL,1,777,NULL,NULL),(782,'Futsal','Masculino',163,180,12,1,'sim',NULL,NULL,4,NULL,163,NULL),(783,'Futsal','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,782,NULL,NULL),(784,'Futsal','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,782,NULL,NULL),(785,'Futsal','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,2,783,NULL,NULL),(786,'Futsal','Masculino',148,NULL,NULL,NULL,'nao',NULL,NULL,2,783,NULL,NULL),(787,'Futsal','Masculino',159,151,NULL,NULL,'nao',NULL,NULL,2,784,NULL,NULL),(788,'Futsal','Masculino',NULL,165,NULL,NULL,'nao',NULL,NULL,2,784,NULL,NULL),(789,'Futsal','Masculino',195,226,NULL,NULL,'nao',NULL,NULL,1,785,NULL,NULL),(790,'Futsal','Masculino',179,241,NULL,NULL,'nao',NULL,NULL,1,785,NULL,NULL),(791,'Futsal','Masculino',148,NULL,NULL,NULL,'sim',NULL,NULL,1,786,148,NULL),(792,'Futsal','Masculino',196,198,NULL,NULL,'nao',NULL,NULL,1,786,NULL,NULL),(793,'Futsal','Masculino',159,NULL,NULL,NULL,'sim',NULL,NULL,1,787,159,NULL),(794,'Futsal','Masculino',151,NULL,NULL,NULL,'sim',NULL,NULL,1,787,151,NULL),(795,'Futsal','Masculino',169,274,NULL,NULL,'nao',NULL,NULL,1,788,NULL,NULL),(796,'Futsal','Masculino',165,NULL,NULL,NULL,'sim',NULL,NULL,1,788,165,NULL),(797,'Futsal','Feminino',152,194,3,2,'sim',NULL,NULL,3,NULL,152,NULL),(798,'Futsal','Feminino',152,NULL,NULL,NULL,'nao',NULL,NULL,2,797,NULL,NULL),(800,'Futsal','Feminino',152,NULL,NULL,NULL,'sim',NULL,NULL,1,798,152,NULL),(801,'Futsal','Feminino',223,259,NULL,NULL,'nao',NULL,NULL,1,798,NULL,NULL),(802,'Futsal','Feminino',194,NULL,NULL,NULL,'sim',NULL,NULL,1,799,194,NULL),(803,'Futsal','Feminino',215,NULL,NULL,NULL,'sim',NULL,NULL,1,799,215,NULL),(804,'Basquete','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,4,NULL,NULL,NULL),(805,'Basquete','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,804,NULL,NULL),(806,'Basquete','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,804,NULL,NULL),(807,'Basquete','Masculino',186,NULL,NULL,NULL,'nao',NULL,NULL,2,805,NULL,NULL),(808,'Basquete','Masculino',NULL,166,NULL,NULL,'nao',NULL,NULL,2,805,NULL,NULL),(809,'Basquete','Masculino',188,177,NULL,NULL,'nao',NULL,NULL,2,806,NULL,NULL),(810,'Basquete','Masculino',NULL,192,NULL,NULL,'nao',NULL,NULL,2,806,NULL,NULL),(811,'Basquete','Masculino',186,NULL,NULL,NULL,'sim',NULL,NULL,1,807,186,NULL),(812,'Basquete','Masculino',232,235,NULL,NULL,'nao',NULL,NULL,1,807,NULL,NULL),(813,'Basquete','Masculino',202,265,NULL,NULL,'nao',NULL,NULL,1,808,NULL,NULL),(814,'Basquete','Masculino',166,NULL,NULL,NULL,'sim',NULL,NULL,1,808,166,NULL),(815,'Basquete','Masculino',188,NULL,NULL,NULL,'sim',NULL,NULL,1,809,188,NULL),(816,'Basquete','Masculino',177,NULL,NULL,NULL,'sim',NULL,NULL,1,809,177,NULL),(817,'Basquete','Masculino',213,244,NULL,NULL,'nao',NULL,NULL,1,810,NULL,NULL),(818,'Basquete','Masculino',192,NULL,NULL,NULL,'sim',NULL,NULL,1,810,192,NULL),(819,'Basquete','Feminino',164,NULL,NULL,NULL,'nao',NULL,NULL,2,NULL,NULL,NULL),(820,'Basquete','Feminino',164,261,2,1,'sim',NULL,NULL,1,819,164,NULL),(821,'Basquete','Feminino',218,230,NULL,NULL,'nao',NULL,NULL,1,819,NULL,NULL),(822,'Xadrez','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,5,NULL,NULL,NULL),(823,'Xadrez','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,4,822,NULL,NULL),(824,'Xadrez','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,4,822,NULL,NULL),(825,'Xadrez','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,823,NULL,NULL),(826,'Xadrez','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,823,NULL,NULL),(827,'Xadrez','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,824,NULL,NULL),(828,'Xadrez','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,3,824,NULL,NULL),(829,'Xadrez','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,2,825,NULL,NULL),(830,'Xadrez','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,2,825,NULL,NULL),(831,'Xadrez','Masculino',130,138,NULL,NULL,'nao',NULL,NULL,2,826,NULL,NULL),(832,'Xadrez','Masculino',142,NULL,NULL,NULL,'nao',NULL,NULL,2,826,NULL,NULL),(833,'Xadrez','Masculino',NULL,106,NULL,NULL,'nao',NULL,NULL,2,827,NULL,NULL),(834,'Xadrez','Masculino',110,123,NULL,NULL,'nao',NULL,NULL,2,827,NULL,NULL),(835,'Xadrez','Masculino',NULL,NULL,NULL,NULL,'nao',NULL,NULL,2,828,NULL,NULL),(836,'Xadrez','Masculino',140,NULL,NULL,NULL,'nao',NULL,NULL,2,828,NULL,NULL),(837,'Xadrez','Masculino',104,144,NULL,NULL,'nao',NULL,NULL,1,829,NULL,NULL),(838,'Xadrez','Masculino',109,137,NULL,NULL,'nao',NULL,NULL,1,829,NULL,NULL),(839,'Xadrez','Masculino',115,143,NULL,NULL,'nao',NULL,NULL,1,830,NULL,NULL),(840,'Xadrez','Masculino',129,113,NULL,NULL,'nao',NULL,NULL,1,830,NULL,NULL),(841,'Xadrez','Masculino',130,NULL,NULL,NULL,'sim',NULL,NULL,1,831,130,NULL),(842,'Xadrez','Masculino',138,NULL,NULL,NULL,'sim',NULL,NULL,1,831,138,NULL),(843,'Xadrez','Masculino',142,NULL,NULL,NULL,'sim',NULL,NULL,1,832,142,NULL),(844,'Xadrez','Masculino',135,133,NULL,NULL,'nao',NULL,NULL,1,832,NULL,NULL),(845,'Xadrez','Masculino',119,105,NULL,NULL,'nao',NULL,NULL,1,833,NULL,NULL),(846,'Xadrez','Masculino',106,NULL,NULL,NULL,'sim',NULL,NULL,1,833,106,NULL),(847,'Xadrez','Masculino',110,NULL,NULL,NULL,'sim',NULL,NULL,1,834,110,NULL),(848,'Xadrez','Masculino',123,NULL,NULL,NULL,'sim',NULL,NULL,1,834,123,NULL),(849,'Xadrez','Masculino',108,107,NULL,NULL,'nao',NULL,NULL,1,835,NULL,NULL),(850,'Xadrez','Masculino',126,114,NULL,NULL,'nao',NULL,NULL,1,835,NULL,NULL),(851,'Xadrez','Masculino',140,NULL,NULL,NULL,'sim',NULL,NULL,1,836,140,NULL),(852,'Xadrez','Masculino',116,141,NULL,NULL,'nao',NULL,NULL,1,836,NULL,NULL),(854,'Futsal','Masculino',169,179,0,0,'nao',NULL,NULL,1,NULL,NULL,'2026-08-14 21:30:00'),(857,'Futsal','Masculino',215,215,0,0,'nao',NULL,NULL,1,NULL,NULL,'2026-08-14 21:30:00'),(858,'Futsal','Masculino',152,215,0,0,'nao',NULL,NULL,1,NULL,NULL,'2026-08-14 21:30:00'),(859,'Futsal','Masculino',226,275,0,0,'nao',NULL,NULL,1,NULL,NULL,'2026-08-14 21:30:00'),(860,'Basquete','Masculino',152,159,0,0,'nao',NULL,NULL,1,NULL,NULL,'2026-08-14 21:30:00');
/*!40000 ALTER TABLE `partidas` ENABLE KEYS */;
UNLOCK TABLES;

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
  `data_hora` datetime DEFAULT NULL,
  `status` enum('nao_iniciada','em_andamento','finalizada') COLLATE utf8mb3_unicode_ci NOT NULL DEFAULT 'nao_iniciada',
  PRIMARY KEY (`pk_prova`),
  KEY `idx_modalidade` (`fk_modalidade`),
  KEY `idx_genero` (`fk_genero`),
  CONSTRAINT `fk_prova_genero` FOREIGN KEY (`fk_genero`) REFERENCES `classificacao` (`pk_genero`),
  CONSTRAINT `fk_prova_modalidade` FOREIGN KEY (`fk_modalidade`) REFERENCES `modalidades_atletismo` (`pk_modalidade`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provas_atletismo`
--

LOCK TABLES `provas_atletismo` WRITE;
/*!40000 ALTER TABLE `provas_atletismo` DISABLE KEYS */;
/*!40000 ALTER TABLE `provas_atletismo` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `recordes_atletismo`
--

LOCK TABLES `recordes_atletismo` WRITE;
/*!40000 ALTER TABLE `recordes_atletismo` DISABLE KEYS */;
/*!40000 ALTER TABLE `recordes_atletismo` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `tipo_estatistica`
--

LOCK TABLES `tipo_estatistica` WRITE;
/*!40000 ALTER TABLE `tipo_estatistica` DISABLE KEYS */;
INSERT INTO `tipo_estatistica` VALUES ('Arremessos de Três'),('Eliminações'),('Empurrão'),('Empurrar'),('Finalizações'),('Fora Da Area'),('Gols'),('Matchpoints'),('Passes'),('Pontos'),('Rebotes'),('Saques'),('Sets');
/*!40000 ALTER TABLE `tipo_estatistica` ENABLE KEYS */;
UNLOCK TABLES;

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

--
-- Dumping data for table `turmas`
--

LOCK TABLES `turmas` WRITE;
/*!40000 ALTER TABLE `turmas` DISABLE KEYS */;
INSERT INTO `turmas` VALUES ('1TDSA',''),('1TDSB','/static/imgTurmas/1tdsb.jpg'),('2MKTA','/static/imgTurmas/2mkta.jpg'),('2MKTB','/static/imgTurmas/2mktb.jpg'),('2TDSA','/static/imgTurmas/2tdsa.jpg'),('2TDSB','/static/imgTurmas/2tdsb.jpg'),('3MKTA','/static/imgTurmas/3mkta.jpg'),('3MKTB','/static/imgTurmas/3mktb.jpg'),('3TDSA','/static/imgTurmas/3tdsa.jpg'),('3TDSB','/static/imgTurmas/3tdsb.jpg');
/*!40000 ALTER TABLE `turmas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-14 23:27:41
