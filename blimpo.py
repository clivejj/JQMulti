import random
from flask import Flask, render_template
from utils import csv


#create the dictionary that will store the csv data
dict = csv.csvToDict("data/occupations.csv")

#print dict

#Render the occupations page
app=Flask(__name__)
@app.route('/occupations')
def occu():
	return render_template('base.html',passedDict = dict, randOcc = csv.randOccupation(dict));


if __name__ == '__main__':
	app.debug = True
	app.run()

	
