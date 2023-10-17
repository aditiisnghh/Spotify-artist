from flask import Flask, request, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set your Spotify API credentials
client_id = '01105e68ba5b423b88d43f7d83f0a878'
client_secret = '4c1ed0ecb2754a42956762fce0b854d0'

# Initialize the Spotipy client with your credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

app = Flask(__name__)

# Define the homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to search for an artist
@app.route('/search', methods=['POST'])
def search_artist():
    artist_name = request.form['artist_name']
    results = sp.search(q=artist_name, type='artist')
    artist = results['artists']['items'][0]

    # Get top tracks of the artist
    top_tracks = sp.artist_top_tracks(artist['id'], country='US')

    # Get artist's albums
    albums = sp.artist_albums(artist['id'], album_type='album')

  

    return render_template('artist.html', artist=artist, top_tracks=top_tracks['tracks'], albums=albums['items'])

if __name__ == '__main__':
    app.run(debug=True)
