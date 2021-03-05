# API Code
This the source code for the API I have built/working on

For Now,
This API supports:

  + compiling the code(of different languages) and getting the output
  + getting the lyrics of a song
  + getting a random post from a _subreddit_

# Code snippets
## Compile API:
<a href="https://apis.theunkowncoder.repl.co/compile=support+support">
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
print(r.get(f"{URL}/compile={lang}+{code}").text)

# run java
lang = "java"
code = '''
class Compiler{
    public static void main(String[] args){
        System.out.println("This must work");
    }
}
'''
print(r.get(f"{URL}/compile={lang}+{code}").text)

# run javascript
lang = "js"
code = '''
console.log("Hi")
'''
print(r.get(f"{URL}/compile={lang}+{code}").text)
```
<a href="https://apis.theunkowncoder.repl.co/compile=support+support">
  Get all the supported languages here
</a>

## Lyrics API:
<a href="https://apis.theunkowncoder.repl.co/lyrics=falling">
  Example: 
</a>

```py
import requests as r

URL = "https://apis.theunkowncoder.repl.co"
SongName = "name_of_song"
print(f"{URL}/lyrics={SongName}")
```
## Reddit API:
Example:
```py
import requests as r

URL = "https://apis.theunkowncoder.repl.co"
name_of_subreddit = "name_of_a_valid_subreddit"
number_of_posts = 10 # number of posts to be retuned
print(f"{URL}/reddit={name_of_subreddit}+{number_of_posts}")
```
<a href="https://apis.theunkowncoder.repl.co/reddit=meme+10">
  Demo:
</a>

```py
import requests as r

URL = "https://apis.theunkowncoder.repl.co"
name_of_subreddit = "meme"
number_of_posts = 10
print(f"{URL}/reddit={name_of_subreddit}+{number_of_posts}")
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
