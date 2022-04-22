SELECT pd.name, pv.name FROM products pd
INNER JOIN providers pv ON pv.id = pd.id_providers
WHERE id_categories = 6;
