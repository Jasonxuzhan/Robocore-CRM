# Mysql Database operation 
- [Mysql Homepage](https://www.mysql.com/cn/)
- [Mysql 8.0 manual](https://dev.mysql.com/doc/refman/8.0/en/)
- [Mysql python connector guide](https://dev.mysql.com/doc/connector-python/en/)

## Database 
- CREATE DATABASE myDB - 建立数据库
- DROP DATABASE myDB - 删除数据库
- ALTER DATABASE myDB READ ONLY = 1 - 只读
- ALTER DATABASE mYDB RAD ONLY = 0 - 取消只读  

## Table 
- CREATE TABLE employees （
    employee_id INT,  
    first_name VARCHAR(255),  
    last_name VARCHAR(255),  
    hourly_pay DECIMAL(5, 2), - 显示5个数字，保留小数点后面两位   
    hire_date DATE - 或者datetime  
）

### Select 
- SELECT * FROM employees - 选择所有列

- SELECT first_name, last_name FROM employees - 选择特定的列

- SELECT * FROM employees WHERE employee_id IS NULL - 根据条件选择特定的列 

### Rename table  
- RENAME TABLE employees TO workers - 修改table的名字  

### Drop table 
- DROP TABLE employees - 删除table

### Alter functions 
- ALTER TABLE employees ADD phone_num VARCHAR(15) - 添加列  

- ALTER TABLE employees RENAME COLUMN phone_num TO email - 修改列名称

- ALTER TABLE employess MODIFY COLUMN email VARCHAR(100) - 修改列的数据类型  

- ALTER TABLE employees MODIFY email VARCHAR(100) AFTER last_name - 修改列在table中的位置 

- ALTER TABLE employees MODIFY email VARCHAR(100) FIRST - 放在table中的第一个列  

- ALTER TABLE employees DROP COLUMN email - 删除列  

## Rows 
- INSERT INTO employees VALUES (1, "xu", "zhan", 25.50, "2024-4-5") - 需要与列的数量对应  

- INSERT INTO employees VALUES (1, "xu", "zhan", 25.50, "2024-4-5")，(1, "xu", "zhan", 25.50, "2024-4-5") - 插入多行  

- INSERT INTO employees (emplyees_id, first_name, last_name) VALUES (6. "jason", "xu) - 选择特定的列输入数据  

### Update and Delete 
- UPDATE employees SET hourly_pay = 10.25 WHERE employee_id = 6 - ID是6的员工小时工资改为10.25 

- UPDATE employees SET hourly_pay = 10.25, hire_date = "20204-04-05" WHERE employee_id = 6  

- UPDATE employees SET hourly_pay = 10.25, hire_date = "20204-04-05" 

- DELETE FROM employees WHERE employee_id = 6 - 删除一条数据，没有指定条件则删除所有数据

## Autocommit and Rollback 
- SET AUTOCOMMIT = OFF - 取消自动执行 

- COMMIT - 执行 

- ROLLBACK - 恢复

## Currentdate & Currenttime 
- CREATE TABLE test(
    date DATE,
    time TIME,
    datetime DATETIME 
)

- INSERT INTO test VALUES(CURRENT_DATE(), CURRENT_TIME(), NOW()) CURRENT_DATE+1 = tomorrow 

## UNIQUE 
- CREATE TABLE products(
    product_id INT,
    product_name VARCHAR(25) UNIQUE - value不能重复
    PRICE DEMICAL(4, 2)
)

- ALTER TABLE products ADD CONSTRAINT UNIQUE(product_name)

## Not NULL 
- CREATE TABLE products(
    product_id INT,
    product_name VARCHAR(25) UNIQUE - value不能重复
    PRICE DEMICAL(4, 2) NOT NULL - value不能为空
)

- ALTER TABLE products MODIFY price DEMICAL(4, 2) NOT NULL 

## CHECK
- CREATE TABLE employees （
    employee_id INT,  
    first_name VARCHAR(255),  
    last_name VARCHAR(255),  
    hourly_pay DECIMAL(5, 2), 
    hire_date DATE   
    CONSTRAINT chk_hourly_pay CHECK(hourly_pay >=10.00) - 检查Value必须大于10
）

- ALTER TABLE employees ADD CONSTRAINT chk_hourly_pay CHECK(hourly_pay >=10.00)

- ALTER TABLE employees DROP CHECK chk_hourly_pay - 取消检查

## DEFAULT 
- CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(25),
    price DECIMAL(4, 2) DEFAULT 0 
)

- ALTER TABLE products ALTER price SET DEFAULT 0 

- INSERT INTO products (product_id, product_name) VALUES(104, "berry") - 默认的数据可以不输入 

## PRIMARY KEY 
- CREATE TABLE treansctions(
    transction_id INT PRIMARY KEY,
    amount DECIMAL(5, 2)
)

- ALTER TABLE treansctions ADD CONSTRAINT PRIMARY KEY(transction_id) - PRIMARY KEY 是唯一的,且只有一个,且不能是NULL

## Auto_increment 
- CREATE TABLE treansctions(
    transction_id INT PRIMARY KEY AUTO_INCREMENT  
    amount DECIMAL(5, 2)
)

- ALTER TABLE transctions AUTO_INCREMENT = 100 - 调整自动生成的数 

## Foreign key 
- CREATE TABLE customers(
    customer_id INT PRIMARY KEY AUTO_INCREMENT, 
    first_name VARCHAR(25),
    last_name VARCHAR(25)
)

- CREATE TABLE treansctions(
    transction_id INT PRIMARY KEY AUTO_INCREMENT  
    amount DECIMAL(5, 2)
    customer_id INT,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id) - 与其他表建立key的关系
)

- ALTER TABLE transactions DROP FOREIGN KEY transaction_ibfk_1 - 取消foreign key

- ALTER TABLE transactions ADD CONSTRANIT fk_customer_id FORIEGN KEY (customer_id) REFERENCE customer(customer_id) - 建立foriegn key 关系 

- DELETE FROM customers WHERE customer_id = 3 - 不能删除，因为对应了其他表的foreign key

## Joins
### Inner join 
- SELECT * FROM transaction INNER JOIN customers ON transactions.customer_id = customers.customer_id
 
### Left join 
- SELECT * FROM transaction LEFT JOIN customers ON transactions.customer_id = customers.customer_id - 显示左边表所有的数据，右边有对应的则显示，没有对应的则不显示

### Right join 
- SELECT * FROM transaction RIGHT JOIN customers ON transactions.customer_id = customers.customer_id - 显示右边所有的数据，左边有对应的则显示，没有对应的则不显示  

## Some functions
- SELECT COUNT(amount) AS count FROM transactions - 有多少rows在amount列, AS count 是命名

- SELECT MAX(amount) AS max FROM transactions - 在amount列的最大值 

- SELECT MIN(amount) AS min FROM transactions - 在amount列的最小值

- SELECT AVG(amount) AS avg FROM transactions - 在amount列的平均值

- SELECT SUM(amount) AS sum FROM transactions - 在amount列的数值相加

- SELECT * CONTACT(first_name, last_name) AS full_name FROM employees - 把employess中的两列合并和一列并显示出来

## AND OR NOT 
- SELECT * FROM employees WHERE hire_date < "2023-1-5" AND job = "cook"

- SELECT * FROM employees WHERE hire_date < "2023-1-5" OR job = "cook" 

- SELECT * FROM employees WHERE hire_date < "2023-1-5" NOT job = "cook"

- SELECT * FROM employees WHERE hire_date BETWEEN "2023-1-5" AND "2023-1-10" 

- SELECT * FROM employees WHERE jon IN("cook", "cashier") 

## Wild card characters % _ , used to substitute one od more characteres in a string 
- SELECT * FROM employees WHERE first_name LIKE "s% - firstname begin s , %s end with s ，%代表所有字符

- SELECT * FROM employees WHERE first_name LIKE "_ook" - _ 只代表一个字符 

## ORDER BY  升序（从小到大）或者降序（从大到小）
- SELECT * FROM ORDER BY last_name DESC - 降序排列， - ASC 升序排列

## LIMIT clause is used to limit the numer of records, useful if you are working with a lot of data, can be used to display a larger data on pages 
- SELECT * FROM customers LIMIT 1  - 显示一个row，2显示两个row

## UNION combine the result of two ot more SELECT statments 
- SELECT * FROM incomes 
  UNION
  SELECT * FROM expenses - 向下添加table，必须是同样数量的column 

- SELECT first_name, last_name FROM employees
  UNION ALL
  SELECT first_name, last_name FROM customers - 在两个表中选择同样数量的column即可合并 

- UNION 会去重， UNION ALL 不会去重 

## Sef join, join another copy of a tbale to itself, used to compare rows of the same table, helps to display a heriarchy of data  (转介)
- SELECT * FROM customers AS a INNER JOIN customers as b ON a.referral_id = b.customer_id - 根据referralid 对应的customerid 来生成一个新的表格 （必须是同一个表格， b是copy的表格）

- SELECT a.first_name, a.last_name, 
         CONTACT(b.first_name, " ", b.last_name) AS "reports to"
  FROM employees AS a 
  LEFT JOIN employees AS b 
  ON a.supervisor_id = b.employee_id 

## VIEW, a virtual table based on the result of an SQL statement, the fields in a view are fields from one or more table in the database, they are not real table, but can be interacted with as if they were 
- CREATE VIEW employ_attendance AS 
  SELECT first_name, last_name 
  FROM employees - 创建一个虚拟table，引用实际table的column数据

  SELECT * FROM employees_attendance - 访问虚拟table
  
  DROP VIEW employees_attendance - 删除虚拟table 
  实际table的修改会影响虚拟table

## INDEX， Indexes are used to find values within a specific column quickly, it wil take less time. if the column is so long, whom search will take long time to get the result. but UPDATE wil take long time. 
- CREATE INDEX last_name_idx ON customers(last_name), - 把last_name作为索引
  SHOW INDEXES FROM customers 
  SELECT * FROM customer WHERE last_name = "Puff", - 以索引来搜索

- CREATE INDEX last_name_first_name_idx ON customers(last_name, first_name) - 建立多索引
  SELECT * FROM customers WHERE last_name = "puff" AND fist_name = "poppy"  - 多条件索引

- ALTER TABLE customers DROP INDEX last_name_idx, - 删除索引

## Subquery, a query within another query 
- SELECT first_name, last_name, hourly_pay, 
         (SELECT AVG(hourly_pay) FROM employees) 
  FROM employees 

- SELECT first_name, last_name, hourly_pay FROM employees 
  WHERE hourly_pay > (SELECT AVG(hourly_pay) FROM employees)

- SELECT first_name, last_name FROM transcations WHERE customer_id IN  
 （SELECT DISTINCT customer_id from customers WHERE customer_id IS NOT NULL , - DISTINCT就是去重

## GROUP BY, aggregate(sum) all rows by a specific column often used with aggregate functions, such as SUM, MAX, MIN, AVG, COUNT
- SELECT SUM(amount), order_date FROM transcation GROUP BY order_date - 多行同样的orderdate，整合到一行并求和，或者求最大值，最小值，平均值 或者求次数（如下）

- SELECT COUNT（amount，customer_id  
  FROM transcations  
  GROUP BY customer_id   
  HAVING COUNT(amount) > 1 AND customer_id IS NOT NULL, - HAVING 与 WHERE 一个意思，在GROUP BY 里有HAVING替代WHERE

## ROLLUP， extension of the GROUP BY clause, produces another row and shows the GRAND TOTAL(super-aggregate value)
- SELECT SUM(amount), order_date FROM transcations GROUP BY order_date WITH ROLLUP - 添加一个grand total的row

## ON DELETE SET NULL = When a FK is deleted, replace FK with NULL ; ON DELETE CASCADE = When FK is deleted, delete row  FK means Foreign key
- SET foreign_key_checks = 0   取消fk

- CREATE TABLE transcations (
    transcation_id = INT PRIMARY KEY,
    amount DECIMAL(5, 2),
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    ON DELETE SET NULL   (When a FK is deleted, replace FK with NULL)
)

  ALTER TABLE transcations FROP FOREIGN KEY fk_customer_id - 删除foreign key

  ALTER TABLE transcations 
  ADD CONSTRAINT fk_customer_id
  FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
  ON DELETE SET NULL - 修改table的forign key的条件

  ALTER TABLE transcations 
  ADD CONSTRAINT fk_tanscations_id - foreign key的名字
  FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
  ON DELETE SET CASCADE - 修改table的forign key的条件

## Stored procedure = is prepared SQL code that you can save great if there's a query thay you write often 
- Functions:

 DELIMITER $$ 
 CREATE PROCEDURE get_customers()
 BEGIN 
      SELECT * FROM customers;
 END $$
 DELIMITER ;

- Use function
  CALL get_customers();

- DROP PROCEDURE get_customers;

- 带参数的函数
  DELIMITER $$
  CREATE PROCEDURE find_customer(IN id INT)
  BEGIN
      SELECT * FROM customers WHERE customer_id = id;
  END$$
  DELIMITER ; 

- 带多参数的函数
  DELIMITER $$
  CREATE PROCEDURE find_customer(IN id INT, IN f_name VARCHAR(50))
  BEGIN
      SELECT * FROM customers WHERE customer_id = id AND first_name = f_name;
  END$$
  DELIMITER ; 

## Trigger 联动
- CREATE TRIGGER before_hourly_pay_update   
  BEFORE UPDATE ON employees   
  FOR EACH ROW  
  SET NEW.salary = (NEW.hourly_pay * 2080)  

- SHOW TRIGGERS