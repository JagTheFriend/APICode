# API Code
This the source code for the API I have built/working on

For Now, <br>
This API supports:

  + compiling the code(of different languages) and getting the output
  + getting the lyrics of a song
  + getting a random post from a _subreddit_
  + finding the length of a youtube playlist

# Code snippets
## Compile API:
<a href="https://apis.theunkowncoder.repl.co/compile_support_support">
  Example:
</a>

```py
import requests as r

URL = "https://apis.theunkowncoder.repl.co"

# run python
lang = "python"
code = '''
print('hello')
'''
print(r.get(f"{URL}/compile_{lang}_{code}").text)

# run java
lang = "java"
code = '''
class Compiler{
    public static void main(String[] args){
        System.out.println("This must work");
    }
}
'''
print(r.get(f"{URL}/compile_{lang}_{code}").text)

# run javascript
lang = "js"
code = '''
console.log("Hi")
'''
print(r.get(f"{URL}/compile_{lang}_{code}").text)
```
<a href="https://apis.theunkowncoder.repl.co/compile_support_support">
  Get all the supported languages here
</a>

## Lyrics API:
<a href="https://apis.theunkowncoder.repl.co/lyrics_falling">
  Example: 
</a>

```py
import requests as r

URL = "https://apis.theunkowncoder.repl.co"
SongName = "name_of_song"
print(f"{URL}/lyrics_{SongName}")
```
## Reddit API:
Example:
```py
import requests as r

URL = "https://apis.theunkowncoder.repl.co"
name_of_subreddit = "name_of_a_valid_subreddit"
number_of_posts = 10 # number of posts to be retuned
print(f"{URL}/reddit_{name_of_subreddit}_{number_of_posts}")
```
<a href="https://apis.theunkowncoder.repl.co/reddit_meme_10">
  Demo:
</a>

```py
import requests as r

URL = "https://apis.theunkowncoder.repl.co"
name_of_subreddit = "meme"
number_of_posts = 10
print(f"{URL}/reddit_{name_of_subreddit}_{number_of_posts}")
```
## Youtube Playlist length finder API:
<a href="https://apis.theunkowncoder.repl.co/playlist_PL59LTecnGM1OGgddJzY-0r8vdqibi3S2H">
  Example: 
</a>

```py
import requests as r

URL = "https://apis.theunkowncoder.repl.co"
# example URL: https://www.youtube.com/playlist?list=PL59LTecnGM1OGgddJzY-0r8vdqibi3S2H
# id = PL59LTecnGM1OGgddJzY-0r8vdqibi3S2H
play_list_link = "id"
print(f"{URL}/playlist_{play_list_link}")
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
