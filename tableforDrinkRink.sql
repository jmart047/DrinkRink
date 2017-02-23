/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`classicmodels` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `classicmodels`;

/*Table structure for table `customers` */

DROP TABLE IF EXISTS `drinks`;

CREATE TABLE `drinks` (
  `DrinkName` int(11) NOT NULL,
  `Ing_1` varchar(50) NOT NULL,
  `Ing_2` varchar(50) NOT NULL,
  `Ing_4` varchar(50) NOT NULL,
  `Ing_5` varchar(50) NOT NULL,
  `Ing_6` varchar(50) NOT NULL,
  `Ing_7` varchar(50) NOT NULL,
  `Ing_9` varchar(50) NOT NULL,
  `Ing_10` varchar(50) NOT NULL,
  PRIMARY KEY (`DrinkName`),
  KEY `Ing_1` (`Ing_1`),
  CONSTRAINT `drinks_ibfk_1` FOREIGN KEY (`Ing_1`) REFERENCES `drink`(`DrinkName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `drinks` */

insert  into `drinks`(`Ing_1`,`Ing_2`,`Ing_3`,`Ing_4`,`Ing_5`,`Ing_7`,`Ing_8`,`Ing_9`,`Ing_10`) values 