import json
from goose import Goose


DEFAULT = 'http://reddit.lucasou.com/static/imgs/reddit-camera.png'
def extractt(content):
	g = Goose()
	thumbnail = g.extract(raw_html=content)
	if thumbnail.top_image is None:
		return DEFAULT 

	else:
		if thumbnail.top_image.src is None:
			return DEFAULT
		else:
			resposne = {'image':thumbnail.top_image.src}
			return thumbnail.top_image.src
	