SELECT cus.name, r.rentals_date FROM rentals r
INNER JOIN customers cus ON cus.id = r.id_customers
WHERE EXTRACT(month FROM r.rentals_date) = 9 
AND EXTRACT(year FROM r.rentals_date) = 2016;
