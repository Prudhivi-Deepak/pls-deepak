# https://python-cloudant.readthedocs.io/en/stable/getting_started.html#connecting-with-a-client
from flask import Flask, render_template, flash, redirect, request, url_for, send_file, session
import datetime
import os
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

app = Flask(__name__,static_url_path='')
port = int(os.getenv('PORT', 8001))

# client = Cloudant.iam("a1c47c16-1328-46c9-9a6e-ea7970217b2a-bluemix","HmDxp6MmgMyRoIC1b5lbl21PloMdqJTcIfb6d8Z8bda9",connect=True)

client = Cloudant.iam("e9a1474d-2a68-4b11-b60c-a60c87c061a9-bluemix","oUFFwB9qB-SghbaQbaj7y7TSu7N4yS3mWrDdyYHxtjJn",connect=True)
client.connect()

def dbCreate(dbname,client):
    if dbname in client:
        db = client[dbname]
    else:
        db = client.create_database(dbname)
    return db

db = client.create_database("database1")
result = Result(db.all_docs, include_docs=True)

print(result,list(result))

print(result[0][0]['doc'])
print(result[1][0]['doc'])





print(result['doc'])

db = dbCreate('database1',client)

rating = {"eventid":"2",
					  "eventName":"eventname2",
					  "partName":"prtName2",
					  "partEmail":"partEmail2",
					  "eventDate":"eventdate2",
					  "rating" : "ratingList2",
					  "submittedDate" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
					  }
db.create_document(rating)
