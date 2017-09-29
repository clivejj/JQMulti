import random

def csvToDict(csvName):
    #read csv file
    reader = open(csvName, "r")
    data = reader.read()
    #print data
    reader.close()

    #split csv file by line
    dataList = data.splitlines()
    #print dataList
    dataList = dataList[:-1]
    #print dataList

    dict = {}
    for x in dataList[1:]:
        #deal with case of commas within quotations
        if x[0] == '"':
            #split by quotations
            temp = x.split('"')
            #convert to float
            dict[temp[1]] = [float(temp[2].split(",")[1]), temp[2].split(",")[2]]
            #normal case
        else:
            temp = x.split(",")
            #convert to float
            dict[temp[0]] = [float(temp[1]), temp[2]]
    #dict.pop("Total")
    return dict

def randOccupation(dict):
	num = random.uniform(0, 99.8)
	cumsum = 0
	for key in dict:
		if cumsum + dict[key][0] >= num:
			return key
		cumsum += dict[key][0]
		print cumsum
