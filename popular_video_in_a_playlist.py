from googleapiclient.discovery import build
import os

# loading the api token
api_key = os.environ.get('yt_token')
youtube = build('youtube', 'v3', developerKey=api_key)

youtube = build('youtube', 'v3', developerKey=api_key)
videos = []  # view count and the link,could be a dictionary
playlist = "PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS"

nextPageToken = None
while True:
    # to get play list
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist,
        maxResults=50,
        pageToken=nextPageToken
    )

    pl_response = pl_request.execute()
    # to store vids of the play list
    vid_ids = []
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    # to get likes etc of the vid
    vid_request = youtube.videos().list(
        part="statistics",
        id=','.join(vid_ids)
    )

    vid_response = vid_request.execute()

    # using the stat of the vid
    for item in vid_response['items']:
        vid_view = item['statistics']['viewCount']  # to get the view count

        vid_id = item['id']
        yt_link = f'https://youtu.be/{vid_id}'

        videos.append(
            # adding videos view and url as a dictionary
            {
                'views': int(vid_view),
                'url': yt_link
            }
        )

    nextPageToken = pl_response.get('nextPageToken')

    # check whether there is another page
    if not nextPageToken:   # each page has 50 vid
        break

# sorting the vid according the view, highest to lowest
# sorting the list according to views
videos.sort(key=lambda vid: vid['views'], reverse=True)

# showing the top ten vid
print("Link:                        Views:\n")
for video in videos[:10]:
    print(video['url'], video['views'])  # to access url and views
