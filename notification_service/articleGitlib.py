toket = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODI1MzM2MTksImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkF2aWFkT2xzc29uIn0.jTB_m673hfcxHiXnaaE4DIbohmywohC3NlbADMxCguE"

class notification:
    
    def __init__(self, id, start_date, text, tag, end_date):
        self.id = id
        self.start_date = start_date
        self.text = text
        self.tag = tag
        self.end_date = end_date

class client:

    def __init__(self, id, phone, code, tag, time_zone):
        self.id = id
        self.phone = phone
        self.code = code
        self.tag = tag
        self.time_zone = time_zone

class message:

    def __init__(self, id, date, status, id_notifi, id_client):
        self.id = id
        self.date = date
        self.status = status
        self.id_notifi = id_notifi
        self.id_client = id_client