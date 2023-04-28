#Dempster Shafer
import random
print('Cat is dead or alive based on Dempster Chafer Theory')
print("Basic values: Alive: {} Dead: {}".format(0.5,0.5))
ma=random.randrange(0,5)
ma=0.1*ma
md=random.randrange(0,5)
md=0.1*md
ba=random.randrange(0,5)
ba=ba*0.1
print("None Mass:0 Belief:0 Plausibility:0")
print("Alive Mass:{}Belief:{} Plausibility:{}".format(ma,ba,1-md))
print("Dead Mass:{} Belief:{} Plausibility:{}".format(md,0.5,1-ma))
print("Either Mass:{} Belief:1 Plausibility:1".format(0.5-ma))
