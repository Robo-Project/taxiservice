from hashlib import sha1
import json
import sys
import xml.etree.ElementTree as ET

from sqlalchemy import (Boolean, Column, create_engine, DateTime, Float,
                        Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

"""Parser"""


def parse_file(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    for testElement in root.iter('test'):
        for keywordElement in testElement.iter('kw'):
            if keywordElement.get('name') == 'Log':
                result = keywordElement.find('msg').text
    return json.loads(result)


"""Hash function"""


def make_hash(xml_file):
    block_size = 68157440
    hasher = sha1()
    with open(xml_file, 'rb') as f:
        chunk = f.read(block_size)
        while len(chunk) > 0:
            hasher.update(chunk)
            chunk = f.read(block_size)
    return hasher.hexdigest()


"""Database"""


def save_to_database(data_base_string, path_to_xml):
    db = create_engine(data_base_string)
    base = declarative_base()

    class TaxiDrive(base):
        __tablename__ = 'taxi_drives'

        xml_hash = Column(String, primary_key=True)
        driver = Column(String)
        car_number = Column(Integer)
        startTime = Column(DateTime)
        lengthOfDrive = Column(Float)
        durationOfDrive = Column(Float)
        endTime = Column(DateTime)
        passengers = Column(Integer)
        price = Column(Float)
        reason_for_failure = Column(String)
        trip_succeeded = Column(Boolean)
        test_runs_id = Column(Integer)

    session = sessionmaker(db)
    session = session()

    base.metadata.create_all(db)
    hash_for_test_run = make_hash(xml_path)

    # Search for the foreign key

    stmt = text("select test_runs.id from test_runs "
                " WHERE test_runs.hash = '" + hash_for_test_run + "';")

    res = db.engine.execute(stmt)

    result = ""
    for row in res:
        result = row[0]

    taxi = parse_file(path_to_xml)
    taxi = TaxiDrive(xml_hash=hash_for_test_run,
                     driver=taxi['driver'],
                     car_number=taxi['car_number'],
                     startTime=taxi['start'],
                     lengthOfDrive=taxi['length'],
                     durationOfDrive=taxi['time'],
                     endTime=taxi['end'],
                     passengers=taxi['passengers'],
                     price=taxi['price'],
                     reason_for_failure=taxi['reason_for_failure'],
                     trip_succeeded=taxi['trip_succeeded'],
                     test_runs_id=result)

    session.add(taxi)
    session.commit()
    session.close()


# Insert paths to test
db_string = sys.argv[1]
xml_path = sys.argv[2]
save_to_database(db_string, xml_path)
