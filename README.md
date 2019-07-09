# Django watching-storage app
Application contains few views which purpose is to connect to remote server
and display data about visits and passcodes.
You can obtain database credentials only if you are user of [dvmn](https://dvmn.org). 
## Usage
* Setup requirements
```bash
pip install -r requirements.txt
```
* Update .env file (example.env provided)
    * HOST
    * PORT
    * NAME(database name)
    * USER
    * PASSWORD
    * SECRET_KEY
    * DEBUG
* Run application
```bash
python manage.py runserver 0.0.0.0:8000
```
Then open in browser
```bash
http://localhost:8000/
```
## Project goals
The code is written for educational purposes. 
Training course for web-developers[dvmn](https://dvmn.org).