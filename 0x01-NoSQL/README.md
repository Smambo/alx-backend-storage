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

* The database name will be passed as option of `mongo` command <br>
```
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 5-count | mongo my_db
MongoDB shell version v4.2.19
connecting to: mongodb://127.0.0.1:27017/my_db?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("f866b90f-39e3-48e9-90c6-e661fab667b6") }
MongoDB server version: 4.2.19
1
bye
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
```

[6. Update](./6-update)<br>
Write a script that adds a new attribute to a document in the collection `school`:

* The script should update only document with `name="Holberton school"` (all of them)
* The update should add the attribute `address` with the value “972 Mission street”
* The database name will be passed as option of `mongo` command <br>
```
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 6-update | mongo my_db
MongoDB shell version v4.2.19
connecting to: mongodb://127.0.0.1:27017/my_db?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("e0127d4c-34a3-4535-86c8-b1ad91a3f63d") }
MongoDB server version: 4.2.19
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
bye
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 4-match | mongo my_db
MongoDB shell version v4.2.19
connecting to: mongodb://127.0.0.1:27017/my_db?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("04315185-49d4-48d6-932b-14460a3f6d20") }
MongoDB server version: 4.2.19
{ "_id" : ObjectId("66015bc61a53cbc271d81fce"), "name" : "Holberton school", "address" : "972 Mission street" }
bye
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
```

[7. Delete by match](./7-delete)<br>
Write a script that deletes all documents with `name="Holberton school"` in the collection `school`:

* The database name will be passed as option of `mongo` command <br>
```
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 7-delete | mongo my_db
MongoDB shell version v4.2.19
connecting to: mongodb://127.0.0.1:27017/my_db?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("4c257410-4429-4ea3-9699-daa5e92d8c49") }
MongoDB server version: 4.2.19
{ "acknowledged" : true, "deletedCount" : 1 }
bye
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 4-match | mongo my_db
MongoDB shell version v4.2.19
connecting to: mongodb://127.0.0.1:27017/my_db?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("b76bc0c3-2b98-4316-854f-e62c064fbb7a") }
MongoDB server version: 4.2.19
bye
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
```

[8. List all documents in Python](./8-all.py)<br>
Write a Python function that lists all documents in a collection:

* Prototype: `def list_all(mongo_collection):`
* Return an empty list if no document in the collection
* `mongo_collection` will be the `pymongo` collection object <br>
```
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 8-main.py
#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# ./8-main.py
[66018369500c665e4118469c] Holberton school
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
```

[9. Insert a document in Python](./9-insert_school.py)<br>
Write a Python function that inserts a new document in a collection based on kwargs:

* Prototype: `def insert_school(mongo_collection, **kwargs):`
* `mongo_collection` will be the `pymongo` collection object
* Returns the new `_id` <br>
```
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 9-main.py
#!/usr/bin/env python3
""" 9-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('address', "")))
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# ./9-main.py
New school created: 660186909788f6f8d2515c5d
[66018369500c665e4118469c] Holberton school
[660186909788f6f8d2515c5d] UCSF 505 Parnassus Ave
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
```

[10. Change school topics](./10-update_topics.py)<br>
Write a Python function that changes all topics of a school document based on the name:

* Prototype: `def update_topics(mongo_collection, name, topics):`
* `mongo_collection` will be the `pymongo` collection object
* `name` (string) will be the school name to update
* `topics` (list of strings) will be the list of topics approached in the school <br>
```
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 10-main.py
#!/usr/bin/env python3
""" 10-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all
update_topics = __import__('10-update_topics').update_topics

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

    update_topics(school_collection, "Holberton school", ["iOS"])

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# ./10-main.py
[66018369500c665e4118469c] Holberton school ['Sys admin', 'AI', 'Algorithm']
[6601c79185403e21f717c328] UCSF
[66018369500c665e4118469c] Holberton school ['iOS']
[6601c79185403e21f717c328] UCSF
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
```

[11. Where can I learn Python?](./11-schools_by_topic.py)<br>
Write a Python function that returns the list of school having a specific topic:

* Prototype: `def schools_by_topic(mongo_collection, topic):`
* `mongo_collection` will be the `pymongo` collection object
* `topic` (string) will be topic searched <br>
```
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# cat 11-main.py
#!/usr/bin/env python3
""" 11-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school
schools_by_topic = __import__('11-schools_by_topic').schools_by_topic

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    j_schools = [
        { 'name': "Holberton school", 'topics': ["Algo", "C", "Python", "React"]},
        { 'name': "UCSF", 'topics': ["Algo", "MongoDB"]},
        { 'name': "UCLA", 'topics': ["C", "Python"]},
        { 'name': "UCSD", 'topics': ["Cassandra"]},
        { 'name': "Stanford", 'topics': ["C", "React", "Javascript"]}
    ]
    for j_school in j_schools:
        insert_school(school_collection, **j_school)

    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# ./11-main.py
[6601c9b0bc860ad3075c5315] Holberton school ['Algo', 'C', 'Python', 'React']
[6601c9b1bc860ad3075c5317] UCLA ['C', 'Python']
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
```

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
The output of your script <b>must be exactly the same as the example</b> <br>
```
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# curl -o dump.zip -s "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-webstack/411/dump.zip"
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# unzip dump.zip
Archive:  dump.zip
   creating: dump/
   creating: dump/logs/
  inflating: dump/logs/nginx.metadata.json
  inflating: dump/logs/nginx.bson
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# mongorestore dump
2024-03-26T04:39:53.176-0700    preparing collections to restore from
2024-03-26T04:39:53.178-0700    reading metadata for logs.nginx from dump/logs/nginx.metadata.json
2024-03-26T04:39:53.226-0700    restoring logs.nginx from dump/logs/nginx.bson
2024-03-26T04:39:56.199-0700    [######..................]  logs.nginx  3.55MB/13.4MB  (26.4%)
2024-03-26T04:39:59.198-0700    [############............]  logs.nginx  7.11MB/13.4MB  (52.9%)
2024-03-26T04:40:02.198-0700    [##################......]  logs.nginx  10.2MB/13.4MB  (76.1%)
2024-03-26T04:40:04.702-0700    [########################]  logs.nginx  13.4MB/13.4MB  (100.0%)
2024-03-26T04:40:04.702-0700    no indexes to restore
2024-03-26T04:40:04.702-0700    finished restoring logs.nginx (94778 documents, 0 failures)
2024-03-26T04:40:04.702-0700    94778 document(s) restored successfully. 0 document(s) failed to restore.
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL# ./12-log_stats.py
94778 logs
Methods:
        method GET: 93842
        method POST: 229
        method PUT: 0
        method PATCH: 0
        method DELETE: 0
47415 status check
root@5292f0d32cbc:/alx-backend-storage/0x01-NoSQL#
```
