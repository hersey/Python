import pandas as pd
import numpy as np

# For .read_csv, always use header=0 when you know row 0 is the header row
df = pd.read_csv('train.csv', header=0)

#show first 3 rows 
df.head(3)

#show data type of the entire data frame
type(df)

#show individual variable data type
df.dtypes

#Another valuable comment
df.info()
df.describe()

#Display the 0-10 rows of "age" column 
df.Age[0:10]    #Variable names are case sensitive

#Give constraint range to certain variable 
df[df.Age>60][['Sex','Pclass','Age']]

#Print out people from each class:
for i in range(1,4):
    print i, len(df[ (df['Sex'] == 'male') & (df['Pclass'] == i) ])

#Create histogram: 
import pylab as P
df['Age'].hist()
P.show()

#drooping missing values of Age:
df['Age'].dropna().hist(bins=16, range=(0,80), alpha = .5)
P.show()

#adding new variable called gender with default value of 4:
df['Gender']=4

#lambda x is a build-in function---generate anonymous function at run time, get the first letter of column "Sex"
df['Gender'] = df['Sex'].map( lambda x: x[0].upper() )

#Transfer the "Gender" variable in to 0 and 1
df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)

# In order to populate the missing value of age, calculate the median age for each class
median_ages = np.zeros((2,3))
median_ages

#After create the empty array, loop through Gender and class variable to calculate median

for i in range(0, 2):
    for j in range(0, 3):
        median_ages[i,j] = df[(df['Gender'] == i) & \
                              (df['Pclass'] == j+1)]['Age'].dropna().median()

#Create a new variable called AgeFill to copy all values from Age
df['AgeFill'] = df['Age']
df.head()

#Only look at columns with missing value
df[df['Age'].isnull()][['Gender','Pclass','Age','AgeFill']].head(10)

#Fill AgeFill with the median age based on the median_age table: 
for i in range(0,2):
	for j in range(0,3):
			df.loc[(df.Age.isnull())&(df.Gender==i) & (df.Pclass==j+1),\
			'AgeFill']==median_ages[i,j]


#Transform "Embarked" into numeric value
df['Port']=df['Embarked'].map({'S':0,'Q':1,'C':2}).astype(int)

#Drop rows with missing values
df = df.dropna()
df.drop(df.columns[0], axis=1)

#Export into CSV



