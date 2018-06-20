-- MySQL Script generated by MySQL Workbench
-- Qua 20 Jun 2018 13:48:44 -03
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

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
  `idLocal` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `regiao` VARCHAR(45) NOT NULL,
  `estatistica_partidaria` VARCHAR(45) NULL,
  `Populacao` INT NULL,
  PRIMARY KEY (`idLocal`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Coligacao`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Coligacao` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Coligacao` (
  `idColigacao` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `majoritaria` TINYINT(1) NOT NULL,
  `proporcional` TINYINT(1) NOT NULL,
  `presidente` INT NOT NULL,
  PRIMARY KEY (`idColigacao`),
  CONSTRAINT `fk_Presidente`
    FOREIGN KEY (`presidente`)
    REFERENCES `mydb`.`Candidato` (`idCandidato`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE UNIQUE INDEX `nome_UNIQUE` ON `mydb`.`Coligacao` (`nome` ASC);


-- -----------------------------------------------------
-- Table `mydb`.`Partido`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Partido` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Partido` (
  `idPartido` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `sigla` VARCHAR(10) NOT NULL,
  `alinhamento` VARCHAR(45) NULL,
  `coligacao` INT NULL,
  PRIMARY KEY (`idPartido`),
  CONSTRAINT `fk_Partido_Coligação1`
    FOREIGN KEY (`coligacao`)
    REFERENCES `mydb`.`Coligacao` (`idColigacao`)
    ON DELETE SET NULL
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Partido_Coligação1_idx` ON `mydb`.`Partido` (`coligacao` ASC);

CREATE UNIQUE INDEX `Sigla_UNIQUE` ON `mydb`.`Partido` (`sigla` ASC);


-- -----------------------------------------------------
-- Table `mydb`.`Candidato`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Candidato` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Candidato` (
  `idCandidato` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `foto` LONGBLOB NULL,
  `formacao` VARCHAR(45) NULL,
  `alfabetizacao` TINYINT(1) NOT NULL,
  `origem` INT NOT NULL,
  `partido` INT NOT NULL,
  `propostas` VARCHAR(45) NULL,
  PRIMARY KEY (`idCandidato`),
  CONSTRAINT `fk_Candidato_Local1`
    FOREIGN KEY (`origem`)
    REFERENCES `mydb`.`Local` (`idLocal`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Candidato_Partido1`
    FOREIGN KEY (`partido`)
    REFERENCES `mydb`.`Partido` (`idPartido`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Candidato_Local1_idx` ON `mydb`.`Candidato` (`origem` ASC);

CREATE INDEX `fk_Candidato_Partido1_idx` ON `mydb`.`Candidato` (`partido` ASC);


-- -----------------------------------------------------
-- Table `mydb`.`Cargo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Cargo` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Cargo` (
  `idCargo` INT NOT NULL AUTO_INCREMENT,
  `poder` VARCHAR(45) NOT NULL,
  `prereq` VARCHAR(45) NULL,
  `TelefonePublico` VARCHAR(45) NOT NULL,
  `Local` INT NOT NULL,
  PRIMARY KEY (`idCargo`),
  CONSTRAINT `fk_Cargo_Local1`
    FOREIGN KEY (`Local`)
    REFERENCES `mydb`.`Local` (`idLocal`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Cargo_Local1_idx` ON `mydb`.`Cargo` (`Local` ASC);


-- -----------------------------------------------------
-- Table `mydb`.`Candidatura`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Candidatura` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Candidatura` (
  `intencao_de_votos` INT NULL,
  `candidato` INT NOT NULL,
  `local` INT NOT NULL,
  `cargo` INT NOT NULL,
  `idCandidatura` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idCandidatura`),
  CONSTRAINT `fk_Candidatura_Candidato`
    FOREIGN KEY (`candidato`)
    REFERENCES `mydb`.`Candidato` (`idCandidato`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Candidatura_Local1`
    FOREIGN KEY (`local`)
    REFERENCES `mydb`.`Local` (`idLocal`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Candidatura_Cargo`
    FOREIGN KEY (`cargo`)
    REFERENCES `mydb`.`Cargo` (`idCargo`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Candidatura_Candidato_idx` ON `mydb`.`Candidatura` (`candidato` ASC);

CREATE INDEX `fk_Candidatura_Local1_idx` ON `mydb`.`Candidatura` (`local` ASC);

CREATE INDEX `fk_Candidatura_Cargo_idx` ON `mydb`.`Candidatura` (`cargo` ASC);


-- -----------------------------------------------------
-- Table `mydb`.`Prefeito`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Prefeito` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Prefeito` (
  `idPrefeito` INT NOT NULL AUTO_INCREMENT,
  `Cargo` INT NOT NULL,
  `EhVice` TINYINT(1) NOT NULL,
  `Vice` INT NULL,
  PRIMARY KEY (`idPrefeito`),
  CONSTRAINT `fk_Vereador_100`
    FOREIGN KEY (`Cargo`)
    REFERENCES `mydb`.`Cargo` (`idCargo`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Prefeito_Prefeito1`
    FOREIGN KEY (`Vice`)
    REFERENCES `mydb`.`Prefeito` (`idPrefeito`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Vereador_1_idx` ON `mydb`.`Prefeito` (`Cargo` ASC);

CREATE INDEX `fk_Prefeito_Prefeito1_idx` ON `mydb`.`Prefeito` (`Vice` ASC);


-- -----------------------------------------------------
-- Table `mydb`.`Federacao`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Federacao` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Federacao` (
  `idFederacao` INT NOT NULL AUTO_INCREMENT,
  `Local` INT NOT NULL,
  PRIMARY KEY (`idFederacao`),
  CONSTRAINT `fk_Federacao_1`
    FOREIGN KEY (`Local`)
    REFERENCES `mydb`.`Local` (`idLocal`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Federacao_1_idx` ON `mydb`.`Federacao` (`Local` ASC);


-- -----------------------------------------------------
-- Table `mydb`.`Presidente`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Presidente` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Presidente` (
  `idPresidente` INT NOT NULL AUTO_INCREMENT,
  `Cargo` INT NOT NULL,
  `EhVice` TINYINT(1) NOT NULL,
  `Vice` INT NULL,
  PRIMARY KEY (`idPresidente`),
  CONSTRAINT `fk_Vereador_1000`
    FOREIGN KEY (`Cargo`)
    REFERENCES `mydb`.`Cargo` (`idCargo`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Presidente_Presidente1`
    FOREIGN KEY (`Vice`)
    REFERENCES `mydb`.`Presidente` (`idPresidente`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Vereador_1_idx` ON `mydb`.`Presidente` (`Cargo` ASC);

CREATE INDEX `fk_Presidente_Presidente1_idx` ON `mydb`.`Presidente` (`Vice` ASC);


-- -----------------------------------------------------
-- Table `mydb`.`Governador`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Governador` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Governador` (
  `idGovernador` INT NOT NULL AUTO_INCREMENT,
  `Cargo` INT NOT NULL,
  `EhVice` TINYINT(1) NOT NULL,
  `Vice` INT NULL,
  PRIMARY KEY (`idGovernador`),
  CONSTRAINT `fk_Vereador_10000`
    FOREIGN KEY (`Cargo`)
    REFERENCES `mydb`.`Cargo` (`idCargo`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Governador_Governador1`
    FOREIGN KEY (`Vice`)
    REFERENCES `mydb`.`Governador` (`idGovernador`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Vereador_1_idx` ON `mydb`.`Governador` (`Cargo` ASC);

CREATE INDEX `fk_Governador_Governador1_idx` ON `mydb`.`Governador` (`Vice` ASC);


-- -----------------------------------------------------
-- Table `mydb`.`Deputado`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Deputado` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Deputado` (
  `idDeputado` INT NOT NULL AUTO_INCREMENT,
  `Cargo` INT NOT NULL,
  `EhSuplente` TINYINT(1) NOT NULL,
  `Suprido` INT NULL,
  PRIMARY KEY (`idDeputado`),
  CONSTRAINT `fk_Vereador_100000`
    FOREIGN KEY (`Cargo`)
    REFERENCES `mydb`.`Cargo` (`idCargo`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Deputado_Deputado1`
    FOREIGN KEY (`Suprido`)
    REFERENCES `mydb`.`Deputado` (`idDeputado`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Vereador_1_idx` ON `mydb`.`Deputado` (`Cargo` ASC);

CREATE INDEX `fk_Deputado_Deputado1_idx` ON `mydb`.`Deputado` (`Suprido` ASC);


-- -----------------------------------------------------
-- Table `mydb`.`Senador`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Senador` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Senador` (
  `idSenador` INT NOT NULL AUTO_INCREMENT,
  `Cargo` INT NOT NULL,
  `EhSuplente` TINYINT(1) NOT NULL,
  `Suprido` INT NULL,
  PRIMARY KEY (`idSenador`),
  CONSTRAINT `fk_Vereador_100001`
    FOREIGN KEY (`Cargo`)
    REFERENCES `mydb`.`Cargo` (`idCargo`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Senador_Senador1`
    FOREIGN KEY (`Suprido`)
    REFERENCES `mydb`.`Senador` (`idSenador`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Vereador_1_idx` ON `mydb`.`Senador` (`Cargo` ASC);

CREATE INDEX `fk_Senador_Senador1_idx` ON `mydb`.`Senador` (`Suprido` ASC);


-- -----------------------------------------------------
-- Table `mydb`.`Vereador`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Vereador` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Vereador` (
  `idVereador` INT NOT NULL AUTO_INCREMENT,
  `Cargo` INT NOT NULL,
  `EhSuplente` TINYINT(1) NOT NULL,
  `Suprido` INT NULL,
  PRIMARY KEY (`idVereador`),
  CONSTRAINT `fk_Vereador_100002`
    FOREIGN KEY (`Cargo`)
    REFERENCES `mydb`.`Cargo` (`idCargo`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Vereador_Vereador1`
    FOREIGN KEY (`Suprido`)
    REFERENCES `mydb`.`Vereador` (`idVereador`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Vereador_1_idx` ON `mydb`.`Vereador` (`Cargo` ASC);

CREATE INDEX `fk_Vereador_Vereador1_idx` ON `mydb`.`Vereador` (`Suprido` ASC);


-- -----------------------------------------------------
-- Table `mydb`.`Estado`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Estado` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Estado` (
  `idEstado` INT NOT NULL AUTO_INCREMENT,
  `Local` INT NOT NULL,
  `Sigla` VARCHAR(2) NOT NULL,
  PRIMARY KEY (`idEstado`),
  CONSTRAINT `fk_Federacao_10`
    FOREIGN KEY (`Local`)
    REFERENCES `mydb`.`Local` (`idLocal`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Federacao_1_idx` ON `mydb`.`Estado` (`Local` ASC);


-- -----------------------------------------------------
-- Table `mydb`.`Municipio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Municipio` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Municipio` (
  `idMunicipio` INT NOT NULL AUTO_INCREMENT,
  `Local` INT NOT NULL,
  `Estado` INT NOT NULL,
  PRIMARY KEY (`idMunicipio`),
  CONSTRAINT `fk_Federacao_100`
    FOREIGN KEY (`Local`)
    REFERENCES `mydb`.`Local` (`idLocal`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Municipio_1`
    FOREIGN KEY (`Estado`)
    REFERENCES `mydb`.`Estado` (`idEstado`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Federacao_1_idx` ON `mydb`.`Municipio` (`Local` ASC);

CREATE INDEX `fk_Municipio_1_idx` ON `mydb`.`Municipio` (`Estado` ASC);


-- -----------------------------------------------------
-- Table `mydb`.`RegiaoAdm`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`RegiaoAdm` ;

CREATE TABLE IF NOT EXISTS `mydb`.`RegiaoAdm` (
  `idRegiaoAdm` INT NOT NULL AUTO_INCREMENT,
  `Local` INT NOT NULL,
  `Estado` INT NOT NULL,
  PRIMARY KEY (`idRegiaoAdm`),
  CONSTRAINT `fk_Federacao_1000`
    FOREIGN KEY (`Local`)
    REFERENCES `mydb`.`Local` (`idLocal`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Municipio_10`
    FOREIGN KEY (`Estado`)
    REFERENCES `mydb`.`Estado` (`idEstado`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Federacao_1_idx` ON `mydb`.`RegiaoAdm` (`Local` ASC);

CREATE INDEX `fk_Municipio_1_idx` ON `mydb`.`RegiaoAdm` (`Estado` ASC);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


CREATE PROCEDURE `mydb`.`candlocal` (locnome nvarchar(45))
  select Candidato.idCandidato, Candidato.nome from Candidato inner join Local on Candidato.origem=Local.idLocal and Local.nome=locnome;

CREATE PROCEDURE `mydb`.`candpart` (locnome nvarchar(45))
  select Candidato.idCandidato, Candidato.nome from Candidato inner join Partido on Candidato.partido=Partido.idPartido and Partido.nome=locnome;

#Create Procedure `mydb`.`procswitch` (locnome nvarchar(45), specase smallint) 
#BEGIN
#IF (specase > 1) THEN CALL candlocal(locnome)
#ELSE CALL candpart(locnome)
#END IF;
#END

DELIMITER //


Create Procedure `mydb`.`procswitch` (locnome nvarchar(45), specase smallint) 
BEGIN
IF (specase > 1) begin CALL candlocal(locnome); end
ELSE begin CALL candpart(locnome); end
END //

DELIMITER ;
