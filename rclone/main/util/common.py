from enum import Enum


class SortMethods(Enum):
	"""This class is enum for sorting methods.
	Thread is sorted by score and date.
	"""
	score = 1
	date = 2