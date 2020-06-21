import yaml

# --------------------
# yd : yaml data
# 資料勾手
# --------------------

class yamlhook:
    def __init__(self,filename):
        self.filename = filename

    # load : 純讀取

    def load(self):    
        with open(self.filename,'r',encoding="utf8") as yd:
            return yaml.safe_load(yd)

    def operate(self,did:int,db="",process=""):

        # owner: 自訂權限
        # blacklist: 黑名單

        with open(self.filename,'r',encoding="utf8") as yd:
            data = yaml.safe_load(yd)

        # append: 增加
        # remove: 移除

        if process == "append":
            if db == "owner":
                data['bot']['owner'].append(did)
            elif db == "blacklist":
                data['blacklist'].append(did)

        elif process == "remove":
            if db == "owner":
                data['bot']['owner'].remove(did)
            elif db == "blacklist":
                data['blacklist'].remove(did)

        with open(self.filename,'w',encoding="utf8") as yd:
            yaml.safe_dump(data,yd)