import os
import re
from datetime import timedelta
from googleapiclient.discovery import build

api_key = os.environ.get('yt_token')

youtube = build('youtube', 'v3', developerKey=api_key)

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')


def main(playlist_id: str) -> dict:
    """
    This function returns the time it would take to
    watch an entire playlist, from the start to end

    Arguments:
        @playlist_id => This a unique id given to each playlist

    :return: Python Dictionary
    """
    playlist_id = playlist_id.split("=")[1]
    total_seconds = 0
    next_page_token = None
    while True:
        pl_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )

        pl_response = pl_request.execute()

        vid_ids = []
        for item in pl_response['items']:
            vid_ids.append(item['contentDetails']['videoId'])

        vid_request = youtube.videos().list(
            part="contentDetails",
            id=','.join(vid_ids)
        )

        vid_response = vid_request.execute()

        for item in vid_response['items']:
            duration = item['contentDetails']['duration']

            hours = hours_pattern.search(duration)
            minutes = minutes_pattern.search(duration)
            seconds = seconds_pattern.search(duration)

            hours = int(hours.group(1)) if hours else 0
            minutes = int(minutes.group(1)) if minutes else 0
            seconds = int(seconds.group(1)) if seconds else 0

            video_seconds = timedelta(
                hours=hours,
                minutes=minutes,
                seconds=seconds
            ).total_seconds()

            total_seconds += video_seconds

        next_page_token = pl_response.get('nextPageToken')

        if not next_page_token:
            break

    total_seconds = int(total_seconds)

    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return {"output": f'{hours} hour(s):{minutes} minute(s):{seconds} second(s)'}


if __name__ == '__main__':
    playlistId = "PLYMreygRONRAYHAfALESBgZJpftQQWSjz"  # a yt playlist
    print(main(playlistId))
