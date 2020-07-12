from flask import *
from threading import Thread, Event

plan = Flask(__name__)

@plan.route('/')
def Main():
	return render_template('search.html')

@plan.route('/trip_page',methods =['POST'])
def getvalue():
    return render_template('trip.html')

@plan.route('/trip_page/test_page',methods =['POST'])
def setvalue():
    return render_template('test.html')

if __name__ == '__main__':
    plan.run()

