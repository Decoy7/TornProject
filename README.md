# Torn Flight Site For Factions

### Features
- Database ORM (flask-sqlalchemy)

### How to Run

1. Clone the repository
 ```git clone https://github.com/Decoy7/TornProject.git```
 
2. Run with gunicorn the following command
  ```gunicorn -w 4 -b 0.0.0.0:5000 "TornProject.main:create_app()"```
