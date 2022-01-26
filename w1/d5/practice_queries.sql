-- SELECT
SELECT * FROM pokemon;

-- WHERE
SELECT * FROM pokemon WHERE Generation = "1";

-- AND
SELECT * FROM pokemon 
WHERE Generation = "1"
    AND Type_1 = "Grass";

-- OR
SELECT * FROM pokemon
WHERE Type_1 = "Grass"
    OR Type_2 = "Grass";

-- IN
SELECT * FROM pokemon
WHERE Type_1 IN
    ("Grass", "Water", "Fire");

-- Aggregating & GROUP BY
SELECT Generation, COUNT(*) AS number_of_pokemon FROM pokemon
GROUP BY Generation;

-- HAVING
SELECT Type_1, ROUND(AVG(Sp_Atk)) AS Avg_Sp_Atk FROM pokemon
GROUP BY Type_1
HAVING Avg_Sp_Atk > 75;

-- CASE
SELECT *, 
    CASE
    WHEN Total > 650 THEN "S+"
    WHEN Total > 575 THEN "S"
    WHEN Total > 512 THEN "A"
    WHEN Total > 450 THEN "B"
    WHEN Total > 375 THEN "C"
    WHEN Total > 300 THEN "D"
    WHEN Total > 225 THEN "E"
    ELSE "F"
    END AS "Tier"
FROM pokemon;


