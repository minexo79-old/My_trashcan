import yaml,pymongo
import datetime,pytz

# 資料勾手
# 讀取Yaml的資料，通常是機器人設定檔

class Hook: # 機器人設定檔
    def __init__(self,filename):
        self.filename = filename

    def open(self):
        with open(self.filename,'r',encoding="utf-8") as f:
            ydata = yaml.safe_load(f)
            return ydata


# 取得台灣時間-utf8
def get_time(choose='default'):
    # 設定國家
    tz = pytz.timezone('Asia/Taipei')
    if choose == 'default': # 預設顯示方式
        time = datetime.datetime.now(tz).strftime('%Y.%m.%d-%H:%M:%S')
    elif choose == 'sql': # sql-ID顯示方式
        time = datetime.datetime.now(tz).strftime('%Y%m%d%H%M%S')
    return str(time)

# mongoDB 資料庫
class Mongodb:
    def __init__(self,guild,channel,data):
        self.guild = guild
        self.channel = channel
        self.data = data
        self.dbhook = None

    def connect(self):
        f = Hook(".//mconfig.yaml").open()
        servername = f['db']['address']
        # 連接mongoDB
        self.dbhook = pymongo.MongoClient(servername)

    def insert(self):
        # database      :server name
        # collection    :channel name
        col = self.dbhook[self.guild][self.channel]
        # 插入一筆data
        col.insert_one(self.data)
        # debug
        # print("(MON) Send to the mongoDB!")