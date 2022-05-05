SELECT CONCAT(SUBSTRING(nt.cpf,1,3),'.',
                         SUBSTRING(nt.cpf,4,3),'.',
                         SUBSTRING(nt.cpf,7,3),'-',
SUBSTRING(nt.cpf,10,2)) FROM natural_person nt
INNER JOIN customers c ON c.id = nt.id_customers;
