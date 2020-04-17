# Taxiservice

This is a class that simulates taxi drives.

Running it

- first [simulates](https://github.com/Robo-Project/taxiservice/blob/master/pythonscripts/TaxiService.py) a taxi drive that is run through [Robot Framework](https://github.com/Robo-Project/taxiservice/blob/master/tasks/TaxiRobo.robot)
- then logs related task metadata with [dbbot-sqlalchemy](https://github.com/pbylicki/DbBot-SQLAlchemy)
- then uses [databasesaver.py](https://github.com/Robo-Project/taxiservice/blob/master/pythonscripts/DatabaseSaver.py) to create a new table called taxi_drives that has a foreign key to dbbot table test_runs ([dbbot-sqlalchemy tables](https://github.com/pbylicki/DbBot-SQLAlchemy/blob/master/doc/robot_database.md))

DbBot proved not to be suitable for saving task related data. This is why we had to create our own dbsaver, that saves required data from the task. More about that [here](https://github.com/Robo-Project/rpa_dashboard/blob/master/documentation/dbbotreport.md)

### Schema:

taxi_drives
-----------

column              | type     | not null | description
--------------------|----------|----------|------------
xml_hash            | TEXT     |          | primary key, a SHA1 hash of the source file
driver              | TEXT     |          | taxi driver
car_number          | INTEGER  |          | number of car
start_time          | DATETIME |          | when was taxi drive started at
length_of_drive     | FLOAT    |          | length of drive in kilometers 
duration_of_drive   | FLOAT    |          | duration of drive in minutes
end_time            | DATETIME |          | time when drive was finished
passengers          | INTEGER  |          | number of car
price               | FLOAT    |          | price in eur
reason_for_failure  | TEXT     |          | if drive failed, the reason
trip_succeeded      | BOOLEAN  |          | trip succeeded or not
test_runs_id        | INTEGER  |          | foreign key to test_runs.id
