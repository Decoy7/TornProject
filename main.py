from crypt import methods
from flask import Flask, render_template, request, send_file
from json import load
import sqlite3
from os.path import getsize


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = ""

    @app.route("/abroad")
    @app.route("/")
    def abroad():
        try:
            abroad_file = open("/home/michael/repos/python/TornFlightListChecker/abroad_ok.json")
            hosp_file = open("/home/michael/repos/python/TornFlightListChecker/abroad_hospital.json")
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
            travelling_file = open("/home/michael/repos/python/TornFlightListChecker/travelling.json")
            travelling = load(travelling_file)
            travelling_file.close()
            return render_template("travelling.html", travelling=travelling)
        except:
            return render_template("404.html"), 404

    @app.route("/returning")
    def returning():
        try:
            returning_file = open("/home/michael/repos/python/TornFlightListChecker/returning.json")
            returning = load(returning_file)
            returning_file.close()
            return render_template("returning.html", returning=returning)
        except:
            return render_template("404.html"), 404

    @app.route("/leaderboard", methods=["GET", "POST"])
    def leaderboard():
        if request.method == "POST":
            user = str(request.form["torn_id"])
            con = sqlite3.connect("/home/michael/repos/python/TornDatabase/players.db")
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
        elif request.method == "GET":
            con = sqlite3.connect("/home/michael/repos/python/TornDatabase/leaderboard.db")
            cur = con.cursor()

            multiple_choice = cur.execute('SELECT * FROM Leaderboard').fetchall()

            ids = []
            names = []
            mexico = []
            canada = []
            hawaii = []
            uk = []
            argentina = []
            switzerland = []
            china = []
            japan = []
            uae = []
            sa = []
            ci = []

            for item in multiple_choice:
                ids.append(item[0])
                names.append(item[1])
                mexico.append(item[2])
                canada.append(item[3])
                hawaii.append(item[4])
                uk.append(item[5])
                argentina.append(item[6])
                switzerland.append(item[7])
                china.append(item[8])
                japan.append(item[9])
                uae.append(item[10])
                sa.append(item[11])
                ci.append(item[12])


            length = len(ids)

            con.close()
            return render_template("leaderboard_multiple.html", ids=ids, names=names, length=length, mexico=mexico, canada=canada, hawaii=hawaii, uk=uk, argentina=argentina, switzerland=switzerland, china=china, japan=japan, uae=uae, sa=sa, ci=ci)


    @app.route("/about")
    def about():
        size = getsize("/home/michael/repos/python/TornDatabase/players.db")
        return render_template("about.html", size=round(size/1024/1024, 2))

    @app.route("/database")
    def download():
        path = r"/home/michael/repos/python/TornDatabase/players.db"
        return send_file(path, as_attachment=True)

    return app
