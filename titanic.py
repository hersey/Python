import csv as csv
import numpy as np 


########## Reading in train.csv ##############
 # Open up the csv file in to a Python object
train_file = csv.reader(open('train.csv', 'rb')) 
header = train_file.next()  # The next() command just skips the 
                                 # first line which is a header
train=[]                          # Create a variable called 'train'.
for row in train_file:      # Run through each row in the csv file,
    train.append(row)             # adding each row to the train variable
train = np.array(train) 	         # Then convert from a list to an array

# Be aware that each item is currently a string in this format

print len(train)

##### Calculate the percentage of survivors #######
# The size() function counts how many elements are in
# in the array and sum() (as you would expects) sums up
# the elements in the array.

n_passengers=np.size(train[0::,1].astype(np.float))  #convert "survived" (0/1 value) strings into float
n_survived=np.sum(train[0::,1].astype(np.float))
p_survivors=n_survived/n_passengers

print p_survivors

#### Gender Specific stats ####

f_only=train[0::,4]=='female' #[0::,4] means all rows of column 4
m_only=train[0::,4]!='female'


# Using the index from above we select the females and males separately
f_onboard = train[f_only,1].astype(np.float)     
m_onboard = train[m_only,1].astype(np.float)


# Then we finds the proportions of them that survived
p_f_survived = np.sum(f_onboard) / np.size(f_onboard)  
p_m_survived = np.sum(m_onboard) / np.size(m_onboard) 

print 'Percentage of woman survived is %s' %p_f_survived
print 'Percentage of man survived is %s' %p_m_survived



######### Reading in test.csv  and build predict_file #############
test_file=open('test.csv','rb')
test_file_object=csv.reader(test_file)
header=test_file.next()

predict_file=open('gendermodel.csv','wb')
predict_file_object=csv.writer(predict_file)

predict_file_object.writerow(["PassengerId","Survived"])
for row in test_file_object: 
	if row[3]=='female':
		predict_file_object.writerow([row[0],'1']) #if female, predict survive=1
	else:
		predict_file_object.writerow([row[0],'0']) #if male, predict survived=0

test_file.close()
predict_file.close()



###### Adding class + ticket price bins ########

# In order to analyse the price column I need to bin up that data
# here are my binning parameters, the problem we face is some of the fares are very large
# So we can either have a lot of bins with nothing in them or we can just lose some
# information by just considering that anythng over 39 is simply in the last bin.
# So we add a ceiling

fare_ceiling=40
# then modify the data in the Fare column to = 39, if it is greater or equal to the ceiling
train[ train[0::,9].astype(np.float) >= fare_ceiling, 9 ] = fare_ceiling - 1.0

fare_bracket_size=10
number_of_price_brackets=fare_ceiling / fare_bracket_size

# There were 1st, 2nd and 3rd classes on board
number_of_classes = 3

# But it's better practice to calculate this from the data directly
# Take the length of an array of unique values in column index 2
number_of_classes = len(np.unique(train[0::,2])) 


# Initialize the survival table with all zeros
survival_table = np.zeros([2, number_of_classes, number_of_price_brackets],float)


#Loop through each class and each price bin
#find element that is a female/male and was ith class and paied greater than j*bracket_size but less than(j+1)*bracket_size

for i in xrange(number_of_classes):
	for j in xrange(number_of_price_brackets):
		f_only=train[(train[0::,4]=="female")  \
		&(train[0::,2].astype(np.float)==i+1)  \
		&(train[0::,9].astype(np.float)>=j*fare_bracket_size) \
		&(train[0::,9].astype(np.float)<(j+1)*fare_bracket_size),1]

		m_only=train[(train[0::,4]!='female') \
		&(train[0::,2].astype(np.float)==i+1) \
		&(train[0:,9].astype(np.float) >=j*fare_bracket_size) \
		&(train[0:,9].astype(np.float) <(j+1)*fare_bracket_size) ,1]
		
		survival_table[0,i,j]=np.mean(f_only.astype(np.float))  #be careful of indentation!!
		survival_table[1,i,j]=np.mean(m_only.astype(np.float))

survival_table[survival_table!=survival_table]=0

survival_table[survival_table<0.5]=0
survival_table[survival_table>=0.5]=1


print survival_table

#### Create gendercassmodel ######

test_file=open('test.csv','rb')
test_file_object=csv.reader(test_file)
header=test_file.next()

predict_file2=open('genderclassmodel.csv','wb')
p=csv.writer(predict_file2)
p.writerow(["PassengerId","Survived"])

for row in test_file_object:
	for j in xrange(number_of_price_brackets):
		try:
			row[8]=flow(row[8])
		except: 
			bin_fare=3-float(row[1])
			break
		if row[8]>fare_ceiling:
			bin_fare=number_of_price_brackets-1
			break
		if row[8]>=j*fare_bracket_size and row[8]<(j+1)*fare_bracket_size:
			bin_fare=j
			break

	if row[3]=='female':
		p.writerow([row[0],"%d" % int(survival_table[0,float(row[1])-1,bin_fare])])
	else:
		p.writerow([row[0],"%d" % int(survival_table[1,float(row[1])-1,bin_fare])])


test_file.close()
predict_file2.close()
































