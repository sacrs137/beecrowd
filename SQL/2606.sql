SELECT  pd.id, pd.name FROM products pd
INNER JOIN categories ct ON ct.id = pd.id_categories
WHERE ct.name LIKE 'super%';
