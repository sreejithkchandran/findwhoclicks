import socket
import datetime
from pymongo import MongoClient
import sys
import getpass

__author__ = "SREEJITH KOVILAKATHUVEETTIL CHANDRAN"
__copyright__ = " Copyright 2015,SREEJITH KOVILAKATHUVEETTIL CHANDRAN"
__email__ = "sreeju_kc@hotmail.com"
__license__ = "Apache License 2.0"

def fipandhost():
    ip = socket.gethostbyname(socket.gethostname())#To fetch the IP address
    host = socket.getfqdn()#To fetch the hostname
    user = getpass.getuser()#To fetch the username
    conn = MongoClient()
    conn = MongoClient('mongodb://X.X.X.X:27017/')#You need to setup a mongoDB server first and provide mongoDB server IP address.
    db = conn.socail_eng
    collection = db.sc_feed
    post = {"IP": ip,
       "Hostname": host,
       "Username": user}
    pf = collection.find({"IP":ip,"Hostname":host}).count()
    if pf > 0: #This will make sure no duplicate entry is created,even if user clicks multiple times it wont matter
        sys.exit()
    collection.insert(post)
if __name__ == '__main__':
    fipandhost()
    
