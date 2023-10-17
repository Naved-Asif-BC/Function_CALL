#you need to generate a youtube data api key to use this code


from googleapiclient.discovery import build
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Loading API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")

# Build YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# List of channel IDs
channel_ids = []

# Function to get channel stats
def get_channel_stats(youtube, channel_id):
    all_data = []
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=','.join(channel_ids)
    )
    response = request.execute()
    for i in range(len(response['items'])):
        data = dict(
            Channel_name=response['items'][i]['snippet']['title'],
            Subscribers=response['items'][i]['statistics']['subscriberCount'],
            Views=response['items'][i]['statistics']['viewCount'],
            Total_videos=response['items'][i]['statistics']['videoCount'],
            playlist_id=response['items'][i]['contentDetails']['relatedPlaylists']['uploads']
        )
        all_data.append(data)
    return all_data

# Get channel stats
channel_stats = get_channel_stats(youtube, channel_id)

# Create DataFrame from channel stats
channel_data = pd.DataFrame(channel_stats)

# Get the playlist ID for a specific channel (e.g., 'Drake')
playlist_id = channel_data.loc[channel_data['Channel_name'] == 'Drake', 'playlist_id'].iloc[0]

# Function to get video IDs from a playlist
def get_video_ids(youtube, playlist_id):
    request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50
    )
    response = request.execute()
    video_ids = []
    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])
    next_page_token = response.get('nextPageToken')
    more_pages = True

    while more_pages:
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )
            response = request.execute()
            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
            next_page_token = response.get('nextPageToken')

    return video_ids

# Get video IDs from the playlist
video_ids = get_video_ids(youtube, playlist_id)

# Function to get details of each video
def get_video_details(youtube, video_ids):
    all_video_stats = []
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part='snippet,statistics',
            id=','.join(video_ids[:50])
        )
        response = request.execute()
        for video in response['items']:
            video_stats = dict(
                Title=video['snippet']['title'],
                Published_date=video['snippet']['publishedAt'],
                Views=video['statistics']['viewCount'],
                Likes=video['statistics']['likeCount'],
                Comments=video['statistics']['commentCount']
            )
            all_video_stats.append(video_stats)
    return all_video_stats

# Get details of each video
video_details = get_video_details(youtube, video_ids)

# Create DataFrame from video details
video_data = pd.DataFrame(video_details)

# Save video data to a CSV file
video_data.to_csv('Youtube_data.csv')
