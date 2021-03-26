################################################################################
# Copyright (c) 2021 JagTheFriend
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################

# NECESSARY IMPORTS
from unittest import TestCase
import requests
import time

# LOCAL HOST
URL = "http://127.0.0.1:5000/"

# Calculator API
formula = "6*9+6+9"
Expected = "69"

# Hexadecimal To Denary
formula_hex = "123ABCDEF"
Expected_hex = "4893429231"

# Compiler
Compile_Tests = {
    "python": {"code": 'print("python")', "output": 'python'},
    "java": {"code": 'class Java{\n\tpublic static void main(String[] works){\n\t\tSystem.out.println("java");\n\t}\n}\n', "output": 'java'},
    "js": {"code": "console.log('JavaScript')", "output": 'JavaScript'}
}

# Pixel Art
Input = "hello"
Expected_art = " _            _  _        \n| |__    ___ | || |  ___  \n| '_ \\  / _ \\| || | / _ \\ \n| | | ||  __/| || || (_) |\n|_| |_| \\___||_||_| \\___/ \n                          \n"

# Reddit
subreddit = "memes"
reddit_limit = 10

# Lyrics
Song_name = "Falling"
lyrics = "[Intro]\nOh\nOoh, ooh\n\n[Chorus]\nMy last made me feel like I would never try again\nBut when I saw you, I felt something I never felt\nCome closer, I'll give you all my love\nIf you treat me right, baby, I'll give you everything\nMy last made me feel like I would never try again\nBut when I saw you, I felt something I never felt\nCome closer, I'll give you all my love\nIf you treat me right, baby, I'll give you everything\n\n[Verse]\nTalk to me, I need to hear you need me like I need ya\nFall for me, I wanna know you feel how I feel for you, love\nBefore you, baby, I was numb, drown out pain by pourin' up\nSpeedin' fast on the run, never wanna get caught up\nNow you're the one that I'm callin'\nSwore I thought I'd never fall again, don't think I'm just talkin'\nI think I might go all in, no exceptions, girl, I need ya\n\n[Bridge]\nFeeling like I'm out of my mind, 'cause I can't get enough\nOnly one that I give my time, 'cause I got eyes for ya\nMight make an exception for ya, 'cause I been feelin' ya\nThink I might be out of my mind, I think that you're the one\n\n[Chorus]\nMy last made me feel like I would never try again\nBut when I saw you, I felt something I never felt\nCome closer, I'll give you all my love\nIf you treat me right, baby, I'll give you everything\nMy last made me feel like I would never try again\nBut when I saw you, I felt something I never felt\nCome closer, I'll give you all my love\nIf you treat me right, baby, I'll give you everything\n\n[Outro]\nWill never give my all again\n'Cause I'm sick of falling down\nWhen I open up and give my trust\nThey find a way to break it down\nBreak down\nTear me up inside\nWhen you break me down"

# Youtube playlist length
Length = "0 hour(s):46 minute(s):39 second(s)"
Playlist = "PLYMreygRONRAYHAfALESBgZJpftQQWSjz"

# AI
AI_WORDS = "Hello"

# home page
Main_page = "Providing service to other user(s) <br> Here is my code: <a href='https://github.com/JagTheFriend/APICode'> Click me </a>"


class CalculationTests(TestCase):
    def test_calculator(self):
        """
        Checks:
            whether the result of the calculator is correct or not
        """

        result = requests.get(f"{URL}/cal_{formula}").json()["output"]
        # check whether the correct type is returned
        self.assertIsInstance(result, str)
        # check whether the result is correct
        self.assertEqual(result, Expected)

    def test_hex_to_denary(self):
        """
        Checks:
            whether the result of hexadecimal to denary is correct or not
        """

        result = requests.get(
            f"{URL}/hex_to_denary+{formula_hex}").json()["output"]
        # check whether the correct type is returned
        self.assertIsInstance(result, str)
        # check whether the result is correct
        self.assertEqual(result, Expected_hex)


class CompileTest(TestCase):
    def test_compile(self):
        """
        Checks:
            whether the result of the compiler is correct or not
        """
        for i in Compile_Tests.keys():
            result = requests.get(
                f"{URL}/compile={i}_{Compile_Tests[i]['code']}").json()["output"]
            # check whether the result is a string
            self.assertIsInstance(result, str)
            self.assertEqual(result, Compile_Tests[i]["output"])

    def test_ascii(self):
        """
        Checks:
            whether the `Pixel Art` is correct or not
        """

        result = requests.get(
            f"{URL}/ascii_{Input}").json()["output"]
        self.assertEqual(result, Expected_art)


class OtherAPIS(TestCase):
    def test_reddit(self):
        """
        Checks:
            whether the `Reddit API`:
                + returns a set amount of posts
                + all the posts are related to the subreddit
        """

        result = requests.get(
            f"{URL}/reddit={subreddit}+{reddit_limit}").json()
        time.sleep(2)
        result_2 = requests.get(
            f"{URL}/reddit={subreddit}+{reddit_limit}").json()
        # both of them should be almost the same
        self.assertAlmostEqual(result, result_2)

    def test_inspire(self):
        """
        Checks:
            whether the `Inspire API` doesn't give the same text twice
        """

        result = requests.get(
            f"{URL}/inspire").json()
        time.sleep(2)
        result_2 = requests.get(
            f"{URL}/inspire").json()
        # both of them should be almost the same
        self.assertNotEqual(result, result_2)

    def test_lyrics(self):
        """
        Checks:
            whether the `Lyrics API` gives the same lyrics of a song when ran
        """

        result = requests.get(f"{URL}/lyrics+{Song_name}").json()["output"]
        # check whether the correct lyrics is given
        self.assertEqual(result, lyrics)

    def test_length(self):
        """
        Checks:
            whether the `Youtube playlist length finder API` gives the correct time
        """

        result = requests.get(f"{URL}/length+{Playlist}").json()["output"]
        # check whether a string is returned
        self.assertIsInstance(result, str)
        self.assertEqual(result, Length)

    def test_chatbot(self):
        """
        Checks:
            whether the response from the `AI` is a string    
        """
        result = requests.get(f"{URL}/ai_{AI_WORDS}").json()["output"]
        self.assertIsInstance(result, str)

    def test_main_page(self):
        """
        THIS TEST WAS NOT REQUIRED
        """
        result = requests.get(f"{URL}/").text
        self.assertEqual(result, Main_page)
