-- on jette on créé
DROP DATABASE IF EXISTS exo_sql_sales;
CREATE DATABASE exo_sql_sales;

-- On utilise la bonne DB
USE exo_sql_sales;

-- Création de tables

-- 1. tables des dates

CREATE TABLE Pays
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Pays VARCHAR(45),
    PRIMARY KEY (ID)
    );

-- 2. tables des localite
    
CREATE TABLE Localites
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Ville VARCHAR(40),
    Pays_ID SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (Pays_ID) REFERENCES Pays(ID)
    );
 
 -- 3. tables des Magasins
 
CREATE TABLE Magasins
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Adresse_Magasin VARCHAR(120),
    ID_Localite SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (ID_Localite) REFERENCES Localites(ID)
    );
    
-- 4. tables des Categories des Clients
    
CREATE TABLE Clients
(
	ID_Client SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Nom_Client VARCHAR(45),
    Prenom_Client VARCHAR(45),
    Adresse_Client VARCHAR(45),
    Email_Client VARCHAR(45),
    ID_Localite SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (ID_Client),
    FOREIGN KEY (ID_Localite) REFERENCES Localites(ID)
    );

-- 5. tables des Catégorie_produit

CREATE TABLE Categorie_produits
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Categorie_produit VARCHAR(80),
    PRIMARY KEY (ID)
    );
    
    -- 6. tables des Produits

CREATE TABLE Produits
(
	ID_Produit SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Nom_produit VARCHAR(100),
    ID_Cat_Produit SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (ID_Produit),
    FOREIGN KEY (ID_Cat_Produit) REFERENCES Categorie_produits(ID)
    );
    
  
-- 7. tables des Commandes (principale)

CREATE TABLE Commandes
(
    ID_Commande SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    Date_Commande DATE,
    Montant_Commande DEC(9,1),
    ID_Magasin SMALLINT UNSIGNED NOT NULL,
    ID_Client SMALLINT UNSIGNED NOT NULL,
    ID_Produit SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (ID_Commande),
    FOREIGN KEY (ID_Magasin) REFERENCES Magasins(ID),
    FOREIGN KEY (ID_Client) REFERENCES Clients(ID_Client)
    );
    
    -- 8. tables des Assoc_Prod_Commandes
    
CREATE TABLE Assoc_Prod_Commandes
(
    ID_Produit SMALLINT UNSIGNED NOT NULL,
    ID_Commande SMALLINT UNSIGNED NOT NULL,
    FOREIGN KEY (ID_Produit) REFERENCES Produits(ID_Produit),
    FOREIGN KEY (ID_Commande) REFERENCES Commandes(ID_Commande)
    ); 
    
    
    