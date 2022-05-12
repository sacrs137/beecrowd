SELECT  lr.name, round(lr.omega * 1.618, 3) AS "Fator N" FROM life_registry lr
INNER JOIN dimensions d ON d.id = lr.dimensions_id
WHERE d.name IN ('C875', 'C774') AND lr.name LIKE 'Richard%'
ORDER BY "Fator N" ASC;
