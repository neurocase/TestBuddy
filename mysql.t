[mysql][cmd] this default database contains metadata:ANSWER:;information_schema
[mysql][cmd] create own database called mydb:ANSWER:;CREATE DATABASE mydb;
[mysql][cmd] print databases:ANSWER:;SHOW DATABASES;
[mysql][cmd] create a table called customers inside database mydb with fields; 'id' 11 integers, 'first_name' 20chars, last_name 20chars:ANSWER:;CREATE TABLE mydb.customers ('id' int(11) NOT NULL, 'first_name' varchar(20) NOT NULL, 'last_name' varchar(20) NOT NULL);
[mysql][cmd] go to mydb database:ANSWER:;USE mydb;
[mysql][cmd] print availables tables:ANSWER:;SHOW TABLES;
[mysql][cmd] put data into table 'customers'; id:1 first_name:jeff last_name:jefferson use caps for mysql cmds, :ANSWER:;INSERT INTO customers (id,first_name,last_name) VALUES (1,"jeff","jefferson");
[mysql][cmd] query all tables from customers, use caps for mysql statements:ANSWER:;SELECT * FROM customers; 
[mysql][cmd] show all entries from table customers, with id = 1 :ANSWER:;SELECT * FROM customers WHERE id = 1;
[mysql][cmd] add id = 2 first_name = anthony last_name = jefferson into table 'customers', use caps for mysql statements:ANSWER:;INSERT INTO customers (id,first_name,last_name) VALUES (2,"anthony","jefferson"); 
[mysql][cmd] select all members from table customers with last_name jefferson:ANSWER:;SELECT * FROM customers WHERE last_name = "jefferson";
[mysql][cmd] print in human-readable, users from database mysql :ANSWER:;DESCRIBE mysql.users;
[mysql][cmd] print fields user, host from database.table :ANSWER:; SELECT user, host FROM database.table;
[mysql][cmd] create user jeff for local host with password test  :ANSWER:;CREATE USER 'jeff'@'localhost' IDENTIFIED BY 'test';
[mysql][cmd] display  from 'database.table' fields user,host where the user is jeff :ANSWER:; SELECT user,host FROM database.table WHERE user = "jeff";
[mysql][cmd] give full access to jeff on localhost using mydb  :ANSWER:; GRANT ALL PRIVILEGES ON mydb.* TO 'jeff'@'localhost';
[mysql] mysql admin program:ANSWER:;mysqladmin
[mysql] login to mysql and import mysql database "store.sql" into pre-created database store:ANSWER:;mysql -uroot -p store < store.sql
[mysql] update jeff jackson's last name to francis :ANSWER:;UPDATE customers SET last_name="francis" WHERE first_name="jeff' AND last_name="jackson";
[mysql] remove from table customers a member with id 11 :ANSWER:; DELETE FROM customers WHERE id=11;
[mysql] show how many different (type)s of everything there is in table products  :ANSWER:; SELECT * FROM products GROUP BY type;
[mysql]  select all entrues from table 'products', group by type and order those groups by price decending:ANSWER:;SELECT * FROM products GROUP BY type ORDER BY price DESC;
[mysql]  join tables orders and customers, align orders.customers_id with customers.id where the first_name is jeff:ANSWER:; SELECT * FROM orders LEFT JOIN customers ON orders.customer_id = customers.id WHERE first_name ="jeff";
[mysql] as root, dump data base "store" into backup_store.sql :ANSWER:;mysqldump -uroot -p store > backup_store.sql
[mysql] delete database mydb:ANSWER:;DROP DATABASE mydb;
[mysql] What command updates the users database and set the firstName = Jeff and lastName = Jones where the users current first_name is John and last_name is Johnson?:ANSWER:;UPDATE USERS set first_name ='jeff', last_name='jones' where first_name='John' and last_name='Johnson';
[mysql] What command will update the inactive field to equal 1 where inactive is not equal to 1?:ANSWER:;UPDATE users SET inactive = 1 WHERE inactive <> 1;
[mysql] delete every row from the users table where inactive = 1:ANSWER:;DELETE FROM users WHERE inactive=1;
