#!/usr/bin/python3

from requests import get
from json import loads
import sqlite3
from datetime import datetime

con_stock = sqlite3.connect("API/foreign_stock.db")
cur_stock = con_stock.cursor()

resp = loads(get("https://yata.yt/api/v1/travel/export/").content)

#Calculate froom unix time into UTC time ex. "2022-10-08 20:51:17" as string variable
mexico_update = datetime.utcfromtimestamp(int(resp["stocks"]["mex"]["update"])).strftime("%Y-%m-%d %H:%M:%S")
cayman_update = datetime.utcfromtimestamp(int(resp["stocks"]["cay"]["update"])).strftime("%Y-%m-%d %H:%M:%S")
canada_update = datetime.utcfromtimestamp(int(resp["stocks"]["can"]["update"])).strftime("%Y-%m-%d %H:%M:%S")
hawaii_update = datetime.utcfromtimestamp(int(resp["stocks"]["haw"]["update"])).strftime("%Y-%m-%d %H:%M:%S")
uk_update = datetime.utcfromtimestamp(int(resp["stocks"]["uni"]["update"])).strftime("%Y-%m-%d %H:%M:%S")
argentina_update = datetime.utcfromtimestamp(int(resp["stocks"]["arg"]["update"])).strftime("%Y-%m-%d %H:%M:%S")
switzerland_update = datetime.utcfromtimestamp(int(resp["stocks"]["swi"]["update"])).strftime("%Y-%m-%d %H:%M:%S")
japan_update = datetime.utcfromtimestamp(int(resp["stocks"]["jap"]["update"])).strftime("%Y-%m-%d %H:%M:%S")
china_update = datetime.utcfromtimestamp(int(resp["stocks"]["chi"]["update"])).strftime("%Y-%m-%d %H:%M:%S")
uae_update = datetime.utcfromtimestamp(int(resp["stocks"]["uae"]["update"])).strftime("%Y-%m-%d %H:%M:%S")
sa_update = datetime.utcfromtimestamp(int(resp["stocks"]["sou"]["update"])).strftime("%Y-%m-%d %H:%M:%S")
#Calculate froom unix time into UTC time ex. "2022-10-08 20:51:17" as string variable

################# MEXICO #################
mexico = {}
mexico[0] = {
    "name" : resp["stocks"]["mex"]["stocks"][1]["name"],
    "quantity" : (resp["stocks"]["mex"]["stocks"][1]["quantity"]),
    "update" : mexico_update
}
mexico[1] = {
    "name" : resp["stocks"]["mex"]["stocks"][22]["name"],
    "quantity" : (resp["stocks"]["mex"]["stocks"][22]["quantity"]),
    "update" : mexico_update
}
################# MEXICO #################

################# CAYMAN ISLANDS #################
cayman = {}
cayman[0] = {
    "name" : resp["stocks"]["cay"]["stocks"][2]["name"],
    "quantity" : (resp["stocks"]["cay"]["stocks"][2]["quantity"]),
    "update" : cayman_update
}
cayman[1] = {
    "name" : resp["stocks"]["cay"]["stocks"][10]["name"],
    "quantity" : (resp["stocks"]["cay"]["stocks"][10]["quantity"]),
    "update" : cayman_update
}
################# CAYMAN ISLANDS #################

################# CANADA #################
canada = {}
canada[0] = {
    "name" : resp["stocks"]["can"]["stocks"][2]["name"],
    "quantity" : (resp["stocks"]["can"]["stocks"][2]["quantity"]),
    "update" : canada_update
}
canada[1] = {
    "name" : resp["stocks"]["can"]["stocks"][4]["name"],
    "quantity" : (resp["stocks"]["can"]["stocks"][4]["quantity"]),
    "update" : canada_update
}
################# CANADA #################

################# HAWAII #################
hawaii = {}
hawaii[0] = {
    "name" : resp["stocks"]["haw"]["stocks"][9]["name"],
    "quantity" : (resp["stocks"]["haw"]["stocks"][9]["quantity"]),
    "update" : hawaii_update   
}
################# HAWAII #################

################# UNITED KINGDOM #################
uk = {}
uk[0] = {
    "name" : resp["stocks"]["uni"]["stocks"][0]["name"],
    "quantity" : (resp["stocks"]["uni"]["stocks"][0]["quantity"]),
    "update" : uk_update
}
uk[1] = {
    "name" : resp["stocks"]["uni"]["stocks"][6]["name"],
    "quantity" : (resp["stocks"]["uni"]["stocks"][6]["quantity"]),
    "update" : uk_update
}
uk[2] = {
    "name" : resp["stocks"]["uni"]["stocks"][10]["name"],
    "quantity" : (resp["stocks"]["uni"]["stocks"][10]["quantity"]),
    "update" : uk_update
}
################# UNITED KINGDOM #################

################# ARGENTINA #################
argentina = {}
argentina[0] = {
    "name" : resp["stocks"]["arg"]["stocks"][0]["name"],
    "quantity" : (resp["stocks"]["arg"]["stocks"][0]["quantity"]),
    "update" : argentina_update
}
argentina[1] = {
    "name" : resp["stocks"]["arg"]["stocks"][1]["name"],
    "quantity" : (resp["stocks"]["arg"]["stocks"][1]["quantity"]),
    "update" : argentina_update
}
################# ARGENTINA #################

################# SWITZERLAND #################
switzerland = {}
switzerland[0] = {
    "name" : resp["stocks"]["swi"]["stocks"][0]["name"],
    "quantity" : (resp["stocks"]["swi"]["stocks"][0]["quantity"]),
    "update" : switzerland_update
}
switzerland[1] = {
    "name" : resp["stocks"]["swi"]["stocks"][1]["name"],
    "quantity" : (resp["stocks"]["swi"]["stocks"][1]["quantity"]),
    "update" : switzerland_update
}
# THIS IS DOZEN WHITE ROSES WORTH 950 MILLION
# switzerland[2] = {
#     "name" : resp["stocks"]["swi"]["stocks"][13]["name"],
#     "quantity" : (resp["stocks"]["swi"]["stocks"][13]["quantity"]),
#     "update" : switzerland_update
# }
################# SWITZERLAND #################

################# JAPAN #################
japan = {}
japan[0] = {
    "name" : resp["stocks"]["jap"]["stocks"][18]["name"],
    "quantity" : (resp["stocks"]["jap"]["stocks"][18]["quantity"]),
    "update" : japan_update
}
################# JAPAN #################

################# CHINA #################
china = {}
china[0] = {
        "name" : resp["stocks"]["chi"]["stocks"][9]["name"],
        "quantity" : (resp["stocks"]["chi"]["stocks"][9]["quantity"]),
        "update" : china_update
}
china[1] = {
        "name" : resp["stocks"]["chi"]["stocks"][0]["name"],
        "quantity" : (resp["stocks"]["chi"]["stocks"][0]["quantity"]),
        "update" : china_update
}
################# CHINA #################

################# UNITED ARAB EMIRATES #################
uae = {}
uae[0] = {
        "name" : resp["stocks"]["uae"]["stocks"][7]["name"],
        "quantity" : (resp["stocks"]["uae"]["stocks"][7]["quantity"]),
        "update" : uae_update
}
uae[1] = {
         "name" : resp["stocks"]["uae"]["stocks"][10]["name"],
        "quantity" : (resp["stocks"]["uae"]["stocks"][10]["quantity"]),
        "update" : uae_update
}
################# UNITED ARAB EMIRATES #################

################# SOUTH AFRICA #################
sa = {}
sa[0] = {
         "name" : resp["stocks"]["sou"]["stocks"][3]["name"],
        "quantity" : (resp["stocks"]["sou"]["stocks"][3]["quantity"]),
        "update" : sa_update
}
sa[1] = {
        "name" : resp["stocks"]["sou"]["stocks"][7]["name"],
        "quantity" : (resp["stocks"]["sou"]["stocks"][7]["quantity"]),
        "update" : sa_update
}
################# SOUTH AFRICA #################

cur_stock.execute("DELETE FROM Stock")

cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{mexico[0]["name"]}",{mexico[0]["quantity"]},"{mexico[0]["update"]}","Mexico","Plushie")')
cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{mexico[1]["name"]}",{mexico[1]["quantity"]},"{mexico[1]["update"]}","Mexico","Flower")')

cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{cayman[0]["name"]}",{cayman[0]["quantity"]},"{cayman[0]["update"]}","Cayman Islands","Flower")')
cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{cayman[1]["name"]}",{cayman[1]["quantity"]},"{cayman[1]["update"]}","Cayman Islands","Plushie")')

cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{canada[0]["name"]}",{canada[0]["quantity"]},"{canada[0]["update"]}","Canada","Flower")')
cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{canada[1]["name"]}",{canada[1]["quantity"]},"{canada[1]["update"]}","Canada","Plushie")')

cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{hawaii[0]["name"]}",{hawaii[0]["quantity"]},"{hawaii[0]["update"]}","Hawaii","Flower")')

cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{uk[0]["name"]}",{uk[0]["quantity"]},"{uk[0]["update"]}","United Kingdom","Flower")')
cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{uk[1]["name"]}",{uk[1]["quantity"]},"{uk[1]["update"]}","United Kingdom","Plushie")')
cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{uk[2]["name"]}",{uk[2]["quantity"]},"{uk[2]["update"]}","United Kingdom","Plushie")')

cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{argentina[0]["name"]}",{argentina[0]["quantity"]},"{argentina[0]["update"]}","Argentina","Flower")')
cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{argentina[1]["name"]}",{argentina[1]["quantity"]},"{argentina[1]["update"]}","Argentina","Plushie")')

cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{switzerland[0]["name"]}",{switzerland[0]["quantity"]},"{switzerland[0]["update"]}","Switzerland","Plushie")')
cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{switzerland[1]["name"]}",{switzerland[1]["quantity"]},"{switzerland[1]["update"]}","Switzerland","Flower")')

cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{japan[0]["name"]}",{japan[0]["quantity"]},"{japan[0]["update"]}","Japan","Flower")')

cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{china[0]["name"]}",{china[0]["quantity"]},"{china[0]["update"]}","China","Flower")')
cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{china[1]["name"]}",{china[1]["quantity"]},"{china[1]["update"]}","China","Plushie")')

cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{uae[0]["name"]}",{uae[0]["quantity"]},"{uae[0]["update"]}","United Arab Emirates","Flower")')
cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{uae[1]["name"]}",{uae[1]["quantity"]},"{uae[1]["update"]}","United Arab Emirates","Plushie")')

cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{sa[0]["name"]}",{sa[0]["quantity"]},"{sa[0]["update"]}","South Africa","Flower")')
cur_stock.execute(f'INSERT INTO Stock (name,quantity,update_time,country,type) VALUES ("{sa[1]["name"]}",{sa[1]["quantity"]},"{sa[1]["update"]}","South Africa","Plushie")')

con_stock.commit()

cur_stock.close()
con_stock.close()