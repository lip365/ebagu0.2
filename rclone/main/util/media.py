import json
from goose import Goose

def extract(url):
	g = Goose()
	article = g.extract(url=url)
	if article.top_image is None:
		return "hello"

	else:
		if article.top_image.src is None:
		  return "hello"
		else:
			resposne = {'image':article.top_image.src}
			return article.top_image.src