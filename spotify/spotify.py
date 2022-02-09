import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import mysql.connector
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import tokenauth



##
user = 'admin'
password = ''
host = ''
database = ''
port = ''
USER_ID = ""
TOKEN = tokenauth.token


def check_if_valid_data(df: pd.DataFrame): 
    if df.empty:
        print("No songs downloaded. Finishing execution")
        return False 

    # Primary Key Check
    if pd.Series(df['played_at']).is_unique:
        pass
    else:
        raise Exception("Primary Key check is violated")

    #Check for null values
    if df.isnull().values.any():
        raise Exception("Null value found")

    #Check that all times are of 24hrs ago
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)


    return True

## Database are split in to Relational and Nonrelational Databases
    ## SQL, POSTGRESQL 
    ##MongoDB or DYNAMO DB - json docs

##ORM - object relational mappers



if __name__ == "__main__":
    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token = TOKEN)

    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)

    data = r.json()

    song_titles = []
    artists = []
    played_at_list = [] 
    timestamps = []

    for song in data["items"]:
        song_titles.append(song["track"]["name"])
        artists.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    song_dict = {
        "songs" : song_titles,
        "artists" : artists,
        "played_at" : played_at_list,
        "timestamps" : timestamps
    }
    
    song_df = pd.DataFrame(song_dict, columns = ["songs", "artists", "played_at", "timestamps"])

    #Validate data
    if check_if_valid_data(song_df):
        print("Data is valid, proceed to Load stage")

    
    #Load
    conn = mysql.connector.connect(database='', host=host, user = user, password=password)
    cursor = conn.cursor()


    sql = """
        CREATE TABLE database_name (
            songs VARCHAR(200),
            artists VARCHAR(200),
            played_at VARCHAR(200),
            timestamps VARCHAR(200),
            CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
        )
    """
    
    cursor.execute(sql)
    print("Opened database successfully")

    conn.commit()

    conn.close()
    print("Closed successfully")