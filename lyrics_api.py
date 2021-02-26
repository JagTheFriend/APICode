import os
from lyrics_extractor import SongLyrics

def song_lyrics(song):
    """Gets the lyrics of a song

    :param song: Name of the song

    :return: Python dictionary"""
    
    if song:
        extract_lyrics = SongLyrics(os.environ.get(
            "lyrics_token"), os.environ.get("GCS_ENGINE_ID")
        )

        lyrics = extract_lyrics.get_lyrics(" ".join(song)).get("lyrics", "No lyrics was found")
        return {"output": lyrics}

    return {"output": "Also please send the name of the song"}
