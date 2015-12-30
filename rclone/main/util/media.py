import json
from goose import Goose



def extract(url):
	g = Goose()
	article = g.extract(url=url)
	resposne = {'image':article.top_image.src}
	return article.top_image.src