
from flask import Flask, render_template, redirect
import crime_web_scraping
from config import password
from flask_pymongo import PyMongo
from pymongo import MongoClient
import pymongo


app = Flask(__name__)
app.config["MONGO_URI"] = f'mongodb+srv://kitrana08:{password}@nycw-azcb7.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.route("/")
def index():
    # crime_data = crime_web_scraping.scrape()
    # mongo.db.crime.replace_one({}, crime_data, True)
    crime = mongo.db.crime.find_one()
    return render_template("index.html", crime=crime)

# Chart 
@app.route("/chart")
def chart ():
    return render_template("chart.html")

# Map
@app.route("/map")
def fullmap ():
    return render_template("map.html")

# about
@app.route("/documentation")
def about ():
    return render_template("about.html")

# news
@app.route("/news")
def news ():
    crime = mongo.db.crime.find_one()
    return render_template("news.html", crime=crime)

@app.route("/scrape")
def scrape ():
    crime_data = crime_web_scraping.scrape()
    mongo.db.crime.replace_one({}, crime_data, True)
    crime = mongo.db.crime.find_one()
    return redirect("/news")

if __name__ == "__main__":
    app.run(debug=True)
