from app import app
from flask import render_template, session
import requests

@app.route("/")
def index():
    list_people=[]
    list_person = []
    token = session["token"]
    url = 'https://api.vk.com/method/friends.get?fields=sex&access_token={}&v=5.126'.format(token)
    response = requests.get(url)
    count_friends = response.json()['response']['count']
    for item in range(count_friends):
        friend = response.json()['response']['items'][item]
        list_people.append(friend)

    
    
    return render_template('index.html', list_name = list_people)