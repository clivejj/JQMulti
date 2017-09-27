import random
from flask import Flask, render_template


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

dict = csvToDict("occupations.csv")

def randOccupation():
    num = random.uniform(0, 99.8)
    cumsum = 0
    for key in dict:
        if cumsum + dict[key][0] >= num:
            return key
        cumsum += dict[key][0]

#print dict


app=Flask(__name__)
@app.route('/occupations')
def occu():
	return render_template('base.html',passedDict = dict, randOcc = randOccupation());

if __name__ == '__main__':
	app.debug = True
	app.run()

	
