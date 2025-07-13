#Distribution with Histogram

import matplotlib.pyplot as plt

# data
#scores = [40,35,48,55,65,50,30,45,40,50,60,60,70,50]
scores = [88,38,45,55,65,78,92,12,37,80,82,45,89,32]
#scores = [40,50,30,45,40,50,60,60,70,50]


# Create the histogram and get bar containers
counts, bins, patches = plt.hist(scores) #, bins = 14, edgecolor='black')
#counts, bins, patches = plt.hist(scores, bins = 10, edgecolor='black')

# Defines a list of colors
colors = ['red','green','blue','orange','purple','cyan','magenta','brown','gray','pink']

# Apply colors to each bar
for patch, color in zip(patches,colors):
    patch.set_facecolor(color)
# Add lables and title
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

#Show the Plot
plt.tight_layout()
plt.show()