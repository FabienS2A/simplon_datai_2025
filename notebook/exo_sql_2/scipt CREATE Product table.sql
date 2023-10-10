-- on jette on créé
DROP DATABASE IF EXISTS exo_sql_products;
CREATE DATABASE exo_sql_products;

-- On utilise la bonne DB
USE exo_sql_products;

-- Création de tables

-- 1. tables des dates

CREATE TABLE Dates
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    dates DATE UNIQUE,
    days BIT,
    Months VARCHAR(9),
    Years SMALLINT UNSIGNED,
    PRIMARY KEY (ID)
    );

-- 2. tables des localite
    
CREATE TABLE Localite
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Country VARCHAR(40),
    State VARCHAR(40),
    PRIMARY KEY (ID)
    );
 
 -- 3. tables des Ages
 
CREATE TABLE Ages
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Customer_age TINYINT UNSIGNED,
    Age_group VARCHAR(24),
    PRIMARY KEY (ID)
    );
    
-- 4. tables des Categories de produits
    
CREATE TABLE Prod_Cat
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Product_Category VARCHAR(40),
    Sub_Category VARCHAR(40),
    PRIMARY KEY (ID)
    );

-- 5. tables des Categories de produits

CREATE TABLE Product
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Product VARCHAR(80),
    Unit_cost DEC(9,2),
    Unit_price DEC(9,2),
    Prod_Cat_ID SMALLINT UNSIGNED,
    PRIMARY KEY (ID),
    FOREIGN KEY (Prod_Cat_ID) REFERENCES Prod_Cat(ID)
    );
    
-- 5. tables des Categories des Orders (principale)
CREATE TABLE Orders
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Customer_Gender CHAR(1),
    Order_quantity SMALLINT UNSIGNED,
    Profit DEC(9,2),
    Cost DEC(9,2),
    Revenue DEC(9,2),
    Dates_ID SMALLINT UNSIGNED,
    Loc_ID SMALLINT UNSIGNED,
    Age_ID SMALLINT UNSIGNED,
    Product_ID SMALLINT UNSIGNED,
    PRIMARY KEY (ID),
    FOREIGN KEY (Dates_ID) REFERENCES Dates(ID),
    FOREIGN KEY (Loc_ID) REFERENCES Localite(ID),
    FOREIGN KEY (Age_ID) REFERENCES Ages(ID),
    FOREIGN KEY (Product_ID) REFERENCES Product(ID)
    );
    
    
    
    
    