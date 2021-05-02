import os
from flask import Flask, redirect, url_for, render_template, request
import updater
import datetime as dt
import time


def find_path():
    paths = (r'C:\Users\Gabriel Freundt\Google Drive\Multi-Sync\sharedData',r"D:\Google Drive Backup\Multi-Sync\sharedData", r"C:\users\gfreu\Google Drive\Multi-Sync\sharedData")
    for path in paths:
        if os.path.exists(path):
            return path

main_path = find_path()
DATA_PATH = os.path.join(main_path, 'data')
HTML_PATH = os.path.join(main_path, 'templates')
CSS_PATH = os.path.join(main_path, 'static')

print(HTML_PATH)


app = Flask(__name__, template_folder=HTML_PATH, static_folder=CSS_PATH)

@app.route("/dog")
def index():
	with open(os.path.join(DATA_PATH, 'TDC_fixed.txt'), mode='r') as file:
		latest = [i for i in file.readlines()]
		return render_template('index.html', latest=latest)

#return render_template("dashboard.html", date=date, time=time, data=data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


#D:\Google Drive Backup\Multi-Sync\sharedData\templates