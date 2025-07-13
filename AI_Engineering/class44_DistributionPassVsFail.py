#Distribution Pass Vs Fail

import matplotlib.pyplot as plt

# data
scores = [88,38,45,55,65,78,92,12,37,80,82,45,89,32]

# Categorize scores into Pass(>=50) and Fail(<50)
pass_scores = [s for s in scores if s>= 50]
fail_scores = [s for s in scores if s< 50]

# Prepare data for Ploting
categories = ['Fail (<50)', 'Pass (>=50)']
counts = [len(fail_scores),len(pass_scores)]
print(categories)
print(counts)

# Plot
plt.bar(categories, counts, color=['red','green'])
plt.title('Student Score Distribution: Pass VS Fail')
plt.xlabel('Category')
plt.ylabel('Number of Students')
plt.ylim(0, max(counts)+2)

# Show exact count on top of bars
for i,count in enumerate(counts):
    plt.text(i, count+0.2, str(count), ha='center', fontweight='bold')

plt.show()