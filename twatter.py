from twython import Twython
from lxml import etree
import string
import urllib2
import StringIO

twitter = Twython()

class Twatter:

	def frequency(self, keyword):
		'''
		str -> float
		Returns the rate of appearance of keyword in up to 50 tweets in tweets/time format.
		(There is a much better way to do this using datetime objects. Working on this.)
		'''
		
		res = twitter.search(q=keyword)
		id = 0
		try:		# Counts the number of tweets with the keyword in case there is less than 50
			while(id<50):
				check_exist = res[u'statuses'][id][u'created_at']
				id = id + 1
		except:
			pass
		
		# Revisit this whole following section: use datetime/timedelta instead of manual

		time1 = res[u'statuses'][0][u'created_at']
		time2 = res[u'statuses'][id-1][u'created_at']
		
		t1 = string.split(string.split(time1)[3], ':')
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

		
	def followers(self, user):
		'''
		str -> list
		Returns a list of numerical follower IDs for a given username
		'''
		
		followers = []
		data_raw = twitter.getFollowersIDs(screen_name = user)
		followers = followers + data_raw['ids']
		
		return followers


	def mutualfollowers(self, user1, user2):
		mutuals = []
		user1_followers = followers(user1)
		user2_followers = followers(user2)

		for f in user1_followers:
			if f in user2_followers:
				mutuals = mutuals + f

		return mutuals


	def userlocation(self, user_id):
		'''
		int -> dict
		Scrapes the user's profile page for their location (uses numerical ID). Requires lxml and StringIO.
		'''

		locations = {}
		url = "http://twitter.com/account/redirect_by_id?id=" + str(user_id)

		try:
			htmldata = urllib2.urlopen(url)
			html = htmldata.read()

			parser = etree.HTMLParser()
			tree = etree.parse(StringIO.StringIO(html), parser)

			xpath = '/html/body/div/div[3]/div/div[2]/div/div[2]/p[2]/span/text()'

			decode_pre_result = ' '.join(tree.xpath(xpath)).strip().decode('string_escape')

			#print str(user_id) + ": " + decode_pre_result
			locations[str(user_id)] = decode_pre_result

		except:
			#print str(user_id) + ": No location"
			locations[str(user_id)] = "No location"

		return locations
