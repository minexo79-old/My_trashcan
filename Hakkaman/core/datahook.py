import json,os

# 資料勾手：抓取json設定檔的資料

class datahook:
    def __init__(self,jsonname):
        self.jsonname = jsonname
    
    def open(self):
        with open(self.jsonname,'r',encoding="utf-8") as f:
            return json.load(f)


