import json
import urllib2
from urllib2 import Request
from goose import Goose

def get_content(url):
    """This function is intended to return content from url.
    :param url: URL to get content
    :return: The response from url
    """
    req = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
    response = urllib2.urlopen(req).read()
    return response	


def extract(url):
	url = get_content(url)
	g = Goose()
	article = g.extract(url=url)
	resposne = {'image':article.top_image.src}
	return json.dumps(resposne)