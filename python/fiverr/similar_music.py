# http://www.benfrederickson.com/matrix-factorization/

import pandas
# read in triples of user/artist/playcount from the input dataset
data = pandas.read_table("usersha1-artmbid-artname-plays.tsv",
                         usecols=[0, 2, 3],
                         names=['user', 'artist', 'plays'])

# map each artist and user to a unique numeric value
data['user'] = data['user'].astype("category")
data['artist'] = data['artist'].astype("category")

# create a sparse matrix of all the artist/user/play triples
plays = coo_matrix((data['plays'].astype(float),
                   (data['artist'].cat.codes,
                    data['user'].cat.codes)))

artist_factors, _, user_factors = scipy.sparse.linalg.svds(bm25_weight(plays), 50)

class TopRelated(object):
    def __init__(self, artist_factors):
        # fully normalize artist_factors, so can compare with only the dot product
        norms = numpy.linalg.norm(artist_factors, axis=-1)
        self.factors = artist_factors / norms[:, numpy.newaxis]

    def get_related(self, artistid, N=10):
        scores = self.factors.dot(self.factors[artistid])
        best = numpy.argpartition(scores, -N)[-N:]
        return sorted(zip(best, scores[best]), key=lambda x: -x[1])

