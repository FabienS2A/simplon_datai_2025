USE exo_sql_products;
-- Afficher tableau source
SELECT * FROM "nom de table source";
-- Importation des données
INSERT INTO "nom de table destination"("colonne_1","colonne_2")
SELECT DISTINCT State, Country FROM "nom de table source";

-- Vérification
SELECT * FROM "nom de table destination";