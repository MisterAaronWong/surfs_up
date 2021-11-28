##from flask import Flask
##app = Flask(__name__)
##@app.route('/')

##@app.route('/')
##def hello_world():
    ##return 'Hello world'

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
app = Flask(__name__)

##import app

##print("example __name__ = %s", __name__)

##if __name__ == "__main__":
    ##print("example is being run directly.")
##else:
    ##print("example is being imported")

@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

@app.route("/api/v1.0/precipitation")

# With our route defined, we'll create a new function
##def precipitation():
    ## return

# add the line of code that calculates the date one year ago from the most recent date in the database.
## def precipitation():
   ## prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   ## return

# Next, write a query to get the date and precipitation for the previous year.
## def precipitation():
   ## prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   ## precipitation = session.query(Measurement.date, Measurement.prcp).\
      ##filter(Measurement.date >= prev_year).all()
   ##return

# create a dictionary with the date as the key and the precipitation as the value.
#  "jsonify" our dictionary. Jsonify() is a function that converts the dictionary to a JSON file
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

@app.route("/api/v1.0/stations")

# With our route defined, we'll create a new function
## def stations():
    ## return

# create a query that will allow us to get all of the stations in our database.
##def stations():
    ##results = session.query(Station.station).all()
    ##return

# unravel our results into a one-dimensional array.
# use the function np.ravel(), with results as our parameter.
# convert our unraveled results into a list.
# use the list function, which is list(), and then convert that array into a list
# Then we'll jsonify the list and return it as JSON.
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# return the temperature observations for the previous year. As with the previous routes, begin by defining the route
@app.route("/api/v1.0/tobs")

# create a function called temp_monthly()
## def temp_monthly():
    ## return

# calculate the date one year ago from the last date in the database
## def temp_monthly():
    ## prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    ## return

# query the primary station for all the temperature observations from the previous year
## def temp_monthly():
    ## prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    ## results = session.query(Measurement.tobs).\
        ## filter(Measurement.station == 'USC00519281').\
        ## filter(Measurement.date >= prev_year).all()
    ## return

# unravel the results into a one-dimensional array and convert that array into a list.
# Then jsonify the list and return our results
## def temp_monthly():
    ## prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    ## results = session.query(Measurement.tobs).\
      ## filter(Measurement.station == 'USC00519281').\
      ## filter(Measurement.date >= prev_year).all()
    ## temps = list(np.ravel(results))

# jsonify our temps list, and then return it. Add the return statement to the end of your code
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# last route will be to report on the minimum, average, and maximum temperatures
# we will have to provide both a starting and ending date
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# create a function called stats()
## def stats():
    ## return

# add parameters to our stats()function: a start parameter and an end parameter. For now, set them both to None
## def stats(start=None, end=None):
    ## return

# create a query to select the minimum, average, and maximum temperatures from our SQLite database.
# start by just creating a list called sel
## def stats(start=None, end=None):
    ## sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

# Since we need to determine the starting and ending date, add an if-not statement to our code
# query our database using the list that we just made
# unravel the results into a one-dimensional array and convert them to a list
# jsonify our results and return them
# take note of the asterisk in the query next to the sel list
#  the asterisk is used to indicate there will be multiple results for our query: minimum, average, and maximum temperatures
## def stats(start=None, end=None):
    ##sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    ##if not end:
        ##results = session.query(*sel).\
            ##filter(Measurement.date >= start).all()
        ##temps = list(np.ravel(results))
        ##return jsonify(temps=temps)

# calculate the temperature minimum, average, and maximum with the start and end dates
# use the sel list, which is simply the data points we need to collect
# create our next query, which will get our statistics data.
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
