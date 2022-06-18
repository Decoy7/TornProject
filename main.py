from flask import Flask, render_template, request
from json import load
import sqlite3


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dwaskdhygwkasdjlkasgfdebhjqsja'

    @app.route("/abroad")
    @app.route("/")
    def abroad():
        try:
            abroad_file = open(
                "/home/michael/repos/python/TornFlightListChecker/abroad_ok.json")
            hosp_file = open(
                "/home/michael/repos/python/TornFlightListChecker/abroad_hospital.json")
            hosp = load(hosp_file)
            hosp_file.close()
            abroad = load(abroad_file)
            abroad_file.close()
            return render_template("abroad.html", abroad=abroad, hosp=hosp)
        except:
            return render_template("404.html"), 404

    @app.route("/travelling")
    def travelling():
        try:
            travelling_file = open(
                "/home/michael/repos/python/TornFlightListChecker/travelling.json")
            travelling = load(travelling_file)
            travelling_file.close()
            return render_template("travelling.html", travelling=travelling)
        except:
            return render_template("404.html"), 404

    @app.route("/returning")
    def returning():
        try:
            returning_file = open(
                "/home/michael/repos/python/TornFlightListChecker/returning.json")
            returning = load(returning_file)
            returning_file.close()
            return render_template("returning.html", returning=returning)
        except:
            return render_template("404.html"), 404

    # @app.route("/leaderboard")
    # def leaderboard():
    #     con = sqlite3.connect("/home/michael/repos/python/TornDatabase/players.db")
    #     cur = con.cursor()
    #     resp = cur.execute('SELECT * FROM Torn').fetchall()
    #     con.close()
    #     p_id = []
    #     p_name = []
    #     p_status = []
    #     p_country = []
    #     p_timestamp = []
    #     for item in resp:
    #         p_id.append(item[0])
    #         p_name.append(item[1])
    #         p_status.append(item[2])
    #         p_country.append(item[3])
    #         p_timestamp.append(item[4])
    #     length = len(p_id)
    #     return render_template("leaderboard.html", resp=resp, p_id=p_id, p_name=p_name, p_status=p_status, p_country=p_country, p_timestamp=p_timestamp, length=length)

    @app.route("/leaderboard", methods=["GET", "POST"])
    def leaderboard():
        if request.method == "POST":
            user = str(request.form["torn_id"])
            con = sqlite3.connect(
                "/home/michael/repos/python/TornDatabase/players.db")
            cur = con.cursor()
            resp = cur.execute(f'SELECT * FROM Torn WHERE Torn_ID == "{user}";').fetchall()
            p_id = []
            p_name = []
            p_status = []
            p_country = []
            p_timestamp = []
            for item in resp:
                p_id.append(item[0])
                p_name.append(item[1])
                p_status.append(item[2])
                p_country.append(item[3])
                p_timestamp.append(item[4])
            length = len(p_id)
            con.close()
            return render_template("leaderboard.html", p_id=p_id, p_name=p_name, p_status=p_status, p_country=p_country, p_timestamp=p_timestamp, length=length)
        else:
            return render_template("leaderboard.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    return app