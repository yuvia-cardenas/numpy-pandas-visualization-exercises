from pydataset import data
import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)

print(df)

#Create a column named passing_english that indicates whether each student has a passing grade in english.

df['passing_english'] = df.english > 70
#Sort the english grades by the passing_english column. How are duplicates handled? Descending

df.sort_values(by='passing_english')

#Sort the english grades first by passing_english and then by student name.
#All the students that are failing english should be first, 
#and within the students that are failing english they should be ordered alphabetically.
#The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)

df.sort_values(by='passing_english').name

#Sort the english grades first by passing_english, and then by the actual english grade, 
#similar to how we did in the last step.

df.sort_values(by='passing_english').english

#first by grade then by index
#Calculate each students overall grade and add it as a column on the dataframe.
#The overall grade is the average of the math, english, and reading grades.

df['overall_grade'] = (df.english+df.math+df.reading)/3

from pydataset import data
# data('mpg', show_doc=True) # view the documentation for the dataset
mpg = data('mpg') # load the dataset and store it in a variable


mpg.describe()
#What are the data types of each column?
#dtypes: float64(1), int64(4), object(6)


#How many rows and columns are there?
mpg.info()
#234 rows 11 columns

#Rename the cty column to city.
#Rename the hwy column to highway.
#df.rename(columns={'name': 'student'})

mpg = mpg.rename(columns = {'cty': 'city'})
mpg = mpg.rename(columns = {'hwy': 'highway'})

#Do any cars have better city mileage than highway mileage?
#no
#df['passing_english'] = df.english > df.math
#bool_mask = fruit.str.len() == fruit.str.len().max()
#fruit[bool_mask]
better_city = mpg['better_mpg'] = (mpg.city > mpg.highway)
#mpg[better_city]
mpg


#Create a column named mileage_difference this column should contain the difference between 
#highway and city mileage for each car.

mpg['mileage_difference'] = (mpg.highway-mpg.city)
#Which car (or cars) has the highest mileage difference?

mpg.sort_values(by = 'mileage_difference', ascending=False).head()

#Which compact class car has the lowest highway mileage? The best?
#df[['name', 'math']]
#mpg[['highway', 'class']] == 'compact'
compact_list = mpg['class'] == 'compact'
compact_list[compact_list]

#df.sort_values(by='english')





