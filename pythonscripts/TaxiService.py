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

        return results