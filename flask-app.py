#!/usr/bin/env python

from flask import Flask, json, render_template, request
import os

#create instance of Flask app
app = Flask(__name__)

#decorator
@app.route("/")
def echo_hello():
    return "<p>Hello World!</p>"

@app.route("/nobel")
def nobel():
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))

    return render_template('index.html',data=data_json)


@app.route("/nobel/<year>")
def nobel_year(year):
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))

    data = data_json[1]
    year = request.view_args['year']

    output_data = [x for x in data if x['date']==year]
    return render_template('index.html',data=output_data)



if __name__ == "__main__":
    app.run(debug=True)