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
('Negroni','25 ml Gin','25 ml Sweet Red Vermout','25 ml Campari','Orange Peel',NULL,NULL,NULL,NULL,NULL,NULL),
('Bramble','50 ml Gin','10 ml Crème de Mure','25 ml Lemon Juice','12 1/2 ml Sugar Syrup','Blackberry',NULL,NULL,NULL,NULL,NULL),
('Margarita','37 1/2 ml Tequila','12 1/2 ml Triple Sec','25 ml Lime Juice','12 1/2 ml Simple Syrup','salt',NULL,NULL,NULL,NULL,NULL),
('Dark n Stormy','50 ml Dark Rum','4 Lime quarters','1 1/2 bar spoons Brown Sugar','splash Ginger Beer','Lime wedge',NULL,NULL,NULL,NULL,NULL),
('Cuba Libre','50 ml Anejo Rum','7 ml Lime juice,','100 ml Cola','Lime wedge',NULL,NULL,NULL,NULL,NULL,NULL),
('Sanzerac','50 ml Rye Whiskey','5 ml Absinthe','3 dashes of Peychauds Bitters','Sugar Cube','Lemon Peel',NULL,NULL,NULL,NULL,NULL),
('Bloody Mary','37 1/2 ml Peppered Vodka','15 ml Sweet Vermouth','35 ml Tomato Juice','splash Red Wine','splash of Worcestershire sauce','10 dashes Tobasco sauce',' 25 ml Lemon Juice','10 dashes Salt','10 dashes Pepper','3 Cucumber slices'),
('Manhattan','50 ml Bourbon','10 ml Sweet Vermouth','10 ml Dry Vermouth','2 dashes Angostura Bitters','Orange peel',NULL,NULL,NULL,NULL,NULL),
('Long Island Iced Tea','15 ml Gin','15 ml Vodka','15 ml Tequila','15 ml White Rum','15 ml Triple Sec','25 ml Lemon Juice','30 ml Gomme syrup','splash of Cola',NULL,NULL),
('Mai-Tai','20 ml Dark Rum','20 ml Light Rum','Splash of Demerara','20 ml Triple Sec','20 ml Lime Juice','10 ml Orgeat Syrup','Mint spring','Orange wedge',NULL,NULL),
('Amaretto Sour','50 ml Amaretto','25 ml Lemon Juice','12 1/2 ml Simple Syrup','dash Egg-White','dash Angostura Bitters','Lemon Zest',NULL,NULL,NULL,NULL),
('Singapore Sling','37 1/2 ml Gin','12 1/2 ml Cherry Heering','12 1/2 ml Benedictine','25 ml Lemon Juice',' 2 dashes Orange Bitters','2 dashes Angostura Bitters','dash Soda Water','Lemon slice',NULL,NULL),
('French Martini','25 ml Vodka','25 ml Chambord','75 ml Pineapple Juice','3 Raspberries for Garnish',NULL,NULL,NULL,NULL,NULL,NULL),
('Espresso Martini','37 1/2 ml Vanilla Vodka','12 1/2 ml Kahlúa','Double Espresso','12 1/2 ml Sugar Syrup','3 Coffee Beans',NULL,NULL,NULL,NULL,NULL),
('Strawberry Daiquiri','37 `1/2 ml Bacardi Rum','12 1/2 ml Strawberry Liqueur','25 ml Lime Juice,','12 1/2 ml Sugar Syrup','1 Strawberry',NULL,NULL,NULL,NULL,NULL),
('Moscow Mule','37 1/2 ml Vodka','25 ml Lime juice','splash Ginger Beer',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Clover Club','37 1/2 ml Gin','37 1/2 ml Lemon Juice','20 ml Sweet Vermouth','20 ml Raspberry Syrup','1 Egg White',NULL,NULL,NULL,NULL,NULL),
('Mint Julep','50 ml Bourbon','spoon Granulated Sugar','8 Mint leaves','Mint sprigs',NULL,NULL,NULL,NULL,NULL,NULL),
('John Collins','50 ml Bourbon','25 ml Lemon Juice','12 1/2 ml Sugar Syrup','splash of Soda Water','Maraschino Cherry',NULL,NULL,NULL,NULL,NULL),
('Gin Sour','50 ml Gin','25 ml Lemon Juice','12 1/2 ml Simple Syrup','Splash Egg-White',NULL,NULL,NULL,NULL,NULL,NULL),
('Appletini','40 ml Vodka','15 ml Apple Schapps','15 ml Triple Sec','Apple Slice',NULL,NULL,NULL,NULL,NULL,NULL),
('White Lady','50 ml Gin','25 ml Triple Sec','25 ml Lemon Juice','Lemon Rind',NULL,NULL,NULL,NULL,NULL,NULL),
('Black Russian','45 ml Vodka','25 ml Coffee Liqueur',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Brandy Alexander','37 1/2 ml Brandy','20 ml Crème de Cacao','50 ml Milk','Grated Nutmeg',NULL,NULL,NULL,NULL,NULL,NULL),
('French 75','37 1/2 ml Gin','splash Champagne','10 ml Sugar Syrup','15 ml Lemon Juice',NULL,NULL,NULL,NULL,NULL,NULL),
('Navy Grog','50 ml Dark Rum','25 ml Light Rum','20 ml Lime Juice',' 50 ml Pink Grapefruit Juice','12 1/2 ml Runny Honey','Top-Up Soda',NULL,NULL,NULL,NULL),
('Rusty Nail','50 ml Scotch Whisky','25 ml Whiskey Liqueu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Pisco Sour','50 ml Pisco','12 1/2 ml Simple Syrup','25 ml Lime Juice','splash Egg White','Lime wedge',NULL,NULL,NULL,NULL,NULL),
('Bucks Fizz','50 ml Orange Juice','100 ml Champagne',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Rum Runner','37 1/2 ml Aged Rum','20 ml White Rum','12 1/2 ml Creme de Banane','12 1/2 ml Creme de Mure','15 ml Pineapple Juice','15 ml Orange Juice','Orange slice',NULL,NULL,NULL),
('El-Presidente','50 ml Aged Rum','12 1/2 ml Orange Liqueur','10 ml Dry Vermouth','splash Grenadine','Orange Peel',NULL,NULL,NULL,NULL,NULL),
('WooWoo','37 1/2 ml Peach Schnapps','37 1/2 ml Vodka','90 ml Cranberry Juice',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Kir Royale','80 ml Champagne','20 ml Crème de Cassis',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Bellini','100 ml Prosecco','50 ml Peach puree','4 dashes Peach Bitters',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Lemon Drop Martini','37 1/2 ml Vodka','12 1/2 ml Orange Liqueur','12 1/2 ml Sugar Syrup','25 ml Lemon Juice','Lemon Twist','Sugar',NULL,NULL,NULL,NULL),
('Pink Gin','25 ml Gin','3 dashes Angostura Bitters',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Salty Dog','50 ml Vodka','20 ml Dry Sherry','37 1/2 ml Grapefruit Juice','15 ml Sugar Syrup, Salt','Grapefruit Zest',NULL,NULL,NULL,NULL,NULL),
('B-52','10 ml Coffee Liqueur','10 ml Irish Cream Liqueur','10 ml Triple Sec',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Painkiller','50 ml Dark Rum','25 ml Coconut Cream','100 ml Pineapple Juice','25 ml Orange Juice','Orange Wheel',NULL,NULL,NULL,NULL,NULL,NULL),
('Screwdriver','50 ml Vodka','100 ml Orange Juice','Lime wedge',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('French connection ','25 ml Cognac','25 ml Amaretto',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Paloma','50 ml Tequila','27 1/2 ml Pink Grapefruit Juice','20 ml Sugar Syrup','10 ml Lime Juice','Pink Grapefruit wedge',NULL,NULL,NULL,NULL,NULL),
('Royal Hawaiian','37 1/2 ml Gin','25 ml Pineapple Juice','25 ml Lemon Juice','5 ml Orgeat Syrup','12 1/2 ml Simple Syrup','Lemon Slice','Mint Leaves',NULL,NULL,NULL),
('Tommys Margarita','50 ml Tequila','25 ml Lime Juice','Lemon Slices','Blackberry',NULL,NULL,NULL,NULL,NULL,NULL),
('Sea Breeze','50 ml Vodka',' 50 ml Cranberry Juice','37 1/2 ml Grapefruit Juice','Lime Slice',NULL,NULL,NULL,NULL,NULL,NULL),
('Ramos Giz Fizz','50 ml Gin','25 ml Double Cream','1 Egg White','15 ml Lemon Juice','15 ml Lime Juice','20 ml Sugar Syrup','splash soda water',NULL,NULL,NULL),
('El Diablo','37 1/2 ml Tequila','12 1/2 ml Crème de Cassis','12 1/2 ml Lime Juice','Ginger Beer',NULL,NULL,NULL,NULL,NULL,NULL),
('Breakfast Martini','45 ml Gin','20 ml Triple Sec','20 ml Lemon Juice','12 1/2 ml Sugar Syrup','spoon of Orange Marmalade','flamed lemon zest',NULL,NULL,NULL,NULL),
('Caipivodka','50 ml Vodka','1/2 Lime','2 teaspoons Sugar','Lemon Slice',NULL,NULL,NULL,NULL,NULL,NULL),
('Baja Gold','50 ml Tequila','12 1/2 ml Triple Sec','50 ml Pineapple Juice','12 1/2 ml Lime Juice','12 1/2 ml Simple Syrup','Lime Wedge',NULL,NULL,NULL,NULL),
('Sex on the Beach','25 ml Vodka','25 ml Peach Schnapps','40 ml Orange Juice','20 ml Cranberry Juice','Orange Slice',NULL,NULL,NULL,NULL,NULL),
('Tequila Sunrise','50 ml Tequila','80 ml Orange Juice','dash Grenadine Syrup','Lime wedge','Orange slice',NULL,NULL,NULL,NULL,NULL),
('Bronx','50 ml Gin','12 1/2 ml Sweet Red Vermouth','12 1/2 ml Dry Vermouth','25 ml Fresh Orange Juice','Orange Zest Twist','Maraschino Cherry',NULL,NULL,NULL,NULL),
('Caribbean Sunrise','45 ml Rum','60 ml Orange Juice','15 ml Grenadine Syrup','Orange Slice',NULL,NULL,NULL,NULL,NULL,NULL),
('Gibson','60 ml Gin','10 ml Dry Vermouth','1 Silverskin Onion',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Bay Breeze','50 ml Vodka','25 ml Pineapple Juice','25 ml Cranberry Juice','25 ml Lemon Juice','12 1/2 ml Sugar Syrup','Orange Wedge',NULL,NULL,NULL,NULL),
('Rasberry Mojito','50 ml White Rum','15 ml Raspberry Liqueur','25 ml Lime Juice','35 ml Soda Water','2 Bar Spoons Superfine Sugar','5 Raspberries','8 Mint Leaves',NULL,NULL,NULL),
('Sidecar','37 1/2 ml Cognac','12 1/2 ml Triple Sec','20 ml Lemon Juice','dash Egg White','5 ml Sugar Syrup','Orange peel',NULL,NULL,NULL,NULL),
('Champagne Cocktail','100 ml Champagne','25 ml Brandy','spoon Sugar','4 dashes Angostura Bitters',NULL,NULL,NULL,NULL,NULL,NULL),
('Godfather','37 1/2 ml Scotch Whiskey','12 1/2 ml Amaretto',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Hemingway Daiquiri','50 ml White Rum','10 ml Maraschino Liqueur','12 1/2 ml Grapefruit Juice','12 1/2 ml Lime Juice','12 1/2 ml Simple Syrup','Maraschino Cherry',NULL,NULL,NULL,NULL),
('Rasburry Daiquiri','50 ml Light Rum','25 ml Lime Juice','2 spoons Caster Sugar','6 Raspberries',NULL,NULL,NULL,NULL,NULL,NULL),
('Blueberry Collins','50 ml Gin','25 ml Lemon Juice','12 1/2 ml Vanilla Sugar Syrup','19 Blueberries','Top-Up Soda water',NULL,NULL,NULL,NULL,NULL),
('Gimlet','60 ml Premium Gin','10 ml Lime Cordial',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Chocolate-Covered Cherry','30 ml Baileys Cream Liqueur','30 ml Coffee Liqueur','1 Tablespoon Grenadine Syrup',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Lemongrad','50 ml Citron Vodka','25 ml Lemon Juice','12 1/2 ml Elderflower Cordial','Tonic Water','Pink Grapefruit Wedge',NULL,NULL,NULL,NULL,NULL),
('Planters Punch','50 ml Dark Rum','30 ml Lime Juice','10 ml Grenadine Syrup','15 ml Sugar Syrup','Splash of Soda Water','2 dashes Angostura Bitters',NULL,NULL,NULL,NULL),
('Blushing Bride','25 ml Peach Schnapps','100 ml Champagne','25 ml Grenadine Syrup',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
('Gin Rickey','50 ml Gin','25 ml Lime Juice','12 1/2 ml Sugar Syrup','Soda Water','Lime wedge',NULL,NULL,NULL,NULL,NULL),
('Passion Fruit Daiquiri','25 ml Bacardi Rum','25 ml Passoa','25 ml Lime Juice','12 1/2 ml Sugar Syrup','1 Passion Fruit',NULL,NULL,NULL,NULL,NULL),
('Cantarito','37 1/2 ml Tequila','12 1/2 ml Lime Juice','12 1/2 ml Orange Juice','12 1/2 ml Lemon Juice','10 ml Grapefruit Soda','Lemon','Lime & Orange wedges','Salt',NULL,NULL),
('Brandy Collins','37 1/2 ml Gin','splash Champagne','10 ml Sugar Syrup','15 ml Lemon Juice',NULL,NULL,NULL,NULL,NULL,NULL),
('Volcano','125 ml Golden Rum','25 ml Dark Rum','10 ml 151 Rum','50 ml Pink Grapefruit Juice','50 ml Orange Juice','50 ml Pineapple Juice','50 ml Lime Juice','25 ml Falernum','50 ml Grenadine Syrup','Cinnamon'),
('Americano','25 ml Campari','25 ml Sweet Vermouth','dash of Soda Water','Lemon Peel',NULL,NULL,NULL,NULL,NULL,NULL),
('Accomplice','50 ml Raspberry Vodka','5 ml Black Raspberry Liqueur','12 1/2 ml Lemon Juice','8 Blackberries','Top-Up Ginger Beer',NULL,NULL,NULL,NULL,NULL),
('Berry Nice','40 ml White Rum','30 ml Lime Juice','3 Mint Leaves','2 teaspoons Sugar','Splash of Champagne',NULL,NULL,NULL,NULL,NULL),
('Mojito Royal','50 ml Vodka','25 ml Lemon Juice','12 1/2 ml Sugar Syrup','Champagne','3 Strawberries',NULL,NULL,NULL,NULL,NULL),
('Tom Collins','37 1/2 ml Gin','25 ml Lemon Juice','12 1/2 ml Sugar Syrup','splash Soda Water',NULL,NULL,NULL,NULL,NULL,NULL),
('','','','','','','','','','',''),
('','','','','','','','','','',''),
('','','','','','','','','','',''),
('','','','','','','','','','',''),




