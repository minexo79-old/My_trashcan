import paho.mqtt.client as mqtt
from datahook import jsdata 
import os,sys,datetime

#----------------------
# MQTT simulation app 1.0 > subscribe client
# by minexo79
#----------------------

# open json
hook = jsdata("config.json").open

def on_connect(client,userdata,flags,rc): # connect to mqtt server
    # print out connected message
    print(f"successfully connected with result code {str(rc)}.\n")
    # get json topic
    client.subscribe(hook()['topic'],qos=0)

def on_msg(client,userdata,message): # subscribe from mqtt server
    # catch now time
    nowtime = datetime.datetime.now().strftime("[%m/%d] %H:%M:%S")
    if str(message.payload,encoding="utf-8") == 'Done!':
        print("\033[34m",end="")
        print(nowtime,end="")
        print(" ESP8266 has connected!")        
    # cut the data and turn to array
    else:
        data = str(message.payload,encoding="utf-8").split(',')
        # display message
        print("\033[31m",end="")
        print(nowtime,hook()['topic'],end="")
        print(": \033[33m",end="")
        print(f"Tempture: {data[0]} ﾟC / Humidity: {data[1]} % ({data[2]})")

if __name__ == "__main__":
    os.system('cls')
    print("--MQTT subscribe test--")
    # create the mqtt object and send the tcp.
    client = mqtt.Client(transport="tcp")
    # get the json username and password.
    client.username_pw_set(username=hook()['username'],password=hook()['passwd'])
    try:
        # try to connect.
        client.connect(hook()['ip'],1883,10)
    except OSError as e:
        # if lose the connect (like server is off or server can't run the mqtt service)
        # print out error message
        print(f"Unable to connect {hook()['ip']} : Check your network setting!")
        print(e)
        # close the app
        sys.exit()
    else: # connect to server.
        # assignation on_connect function (connected)
        client.on_connect = on_connect
        # assignation on_message function (get message from mqtt server)
        client.on_message = on_msg
        # create the loop
        client.loop_forever()