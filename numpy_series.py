#1. How many negative numbers are there?
print(a[a < 0])
len(a[a < 0])

#2. How many positive numbers are there?
print(a[a >= 0])
len(a[a >= 0])


#3. How many even positive numbers are there?
pos_nums = a[a > 0]
pos_nums[pos_nums % 2 == 0]
len(pos_nums[pos_nums % 2 == 0])

#4. If you were to add 3 to each data point, how many positive numbers 
#would there be?

array_plus_3 = a + 3
pos_array_plus_3 = array_plus_3[array_plus_3 >= 0]
len(pos_array_plus_3)

#5. If you squared each number, what would the new mean 
#and standard deviation be?
array_squared = np.square(a)
mean_array_squared = np.mean(array_squared)
std_array_squared = np.std(array_squared)

print(array_squared)
mean_array_squared
std_array_squared

# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. 
#See this link for more on centering.

# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# 8. Copy the setup and exercise directions from More Numpy Practice into your 
# numpy_exercises.py and add your solutions.


