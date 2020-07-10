from flask import *
from threading import Thread, Event

plan = Flask(__name__)

@plan.route('/')
def Main():
	return render_template('trip.html')

@plan.route('/',methods =['POST'])
def getvalue():
    return render_template('route.html')

if __name__ == '__main__':
    plan.run()

