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
  `DrinkName` varchar(50) NOT NULL,
  `Ing_1` varchar(50) NOT NULL,
  `Ing_2` varchar(50) NOT NULL,
  `Ing_3` varchar(50) NOT NULL,
  `Ing_4` varchar(50) NOT NULL,
  `Ing_5` varchar(50) NOT NULL,
  `Ing_6` varchar(50) NOT NULL,
  `Ing_7` varchar(50) NOT NULL,
  `Ing_8` varchar(50) NOT NULL,
  `Ing_9` varchar(50) NOT NULL,
  `Ing_10` varchar(50) NOT NULL,
  PRIMARY KEY (`DrinkName`),
  KEY `Ing_1` (`Ing_1`),
  CONSTRAINT `drinks_ibfk_1` FOREIGN KEY (`Ing_1`) REFERENCES `drink`(`DrinkName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `drinks` */

insert  into `drinks`(`DrinkName`,`Ing_1`,`Ing_2`,`Ing_3`,`Ing_4`,`Ing_5`,`Ing_6`,`Ing_7`,`Ing_8`,`Ing_9`,`Ing_10`) values 


('Mojito','50 ml White Rum','8 Mint leaves',' 12 1/2 ml Sugar Syrup','25 ml Lime Juice','2 Mint springs',NULL,NULL,NULL,NULL,NULL,),
('Martini','50 ml Gin','10 ml Dry Vermouth','Lemon twist',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Daiquiri','50 ml White Rum','1 1/2 bar spoons Sugar','25 ml Lime Juice','Lime slice',NULL,NULL,NULL,NULL,NULL,NULL),
('Old Fashioned','50 ml Bourbon','2 dashes Angostura Bitters','1 dash Orange Bitters','1 bar spoon Sugar','Orange peel',NULL,NULL,NULL,NULL,NULL),
('Cosmopolitan','37 1/2 ml Citrus Vodka','12 1/2 ml Triple Sec','30 ml Cranberry Juice','1/2 squeezed lemon','12 1/2 ml Sugar Syrup',NULL,NULL,NULL,NULL,NULL),
('Caipirinha','50 ml Cachaca','1/2 Lime','1 teaspoon Brown Sugar','Lime Wedge',NULL,NULL,NULL,NULL,NULL,NULL),
('White Russian','37 1/2 ml Vodka','25 ml Coffee Liqueur','15 ml Cream','15 ml Milk','Chocolate Powder','Coffee Bean',NULL,NULL,NULL,NULL),
('Pina Colada','50 ml White Rum','100 ml Pineapple Juice','25 ml Coconut Cream','25 ml Cream','Pineapple Slice','pinch of Salt',NULL,NULL,NULL,NULL),
('','','','','','','','','','',''),
('','','','','','','','','','',''),
('','','','','','','','','','',''),
('','','','','','','','','','',''),
('','','','','','','','','','',''),
('','','','','','','','','','',''),
('','','','','','','','','','',''),
('','','','','','','','','','',''),