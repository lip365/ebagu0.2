#!/usr/bin/env python
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rclone.settings")
from main.models import Post

def rank_all():
	for single_post in Post:
		single_post.get_score()