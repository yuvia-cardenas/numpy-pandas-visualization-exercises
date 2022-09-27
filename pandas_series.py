# Exercise I
fruit = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

fruit
# 1. Determine the number of elements in fruits.
fruit.size
# 2. Output only the index from fruits.
fruit.index
# 3. Output only the values from fruits.
fruit.count
# 4. Confirm the data type of the values in fruits.
type(fruit)
# 5. Output only the first five values from fruits. 
# Output the last three values. 
# Output two random values from fruits.
fruit.head()
fruit.tail(3)
fruit.sample(2)
# 6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.

fruit.describe
# 7. Run the code necessary to produce only the unique string values from fruits
fruit.value_counts()
fruit_count = fruit.value_counts()
unique_fruit = fruit_count[fruit_count <= 1]
unique_fruit
# 8. Determine how many times each unique string value occurs in fruits.
len(unique_fruit)
# 9. Determine the string value that occurs most frequently in fruits.
fruit.value_counts().head(1)
# 10. Determine the string value that occurs least frequently in fruits.
min(fruit.value_counts())


# Exercise II
#1. Capitalize all the string values in fruits.
fruit.str.capitalize()

#2. Count the letter "a" in all the string values (use string vectorization).

fruit.str.count('a')
#3. Output the number of vowels in each and every string value.

fruit.str.count(r'[aeiou]')
#4. Write the code to get the longest string value from fruits.

fruit_total_length = fruit.str.len()
fruit_max_length = fruit.str.len().max()
fruit[fruit_total_length == fruit_max_length]

#5. Write the code to get the string values with 5 or more letters in the name
fruit[fruit_total_length >= 5]
#6. Find the fruit(s) containing the letter "o" two or more 
fruit[fruit.str.count('o')>=2]


#7. Write the code to get only the string values containing the substring "berry".
fruit[fruit.str.contains('berry')]
#8. Write the code to get only the string values containing

fruit[fruit.str.contains('apple')]
#9. Which string value contains the most vowels?
total_vowel_count = fruit.str.count(r'[aeiou]')
total_vowel_count
total_vowel_count = fruit.str.count(r'[aeiou]')
max_vowel_count = total_vowel_count.max()
fruit[total_vowel_count == max_vowel_count]
#same as
#bool_mask = fruit.str.len() == fruit.str.len().max()
#fruit[bool_mask]

# Exercise III
part3_list = list(    'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
)

letters_list = pd.Series(part3_list)
letters_list
#1.Which letter occurs the most frequently in the letters Series?
letters_list.describe()['top']
#2. Which letter occurs the Least frequently?

#3. How many vowels are in the Series?

#total_vowel_count = fruit.str.count(r'[aeiou]')
#max_vowel_count = total_vowel_count.max()
#fruit[total_vowel_count == max_vowel_count]

ttl_vowel_count_letters = letters_list.str.count(r'[aeiou]')
total_vowels = ttl_vowel_count_letters.sum()
total_vowels

#4. How many consonants are in the Series?
ttl_letters = letters_list.str.len().sum()
ttl_consonants = ttl_letters - total_vowels
ttl_consonants
#5. Create a Series that has all of the same letters but uppercased.

cap_letters_list = letters_list.str.upper()
cap_letters_list
#6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.
numlist = list(    ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
)
numbers = pd.Series(numlist)
numbers
#1. What is the data type of the numbers Series?
#object
numbers.dtype
#How many elements are in the number Series?
numbers.count()
#Perform the necessary manipulations by accessing Series attributes and methods to convert the 
#numbers Series to a numeric data type.
num1 = numbers.str.replace('$', '')

num2 = num1.str.replace(',','')
num2
new_numbers = pd.Series(num2).astype('float')
new_numbers
new_numbers.max()
#Run the code to discover the minimum value from the Series.
new_numbers.min()
#What is the range of the values in the Series?
#Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
pd.cut(new_numbers, 4)
#Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
