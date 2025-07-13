# Probability (Mean, Median, Variance, Standard Deviation)

# Mean: Avg value of all values
# Median: Middle value of all values
# Variance: spread of data. Standard deviation is its square root

import statistics

scores = [75,78,82,63,70,80,87,95,71]
scores1 = [75,78,82,63,70,80,87,95,71,80]
print("Student scores: ", scores)
print("Mean: ", statistics.mean(scores))
print("Median:", statistics.median(scores))
print("Median:", statistics.median(scores1))
print("Variance: ",statistics.variance(scores))
print("Standard Deviation : ",statistics.stdev(scores))

