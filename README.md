# Sentiments
Implements a website using flask that analyze the sentiments of Tweets of a user.

![A Pie chart of the sentiments](https://lh4.googleusercontent.com/_3wPnnWAjUg3hwQqdTIMfItl6EQnvj7jyjq0QB3SysBGJoSTDVIj7JWqIuGR002zwkPf2gwr=w1366-h650)

Dr. Minqing Hu and Prof. Bing Liu of the University of Illinois at Chicago
have put together lists of [2006 positive words](https://raw.githubusercontent.com/cs50/problems/sentiments/positive-words.txt) and [4783 negative words](https://raw.githubusercontent.com/cs50/problems/sentiments/negative-words.txt).

This sentiment Analyzer is baised simply on whether the word lies in which
category, positive or negative.
Each word is awarded a score of 1 or -1 or simply 0 if the word is positive,
negative or neutral.
