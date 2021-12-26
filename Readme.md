
This Yoga class application is a dynamic website which reacts at realtime as well as it is a highly scalable application.
This website is totally developed on tech stacks Django, Python, Html, Css, Bootstrap, Javascript, postgresql(Database). I have used ORM (Object Relationship Mapping) for database handling and DTL (Django Template Library) and Jinja for Rest API connection and dynamic data handling in between backend and frontend.
this application have feature of secure signup and login with django authentication. Signup has password validator and username, email, age validations which is very powerful. login is done using the safer auth library of django authentication. The forgot password option is also given to the user where after submitting some valid information the password will be sent to the user's valid email id. After logging in, users will be able to edit their own profile. where view profile, edit profile, change password, view transaction history and payment option is given to the user. i have added be an instructor page(if someone wants to be yoga instructor at class then he/she can apply it from there), contact us page(where user can write their query,feedback,issues,requests to yoga class), Newsletter(to get regular update from class), Advertisement page (If website admin wants to post some advertisements for class then admin can do it from admin portal),Admin portal(to manage all the database). Everything has an email alert system.
Some problem statements solved are here.. users will be able to check the validity of their membership or will get an alert on their mail also. while payment users will be able to change their batch/shift. Each and every transaction history will be shown to the user.
 
To install this application you need to have following softwares:-
1)python with latest version
2)pip with latest version
3)Postgresql with latest version
4)Visual Studio with latest version
5)All path should be added to system variables
 
Steps to run application:
1)First of all, Go to the location where you want to install the software and make one folder.
2)open cmd .. Follow commands:- write your own names where it is mentioned to type name.. write it down to remember it.
cd nikhil(folder_name)
3)Make an environment for the django application and activate it. whenever want to run a project, I need to start the environment first using the workon command.
pip install virtualenvwrapper-win
mkvirtualenv nick(env_name)
workon nick(env_name)
4)After this, paste the application file in the same location.
5)install all the packages mentioned in requirements.txt
ex. pip install psycopg2
6)open postgresql and make one database named 'yogadb'.
7)open project in cmd ex. cd yoga
8)migrate database schema/model to database 'yogadb'. for that write following commands:-
python manage.py makemigrations
python manage.py sqlmigrate yogaweb 0001
python manage.py migrate
....and database will get migrated to postgresql
9)Now lets create Admin superuser
python manage.py createsuperuser
username=nikhil
email=nikhil@gmail.com
password=123(won't be able to see typed characters.so don't worry.just type it)
confirm password=123(won't be able to see typed characters.so don't worry.just type it)
weak password[Y/N]=Y
superuser will get created.
10)Now you can run your application. Use the following command.
python manage.py runserver
go to google chrome and type in the url bar http://127.0.0.1:8000/ and the application will get executed successfully.
11)to visit admin site visit http://127.0.0.1:8000/admin