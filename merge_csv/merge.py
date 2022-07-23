import csv
dataset1=[]
dataset2=[]
with open ('dataset_1.csv','r') as f:
    csvreader = csv.reader(f)
    for a in csvreader:
        dataset1.append(a)
header1 = dataset1[0]
planetdata1 = dataset1[1:]
with open ('dataset_2.csv','r') as f:
    csvreader = csv.reader(f)
    for a in csvreader:
        dataset2.append(a)
header2 = dataset2[0]
planetdata2 = dataset2[1:]
finalheader = header1+header2
finalplanetdata = []
for i in range(0,len(planetdata1)):
    finalplanetdata.append(planetdata1[i]+planetdata2[i])
for i in range(len(planetdata1),len(planetdata2)):
    finalplanetdata.append(planetdata2[i])
with open ('fianldata.csv','a+',newline='') as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(finalheader)
    csvwriter.writerows(finalplanetdata)