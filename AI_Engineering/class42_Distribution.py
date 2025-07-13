#Distribution
# Distribution: Distribution shows how often values occur

import matplotlib.pyplot as plt

# scores = [75,78,82,63,70,80,87,95,71,72]
scores = [40,50,30,45,40,50,60,60,70,50]
data = [1,10,11,12,21,34,31,33,40,45,100,101,201,25]
# plt.hist(scores,bins=5)
plt.hist(scores,bins=10)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()