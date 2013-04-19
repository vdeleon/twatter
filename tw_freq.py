from twython import Twython
from datetime import datetime, date
import time
import string

TWITTER_APP_KEY = 'XXX'
TWITTER_APP_KEY_SECRET = 'XXX' 
TWITTER_ACCESS_TOKEN = 'XXX'
TWITTER_ACCESS_TOKEN_SECRET = 'XXX'

twitter = Twython(app_key=TWITTER_APP_KEY, 
	app_secret=TWITTER_APP_KEY_SECRET, 
	oauth_token=TWITTER_ACCESS_TOKEN, 
	oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

def alert(frequency):
	if frequency > thresh:
		print "FREQUENCY THRESHOLD REACHED FOR KEYWORD: " + keyword

def find_freq(keyword):
	res = twitter.search(q=keyword)
	id = 0
	try:
		while(id<50):
			check_exist = res[u'statuses'][id][u'created_at']
			id = id + 1
	except:
		pass

	time1 = res[u'statuses'][0][u'created_at']
	time2 = res[u'statuses'][id-1][u'created_at']

	t1 = string.split(string.split(time1)[3], ':')	# Revisit this whole section: use datetime/timedelta instead of manual
	t2 = string.split(string.split(time2)[3], ':')

	diff_hour = int(t1[0]) - int(t2[0])
	diff_mins = int(t1[1]) - int(t2[1])
	diff_secs = int(t1[2]) - int(t2[2])

	if diff_secs < 0:
		diff_mins = diff_mins - 1
		diff_secs = diff_secs*(-1)

	t_frac = diff_mins + (diff_secs / 60.0) + 0.01  # +0.01 ensures division by non-zero number

	frequency = (id-1)/t_frac

	return frequency


keywords = ["earthquake", "korea", "boston"]	# Replace/add keywords as necessary
thresh = 3	# This is the tweets per minute threshold frequency
cycles = 2	# How many times you want the code to run
wait = 30		# The amount of time you want to wait between each cycle in seconds

counter = 0

while(counter < cycles - 1):
	for keyword in keywords:
		alert(find_freq(keyword))
	counter = counter + 1
	time.sleep(wait)
