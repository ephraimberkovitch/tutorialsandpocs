import random

def get_name(names):
    r = random.random()
    #d = dict()
    prev = 0
    for name,prob in names.iteritems():
        #print name,prob
        #d[name] = {"min":prev,"max":prev+prob}
        prev = prev+prob
        if r<prev:
            return name
    #return d

if __name__ == "__main__":
    names = {"avi":0.3,"beni":0.2,"gidi":0.5}
    stats = dict()
    for name in names.keys():
        stats[name] = 0
    #print get_name(names)
    for i in xrange(0,10000):
        stats[get_name(names)] += 1
    print stats