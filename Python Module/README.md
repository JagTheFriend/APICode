# Complex API.py
This the source code for the python module I have built/working on.

This module makes it easy to use my <a href="https://github.com/JagTheFriend/APICode/tree/master/API"> API </a>

Currently, the API supports:
  + compiling the code(of different languages) and getting the output
  + getting a random post from a _subreddit_
  + getting the lyrics of a song
  
  + generating pixel art
  + getting the weather of a place
  + finding the length of a youtube playlist

  + getting a random inspirational text
  + getting a result of a calculation
  + converting hexadecimal to decimal(or denary)

# Code snippets
## Compile API:
<a href="https://complicated-api.herokuapp.com/compile=python_print('This works')">
  Example:
</a>

```py
import package
# run python
lang = "python"
code = '''
print('hello')
'''
print(package.compile(lang=lang, code=code))
# run java
lang = "java"
code = '''
class Compiler{
    public static void main(String[] args){
        System.out.println("This works");
    }
}
'''
print(package.compile(lang=lang, code=code))
```

<a href="https://complicated-api.herokuapp.com/compile=support_support">
  Get all the supported languages here
</a>

## Reddit API:
<a href="https://complicated-api.herokuapp.com/reddit=meme+10">
  Example:
</a>

```py
import package
# example name_of_subreddit = "meme"
name_of_subreddit = "name_of_a_valid_subreddit" 
number_of_posts = 10 # number of posts to be returned
print(package.reddit(limit=number_of_posts, subreddit=name_of_subreddit))
```

## Lyrics API:
<a href="https://complicated-api.herokuapp.com/lyrics+falling">
  Example: 
</a>

```py
import package
SongName = "name of song"
print(package.lyrics(song=SongName))
```

## Pixel Art:
<a href="https://complicated-api.herokuapp.com/ascii_hello">
  Example:
</a>

```py
import package
text = "Hello gammer"
print(package.ascii(text=text))
```

## Weather API:
<a href="https://complicated-api.herokuapp.com/temp=Cape Town">
  Example:
</a>

```py
import package
# example: place = Cape Town
place = "name of a place"
print(package.temp(place=place))
```

## Youtube Playlist length finder:
<a href="https://complicated-api.herokuapp.com/length+PL59LTecnGM1OGgddJzY-0r8vdqibi3S2H">
  Example: 
</a>

```py
import package
# example URL: https://www.youtube.com/playlist?list=PL59LTecnGM1OGgddJzY-0r8vdqibi3S2H
# id = PL59LTecnGM1OGgddJzY-0r8vdqibi3S2H
play_list_link = "id"
print(package.length(playlist=play_list_link))
```

## Calculator:
<a href="https://complicated-api.herokuapp.com/cal_6*9+6+9">
  Example: 
</a>

```py
import package
formula = "6*9+6+9" 
print(package.calculator(formula=formula))
```

## Inspire API:
<a href="https://complicated-api.herokuapp.com/inspire">
  Example: 
</a>

```py
import package
print(package.inspire())
```

## Hexadecimal to Decimal(or Denary) converter:
<a href="https://complicated-api.herokuapp.com/hex_to_denary+ABCDEF">
  Example: 
</a>

```py
import package
formula = "A6B9C1D1E1" 
print(package.hex_to_denary(hex_code=formula))
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