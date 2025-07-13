# Variance Data Plot
import numpy as np
import matplotlib.pyplot as plt


# Step 1: Data
# data = [1,10,11,12,21,34,31,33,40,45,100,101,201,25]
data = [1.1,1.25,1.51,1.63,1.75,1.81,1.008,1.31,1.43,1.73,1.87,1.91,1.93,45]

# Step 2: Calculate variance
variance = np.var(data)
# Step 3: Print Variance
print(f"Variance: {variance:.2f}")
# Step 4: Plot the data
plt.figure(figsize=(10,5))
plt.plot(data,marker='o',label='Data Points')
plt.axhline(y=np.mean(data), color= 'red', linestyle='--', label='Mean')
plt.title(f'Data Plot with Variance = {variance:.2f}')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()