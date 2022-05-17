-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Student`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Student` (
  `StudentID` INT NOT NULL,
  `StudentName` VARCHAR(45) NULL,
  PRIMARY KEY (`StudentID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Professor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Professor` (
  `ProfID` INT NOT NULL,
  `ProfName` VARCHAR(45) NULL,
  PRIMARY KEY (`ProfID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Course`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Course` (
  `courseId` INT NOT NULL,
  `courseName` VARCHAR(45) NULL,
  `courseLevel` INT NULL,
  `courseCredit` INT NULL,
  `Professor_ProfID` INT NOT NULL,
  PRIMARY KEY (`courseId`, `Professor_ProfID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Course_has_Student`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Course_has_Student` (
  `Course_courseId` INT NOT NULL,
  `Student_StudentID` INT NOT NULL,
  PRIMARY KEY (`Course_courseId`, `Student_StudentID`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
