import json
from nltk.tokenize import word_tokenize

#Opens the text file for writing the tokens
output_file = open('tokens.txt', 'w')

#Tokenize the tweets (split them into words)
with open('town_hall_data.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        tokens = word_tokenize(tweet['text'])
        #do_some_analysis(tokens)
