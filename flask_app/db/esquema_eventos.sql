-- -----------------------------------------------------
-- Schema esquema_eventos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_eventos` DEFAULT CHARACTER SET utf8 ;
USE `esquema_eventos` ;

-- -----------------------------------------------------
-- Table `esquema_eventos`.`usuarios`
--------------------------------------------------------

CREATE TABLE IF NOT EXISTS `esquema_usuarios`.`usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB

-- -----------------------------------------------------
-- Table `esquema_eventos`.`eventos`
--------------------------------------------------------

CREATE TABLE IF NOT EXISTS `esquema_usuarios`.`eventos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre_evento` VARCHAR(255) NOT NULL,
  `ubicacion` VARCHAR(255) NOT NULL,
  `fecha` DATE NOT NULL,
  `detalles` TEXT NOT NULL,
  `usuario_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX fk_eventos_usuarios_idx (usuario_id ASC),
  CONSTRAINT fk_eventos_usuarios
    FOREIGN KEY (`usuario_id`)
    REFERENCES usuarios (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
) ENGINE = InnoDB;