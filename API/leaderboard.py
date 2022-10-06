#!/usr/bin/python3

from requests import get
from json import loads
import sqlite3

API = ""  # Your API key here
faction_id = ""  # Your faction ID here

def get_members_ids(faction_id):
    ids = []
    names = []
    players = {}
    url = "https://api.torn.com/faction/" + \
        str(faction_id)+"?selections=&key="+str(API)
    resp = loads(get(url).content)
    for id in resp["members"]:
        ids.append(str(id))
        names.append(str(resp["members"][str(id)]["name"]))
        players[id] = {
            "name": str(str(resp["members"][str(id)]["name"]))
        }
    return players


con_leaderboard = sqlite3.connect("/home/michael/repos/python/TornProject/API/leaderboard.db")
cur_leaderboard = con_leaderboard.cursor()

con_players = sqlite3.connect("/home/michael/repos/python/TornProject/API/players.db")
cur_players = con_players.cursor()

players = {}
players = get_members_ids(faction_id)

try:
    for id in players:
        cur_leaderboard.execute(f'INSERT INTO Leaderboard (Torn_ID,Name) VALUES ("{id}","{players[id]["name"]}")')
    con_leaderboard.commit()
except sqlite3.IntegrityError as e:  # If it already exists
    pass


players_travel = {}

for id in players:
    resp = cur_players.execute(f'SELECT * FROM Torn WHERE Torn_ID == "{id}";').fetchall()

    countries = []
    returning_flag = False
    travelling_flag = False
    for item in range(0, len(resp)):
        if resp[item][2] == "Traveling" and travelling_flag == False:
            travelling_flag = True
            returning_flag = False
            countries.append(resp[item][3])
        elif resp[item][2] == "Abroad":
            pass
        elif resp[item][2] == "Returning" and returning_flag == False:
            returning_flag = True
            travelling_flag = False

    # If player has not a single flight registered don't add them for counting later in the json object
    if len(countries) != 0:
        players_travel[id] = {
            "Country_list": countries
        }

con_players.commit()

countries = [
    "Mexico", "Cayman Islands", "Canada", "Hawaii", "United Kingdom", "Argentina",
    "Switzerland", "Japan", "China", "United Arab Emirates", "South Africa", "Cayman Islands"
]

for id in players_travel:
    Mexico_flag = (players_travel[id]["Country_list"]).count("Mexico")
    Cayman_flag = (players_travel[id]["Country_list"]).count("Cayman Islands")
    Canada_flag = (players_travel[id]["Country_list"]).count("Canada")
    Hawaii_flag = (players_travel[id]["Country_list"]).count("Hawaii")
    UK_flag = (players_travel[id]["Country_list"]).count("United Kingdom")
    Argentina_flag = (players_travel[id]["Country_list"]).count("Argentina")
    Switzerland_flag = (players_travel[id]["Country_list"]).count("Switzerland")
    Japan_flag = (players_travel[id]["Country_list"]).count("Japan")
    China_flag = (players_travel[id]["Country_list"]).count("China")
    UAE_flag = (players_travel[id]["Country_list"]).count("United Arab Emirates")
    SA_flag = (players_travel[id]["Country_list"]).count("South Africa")

    cur_leaderboard.execute(f'UPDATE Leaderboard SET Mexico = {Mexico_flag}, Cayman_Islands = {Cayman_flag}, Canada = {Canada_flag}, Hawaii = {Hawaii_flag}, United_Kingdom = {UK_flag}, Argentina = {Argentina_flag}, Switzerland = {Switzerland_flag}, Japan = {Japan_flag}, China = {China_flag}, United_Arab_Emirates = {UAE_flag}, South_Africa = {SA_flag} WHERE Torn_ID == {id}')
    con_leaderboard.commit()


cur_players.close()
con_players.close()

cur_leaderboard.close()
con_leaderboard.close()
