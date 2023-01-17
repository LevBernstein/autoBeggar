import beggarmypython as bgmp
from random import randint

with open("best.txt", "r") as f: rawBest = f.read().split(",")
best = ((rawBest[0], rawBest[1]), int(rawBest[2]), int(rawBest[3]))
#print(best)

#print(bgmp.play(best[0]))
#print(bgmp.play(("---AJ--Q---------QAKQJJ-QK", "-----A----KJ-K--------A---")))

while True:
	base = "------------------------------------AAAAKKKKQQQQJJJJ"
	hands = ""
	while base != "":
		place = randint(0, len(base) - 1)
		hands += base[place]
		base = base[:place] + base[(place+1):]
	print(hands)
	try:
		test = bgmp.play((hands[:26], hands[26:]))
	except KeyboardInterrupt:
		exit()
	except Exception:
		with open("inf.txt", "w") as f: f.write(f"{test[0][0]},{test[0][1]},{test[1]},{test[2]}")
		exit()
	if test[1] > best[1]:
		best = test
		with open("best.txt", "w") as f: f.write(f"{best[0][0]},{best[0][1]},{best[1]},{best[2]}")
		print(best)