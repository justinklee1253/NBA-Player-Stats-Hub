import requests #imports library to help make HTTP requests (allow browsers to communicate with servers and retrieve web pages or data)

from flask import Flask, render_template, request, redirect, url_for, jsonify #from flask import 

app = Flask(__name__)

BASE_URL = "https://api.balldontlie.io/v1/stats"


player_data = {
    'lebron james': {'formatted_name': 'LeBron James', 'points': 25, 'rebounds': 8, 'assists': 7},
    'stephen curry': {'formatted_name': 'Stephen Curry', 'points': 30, 'rebounds': 5, 'assists': 6},
    'kevin durant': {'formatted_name': 'Kevin Durant', 'points': 28, 'rebounds': 7, 'assists': 5},
}

@app.route('/')
def index():
    return render_template('index.html') #renders the index.html file and returns it as a response to the client. 

@app.route('/search', methods=['POST'])
def search():
    player_name = request.form['player_name'].lower() #retrieves data submitted from an HTML form --> called player_name in this case(value entered by user) in the input from HTML file
    if player_name in player_data: #check if the name that the user entered is in the player_data dictionary
        return redirect(url_for('player_stats', player_name=player_name)) #url_for generates a dynamic URL for the player_stats endpoint by replacing <player_name> in route with player_name variable
        #^ redirects client to the url we generate that is specific to the player. 
    else:
        return "Player not found", 404 #if player not found we print error message 

@app.route('/player_stats/<player_name>') #this function determines what gets displayed when a player is found, and the URL is generated. 
def player_stats(player_name):
    stats = player_data.get(player_name) #gets relevant player data from player_data dictionary 
    formatted_name = stats['formatted_name']
    return render_template('player_stats.html', player_name=formatted_name, stats=stats)

if __name__ == '__main__':
    app.run(debug=True)



