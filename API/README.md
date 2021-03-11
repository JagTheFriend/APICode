# API Code
This the source code for the API I have built/working on

For Now, <br>
This API supports:

  + compiling the code(of different languages) and getting the output
  + getting a random post from a _subreddit_
  + getting the lyrics of a song
  + generating Ascii
  + getting the weather of a place
  + finding the length of a youtube playlist

# Code snippets
## Compile API:
<a href="https://complicated-api.herokuapp.com/compile=python_print('This works')">
  Example:
</a>

```py
import requests

URL = "https://complicated-api.herokuapp.com"

# run python
lang = "python"
code = '''
print('hello')
'''
print(requests.get(f"{URL}/compile+{lang}_{code}").json())

# run java
lang = "java"
code = '''
class Compiler{
    public static void main(String[] args){
        System.out.println("This works");
    }
}
'''
print(requests.get(f"{URL}/compile={lang}_{code}").json())
```

<a href="https://complicated-api.herokuapp.com/compile=support_support">
  Get all the supported languages here
</a>

## Reddit API:
<a href="https://complicated-api.herokuapp.com/reddit=meme+10">
  Example:
</a>

```py
import requests

URL = "https://complicated-api.herokuapp.com"
# example name_of_subreddit = "meme"
name_of_subreddit = "name_of_a_valid_subreddit" 
number_of_posts = 10 # number of posts to be returned
print(requests.get(f"{URL}/reddit={name_of_subreddit}+{number_of_posts}").json())
```

## Lyrics API:
<a href="https://complicated-api.herokuapp.com/lyrics+falling">
  Example: 
</a>

```py
import requests

URL = "https://complicated-api.herokuapp.com"
SongName = "name of song"
print(requests.get(f"{URL}/lyrics+{SongName}").json())
```

## Ascii Art API:
<a href="https://complicated-api.herokuapp.com/ascii_hello">
  Example:
</a>

```py
import requests

URL = "https://complicated-api.herokuapp.com"
text = "Hello gammer"
print(requests.get(f"{URL}/ascii_{text}").json())
```

## Weather API:
<a href="https://complicated-api.herokuapp.com/temp+Cape Town">
  Example:
</a>

```py
import requests

URL = "https://complicated-api.herokuapp.com"
# example: place = Cape Town
place = "name of a place"
print(requests.get(f"{URL}/temp+{text}").json())
```

## Youtube Playlist length finder API:
<a href="https://complicated-api.herokuapp.com/playlist+PL59LTecnGM1OGgddJzY-0r8vdqibi3S2H">
  Example: 
</a>

```py
import requests

URL = "https://complicated-api.herokuapp.com"
# example URL: https://www.youtube.com/playlist?list=PL59LTecnGM1OGgddJzY-0r8vdqibi3S2H
# id = PL59LTecnGM1OGgddJzY-0r8vdqibi3S2H
play_list_link = "id"
print(requests.get(f"{URL}/playlist+{play_list_link}").json())
```

If you find any bugs _or have new ideas_, <br> 
Feel free to raise a 
  <a href="https://github.com/JagTheFriend/APICode/issues"> 
    new issue 
  </a> <br>
Or a
  <a href="https://github.com/JagTheFriend/APICode/pulls">
    pull request
  </a>
