import json

class jsdata:
    def __init__(self,filename):
        self.filename = filename

    def open(self):
        with open (self.filename,'r',encoding='utf-8') as jd:
            return json.load(jd)