import pdb
import random

def run_kmeans(points, initialCentroid1, initialCentroid2):
    cheat = False  # :P
    if cheat:
        import kmeans_solutions
        return kmeans_solutions.kMeansDemo(points, initialCentroid1, initialCentroid2)
    else:
        cent1, cent2 = [], []
        #pdb.set_trace()
        for point in points:
            if abs(point - initialCentroid1) < abs(point - initialCentroid2):
                cent1.append(point)
            else:
                cent2.append(point)
        cent1_result = sum(cent1) * 1.0/ len(cent1)
        cent2_result = sum(cent2) * 1.0 /len(cent2)
        print cent2_result != initialCentroid2
        if cent2_result != initialCentroid2:
            return run_kmeans(points, cent1_result, cent2_result)
        else:
            return cent1_result, cent2_result


points = [80, 65, 70, 65, 86, 70, 38, 67, 38, 41, 70, 70, 70, 70, 65]
initialCentroid1 = 38
initialCentroid2 = 41

finalCentroid1, finalCentroid2 = run_kmeans(points, initialCentroid1, initialCentroid2)
print "Final Centroids: ", finalCentroid1, finalCentroid2

