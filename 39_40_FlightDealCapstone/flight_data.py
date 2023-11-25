from datetime import datetime, timedelta

class FlightData:
    def __init__(self):
        self.fly_from = 'SIN'
        self.date_from = (datetime.today() + timedelta(days=1)).strftime('%d/%m/%Y') # departure flight min
        self.date_to = (datetime.today()  + timedelta(days=6*30)).strftime('%d/%m/%Y') # depature flight max
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 28
        self.curr = 'SGD'

