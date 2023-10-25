-- This creates the glosapp schema

CREATE SCHEMA IF NOT EXISTS `glosapp`;

-- creates the product table and colums
CREATE TABLE `glosapp`.`products` (
  `product_id` INT NOT NULL AUTO_INCREMENT,
  `product_name` VARCHAR(100) NOT NULL,
  `uom_id` INT NOT NULL,
  `price_per_unit` DOUBLE NOT NULL,
  PRIMARY KEY (`product_id`));

-- creates unit of messure  table 
CREATE TABLE `glosapp`.`uom` (
  `uom_id` INT NOT NULL AUTO_INCREMENT,
  `uom_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`uom_id`));

-- create the place holder uom 
INSERT INTO `glosapp`.`uom` (`uom_id`, `uom_name`) VALUES ('1', 'each ');
INSERT INTO `glosapp`.`uom` (`uom_id`, `uom_name`) VALUES ('2', 'kg');
