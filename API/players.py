#!/usr/bin/python3

from time import sleep
from requests import get
from json import loads
from datetime import datetime
import sqlite3

con = sqlite3.connect("TornProject/API/players.db")
cur = con.cursor()

API = "" #your API key here
faction_id = "" #your faction ID here

players = {}

countries = [
    "Mexico", "New Zealand", "Zealand", "NZ", "Canada", "Hawaii", "United Kingdom", "Kingdom", "UK", "Argentina",
    "Switzerland", "Japan", "China", "United Arab Emirates", "Emirates", "UAE", "South Africa", "Africa", "SA", "Torn"
]

def get_members_ids(faction_id):
    url = "https://api.torn.com/faction/" + \
        str(faction_id)+"?selections=&key="+str(API)
    resp = loads(get(url).content)

    ids_total = []
    for id in resp["members"]:
        if ("Traveling" in resp["members"][str(id)]["status"]["description"]):
            ids_total.append(str(id))
        elif ("Returning" in resp["members"][str(id)]["status"]["description"]):
            ids_total.append(str(id))
        elif ("In a " in resp["members"][str(id)]["status"]["description"]) or ("In an" in resp["members"][str(id)]["status"]["description"]):
            ids_total.append(str(id))
        elif (resp["members"][str(id)]["status"]["state"] == "Abroad"):
            ids_total.append(str(id))
    return ids_total

ids_total = get_members_ids(faction_id)

# Get conrent time in the format of "31/5/2022 13:22:17"
now = datetime.now()
res = f"{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}:{now.second}"

# for every ID of a travelling player
for id in ids_total:

    url = r"https://api.torn.com/user/"+id+"?selections=basic&key="+API
    resp = loads(get(url).content)

    desc = resp["status"]["description"].split()

    for country in countries:
        if country in desc:
            if country == "Torn":
                # Torn ID
                players[id] = {
                    "Name": str(resp["name"]),
                    "Status": str("Returning"),
                    "Country": str(country),
                    "Timestamp": str(res)
                }
            elif country == "Africa":
                players[id] = {
                    "Name": str(resp["name"]),
                    "Status": str(resp["status"]["state"]),
                    "Country": str("South Africa"),
                    "Timestamp": str(res)
                }
            elif country == "Kingdom":
                players[id] = {
                    "Name": str(resp["name"]),
                    "Status": str(resp["status"]["state"]),
                    "Country": str("United Kingdom"),
                    "Timestamp": str(res)
                }
            elif country == "Emirates":
                players[id] = {
                    "Name": str(resp["name"]),
                    "Status": str(resp["status"]["state"]),
                    "Country": str("United Arab Emirates"),
                    "Timestamp": str(res)
                }
            elif country == "Zealand":
                players[id] = {
                    "Name": str(resp["name"]),
                    "Status": str(resp["status"]["state"]),
                    "Country": str("New Zealand"),
                    "Timestamp": str(res)
                }
            else:
                players[id] = {
                    "Name": str(resp["name"]),
                    "Status": str(resp["status"]["state"]),
                    "Country": str(country),
                    "Timestamp": str(res)
                }

for id in players:
    cur.execute(f'INSERT INTO Torn (Torn_ID,Name,Status,Country,Timestamp) VALUES ("{id}","{players[id]["Name"]}","{players[id]["Status"]}","{players[id]["Country"]}","{res}");')
    con.commit()

con.close()
sleep(60)