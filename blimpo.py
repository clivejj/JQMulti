import random
from flask import Flask


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



app=Flask(__name__)
@app.route('/occupations')
def occu():
	return 'jninja'

if __name__ == '__main__':
	app.debug==True
	app.run()	

	
