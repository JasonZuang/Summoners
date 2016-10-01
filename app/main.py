#! /usr/bin/python
import json
from flask import Flask,request,render_template
import requests
from Riot import RiotAPI



app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
	api = RiotAPI('RGAPI-9F0BFC59-A908-4A21-8032-901C0E8AFB31')
	r = api.get_stats_by_name(text)
	Name = api.get_summoner_by_name(text)
	print('text:  '+text)
	print r
	n = Name[text]
	sName = n['name']
	statsid = n['id']
	stats = r[str(statsid)]
	tier = (stats[0])['tier']
	divisionn = (stats[0])['name']
	division = (((stats[0])['entries'])[0])['division']
	wins = (((stats[0])['entries'])[0])['wins']
	losses = (((stats[0])['entries'])[0])['losses']
	return render_template("index.html",SNAME = sName,TIER = tier, DIVISIONN = divisionn, RWINS = wins, RLOSS = losses,DIVISION = division)

if __name__ == '__main__':
	app.run()
	
