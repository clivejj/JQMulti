import random

#read csv file
reader = open("occupations.csv", "r")
data = reader.read()
#print data
reader.close()

#split csv file by line
dataList = data.split('\r\n')
dataList = dataList[:-1]
#print dataList

dict = {}
for x in dataList[1:]:
    #deal with case of commas within quotations
    if x[0] == '"':
        #split by quotations
        temp = x.split('"')
        #convert to float
        dict[temp[1]] = float(temp[2][1:])
    #normal case
    else:
        temp = x.split(",")
        #convert to float
        dict[temp[0]] = float(temp[1])


dict.pop("Total", 0)
#print dict

def randOccupation():
    num = random.uniform(0, 99.8)
    cumsum = 0
    for key in dict:
        if cumsum + dict[key] >= num:
            return key
        cumsum += dict[key]

#print randOccupation()

#Test if randOccupation gives expected probability
def probTester(cat):
    counter = 0
    i = 0
    while i < 99800:
        if randOccupation() == cat:
            counter += 1
        i += 1
    print "EXPERIMENTAL: " +str(counter / 1000.0) + " EXPECTED: " + str(dict[cat])

#test probability
probTester("Sales")
probTester("Legal")
probTester("Farming, fishing and forestry")

