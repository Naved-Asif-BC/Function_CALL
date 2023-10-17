from dotenv import load_dotenv
import os
import base64
from requests import post,get
import json
import random

#Loading the local environment variable 
load_dotenv()
#loading key for client_id
client_id=os.getenv("CLIENT_ID")
#loading key for client secret
client_secret=os.getenv("CLIENT_SECRET")

artist_list = [
   'Arijit Singh'
]
#removing duplicates from the artist_list
artists_unique = list(set(artist_list))

# Function to get an access token from Spotify API
def get_token():
    auth_string=client_id+ ":" + client_secret
    auth_bytes=auth_string.encode("utf-8")
    auth_base64=str(base64.b64encode(auth_bytes),"utf-8")

    url="https://accounts.spotify.com/api/token"
    headers={
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data={"grant_type": "client_credentials"}
    result =post(url,headers=headers,data=data)
    json_result=json.loads(result.content)
    token= json_result["access_token"]
    return token

# Function to generate the authorization header for API requests
def get_auth_header(token):
    return {"Authorization": "Bearer "+ token}
# Function to search for an artist id using the Spotify API
def search_for_artist(token,artist_name):
    url="https://api.spotify.com/v1/search"
    headers=get_auth_header(token)
    query=f"?q={artist_name}&type=artist&limit=1"

    query_url=url+query
    result=get(query_url,headers=headers)
    json_result=json.loads(result.content)["artists"]["items"]
    if len(json_result)==0:
        print("No artist with that name")
        return None
    
    return json_result[0]
# Function to get the top tracks of an artist using the Spotify API
def get_songs_by_artist(token,artist_id):
    url=f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers=get_auth_header(token)
    result=get(url,headers=headers)
    json_result=json.loads(result.content)["tracks"]
    print(json_result)
    print("-------------------------------------------------------------------")
    return json_result

tracks=[] # List to store the track data
num=1  # Counter for track number

# Loop through each unique artist
for i in artists_unique:
    token=get_token()   # Get an access token
    result=search_for_artist(token,i)  # Search for the artist
    artist_id=result["id"]  
    songs=get_songs_by_artist(token, artist_id)  # Get the artist's top tracks
    
    
    # Iterate over each track and extract relevant information
    for item in songs:
        music_genres = ["Pop", "Rock", "Hip Hop", "R&B", "Classical","Classical","Romantic"]
        track = {}
        track["S.No."]=num
        track['ID']= item['album']['id']
        track['Title'] = item['name']
        track['Artists'] = ', '.join([artist['name'] for artist in item['artists']])
        track['Album'] = item['album']['name']
        track['Release Date'] = item['album']['release_date']
        track['Duration'] = item['duration_s'] / 1000  # Convert milliseconds to seconds
        track['Popularity'] = item['popularity']
        track['Genre'] = random.choice(music_genres)
        num=num+1
        tracks.append(track)

# Writing data to CSV file
filename = 'Spotify_Data.csv'
fields = ['S.No.','ID','Title', 'Artists', 'Album', 'Release Date', 'Duration', 'Popularity','Genre']

import csv
with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(tracks)
    
print("CSV file created successfully.")


#for idx, song in enumerate(songs):
#    print(f"{idx+1}. {song['name']}")
