from twython import Twython
import string
import urllib2
from lxml import etree
import StringIO

twitter = Twython()
data_raw = twitter.getFollowersIDs(screen_name = "ionainstitute")

followers = data_raw['ids']
dict = {'noloc': 0}
# print followers

for id in followers:
	url = "http://twitter.com/account/redirect_by_id?id=" + str(id)

	try:
		htmldata = urllib2.urlopen(url)
		html = htmldata.read()

		parser = etree.HTMLParser()
		tree = etree.parse(StringIO.StringIO(html), parser)

		xpath = '/html/body/div/div[3]/div/div[2]/div/div[2]/p[2]/span/text()'

		pre_result1 = ' '.join(tree.xpath(xpath))
		pre_result = pre_result1.strip()

		decode_pre_result = pre_result.decode('string_escape')

		print str(id) + " : " + decode_pre_result

		try:
			dict[decode_pre_result] = dict[decode_pre_result] + 1
			print dict
		except:
			dict[decode_pre_result] = 1
			print dict

	except:
		dict['noloc'] = dict['noloc'] + 1
		print str(id) + " : No location"
