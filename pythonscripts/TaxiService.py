from datetime import datetime, time, timedelta
import json
import random


class TaxiService:

    def __init__(self):

        """Driver"""
        drivers = ["Keke", "Jake", "Make", "Kake"]
        self.driver = drivers[random.randint(0, 3)]

        """Car number"""
        self.car_number = random.randint(1, 100)

        """Start timestamp"""
        self.start = datetime.now()
        self.start = self.start - timedelta(days=random.randint(0, 30))
        self.start = self.start - timedelta(hours=random.randint(0, 23))
        self.start = self.start - timedelta(minutes=random.randint(0, 60))

        """Length in kilometers"""
        x = random.randint(1, 10)
        if x > 9:
            self.length = random.randint(1, 1000)
        elif x > 8:
            self.length = random.randint(1, 100)
        else:
            self.length = random.randint(1, 10)

        """Duration in minutes"""
        self.time = (self.length / random.randint(20, 100)) * 10 + 15

        """End timestamp"""
        self.end = self.start + timedelta(minutes=self.time)

        """Passengers"""
        self.passengers = random.randint(1, 8)

        """Price in euros"""
        if self.passengers < 5:
            if self.start.isoweekday() == 7 or self.is_expensive_hours():
                self.price = self.length * 1.09 + 6.9
            else:
                self.price = self.length * 0.99 + 5
        else:
            self.price = self.length * 1.59 + 6.9

        """Does trip fail"""
        failure = random.randint(1, 100)
        self.reason_for_failure = ""
        self.trip_succeeded = True
        if failure > 70:
            self.price = 0
            self.trip_succeeded = False
            reasons = ["Not paid", "Covid", "UFO", "Crash", "Vehicle malfunction"]
            self.reason_for_failure = reasons[random.randint(0, 4)]

    def return_driver(self):
        return self.driver

    def return_car_number(self):
        return self.car_number

    def return_start(self):
        return self.start

    def return_success(self):
        return self.trip_succeeded

    def return_end(self):
        return self.end

    def return_length(self):
        return self.length

    def return_price(self):
        return self.price

    def return_time(self):
        return self.time

    def return_passengers(self):
        return self.passengers

    def return_price(self):
        return self.price

    def return_reason_for_failure(self):
        return self.reason_for_failure

    def is_expensive_hours(self):
        begin_time = time(21, 0)
        end_time = time(5, 00)
        check_time = self.start.time()
        if begin_time < end_time:
            return begin_time <= check_time <= end_time
        else:
            return begin_time <= check_time or check_time <= end_time

    def return_json(self):
        """Convert datetimes into isoformat"""
        self.start = self.start.isoformat()
        self.end = self.end.isoformat()
        self.time = self.time
        return json.dumps(self.__dict__)


"""Test run
for x in range(1, 10):
    taxi = TaxiService()
    print()
    print("TAXI")
    print("Driver:", taxi.return_driver())
    print("Car number:", taxi.return_car_number())
    print("Start time:", taxi.return_start().time())
    print("Day:", taxi.return_start().isoweekday())
    print("Trip succeeded:", taxi.return_success())
    if not taxi.return_success():
        print("Reason for failure:", taxi.return_reason_for_failure())
    print("End time:", taxi.return_end().time())
    print("Duration:", taxi.return_time())
    print("Length:", taxi.return_length())
    print("Passengers:", taxi.return_passengers())
    print("Price:", taxi.return_price())
    print(taxi.return_json())"""
