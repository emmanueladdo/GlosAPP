-- This creates the glosapp schema

CREATE SCHEMA IF NOT EXISTS `glosapp`;

-- creates the product table and colums
CREATE TABLE `glosapp`.`products` (
  `product_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `uom_id` INT NOT NULL,
  `price_per_unit` DOUBLE NOT NULL,
  PRIMARY KEY (`product_id`)
);

-- creates unit of messure  table 
CREATE TABLE `glosapp`.`uom` (
  `uom_id` INT NOT NULL AUTO_INCREMENT,
  `uom_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`uom_id`)
);

-- creates the place holder uom 
INSERT INTO `glosapp`.`uom` (`uom_id`, `uom_name`) VALUES ('1', 'each ');
INSERT INTO `glosapp`.`uom` (`uom_id`, `uom_name`) VALUES ('2', 'kg');

-- creates a foreign key for unit of measurement in products table
ALTER TABLE `glosapp`.`products`
ADD INDEX `fk_uom_id_idx` (`uom_id` ASC) VISIBLE;

ALTER TABLE `glosapp`.`products`
ADD CONSTRAINT `fk_uom_id`
  FOREIGN KEY (`uom_id`)
  REFERENCES `glosapp`.`uom` (`uom_id`)
  ON DELETE NO ACTION
  ON UPDATE RESTRICT;

-- creates orders table
CREATE TABLE `glosapp`.`orders` (
  `order_id` INT NOT NULL AUTO_INCREMENT,
  `customer_name` VARCHAR(225) NOT NULL,
  `total` DOUBLE NOT NULL,
  `datetime` DATETIME NOT NULL,
  PRIMARY KEY (`order_id`)
);

-- creates details for orders
CREATE TABLE `glosapp`.`order_details` (
  `order_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  `quantity` DOUBLE NOT NULL,
  `total_price` DOUBLE NOT NULL,
  INDEX `fk_product_id_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_id`
    FOREIGN KEY (`order_id`)
    REFERENCES `glosapp`.`orders` (`order_id`)
    ON DELETE NO ACTION
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_product_id`
    FOREIGN KEY (`product_id`)
    REFERENCES `glosapp`.`products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE RESTRICT
);

-- creates user called gstore and grants all privileges of glosapp to it
CREATE USER 'gstore'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
GRANT ALL PRIVILEGES ON glosapp.* TO 'gstore'@'localhost';
FLUSH PRIVILEGES;
