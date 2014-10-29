import csv

f=open('fun.csv')

csv_f=csv.reader(f)

fun=[]

for row in csv_f:
	fun.append(row)


f.close()

print len(fun)