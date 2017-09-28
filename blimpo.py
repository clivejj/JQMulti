import random
from flask import Flask, render_template
from utils import csv

dict = csv.csvToDict("data/occupations.csv")

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

	
