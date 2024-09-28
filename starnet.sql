-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `railway`;

-- Use the created or existing database
USE `railway`;

-- Create user table if it doesn't exist
CREATE TABLE IF NOT EXISTS `user` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`uuid` VARCHAR(255),
	`name` VARCHAR(255),
	`surname` VARCHAR(255),
	`idnp` VARCHAR(255),
	`user_type` INTEGER,
	`phone` VARCHAR(255),
	`email` VARCHAR(255),
	`lang` VARCHAR(255),
	`client_category` INTEGER,
	`conection` VARCHAR(255),
	`region` VARCHAR(255),
	`pricing_plan` INTEGER,
	`equipment_type` INTEGER,
	`comments` TEXT(65535),
	PRIMARY KEY(`id`)
);

-- Create history table if it doesn't exist
CREATE TABLE IF NOT EXISTS `history` (
	`history_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`user_id` INTEGER,
	`chat_history` TEXT(65535),
	PRIMARY KEY(`history_id`)
);

-- Create issues table if it doesn't exist
CREATE TABLE IF NOT EXISTS `issues` (
	`issue_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`user_id` INTEGER,
	`issue` TEXT(65535),
	PRIMARY KEY(`issue_id`)
);

-- Create complaints table if it doesn't exist
CREATE TABLE IF NOT EXISTS `complaints` (
	`complaint_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`user_id` INTEGER,
	`complaint` TEXT(65535),
	PRIMARY KEY(`complaint_id`)
);

-- Add foreign key to history table if it doesn't exist
ALTER TABLE `history`
ADD CONSTRAINT IF NOT EXISTS `fk_history_user` FOREIGN KEY(`user_id`) REFERENCES `user`(`id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

-- Add foreign key to issues table if it doesn't exist
ALTER TABLE `issues`
ADD CONSTRAINT IF NOT EXISTS `fk_issues_user` FOREIGN KEY(`user_id`) REFERENCES `user`(`id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

-- Add foreign key to complaints table if it doesn't exist
ALTER TABLE `complaints`
ADD CONSTRAINT IF NOT EXISTS `fk_complaints_user` FOREIGN KEY(`complaint_id`) REFERENCES `user`(`id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
