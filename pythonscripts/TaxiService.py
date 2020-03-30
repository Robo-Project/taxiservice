class TaxiService:

    def __init__(self):
        self.length = 10
        self.price = 50
        self.time = 30

    def drive_taxi(self):
        results = []
        results.append(self.length)
        results.append(self.price)
        results.append(self.time)

        
    def return_length(self):
        return self.length

    def return_price(self):
        return self.price

    def return_time(self):
        return self.time