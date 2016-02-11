import json
from goose import Goose

DEFAULT = 'http://reddit.lucasou.com/static/imgs/reddit-camera.png'
def extract(url):
	g = Goose()
	try:
		article = g.extract(url=url)
		if article.top_image is None:
			return DEFAULT 

		else:
			if article.top_image.src is None:
			  return DEFAULT
			else:
				resposne = {'image':article.top_image.src}
				return article.top_image.src
	except ParseError:
		if can_handle():
	            handle_exception()
	        else:
	            print("couldn't handle exception: url={0}".format(url))
	            raise