-- MySQL dump 10.13  Distrib 5.7.21, for macos10.13 (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `article_articles`
--

DROP TABLE IF EXISTS `article_articles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article_articles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `title` varchar(200) NOT NULL,
  `sub_title` varchar(100) NOT NULL,
  `summarize` varchar(300) DEFAULT NULL,
  `content` longtext NOT NULL,
  `types_id` int(11) NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  `img_header` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `article_articles_user_id_0a9849a7_fk_user_myuser_id` (`user_id`),
  KEY `article_articles_types_id_757ebc43` (`types_id`),
  CONSTRAINT `article_articles_types_id_757ebc43_fk_article_articletype_id` FOREIGN KEY (`types_id`) REFERENCES `article_articletype` (`id`),
  CONSTRAINT `article_articles_user_id_0a9849a7_fk_user_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `user_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article_articles`
--

LOCK TABLES `article_articles` WRITE;
/*!40000 ALTER TABLE `article_articles` DISABLE KEYS */;
INSERT INTO `article_articles` VALUES (1,'2019-07-09 01:23:18.332283','国家药监局：药品、医械生产企业分别达4441家、1.7万家','1','近日，国家药品监督管理局发布《2018年度药品监管统计年报》(以下简称《年报》)，《年报》显示，截至2018年11月底，全国共有原料药和制剂生产企业4441家，实有医疗器械生产企业1.7万家...','<p style=\"text-align:center\"><img alt=\"\" src=\"/media/uploads/2019/07/09/news-img.jpg\" /></p>\r\n\r\n<p>近日，国家药品监督管理局发布《2018年度药品监管统计年报》(以下简称《年报》)，《年报》显示，截至2018年11月底，全国共有原料药和制剂生产企业4441家，实有医疗器械生产企业1.7万家...</p>\r\n\r\n<p>近日，国家药品监督管理局发布《2018年度药品监管统计年报》(以下简称《年报》)，《年报》显示，截至2018年11月底，全国共有原料药和制剂生产企业4441家，实有医疗器械生产企业1.7万家。</p>\r\n\r\n<p>截至2018年11月底，全国共有原料药和制剂生产企业4441家，比去年的4376家多了65家。全国《药品经营许可证》持证企业50.8万家：其中批发企业1.4万家;零售连锁企业5671家，零售连锁企业门店25.5万家;零售药店23.4万家。</p>\r\n\r\n<p>医疗器械生产企业与去年相比增加较多。截至2018年11月底，全国实有医疗器械生产企业1.7万家，比2017年11月底的1.6万家多了1000家。其中：可生产一类产品的企业7513家，可生产二类产品的企业9189家，可生产三类产品的企业1997家。全国共有二、三类医疗器械经营企业51.1万家。</p>\r\n\r\n<p>除了生产和经营许可情况，《年报》还对2018年的药品、医疗器械注册情况做了统计。根据《年报》，2018年国家药监局共批准新药临床312件;共批准仿制药临床申请58件，生产申请464件;共批准进口药品临床申请154件，上市90件。</p>\r\n\r\n<p>医疗器械领域，2018年，全国共完成境内第一类医疗器械备案22167件，进口第一类医疗器械(含港澳台)备案1885件;共批准境内第二类医疗器械首次注册4402件，境内第三类医疗器械首次注册668件;共批准进口(含港澳台)第二类医疗器械首次注册358件，进口(含港澳台)第三类医疗器械首次注册235件。</p>',1,1,1,'upload_img/news-header/certificate-2.jpg'),(13,'2019-07-11 08:32:07.106272','广纳贤才，培训人才，知人善用，人尽其才','广纳贤才，培训人才，知人善用，人尽其才','广纳贤才，培训人才，知人善用，人尽其才','<p>集团全力以赴为员工创建健康、快乐、充满希望的成长空间，尊重人才，培养人才，爱护人才，善用人才。实施全球化的人才开发战略，完善人才成长机制，使员工在和谐的环境中实现价值的提升。</p>\r\n\r\n<hr />\r\n<p><img alt=\"\" src=\"/media/uploads/amdin/2019/07/11/miskgn.jpg\" style=\"float:right; height:150px; width:150px\" /></p>\r\n\r\n<p>如果您对我们的职位感兴趣，欢迎致电咨询，或者邮箱投递简历！&nbsp;<br />\r\n电话：010-56903333&nbsp;<br />\r\n邮箱：hd_zhaopin@handian.com</p>',3,1,1,'upload_img/news-header/r-img.jpg');
/*!40000 ALTER TABLE `article_articles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `article_articletype`
--

DROP TABLE IF EXISTS `article_articletype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article_articletype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `typename` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article_articletype`
--

LOCK TABLES `article_articletype` WRITE;
/*!40000 ALTER TABLE `article_articletype` DISABLE KEYS */;
INSERT INTO `article_articletype` VALUES (1,'2019-07-09 01:21:53.311074','汉典新闻'),(2,'2019-07-09 03:16:02.113928','行业动态'),(3,'2019-07-10 02:53:15.890926','招聘信息');
/*!40000 ALTER TABLE `article_articletype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `article_certificate`
--

DROP TABLE IF EXISTS `article_certificate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article_certificate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `img` varchar(100) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article_certificate`
--

LOCK TABLES `article_certificate` WRITE;
/*!40000 ALTER TABLE `article_certificate` DISABLE KEYS */;
/*!40000 ALTER TABLE `article_certificate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_myuser'),(22,'Can change user',6,'change_myuser'),(23,'Can delete user',6,'delete_myuser'),(24,'Can view user',6,'view_myuser'),(25,'Can add 导航',7,'add_navbar'),(26,'Can change 导航',7,'change_navbar'),(27,'Can delete 导航',7,'delete_navbar'),(28,'Can view 导航',7,'view_navbar'),(29,'Can add 文章',8,'add_articles'),(30,'Can change 文章',8,'change_articles'),(31,'Can delete 文章',8,'delete_articles'),(32,'Can view 文章',8,'view_articles'),(33,'Can add 类别',9,'add_articletype'),(34,'Can change 类别',9,'change_articletype'),(35,'Can delete 类别',9,'delete_articletype'),(36,'Can view 类别',9,'view_articletype'),(37,'Can add 技术/荣誉证书',10,'add_certificate'),(38,'Can change 技术/荣誉证书',10,'change_certificate'),(39,'Can delete 技术/荣誉证书',10,'delete_certificate'),(40,'Can view 技术/荣誉证书',10,'view_certificate'),(41,'Can add 药品',11,'add_product'),(42,'Can change 药品',11,'change_product'),(43,'Can delete 药品',11,'delete_product'),(44,'Can view 药品',11,'view_product'),(45,'Can add 药品种类',12,'add_producttype'),(46,'Can change 药品种类',12,'change_producttype'),(47,'Can delete 药品种类',12,'delete_producttype'),(48,'Can view 药品种类',12,'view_producttype'),(49,'Can add 职位招聘',13,'add_position'),(50,'Can change 职位招聘',13,'change_position'),(51,'Can delete 职位招聘',13,'delete_position'),(52,'Can view 职位招聘',13,'view_position');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_user_myuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `user_myuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=152 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-07-05 09:23:18.396087','1','asd',1,'[{\"added\": {}}]',12,1),(2,'2019-07-05 09:23:26.658819','1','ads',1,'[{\"added\": {}}]',11,1),(3,'2019-07-05 10:23:51.820751','2','中成新药品',1,'[{\"added\": {}}]',12,1),(4,'2019-07-05 10:24:00.478468','1','ads',2,'[{\"changed\": {\"fields\": [\"types\"]}}]',11,1),(5,'2019-07-05 10:24:21.542755','2','fh',1,'[{\"added\": {}}]',11,1),(6,'2019-07-05 11:11:11.776833','3','鞍山市',1,'[{\"added\": {}}]',11,1),(7,'2019-07-06 06:21:25.872852','2','fh',2,'[{\"changed\": {\"fields\": [\"info_detail\"]}}]',11,1),(8,'2019-07-06 06:21:44.553503','1','ads',2,'[{\"changed\": {\"fields\": [\"info_detail\"]}}]',11,1),(9,'2019-07-06 06:21:54.777696','3','鞍山市',2,'[{\"changed\": {\"fields\": [\"info_detail\"]}}]',11,1),(10,'2019-07-06 06:23:36.697191','1','首页',1,'[{\"added\": {}}]',7,1),(11,'2019-07-06 06:24:13.266989','2','走进汉典',1,'[{\"added\": {}}]',7,1),(12,'2019-07-06 06:24:36.989335','3','名医咨询',1,'[{\"added\": {}}]',7,1),(13,'2019-07-06 06:24:53.089857','4','医学中心',1,'[{\"added\": {}}]',7,1),(14,'2019-07-06 06:25:08.076899','5','服务与产品',1,'[{\"added\": {}}]',7,1),(15,'2019-07-06 06:25:23.660348','6','新闻动态',1,'[{\"added\": {}}]',7,1),(16,'2019-07-06 06:26:04.197594','7','招贤纳士',1,'[{\"added\": {}}]',7,1),(17,'2019-07-06 06:26:37.239732','8','联系我们',1,'[{\"added\": {}}]',7,1),(18,'2019-07-06 06:33:28.641730','1','证书',1,'[{\"added\": {}}]',10,1),(19,'2019-07-08 01:36:57.701527','3','经典中成药',1,'[{\"added\": {}}]',12,1),(20,'2019-07-08 01:37:46.705305','4','越剧产品',1,'[{\"added\": {}}]',11,1),(21,'2019-07-08 03:46:47.678726','5','六味地黄丸',1,'[{\"added\": {}}]',11,1),(22,'2019-07-08 06:50:14.852679','3','鞍山市',2,'[{\"changed\": {\"fields\": [\"info_detail\"]}}]',11,1),(23,'2019-07-09 01:21:53.311881','1','汉典新闻',1,'[{\"added\": {}}]',9,1),(24,'2019-07-09 01:23:18.333322','1','国家药监局：药品、医械生产企业分别达4441家、1.7万家',1,'[{\"added\": {}}]',8,1),(25,'2019-07-09 02:32:56.437054','1','国家药监局：药品、医械生产企业分别达4441家、1.7万家',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',8,1),(26,'2019-07-09 02:33:45.433666','1','国家药监局：药品、医械生产企业分别达4441家、1.7万家',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',8,1),(27,'2019-07-09 02:41:32.111862','1','国家药监局：药品、医械生产企业分别达4441家、1.7万家',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',8,1),(28,'2019-07-09 03:14:44.796133','1','国家药监局：药品、医械生产企业分别达4441家、1.7万家',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',8,1),(29,'2019-07-09 03:16:02.114798','2','行业动态',1,'[{\"added\": {}}]',9,1),(30,'2019-07-09 03:17:40.419730','2','扩大规模',1,'[{\"added\": {}}]',8,1),(31,'2019-07-09 03:29:54.460803','2','扩大规模',2,'[{\"changed\": {\"fields\": [\"img_header\"]}}]',8,1),(32,'2019-07-09 03:31:05.495897','2','扩大规模',2,'[]',8,1),(33,'2019-07-09 03:34:55.776764','2','扩大规模',2,'[{\"changed\": {\"fields\": [\"img_header\"]}}]',8,1),(34,'2019-07-09 03:36:42.088465','6','33333',1,'[{\"added\": {}}]',11,1),(35,'2019-07-09 03:42:16.102990','5','六味地黄丸',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',11,1),(36,'2019-07-09 03:42:21.929219','4','越剧产品',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',11,1),(37,'2019-07-09 03:42:35.148568','3','鞍山市',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',11,1),(38,'2019-07-09 03:42:50.880834','2','fh',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',11,1),(39,'2019-07-09 03:42:58.823471','1','ads',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',11,1),(40,'2019-07-09 03:43:27.727567','1','ads',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',11,1),(41,'2019-07-09 03:44:22.264582','1','证书',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',10,1),(42,'2019-07-09 05:02:43.802566','1','证书',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',10,1),(43,'2019-07-09 05:07:33.573076','1','国家药监局：药品、医械生产企业分别达4441家、1.7万家',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',8,1),(44,'2019-07-09 05:41:42.455840','6','33333',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',11,1),(45,'2019-07-09 05:42:26.790505','5','六味地黄丸',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',11,1),(46,'2019-07-09 05:42:44.043603','4','越剧产品',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',11,1),(47,'2019-07-09 05:54:22.447703','1','证书',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',10,1),(48,'2019-07-09 06:14:09.726062','3','鞍山市',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',11,1),(49,'2019-07-09 06:14:23.593956','2','fh',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',11,1),(50,'2019-07-09 06:14:30.809148','1','ads',2,'[{\"changed\": {\"fields\": [\"img\"]}}]',11,1),(51,'2019-07-09 06:20:18.503796','1','国家药监局：药品、医械生产企业分别达4441家、1.7万家',2,'[{\"changed\": {\"fields\": [\"img_header\"]}}]',8,1),(52,'2019-07-09 06:25:25.929479','2','扩大规模',2,'[{\"changed\": {\"fields\": [\"img_header\"]}}]',8,1),(53,'2019-07-09 06:25:33.170752','2','扩大规模',2,'[{\"changed\": {\"fields\": [\"types\"]}}]',8,1),(54,'2019-07-09 06:26:10.355077','2','扩大规模',2,'[{\"changed\": {\"fields\": [\"sub_title\", \"summarize\"]}}]',8,1),(55,'2019-07-09 06:33:06.976045','1','国家药监局：药品、医械生产企业分别达4441家、1.7万家',2,'[{\"changed\": {\"fields\": [\"summarize\"]}}]',8,1),(56,'2019-07-09 06:49:04.347010','3','1',1,'[{\"added\": {}}]',8,1),(57,'2019-07-09 07:24:27.889450','2','扩大规模',2,'[{\"changed\": {\"fields\": [\"types\"]}}]',8,1),(58,'2019-07-09 07:33:08.293089','3','1',2,'[{\"changed\": {\"fields\": [\"summarize\", \"content\"]}}]',8,1),(59,'2019-07-10 01:09:52.682409','4','房屋租赁',1,'[{\"added\": {}}]',8,1),(60,'2019-07-10 01:10:27.176745','5','zhensgu',1,'[{\"added\": {}}]',8,1),(61,'2019-07-10 02:42:25.541069','4','房屋租赁sadsd',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',8,1),(62,'2019-07-10 02:53:15.891607','3','招聘信息',1,'[{\"added\": {}}]',9,1),(63,'2019-07-10 02:53:24.405395','5','zhensgu',2,'[]',8,1),(64,'2019-07-10 02:55:46.596804','6','广纳贤才，培训人才，知人善用，人尽其才',1,'[{\"added\": {}}]',8,1),(65,'2019-07-10 03:37:30.848871','7','dfs',1,'[{\"added\": {}}]',8,1),(66,'2019-07-10 03:39:10.505500','8','大师傅',1,'[{\"added\": {}}]',8,1),(67,'2019-07-10 05:09:04.660115','9','21',1,'[{\"added\": {}}]',8,1),(68,'2019-07-10 05:09:59.455973','10','dfs',1,'[{\"added\": {}}]',8,1),(69,'2019-07-10 05:21:41.024610','10','dfs',2,'[]',8,1),(70,'2019-07-10 05:21:58.567071','11','adsfqweq12',1,'[{\"added\": {}}]',8,1),(71,'2019-07-10 05:23:21.475681','12','jk',1,'[{\"added\": {}}]',8,1),(72,'2019-07-10 05:23:29.318357','12','jk',2,'[{\"changed\": {\"fields\": [\"is_published\"]}}]',8,1),(73,'2019-07-10 05:24:37.077775','1','国家药监局：药品、医械生产企业分别达4441家、1.7万家',2,'[{\"changed\": {\"fields\": [\"is_published\"]}}]',8,1),(74,'2019-07-10 05:24:48.854881','1','国家药监局：药品、医械生产企业分别达4441家、1.7万家',2,'[{\"changed\": {\"fields\": [\"is_published\"]}}]',8,1),(75,'2019-07-10 05:24:53.626071','12','jk',2,'[{\"changed\": {\"fields\": [\"is_published\"]}}]',8,1),(76,'2019-07-10 05:31:09.766009','7','dfs',2,'[{\"changed\": {\"fields\": [\"is_published\"]}}]',8,1),(77,'2019-07-10 05:52:33.604683','6','33333',3,'',11,1),(78,'2019-07-10 05:52:33.612467','5','六味地黄丸',3,'',11,1),(79,'2019-07-10 05:52:33.614698','4','越剧产品',3,'',11,1),(80,'2019-07-10 05:52:33.618255','3','鞍山市',3,'',11,1),(81,'2019-07-10 05:52:33.620757','2','fh',3,'',11,1),(82,'2019-07-10 05:52:33.622445','1','ads',3,'',11,1),(83,'2019-07-10 05:54:39.554051','2','ads',1,'[{\"added\": {}}]',10,1),(84,'2019-07-10 05:55:10.544351','3','ads',1,'[{\"added\": {}}]',10,1),(85,'2019-07-10 05:55:18.062266','4','sda',1,'[{\"added\": {}}]',10,1),(86,'2019-07-10 05:55:26.164983','5','fdsa',1,'[{\"added\": {}}]',10,1),(87,'2019-07-10 07:20:39.923661','1','高级产品组经理（北京）',1,'[{\"added\": {}}]',13,1),(88,'2019-07-10 07:37:36.628513','2','高级产品组经理（北京）',1,'[{\"added\": {}}]',13,1),(89,'2019-07-10 07:37:42.685803','1','高级产品组经理（北京）',2,'[{\"changed\": {\"fields\": [\"types\"]}}]',13,1),(90,'2019-07-10 08:05:34.972422','1','高级产品组经理（北京）',2,'[{\"changed\": {\"fields\": [\"types\"]}}]',13,1),(91,'2019-07-10 08:06:05.124574','3','高级产品组经理（北京）',1,'[{\"added\": {}}]',13,1),(92,'2019-07-10 08:06:26.235072','4','高级产品组经理（北京）',1,'[{\"added\": {}}]',13,1),(93,'2019-07-10 08:06:51.987479','1','高级产品组经理（北京）',2,'[{\"changed\": {\"fields\": [\"types\"]}}]',13,1),(94,'2019-07-10 09:00:56.739294','1','位置',2,'[{\"changed\": {\"fields\": [\"typename\"]}}]',12,1),(95,'2019-07-10 09:03:06.735620','3','经典中成药',3,'',12,1),(96,'2019-07-10 09:03:06.743065','2','中成新药品',3,'',12,1),(97,'2019-07-10 09:03:06.745312','1','位置',3,'',12,1),(98,'2019-07-10 09:04:03.495050','4','weizhi',1,'[{\"added\": {}}]',12,1),(99,'2019-07-10 09:05:23.675112','5','中成新药品',1,'[{\"added\": {}}]',12,1),(100,'2019-07-10 09:08:26.121180','6','dsa',1,'[{\"added\": {}}]',12,1),(101,'2019-07-10 09:09:57.074199','6','dsawqe',2,'[{\"changed\": {\"fields\": [\"typename\"]}}]',12,1),(102,'2019-07-10 09:20:20.388999','7','大',1,'[{\"added\": {}}]',11,1),(103,'2019-07-10 09:21:21.193007','6','经典中成药',2,'[{\"changed\": {\"fields\": [\"typename\"]}}]',12,1),(104,'2019-07-10 09:21:50.430459','8','爱迪生',1,'[{\"added\": {}}]',11,1),(105,'2019-07-11 01:22:01.251163','8','联系我们',2,'[{\"changed\": {\"fields\": [\"nav_url\"]}}]',7,1),(106,'2019-07-11 02:28:30.732939','6','广纳贤才，培训人才，知人善用，人尽其才',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',8,1),(107,'2019-07-11 03:31:44.467484','8','爱迪生',2,'[{\"changed\": {\"fields\": [\"main\"]}}]',11,1),(108,'2019-07-11 05:46:46.986326','1','国家药监局：药品、医械生产企业分别达4441家、1.7万家',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',8,1),(109,'2019-07-11 05:47:12.105248','1','国家药监局：药品、医械生产企业分别达4441家、1.7万家',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',8,1),(110,'2019-07-11 07:21:55.801380','4','weizhi',3,'',12,1),(111,'2019-07-11 07:48:40.746813','8','爱迪生',3,'',11,1),(112,'2019-07-11 07:48:40.755308','7','大',3,'',11,1),(113,'2019-07-11 07:50:58.754507','9','补中益气颗粒',1,'[{\"added\": {}}]',11,1),(114,'2019-07-11 07:51:50.883531','10','参苓白术颗粒',1,'[{\"added\": {}}]',11,1),(115,'2019-07-11 07:52:51.749080','11','银杏酮酯滴丸',1,'[{\"added\": {}}]',11,1),(116,'2019-07-11 07:53:22.957185','12','紫叶丹胶囊',1,'[{\"added\": {}}]',11,1),(117,'2019-07-11 07:53:50.654511','13','越鞠胶囊',1,'[{\"added\": {}}]',11,1),(118,'2019-07-11 07:54:56.266447','14','六味地黄片',1,'[{\"added\": {}}]',11,1),(119,'2019-07-11 07:55:32.260247','15','根痛平颗粒',1,'[{\"added\": {}}]',11,1),(120,'2019-07-11 07:56:16.938806','16','黑骨藤追风活络颗粒',1,'[{\"added\": {}}]',11,1),(121,'2019-07-11 07:56:48.002009','17','小柴胡泡腾片',1,'[{\"added\": {}}]',11,1),(122,'2019-07-11 07:57:22.752167','18','小柴胡颗粒',1,'[{\"added\": {}}]',11,1),(123,'2019-07-11 07:57:52.582338','19','抗感颗粒',1,'[{\"added\": {}}]',11,1),(124,'2019-07-11 07:58:22.531196','20','养阴降糖颗粒',1,'[{\"added\": {}}]',11,1),(125,'2019-07-11 07:58:50.762825','21','益肾灵颗粒',1,'[{\"added\": {}}]',11,1),(126,'2019-07-11 08:00:06.916412','22','七宝美髯颗粒',1,'[{\"added\": {}}]',11,1),(127,'2019-07-11 08:00:43.875444','23','玄麦甘桔颗粒',1,'[{\"added\": {}}]',11,1),(128,'2019-07-11 08:01:19.109514','24','丹七软胶囊',1,'[{\"added\": {}}]',11,1),(129,'2019-07-11 08:18:04.298544','12','jk',3,'',8,1),(130,'2019-07-11 08:18:04.307880','11','adsfqweq12',3,'',8,1),(131,'2019-07-11 08:18:04.309484','10','dfs',3,'',8,1),(132,'2019-07-11 08:18:04.311414','9','21',3,'',8,1),(133,'2019-07-11 08:18:04.313122','8','大师傅',3,'',8,1),(134,'2019-07-11 08:18:04.314895','7','dfs',3,'',8,1),(135,'2019-07-11 08:18:04.316602','6','广纳贤才，培训人才，知人善用，人尽其才',3,'',8,1),(136,'2019-07-11 08:18:04.318040','5','zhensgu',3,'',8,1),(137,'2019-07-11 08:18:04.320543','4','房屋租赁sadsd',3,'',8,1),(138,'2019-07-11 08:18:04.321975','3','1',3,'',8,1),(139,'2019-07-11 08:18:04.323325','2','扩大规模',3,'',8,1),(140,'2019-07-11 08:18:31.372406','18','小柴胡颗粒',2,'[{\"changed\": {\"fields\": [\"main\"]}}]',11,1),(141,'2019-07-11 08:18:57.287354','18','小柴胡颗粒',2,'[{\"changed\": {\"fields\": [\"main\", \"info_detail\"]}}]',11,1),(142,'2019-07-11 08:22:06.127606','4','高级产品组经理（北京）',3,'',13,1),(143,'2019-07-11 08:22:06.133249','3','高级产品组经理（北京）',3,'',13,1),(144,'2019-07-11 08:22:06.135593','2','高级产品组经理（北京）',3,'',13,1),(145,'2019-07-11 08:22:06.137781','1','高级产品组经理（北京）',3,'',13,1),(146,'2019-07-11 08:27:30.248529','5','fdsa',3,'',10,1),(147,'2019-07-11 08:27:30.252706','4','sda',3,'',10,1),(148,'2019-07-11 08:27:30.254182','3','ads',3,'',10,1),(149,'2019-07-11 08:27:30.256966','2','ads',3,'',10,1),(150,'2019-07-11 08:27:39.280572','1','证书',3,'',10,1),(151,'2019-07-11 08:32:07.107473','13','广纳贤才，培训人才，知人善用，人尽其才',1,'[{\"added\": {}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(8,'article','articles'),(9,'article','articletype'),(10,'article','certificate'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(11,'product','product'),(12,'product','producttype'),(5,'sessions','session'),(6,'user','myuser'),(7,'user','navbar'),(13,'user','position');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-07-05 09:21:50.292193'),(2,'contenttypes','0002_remove_content_type_name','2019-07-05 09:21:50.355592'),(3,'auth','0001_initial','2019-07-05 09:21:50.552469'),(4,'auth','0002_alter_permission_name_max_length','2019-07-05 09:21:50.582648'),(5,'auth','0003_alter_user_email_max_length','2019-07-05 09:21:50.589796'),(6,'auth','0004_alter_user_username_opts','2019-07-05 09:21:50.596125'),(7,'auth','0005_alter_user_last_login_null','2019-07-05 09:21:50.602506'),(8,'auth','0006_require_contenttypes_0002','2019-07-05 09:21:50.604910'),(9,'auth','0007_alter_validators_add_error_messages','2019-07-05 09:21:50.612049'),(10,'auth','0008_alter_user_username_max_length','2019-07-05 09:21:50.617994'),(11,'auth','0009_alter_user_last_name_max_length','2019-07-05 09:21:50.625313'),(12,'user','0001_initial','2019-07-05 09:21:50.861525'),(13,'admin','0001_initial','2019-07-05 09:21:50.943216'),(14,'admin','0002_logentry_remove_auto_add','2019-07-05 09:21:50.951966'),(15,'admin','0003_logentry_add_action_flag_choices','2019-07-05 09:21:50.960939'),(16,'article','0001_initial','2019-07-05 09:21:51.037670'),(17,'article','0002_articles_user','2019-07-05 09:21:51.098360'),(18,'product','0001_initial','2019-07-05 09:21:51.215624'),(19,'sessions','0001_initial','2019-07-05 09:21:51.257563'),(20,'product','0002_remove_producttype_typecode','2019-07-08 09:07:14.119907'),(21,'article','0003_auto_20190708_1708','2019-07-08 09:08:30.844899'),(22,'article','0004_auto_20190709_0908','2019-07-09 01:08:15.664463'),(23,'article','0005_auto_20190709_0918','2019-07-09 01:18:51.235188'),(24,'article','0006_auto_20190709_0919','2019-07-09 01:19:58.432508'),(25,'article','0007_auto_20190709_0951','2019-07-09 01:51:42.057469'),(26,'article','0008_articles_img_header','2019-07-09 03:29:10.624401'),(27,'article','0009_auto_20190709_1302','2019-07-09 05:02:33.774001'),(28,'product','0003_auto_20190709_1302','2019-07-09 05:02:33.779259'),(29,'article','0010_auto_20190709_1312','2019-07-09 05:12:15.127062'),(30,'article','0011_remove_articles_is_show','2019-07-10 05:17:42.264345'),(31,'user','0002_position','2019-07-10 07:14:19.192574'),(32,'user','0003_position_types','2019-07-10 07:37:32.364261'),(33,'product','0004_producttype_typecode','2019-07-10 09:03:41.583054'),(34,'product','0005_auto_20190710_1709','2019-07-10 09:09:32.812674'),(35,'product','0006_auto_20190710_1716','2019-07-10 09:16:38.727509');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1q0nere3dbl9soniv33nlfe74v17kpoe','ODIxNzkzYmQ2YzY4OGI1N2YxZDk0YWM1Nzc1Zjg1ZWEzNDE3MzIwYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MGNjNTU1OWRmMzZjODQyZmVmODA3MzhiNWVhNjk3NDI5OThhZjM3In0=','2019-07-24 00:41:35.390994'),('50a16u99macnn2be05whwisasups1pps','ODIxNzkzYmQ2YzY4OGI1N2YxZDk0YWM1Nzc1Zjg1ZWEzNDE3MzIwYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MGNjNTU1OWRmMzZjODQyZmVmODA3MzhiNWVhNjk3NDI5OThhZjM3In0=','2019-07-22 06:54:55.881523'),('hmmpbko4y4wg24ne107rar4kmro3gyvp','ODIxNzkzYmQ2YzY4OGI1N2YxZDk0YWM1Nzc1Zjg1ZWEzNDE3MzIwYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MGNjNTU1OWRmMzZjODQyZmVmODA3MzhiNWVhNjk3NDI5OThhZjM3In0=','2019-07-19 09:22:49.516377');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_product`
--

DROP TABLE IF EXISTS `product_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `name` varchar(50) NOT NULL,
  `composition` varchar(255) NOT NULL,
  `properties` varchar(255) NOT NULL,
  `standard` varchar(255) NOT NULL,
  `main` varchar(255) NOT NULL,
  `dosage` varchar(255) NOT NULL,
  `save_way` varchar(255) NOT NULL,
  `info_detail` longtext NOT NULL,
  `time_long` varchar(100) NOT NULL,
  `img` varchar(100) NOT NULL,
  `types_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `product_product_types_id_5a4d834e` (`types_id`),
  CONSTRAINT `product_product_types_id_5a4d834e_fk_product_producttype_id` FOREIGN KEY (`types_id`) REFERENCES `product_producttype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_product`
--

LOCK TABLES `product_product` WRITE;
/*!40000 ALTER TABLE `product_product` DISABLE KEYS */;
INSERT INTO `product_product` VALUES (9,'2019-07-11 07:50:58.752107','补中益气颗粒','无','无','无','补中益气 升阳举陷 专利提取工艺 有效成分高','无','无','补中益气 升阳举陷 专利提取工艺 有效成分高','无','upload_img/product/汉典集团招聘.jpg',6),(10,'2019-07-11 07:51:50.879325','参苓白术颗粒','无','无','无','健脾养胃 益气祛湿 安补五脏 以参养身','无','无','健脾养胃 益气祛湿 安补五脏 以参养身','无','upload_img/product/汉典集团招聘_fxH4uGr.jpg',5),(11,'2019-07-11 07:52:51.746863','银杏酮酯滴丸','无','无','无','酮酯加滴丸 银杏之臻品 通心脑 稳血压 活血抗栓保健康','无','无','酮酯加滴丸 银杏之臻品 通心脑 稳血压 活血抗栓保健康','无','upload_img/product/汉典集团招聘_JHN9cc6.jpg',5),(12,'2019-07-11 07:53:22.955268','紫叶丹胶囊','无','无','无','抗乙肝病毒 调节免疫 抗纤维化 抑制肿瘤细胞增殖','无','无','抗乙肝病毒 调节免疫 抗纤维化 抑制肿瘤细胞增殖','无','upload_img/product/汉典集团招聘_yGXk5bN.jpg',5),(13,'2019-07-11 07:53:50.652302','越鞠胶囊','无','无','无','解“六郁” 调理气机肝脾舒 治病求本“丹溪”方 气血痰火食湿除','无','无','解“六郁” 调理气机肝脾舒 治病求本“丹溪”方 气血痰火食湿除','无','upload_img/product/汉典集团招聘_2arI0xI.jpg',5),(14,'2019-07-11 07:54:56.264411','六味地黄片','无','无','无','腰膝酸软 头晕耳鸣 肾阴虚就用六味地黄片','无','无','腰膝酸软 头晕耳鸣 肾阴虚就用六味地黄片','无','upload_img/product/汉典集团招聘_T39pDvW.jpg',5),(15,'2019-07-11 07:55:32.258975','根痛平颗粒','无','无','无','活血通络 消肿止痛 強肾壮骨','无','无','活血通络 消肿止痛 強肾壮骨','无','upload_img/product/汉典集团招聘_dUhO2aZ.jpg',5),(16,'2019-07-11 07:56:16.937183','黑骨藤追风活络颗粒','无','无','无','苗药驱风湿 抗炎止痛 调节免疫 阻止关节变形','无','无','苗药驱风湿 抗炎止痛 调节免疫 阻止关节变形','无','upload_img/product/汉典集团招聘_0sW1yT8.jpg',5),(17,'2019-07-11 07:56:48.000645','小柴胡泡腾片','无','无','无','酸酸甜甜不苦的中药 解表散热 和解少阳','无','无','酸酸甜甜不苦的中药 解表散热 和解少阳','无','upload_img/product/汉典集团招聘_wcBkda5.jpg',5),(18,'2019-07-11 07:57:22.750993','小柴胡颗粒','无','无','无','治感冒           护肝胃        中医和解经典方','无','无','治感冒     护肝胃      中医和解经典方','无','upload_img/product/汉典集团招聘_ish3Nc1.jpg',5),(19,'2019-07-11 07:57:52.579373','抗感颗粒','无','无','无','清热解毒抗感冒 同时有效清除感冒七大症状','无','无','清热解毒抗感冒 同时有效清除感冒七大症状','无','upload_img/product/汉典集团招聘_DMzyKgn.jpg',5),(20,'2019-07-11 07:58:22.529265','养阴降糖颗粒','无','无','无','糖尿病好帮手 养阴益气又活血 改善微循环并发症 抗疲劳 解干渴','无','无','糖尿病好帮手 养阴益气又活血 改善微循环并发症 抗疲劳 解干渴','无','upload_img/product/汉典集团招聘_fE4namo.jpg',5),(21,'2019-07-11 07:58:50.760926','益肾灵颗粒','无','无','无','衍生自“古今种子第一方”五子衍宗丸 益肾壮阳 强力生精','无','无','衍生自“古今种子第一方”五子衍宗丸 益肾壮阳 强力生精','无','upload_img/product/汉典集团招聘_GOJjKxT.jpg',5),(22,'2019-07-11 08:00:06.914958','七宝美髯颗粒','无','无','无','七宝美髯抗衰老 皇家御用《本草》方 平补肝肾益精血 延年益寿子嗣传','无','无','七宝美髯抗衰老 皇家御用《本草》方 平补肝肾益精血 延年益寿子嗣传','无','upload_img/product/汉典集团招聘_I3VfqvE.jpg',5),(23,'2019-07-11 08:00:43.873612','玄麦甘桔颗粒','无','无','无','清热滋阴 祛痰利咽 抗炎镇咳 润燥通便','无','无','清热滋阴 祛痰利咽 抗炎镇咳 润燥通便','无','upload_img/product/汉典集团招聘_PA6w8FN.jpg',5),(24,'2019-07-11 08:01:19.107829','丹七软胶囊','无','无','无','有效抑制心室重构及动脉粥样硬化进展 经典活血配伍组合，平和不刺激','无','无','有效抑制心室重构及动脉粥样硬化进展 经典活血配伍组合，平和不刺激','无','upload_img/product/汉典集团招聘_ZO9CxXT.jpg',5);
/*!40000 ALTER TABLE `product_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_producttype`
--

DROP TABLE IF EXISTS `product_producttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_producttype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `typename` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `typename` (`typename`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_producttype`
--

LOCK TABLES `product_producttype` WRITE;
/*!40000 ALTER TABLE `product_producttype` DISABLE KEYS */;
INSERT INTO `product_producttype` VALUES (5,'2019-07-10 09:05:23.674569','中成新药品'),(6,'2019-07-10 09:08:26.120418','经典中成药');
/*!40000 ALTER TABLE `product_producttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_myuser`
--

DROP TABLE IF EXISTS `user_myuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_myuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_myuser`
--

LOCK TABLES `user_myuser` WRITE;
/*!40000 ALTER TABLE `user_myuser` DISABLE KEYS */;
INSERT INTO `user_myuser` VALUES (1,'pbkdf2_sha256$120000$HUMhCXq2WM18$HcruCwAs8uF72aBQDDnRxnKT8sdkm2AHjJBLgmdcs8s=','2019-07-10 00:41:35.385853',1,'amdin','admin@handian.com',NULL,1,1,'2019-07-05 09:22:14.962394');
/*!40000 ALTER TABLE `user_myuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_myuser_groups`
--

DROP TABLE IF EXISTS `user_myuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_myuser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_myuser_groups_myuser_id_group_id_680fbae2_uniq` (`myuser_id`,`group_id`),
  KEY `user_myuser_groups_group_id_e21a6dfd_fk_auth_group_id` (`group_id`),
  CONSTRAINT `user_myuser_groups_group_id_e21a6dfd_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_myuser_groups_myuser_id_dfd02c0f_fk_user_myuser_id` FOREIGN KEY (`myuser_id`) REFERENCES `user_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_myuser_groups`
--

LOCK TABLES `user_myuser_groups` WRITE;
/*!40000 ALTER TABLE `user_myuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_myuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_myuser_user_permissions`
--

DROP TABLE IF EXISTS `user_myuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_myuser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_myuser_user_permiss_myuser_id_permission_id_ae8df385_uniq` (`myuser_id`,`permission_id`),
  KEY `user_myuser_user_per_permission_id_d16c386c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `user_myuser_user_per_myuser_id_5d2dcfb0_fk_user_myus` FOREIGN KEY (`myuser_id`) REFERENCES `user_myuser` (`id`),
  CONSTRAINT `user_myuser_user_per_permission_id_d16c386c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_myuser_user_permissions`
--

LOCK TABLES `user_myuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `user_myuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_myuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_navbar`
--

DROP TABLE IF EXISTS `user_navbar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_navbar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `zh_name` varchar(20) NOT NULL,
  `nav_url` varchar(100) DEFAULT NULL,
  `nav_num` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nav_num` (`nav_num`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_navbar`
--

LOCK TABLES `user_navbar` WRITE;
/*!40000 ALTER TABLE `user_navbar` DISABLE KEYS */;
INSERT INTO `user_navbar` VALUES (1,'2019-07-06 06:23:36.696603',1,'首页','/',1),(2,'2019-07-06 06:24:13.266406',1,'走进汉典','/about/',2),(3,'2019-07-06 06:24:36.988643',1,'名医咨询','/famous/',3),(4,'2019-07-06 06:24:53.088904',1,'医学中心','/center/',4),(5,'2019-07-06 06:25:08.076322',1,'服务与产品','/product/',5),(6,'2019-07-06 06:25:23.659505',1,'新闻动态','/news/',6),(7,'2019-07-06 06:26:04.196693',1,'招贤纳士','/recruitment/',7),(8,'2019-07-06 06:26:37.239158',1,'联系我们','/contact/',8);
/*!40000 ALTER TABLE `user_navbar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_position`
--

DROP TABLE IF EXISTS `user_position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_position` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `position_title` varchar(100) NOT NULL,
  `work_experience` varchar(100) NOT NULL,
  `work_place` varchar(100) NOT NULL,
  `work_salary` varchar(20) NOT NULL,
  `work_time` varchar(20) NOT NULL,
  `work_need_person` varchar(20) NOT NULL,
  `work_need` longtext NOT NULL,
  `work_for` longtext NOT NULL,
  `contact` longtext NOT NULL,
  `types` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_position`
--

LOCK TABLES `user_position` WRITE;
/*!40000 ALTER TABLE `user_position` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_position` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-11 16:36:31
