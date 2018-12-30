# Build a Command Line Quiz Game!

#### The Goal

We're going to build a CLI trivia game! When it's finished, it will look something like this:

<img src="jeopardyCLI.gif" width="850">

We will use a url (those things we usually call 'links') to get random trivia questions!

Then, we're going to write a program to ask those questions to a user and tell them whether or not they got a question right.

<details>
  <summary> Click for more detail</summary>

  We've spent all day learning about data structures, and we've come up with a lot of ways to use them to make our code more efficient, but dictionaries and lists are hugely important because almost all data sent back and forth through the internet is sent packaged and organized in a dictionary; even if it's called other things, would not a dictionary - by any other name - be just as 1337?

  Web applications typically do this through something called an application program interface - an API for short.

</details>
<br>

## Environment Setup

In order for this game to work, we will need a few things:

1. A program that will "get" the quiz question. In other words, if we think of the url (the 'link') as an address, we need a way to go get the data waiting for us at that address. We will use a python library called "Requests."
2. A way to easily read the information that comes back to us from that address.

#### Install a URL handler

To install Requests, type the following into the console:
```bash
curl https://bootstrap.pypa.io/get-pip.py | python3
pip install requests
```

We also need to tell the python program to actually USE the library we just installed. That's why line 1 of 'jeopardy.py' looks like this:
```Ruby
import requests
```

#### Enable a JSON formatter

We're going to use the Requests library to retrieve information from this address: [http://jservice.io/api/clues?category=139](http://jservice.io/api/clues?category=139 "Let's get some questions!")

Go ahead and click on it.

It looks pretty messy and hard to read, doesn't it?

<details>
  <summary> Click to see a more readable version: </summary>

  ![JSONview Example](JSONview.png "This is better, right?")

  It looks like a mashup of lists and dictionaries!

</details>
<br>

This data structure is called a [JSON](https://www.w3schools.com/js/js_json_intro.asp "This stands for JavaScript Object Notation") object, and yes, it looks like a bunch of lists and dictionaries because that's exactly what it is! Once it's formatted, it's MUCH less intimidating.

To make YOUR browser format it this way, you'll want to find a plugin that will do this. There are many options; the example used one for Chrome called JSONview. To install that one, just search for "JSONview" and navigate to the Chrome Web Store.

![JSONview Install](JSONviewPlugin.png)

###### Note: While it is possible to do this without JSONview or another JSON formatter, it's extremely difficult.

Once you've installed Requests and enabled a JSON formatter, you're ready to jump in.

## API Basics

We're going to use an api called [jservice](http://jservice.io/), and if you go to their homepage, you'll see some advice for how to use their API.

For example, if you want to see the first 10 categories you could choose from, you could use the url http://jservice.io/api/categories?count=10

Based on that url, you can probably already figure out how to show the first 50 categories too. Try it out!

While that's cool, the jService team also built a cool category interface that is a bit easier for humans to use: [jService Popular Categories](http://jservice.io/popular).

Earlier, you used [http://jservice.io/api/clues?category=139](http://jservice.io/api/clues?category=139 "Let's get some questions!") to get some questions. You'll notice that the category in the url is coded number 139; if you open the link, you'll see that all the questions are in the category "5-letter words".

Feel free to change the category to whatever other category you choose. When you've picked a category you like (or if you want to stick to 5-letter words), it's time to really get started.  

## The Challenges

run the code as it is:

```bash
python jeopardy.py
```

You'll notice that it prints the entire response out all at once. That's *way* too much.  We'll go one step at a time and try to build this up as a fully functional and interactive game.

#### LEVEL 1

1. Print out just the first item in the entire response.

2. Print out just the question of the first item in the entire response.

3. Refactor your code so that it prints out a random question, not just the first one every time.

4. Now, get some user input after the question. If what they type matches the answer, print a "congratulations!" message of some sort. If it doesn't match, print a "sorry" message of some sort.
    * It's important to think about how specific Python's matching will be. If the user types "gorge" but the correct answer is "Gorge.", then the user will get the question wrong. *Consider finding a way of making your program responsive to small variations in capitalization or punctuation.*
    
5. If you get it wrong, you probably still want to know the right answer - it can be so frustrating if you were sure you were right. If the user gets it wrong, print out a message that tells them what the correct answer really was.

#### LEVEL 2

6. Wrap this game in a loop so the user can play multiple rounds.

7. Create a score variable:
    * If the user gets a question right, increase their score by the point value of the question.
    * If the user gets a question wrong, decrease their score by the point value of the question.
    * Print out their score after each round.

#### LEVEL 3

8. One of the most frustrating parts of this game is missing an answer due to typos, spelling errors, capitalization mismatches, or unexpected punctuation. Some of this is relatively easy to fix with Python's core methods, but there is no core function to show that "george" and "gorge" are SO CLOSE that the user probably actually knew the answer.
    * There's a library called [similar-text](https://pypi.org/project/similar_text/) that will let us examine how similar two strings are.
    * Install that library, require it at the top of your program, and then look at the documentation to figure out how to use it.
    * If the user's answer is really close to the real answer, let them know that they almost have it, but that they may want to type it more carefully.
    * It may also be beneficial to consider a way of recognizing that "Grapes of Wrath" and "The Grapes of Wrath" would be considered a mismatch. Are you going to give the user another chance if all they're missing is a small word like "the"?

![Jeopardy Board](jBoard.jpg)

#### LEVEL 4

9. The real jeopardy board has six categories, and 5 questions per category of increasing difficulty. That's 30 unique questions. The player also gets to CHOOSE which questions to answer and when.
    * Find a way to load all 30 questions, and then offer the user a choice of which question to attempt.
    * Find a way to print out a visual representation of the board in the console.
      * Bonus: print the score at the top or bottom of the board.
    * Keep track of which questions the user has already tried, and throw them an error if they try to access the same question twice.
