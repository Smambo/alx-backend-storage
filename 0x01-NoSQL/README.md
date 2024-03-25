## NoSQL
### Learning Objectives <br>
* What [NoSQL](https://riak.com/resources/nosql-databases/) means
* What is difference between SQL and NoSQL
* What is ACID
* What is a document storage
* What are NoSQL types
* What are benefits of a NoSQL database
* How to query information from a NoSQL database
* How to insert/update/delete information from a NoSQL database
* How to use MongoDB

### Tasks: <br>
[0. List all databases](./0-list_databases)<br>
Write a script that lists all databases in MongoDB.<br>
```
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 0-list_databases | mongo
MongoDB shell version v4.2.19
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("7569e7e9-a907-471a-bfaa-0429258513cf") }
MongoDB server version: 4.2.19
admin   0.000GB
config  0.000GB
local   0.000GB
bye
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
```

[1. Create a database](./1-use_or_create_database)<br>
Write a script that creates or uses the database `my_db`:<br>
```
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 0-list_databases | mongo
MongoDB shell version v4.2.19
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("9c4faef5-db9a-49dc-82fa-0e42919824f6") }
MongoDB server version: 4.2.19
admin   0.000GB
config  0.000GB
local   0.000GB
bye
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 1-use_or_create_database | mongo
MongoDB shell version v4.2.19
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("30dcf9fa-3df0-4be5-a497-a0d9e378392d") }
MongoDB server version: 4.2.19
switched to db my_db
bye
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
```

[2. Insert document](./2-insert)<br>
Write a script that inserts a document in the collection `school`:<br>
* The document must have one attribute `name` with value “Holberton school”
* The database name will be passed as option of `mongo` command <br>
```
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 2-insert | mongo my_db
MongoDB shell version v4.2.19
connecting to: mongodb://127.0.0.1:27017/my_db?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("243c11f8-4c3d-4142-becc-4d0d15da5a35") }
MongoDB server version: 4.2.19
WriteResult({ "nInserted" : 1 })
bye
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
```

[3. All documents](./3-all)<br>
Write a script that lists all documents in the collection `school`:

* The database name will be passed as option of `mongo` command <br>
```
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 3-all | mongo my_db
MongoDB shell version v4.2.19
connecting to: mongodb://127.0.0.1:27017/my_db?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("785c1a3b-c04a-4718-8007-90084665f242") }
MongoDB server version: 4.2.19
{ "_id" : ObjectId("66015bc61a53cbc271d81fce"), "name" : "Holberton school" }
bye
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
```

[4. All matches](./4-match)<br>
Write a script that lists all documents with `name="Holberton school"` in the collection `school`:

* The database name will be passed as option of `mongo` command <br>
```
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 4-match | mongo my_db
MongoDB shell version v4.2.19
connecting to: mongodb://127.0.0.1:27017/my_db?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("c225717a-8c5e-4cfa-a608-cbc1a26495a5") }
MongoDB server version: 4.2.19
{ "_id" : ObjectId("66015bc61a53cbc271d81fce"), "name" : "Holberton school" }
bye
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
```

[5. Count](./5-count)<br>
Write a script that displays the number of documents in the collection `school`:

* The database name will be passed as option of `mongo` command

[6. Update](./6-update)<br>
Write a script that adds a new attribute to a document in the collection `school`:

* The script should update only document with `name="Holberton school"` (all of them)
* The update should add the attribute `address` with the value “972 Mission street”
* The database name will be passed as option of `mongo` command

[7. Delete by match](./7-delete)<br>
Write a script that deletes all documents with `name="Holberton school"` in the collection `school`:

* The database name will be passed as option of `mongo` command

[8. List all documents in Python](./8-all.py)<br>
Write a Python function that lists all documents in a collection:

* Prototype: `def list_all(mongo_collection):`
* Return an empty list if no document in the collection
* `mongo_collection` will be the `pymongo` collection object

[9. Insert a document in Python](./9-insert_school.py)<br>
Write a Python function that inserts a new document in a collection based on kwargs:

* Prototype: `def insert_school(mongo_collection, **kwargs):`
* `mongo_collection` will be the `pymongo` collection object
* Returns the new `_id`

[10. Change school topics](./10-update_topics.py)<br>
Write a Python function that changes all topics of a school document based on the name:

* Prototype: `def update_topics(mongo_collection, name, topics):`
* `mongo_collection` will be the `pymongo` collection object
* `name` (string) will be the school name to update
* `topics` (list of strings) will be the list of topics approached in the school

[11. Where can I learn Python?](./11-schools_by_topic.py)<br>
Write a Python function that returns the list of school having a specific topic:

* Prototype: `def schools_by_topic(mongo_collection, topic):`
* `mongo_collection` will be the `pymongo` collection object
* `topic` (string) will be topic searched

[12. Log stats](./12-log_stats.py)<br>
Write a Python script that provides some stats about Nginx logs stored in MongoDB:

* Database: `logs`
* Collection: `nginx`
* Display (same as the example):
  * first line: `x logs` where `x` is the number of documents in this collection
  * second line: `Methods:`
  * 5 lines with the number of documents with the `method` = `["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order (see example below - warning: it’s a tabulation before each line)
  * one line with the number of documents with:
    * `method=GET`
    * `path=/status`
You can use this dump as data sample: [dump.zip]()

