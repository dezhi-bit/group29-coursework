# group29-coursework
**Group29-coursework RESTFUL API for Calendar**

This project is use python and flask to implement RESTful API for Calendar. 

The calendar api is from:

[https://calendarific.com/api-documentation]

**Basic functions**
1. API
```
calendarific_data = 'https://calendarific.com/api/v2/holidays?&api_key={api_key}&country={country}&year={year}'
```
This api include the api_key, the deatil is can choose different country and year. 

2. cloud database
This project using the mysql that is running in the docker to save the data of calendar's holidays. 
mysql 5.7 is Stable version. 
```
docker pull mysql:5.7
docker run -p 3306:3306 --name mysql  -e MYSQL_ROOT_PASSWORD=root  -d mysql:5.7
docker start mysql
```

2.1 auth database 
This project use sqlite to save the account name and password
```
class User(UserMixin, db.Model):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    ```
    
3. CRUD method

All code is in the db11.py


3.1 POST
```
#use POST to insert holidays
@main.route('/records/holidays/', methods=['POST'])
def add_holidays():
    for dic in calendarifics['response']['holidays']:
        response = Mysql.insert(dic)
        return jsonify(response)
```
3.2 GET
```
# use GET to select the holidays from database
@main.route('/records/holidays/', methods=['GET'])
def get_data():
    response = Mysql.select1()
    return Response(
        response=json.dumps(response),
        status=200,
        mimetype="application/json"
    )
```
3.3 PUT
```
# use put to update holidays
@main.route('/records/holidays/<oldname>/<newname>', methods=['PUT'])
def update_holidays(oldname,newname):
    a = oldname
    a.replace('%20', ' ')
    b=newname
    b.replace('%20', ' ')
    response = Mysql.update1(a,b)
    return jsonify(response)
```
3.4 DELETE
```
# use DELETE to delete holidays
@main.route('/records/holidays/<name>', methods=['DELETE'])
def del_holidays(name):
    a = name
    a.replace('%20', ' ')
    response = Mysql.delete1(a)
    return jsonify(response)
```

**Option2**

2.1 
The https is using ssl_context='adhoc'
```
if __name__ == "__main__":
    app.run(host='localhost', ssl_context='adhoc')
```

2.2
Implementing user accounts and access management is using flask_login

All code is in the auth.py


**Requirement**

All libraries package is in the requirement.txt






    
