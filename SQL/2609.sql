SELECT ct.name, SUM(pd.amount) FROM categories ct
INNER JOIN products pd ON pd.id_categories = ct.id
GROUP BY ct.name;
