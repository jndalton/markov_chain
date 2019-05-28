""" This method should draw data from the web and return the data as readable text"""

def fetch_web_data(source):
	from bs4 import BeautifulSoup
	import urllib2

	request = urllib2.Request(source)
	response = urllib2.urlopen(request)

	text = response.read()

	response.close()

	text = BeautifulSoup(text, "html.parser").get_text(strip = True)
	return text
