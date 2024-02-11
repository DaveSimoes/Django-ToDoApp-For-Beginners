<div align="center"> <h2> ⚡️ Simple ToDo app built with Django for beginners ⚡️ </h2></div>


![image](https://github.com/DaveSimoes/ToDo-Django/assets/109705197/cddf7ad3-f133-48fe-b1b9-b6ebd7e99b1e)


### Setup ⚙️
To get this repository, run the following command inside your git enabled terminal 
```bash
$ git clone https://github.com/DaveSimoes/ToDo-Django.git
```
⚠️ You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

## Get started  🚀
Once you have downloaded django, go to the cloned repo directory and run the following command

```bash
$ python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
$ python manage.py migrate
```

One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user
```bash
$ python manage.py createsuperuser
```

🚨 We just need to start the server now and then we can start using our simple todo App. Start the server by following command

```bash
$ python manage.py runserver
```

Once the server is hosted, head over to http://127.0.0.1:8000/todos for the App.

 Happy Coding 
