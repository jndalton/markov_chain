
def fetch_web_data(source):
	from bs4 import BeautifulSoup
	import urllib2

	request = urllib2.request(source)
	response = urllib2.urlopen(request)

	text = response.read()

	response.close()

	text = BeautifulSoup(text, "html.parser").get_text(strip = True)
	return text


