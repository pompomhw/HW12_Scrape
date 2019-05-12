from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_to_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
mongo.db.test.drop()

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    A = mongo.db.test
    B= A.find_one()
    # B = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", B=B)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    A = mongo.db.test
    mars_data = scrape_to_mars.collect_info()
    # mars.update
    A.update({}, mars_data, upsert=True)
    # redirect back to the home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
