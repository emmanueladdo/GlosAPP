-- This creates the glosapp schema

CREATE SCHEMA IF NOT EXISTS `glosapp`;

-- creates the product table and colums
CREATE TABLE `glosapp`.`products` (
  `product_id` INT NOT NULL AUTO_INCREMENT,
  `product_name` VARCHAR(100) NOT NULL,
  `uom_id` INT NOT NULL,
  `price_per_unit` DOUBLE NOT NULL,
  PRIMARY KEY (`product_id`));
