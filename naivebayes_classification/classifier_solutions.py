'''
My Classifier

p(A|B) = P(B|A)P(A)/P(B)
'''

class NaiveBayesClassifierInMemory():

    def __init__(self):
        self.set = None
        self.counts = {}
        self.class_stuff = {}

    def train(self, train_set):
        self.set = train_set
        self.counts['length'] = len(train_set)

        for bar in train_set:
            self.counts[bar[1]] = self.counts.get(bar[1], 0) + 1 
            for descrip in bar[0].keys():
                
                self.counts[(descrip,bar[1])] = self.counts.get((descrip, bar[1]), 0) + 1 

        # print "counts", self.counts['miss']           


    def predict(self, unknown):
        print "in predict"
        match_result, miss_result = 1, 1
        for word in unknown.split():
            check_match = ("contains_word_(%s)" % word, "match")
            check_miss = ("contains_word_(%s)" % word, "miss")

            if check_match in self.counts:
                match_result *= self.counts[check_match] * 1.0 / self.counts["match"]
            else:
                match_result *= 0.1 / self.counts["match"]

            if check_miss in self.counts:
                miss_result *= self.counts[check_miss] * 1.0 / self.counts["miss"]
            else:
                miss_result *= 0.1 / self.counts["miss"]

        match_result *= self.counts["match"] / self.counts["length"]
        miss_result *= self.counts["miss"] / self.counts["length"]

        print match_result, miss_result

        if match_result < miss_result:
            print "match"
        else:
            print "miss" 

