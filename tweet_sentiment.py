import sys
import json
import string

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

##
# Parse AFINN-111.txt file;
# Push into 'term => score' key pairing and return
#
def parse_scores(afinnfile):

	scores = {}

	for line in afinnfile:
		term,score 		= line.split("\t")
		scores[term] 	= int(score)
		#print(term)

	return scores

def parse_tweets(tweet_file):

	#tweets = {}

	#tweets_decompressed = json.loads(tweet_file)

	for entry in tweet_file:
		tweet = json.loads(entry.read())
		print(tweet)

	return 1

def main():
    
    #sent_file 	= open(sys.argv[1])
    #tweet_file  = open(sys.argv[2])

    sent_file  	= open("AFINN-111.txt")
    scores 		= parse_scores(sent_file)

    tweet_file 	= open("output.txt")

    for entry in tweet_file:	

		tweet 	= json.loads(entry)

		#ensure english tweet
		if "lang" not in tweet or tweet["lang"] != "en":
			continue

		if "created_at" not in tweet:
			continue

		#extract, explode tweet
		text 	= tweet["text"]
		words 	= text.split()

		#calculate sentiment
		sentiment = 0

		for word in words:
			if word in scores:
				sentiment += scores[word]

		print "sentiment:", sentiment
		
	
	#end main()

if __name__ == '__main__':
    main()
