-- MySQL Script generated by MySQL Workbench
-- Sun 17 Jun 2018 08:52:54 PM -03
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Local`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Local` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Local` (
  `id` INT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `unidade` VARCHAR(45) NOT NULL,
  `regiao` VARCHAR(45) NULL,
  `estatistica_partidaria` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Coligacao`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Coligacao` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Coligacao` (
  `id` INT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `majoritaria` TINYINT(1) NOT NULL,
  `proporcional` TINYINT(1) NOT NULL,
  `presidente` INT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `Presidente_UNIQUE` (`presidente` ASC),
  UNIQUE INDEX `nome_UNIQUE` (`nome` ASC),
  CONSTRAINT `fk_Presidente`
    FOREIGN KEY (`presidente`)
    REFERENCES `mydb`.`Candidato` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Partido`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Partido` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Partido` (
  `id` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `sigla` VARCHAR(10) NOT NULL,
  `alinhamento` VARCHAR(45) NULL,
  `coligacao` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Partido_Coligação1_idx` (`coligacao` ASC),
  UNIQUE INDEX `Sigla_UNIQUE` (`sigla` ASC),
  CONSTRAINT `fk_Partido_Coligação1`
    FOREIGN KEY (`coligacao`)
    REFERENCES `mydb`.`Coligacao` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Candidato`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Candidato` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Candidato` (
  `id` INT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `foto` BLOB NULL,
  `formacao` VARCHAR(45) NULL,
  `alfabetizacao` LONGTEXT NULL,
  `origem` INT NOT NULL,
  `partido` INT NOT NULL,
  `propostas` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Candidato_Local1_idx` (`origem` ASC),
  INDEX `fk_Candidato_Partido1_idx` (`partido` ASC),
  CONSTRAINT `fk_Candidato_Local1`
    FOREIGN KEY (`origem`)
    REFERENCES `mydb`.`Local` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Candidato_Partido1`
    FOREIGN KEY (`partido`)
    REFERENCES `mydb`.`Partido` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Cargo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Cargo` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Cargo` (
  `id` INT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `poder` VARCHAR(45) NOT NULL,
  `prereq` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Candidatura`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Candidatura` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Candidatura` (
  `intencao_de_votos` INT NOT NULL,
  `candidato` INT NULL,
  `local` INT NOT NULL,
  `cargo` INT NOT NULL,
  PRIMARY KEY (`candidato`),
  INDEX `fk_Candidatura_Candidato_idx` (`candidato` ASC),
  INDEX `fk_Candidatura_Local1_idx` (`local` ASC),
  INDEX `fk_Candidatura_Cargo_idx` (`cargo` ASC),
  CONSTRAINT `fk_Candidatura_Candidato`
    FOREIGN KEY (`candidato`)
    REFERENCES `mydb`.`Candidato` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Candidatura_Local1`
    FOREIGN KEY (`local`)
    REFERENCES `mydb`.`Local` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Candidatura_Cargo`
    FOREIGN KEY (`cargo`)
    REFERENCES `mydb`.`Cargo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
