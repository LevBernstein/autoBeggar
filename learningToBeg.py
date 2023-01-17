import beggarmypython as bgmp
import numpy
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from collections import Counter
from random import choice, randint
from statistics import median, mean
from typing import List, Tuple

base = "------------------------------------AAAAKKKKQQQQJJJJ"

def get_training_data(iters: int) -> List[Tuple[Tuple[str, str], int, int]]:
	results = []

	for i in range(5000):
		base = "------------------------------------AAAAKKKKQQQQJJJJ"
		hands = ""
		while base != "":
			place = randint(0, len(base) - 1)
			hands += base[place]
			base = base[:place] + base[(place+1):]
		results.append(bgmp.play((hands[:26], hands[26:])))

	return results