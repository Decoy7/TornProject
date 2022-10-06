from flask import Flask, render_template, request, send_file
import sqlite3
from os.path import getsize


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "" #Your secret key heres

    con_torn = sqlite3.connect("/home/michael/repos/python/TornProject/API/players.db")
    cur_torn = con_torn.cursor()

    con_leaderboard = sqlite3.connect("/home/michael/repos/python/TornProject/API/leaderboard.db")
    cur_leaderboard = con_leaderboard.cursor()

    @app.route("/abroad")
    @app.route("/")
    def abroad():
        try:
            names = []
            status = []
            resp = cur_torn.execute(f'SELECT Name,Status FROM Abroad;').fetchall()
            time = cur_torn.execute(f'SELECT Timestamp FROM Torn ORDER BY ROWID DESC LIMIT 1;').fetchall() #GET LATEST RECORD FOR (SINCE LATEST UPDATE)
            for item in resp:
                names.append(item[0])
                status.append(item[1])
            length = len(names)
            return render_template("abroad.html", names=names, status=status, length=length, time=time)
        except:
            return render_template("404.html"), 404

    @app.route("/travelling")
    def travelling():
        try:
            names = []
            status = []
            resp = cur_torn.execute(f'SELECT Name,Status FROM Traveling;').fetchall()
            time = cur_torn.execute(f'SELECT Timestamp FROM Torn ORDER BY ROWID DESC LIMIT 1;').fetchall()
            for item in resp:
                names.append(item[0])
                status.append(item[1])
            length = len(names)
            return render_template("travelling.html", names=names, status=status, length=length, time=time)
        except:
            return render_template("404.html"), 404

    @app.route("/returning")
    def returning():
        try:
            names = []
            status = []
            resp = cur_torn.execute(f'SELECT Name,Status FROM Returning;').fetchall()
            time = cur_torn.execute(f'SELECT Timestamp FROM Torn ORDER BY ROWID DESC LIMIT 1;').fetchall()
            for item in resp:
                names.append(item[0])
                status.append(item[1])
            length = len(names)

            return render_template("returning.html", names=names, status=status, length=length, time=time)
        except:
            return render_template("404.html"), 404

    @app.route("/leaderboard", methods=["GET", "POST"])
    def leaderboard():
        if request.method == "POST":
            user = str(request.form["torn_id"])

            resp = cur_leaderboard.execute(f'SELECT * FROM Leaderboard WHERE Torn_ID == "{user}";').fetchall()
            time = cur_torn.execute(f'SELECT Timestamp FROM Torn ORDER BY ROWID DESC LIMIT 1;').fetchall()

            p_id = resp[0][0]
            p_name = resp[0][1]
            p_mexico = resp[0][2]
            p_canada = resp[0][3]
            p_hawaii = resp[0][4]
            p_uk = resp[0][5]
            p_argentina = resp[0][6]
            p_switzerland = resp[0][7]
            p_china = resp[0][8]
            p_japan = resp[0][9]
            p_uae = resp[0][10]
            p_sa = resp[0][11]
            p_ci = resp[0][12]

            return render_template("leaderboard.html", p_id=p_id, p_name=p_name, p_mexico=p_mexico, p_canada=p_canada, p_hawaii=p_hawaii, p_uk=p_uk, p_argentina=p_argentina, p_switzerland=p_switzerland, p_china=p_china, p_japan=p_japan, p_uae=p_uae, p_sa=p_sa, p_ci=p_ci, time=time)

        elif request.method == "GET":
            multiple_choice = cur_leaderboard.execute('SELECT * FROM Leaderboard;').fetchall()
            time = cur_torn.execute(f'SELECT Timestamp FROM Torn ORDER BY ROWID DESC LIMIT 1;').fetchall()
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

            return render_template("leaderboard_multiple.html", ids=ids, names=names, length=length, mexico=mexico, canada=canada, hawaii=hawaii, uk=uk, argentina=argentina, switzerland=switzerland, china=china, japan=japan, uae=uae, sa=sa, ci=ci, time=time)

    @app.route("/about")
    def about():
        size = getsize("/home/michael/repos/python/TornProject/API/players.db")
        time = cur_torn.execute(f'SELECT Timestamp FROM Torn ORDER BY ROWID DESC LIMIT 1;').fetchall()

        return render_template("about.html", size=round(size/1024/1024, 2), time=time)

    @app.route("/database")
    def download():
        path = r"/home/michael/repos/python/TornProject/API/players.db"

        return send_file(path, as_attachment=True)

    return app
