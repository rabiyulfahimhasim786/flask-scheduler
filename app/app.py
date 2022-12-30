#from flask import Flask
import time
import atexit
from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
import requests
app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    return 'Hello World from Python Flask!'


@app.route("/ssl", methods =["GET", "POST"])
def sslchecker():
  #if request.method == "GET":
    #if True:
  requests.get("https://hrfcreation.blogspot.com/")
  print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))#time.strftime convert a time string to tuple 
  return "Welcome Home :) !"

@app.route("/ssl", methods =["GET", "POST"])
def statuscodechecker():
  #if request.method == "GET":
    #if True:
  requests.get("https://hrfcreation.blogspot.com/")
  print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))#time.strftime convert a time string to tuple 
  return "Welcome Home :) !"


scheduler = BackgroundScheduler()
scheduler.add_job(func=sslchecker, trigger="interval", seconds=5)#seconds=60)#minutes=13# hours=11
scheduler.add_job(func=sslchecker, trigger="interval", hours=12)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

app.run(host='0.0.0.0', port=5000)