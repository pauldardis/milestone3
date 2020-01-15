import os
import env

from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env
app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('DATABASE')
if os.path.exists("env.py"):
    app.config["MONGO_URI"] = env.mongo_uri
else:
    app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipe')
def get_tasks():
    return render_template("recipe_list.html", 
                            recipe_data=mongo.db.recipe_data.find())

@app.route('/get_recipe/<recipe_id>')
def about_recipe_details(recipe_id):
    the_recipe = mongo.db.recipe_data.find_one({"_id: ObjectID":(recipe_id)})
    return render_template('recipe_details.html', recipe=the_recipe)


    for obj in data:
        if obj["url"] == _id:
            name1 = obj
    return render_template("recipe_details.html",  recipe_data=mongo.db.recipe_data.find())






if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=(os.environ.get('PORT')),
        debug=True)
