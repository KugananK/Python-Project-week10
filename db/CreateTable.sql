CREATE TABLE IF NOT EXISTS `games` (
    `game_id` INT(11) NOT NULL AUTO_INCREMENT,
    `game_name` VARCHAR(40) NULL,
    `genre` VARCHAR(40) NULL,
    `release_date` int NULL,
    `price` float NULL,
    `publisher_id` INT NOT NULL,
    Foreign KEY (`publisher_id`) REFERENCES `publishers`(`publisher_id`) ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY (`game_id`)
    ) 
    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE IF NOT EXISTS `publishers` (
    `publisher_id` INT NOT NULL UNIQUE AUTO_INCREMENT,
    `publisher_name` VARCHAR(40) NOT NULL,
    PRIMARY KEY (`publisher_id`)
    ) 
    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `games` WRITE;
LOCK TABLES `publishers` WRITE;

INSERT INTO
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `games` VALUES (1,'Divinity','RPG','2014', '39.99', 1),(2,'Divinity 2','RPG','2017', '49.99', 1), (3,'Borderlands','Loot and Shoot','2008', '39.99', 2);
INSERT INTO `publishers` VALUES (1, 'Larian'), (2, 'Gearbox')
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;