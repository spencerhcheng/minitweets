#!/usr/bin/python3
from app import app
from flask import render_template, redirect
from forms import PostForm, NameForm
import json
import os.path
import os

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():
    tweet = {}
    form = PostForm()
    name = NameForm()

    tweetText = form.post.data
    userName = name.name.data

    if tweetText != "":
        tweet[userName] = tweetText
        if (os.path.exists('./file.json')):
            with open('./file.json', 'r') as fr:
                data = json.load(fr)
            data.append(tweet)
            with open('./file.json', "w") as fw:
                f = json.dumps(data)
                fw.write(f)
        else:
            print("File doesn't exist!")
            with open('./file.json', "w+") as f:
                json.dump([], f)
    else:
        pass

    with open('./file.json', 'r') as fr:
        posts  = json.load(fr)

    posts = reversed(posts)

    print(posts)
    return render_template('index.html', title='Twitter Clone', name=name, form=form, posts=posts)


if __name__ == "__main__":
	app.run(host='0.0.0.0')
