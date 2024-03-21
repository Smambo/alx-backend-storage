## MySQL Advanced
### Learning Objectives <br>
* How to create tables with constraints
* How to optimise queries by adding indexes
* What is and how to implement stored procedures and functions in MySQL
* What is and how to implement views in MySQL
* What is and how to implement triggers in MySQL

### Requirements
* All your files will be executed on Ubuntu 18.04 LTS using `MySQL 5.7` (version 5.7.30)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)

### Tasks:<br>
[0. We are all unique](./0-uniq_users.sql)

Write a SQL script that creates a table `users` following these requirements:

* With these attributes:
  * `id`, integer, never null, auto increment and primary key
  * `email`, string (255 characters), never null and unique
  * `name`, string (255 characters)
* If the table already exists, your script should not fail
* Your script can be executed on any database<br>
<b>Context:</b> <i>Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application</i>

```
root@e4bd5507cf98:/alx-backend-storage# echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password:
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
root@e4bd5507cf98:/alx-backend-storage#
root@e4bd5507cf98:/alx-backend-storage# cat 0-uniq_users.sql | mysql -uroot -p holberton
Enter password:
root@e4bd5507cf98:/alx-backend-storage# echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password:
root@e4bd5507cf98:/alx-backend-storage# echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password:
root@e4bd5507cf98:/alx-backend-storage# echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password:
ERROR 1062 (23000) at line 1: Duplicate entry 'sylvie@dylan.com' for key 'email'
root@e4bd5507cf98:/alx-backend-storage#
root@e4bd5507cf98:/alx-backend-storage# echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password:
id      email   name
1       bob@dylan.com   Bob
2       sylvie@dylan.com        Sylvie
root@e4bd5507cf98:/alx-backend-storage#
```

