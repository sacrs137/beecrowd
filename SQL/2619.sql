SELECT pd.name,pv.name, pd.price FROM categories c 
INNER JOIN products pd ON pd.id_categories = c.id 
INNER JOIN providers pv ON pv.id = pd.id_providers 
WHERE c.name = 'Super Luxury' AND pd.price > 1000;
