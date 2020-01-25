import os
import env

from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env
app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('DATABASE')
if os.path.exists("env.py"):
    app.config["MONGO_URI"] = env.mongo_uri
    app.config['SECRET_KEY'] = env.SECRET_KEY
else:
    app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)





@app.route('/')
@app.route('/get_recipe')
def get_recipe():
    return render_template("recipe_list.html", 
                            recipe_data=mongo.db.recipe_data.find())



@app.route('/get_recipe/<recipe_id>')
def about_recipe_details(recipe_id):
    the_recipe = mongo.db.recipe_data.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe_details.html', recipe=the_recipe)


@app.route('/add_recipe')
def add_recipe():
    return render_template ('addrecipe.html', 
                            categories=mongo.db.recipe_data.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe_data = mongo.db.recipe_data
    recipe_data.insert_one(  {
        'recipe_name':request.form.get('recipe_name'),
        'authors_name':request.form.get('authors_name'),
        'recipe_image': request.form.get('recipe_image'),
        'preparation_time': request.form.get('preparation_time'),
        'cooking_time':request.form.get('cooking_time'),
        'difficulty_rating':request.form.get('difficulty_rating'),
        'ingredients':request.form.getlist('ingredient'),
        'method_steps':request.form.getlist('method_step')        
        })
        
    return redirect(url_for('get_recipe'))
















@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipe_data.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe_data = mongo.db.recipe_data
    recipe_data.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'authors_name':request.form.get('authors_name'),
        'recipe_image': request.form.get('recipe_image'),
        'preparation_time': request.form.get('preparation_time'),
        'cooking_time':request.form.get('cooking_time'),
        'difficulty_rating':request.form.get('difficulty_rating'),
        'ingredients':request.form.getlist('ingredient'),
        'method_steps':request.form.getlist('method_step'),
        'method_step_1':request.form.get('method_step_1'),
        'method_step_2':request.form.get('method_step_2'),
        'method_step_3':request.form.get('method_step_3'),
        'method_step_4':request.form.get('method_step_4'),
        'method_step_5':request.form.get('method_step_5'),
        'method_step_6':request.form.get('method_step_6'),
        'method_step_7':request.form.get('method_step_7'),
        'method_step_8':request.form.get('method_step_8'),
        'method_step_9':request.form.get('method_step_9'),
        'method_step_10':request.form.get('method_step_10'),
        'like_rating':request.form.get('like_rating')
    })
    return redirect(url_for('get_recipe'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe_data.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipe'))



@app.route('/insert_comment/<recipe_id>', methods=["POST",'GET'])
def insert_comment(recipe_id):
    comments = mongo.db.comments
    comments.insert_one({
        'comment': request.form['comment'],
        'recipe_id': ObjectId(recipe_id)
    })
    flash('Your comment has been recorded ')

    return redirect(url_for('about_recipe_details',
                    _anchor='comments-section', 
                    recipe_id=recipe_id))

   







# Error Page Section

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")


@app.errorhandler(403)
def not_found(error):
    return render_template("403.html")

@app.errorhandler(500)
def not_found(error):
    return render_template("500.html")





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=(os.environ.get('PORT')),
        debug=True)
