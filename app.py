import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'podcasts'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_landing')
def get_landing():
    return render_template("landing.html",
                           podcasts=mongo.db.podcasts.find())


@app.route('/get_manage')
def get_manage():
    return render_template("manage.html",
                           podcasts=mongo.db.podcasts.find())


@app.route('/get_contact')
def get_contact():
    return render_template("contact.html",
                           podcasts=mongo.db.podcasts.find())


@app.route('/get_sent')
def get_sent():
    return render_template("form_sent.html",
                           podcasts=mongo.db.podcasts.find())


@app.route('/delete_podcast/<podcast_id>')
def get_delete(podcast_id):
    mongo.db.podcasts.remove({'_id': ObjectId(podcast_id)})
    return redirect(url_for('get_manage'))


@app.route('/get_add')
def get_add():
    return render_template("add.html",
                           podcasts=mongo.db.podcasts.find())


@app.route('/get_gatekeeper')
def get_gatekeeper():
    return render_template("gatekeeper.html",
                           podcasts=mongo.db.podcasts.find())


@app.route('/insert_podcast', methods=['POST'])
def insert_podcast():
    podcasts = mongo.db.podcasts
    podcasts.insert_one(request.form.to_dict())
    return redirect(url_for('get_manage'))


@app.route('/edit_podcast/<podcast_id>')
def get_edit(podcast_id):
    the_podcast = mongo.db.podcasts.find_one({"_id": ObjectId(podcast_id)})
    all_podcasts = mongo.db.podcasts.find()
    return render_template('edit.html', podcast=the_podcast,
                           categories=all_podcasts)


@app.route('/update_podcast/<podcast_id>', methods=["POST"])
def get_update(podcast_id):
    podcasts = mongo.db.podcasts
    podcasts.update({'_id': ObjectId(podcast_id)},
                    {
        'podcast_name': request.form.get('podcast_name'),
        'podcast_description': request.form.get('podcast_description'),
        'podcast_image': request.form.get('podcast_image'),
        'podcast_website': request.form.get('podcast_website'),
    })
    return redirect(url_for('get_manage'))


@app.route('/podcast_details/<podcast_id>')
def get_details(podcast_id):
    the_podcast = mongo.db.podcasts.find_one({'_id': ObjectId(podcast_id)})
    return render_template("podcast_details.html", podcast=the_podcast)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
