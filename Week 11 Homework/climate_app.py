####################################################################################################
# Import Dependencies
####################################################################################################
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


####################################################################################################
# Database Setup
####################################################################################################
engine = create_engine('sqlite:///hawaii.db')

Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to the tables
Stations = Base.classes.stations
Measures = Base.classes.measures

# Create our session (link) from Python to the DB
session = Session(engine)


####################################################################################################
# Flask Setup
####################################################################################################
app = Flask(__name__)


####################################################################################################
# Flask Routes
####################################################################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Avalable Routes:<br/>"
        f"1) Precipitation Analysis: /api/v1.0/precipitation<br/>"
        f"2) List of Stations: /api/v1.0/stations<br/>"
        f"3) Temperature Observations: /api/v1.0/tobs<br/>"
        f"4) Average Temp After Start Date: /api/v1.0/&ltstart&gt<br/>"
        f"5) Average Temp Between Start & End Dates: /api/v1.0/&ltstart&gt/&ltend&gt"
    )
####################################################################################################

####################################################################################################
@app.route("/api/v1.0/precipitation")
def precip_func():

    """Return a list of dates and precipitation observations from the past year.
    Each item in the list is a dictionary with keys `date` and `prcp`"""

    # Query all prcp observations from the Measures table
    results = session.query(Measures.date, Measures.prcp).filter(Measures.date > "2016-08-25").\
        group_by(Measures.date).all()

    # Create a list of dicts with `date` and `prcp` as the keys
    prcp_totals = []
    for result in results:
        row = {}
        row["date"] = result[0]
        row["prcp"] = float(result[1])
        prcp_totals.append(row)

    return jsonify(prcp_totals)
####################################################################################################

####################################################################################################
@app.route("/api/v1.0/stations")
def stations_func():

    """Return a list of stations from the Stations table."""
    results = session.query(Stations.name).order_by(Stations.name).all()

    return jsonify(results)
####################################################################################################

####################################################################################################
@app.route("/api/v1.0/tobs")
def tobs_func():
    
    """Return a list of dates and temperature observations (tobs) from the past year.
    Each item in the list is a dictionary with keys `date` and `tobs`"""

    # Query all tobs observations from the Measures table
    results = session.query(Measures.date, Measures.tobs).filter(Measures.date > "2016-08-25").\
        group_by(Measures.date).all()

    # Create a list of dicts with `date` and `prcp` as the keys
    tobs_totals = []
    for result in results:
        row = {}
        row["date"] = result[0]
        row["tobs"] = float(result[1])
        tobs_totals.append(row)

    return jsonify(tobs_totals)
####################################################################################################

####################################################################################################
@app.route("/api/v1.0/<start_date>")
def temp_start(start_date="2017-05-04"):
    
    qry = session.query(Measures.date, Measures.tobs).filter(Measures.date >= start_date)\
        .group_by(Measures.date).all()
    
    df = pd.DataFrame({'temp': [result[1] for result in qry[:len(qry)]]})
    
    temp_df = pd.DataFrame({"Measure": ["Min Temp", "Avg Temp", "Max Temp"],
        "Value": [df.min().values[0], df.mean().values[0], df.max().values[0]]})

    temp_dict = dict(zip(temp_df.Measure, temp_df.Value))

    return jsonify(temp_dict)
####################################################################################################

####################################################################################################
@app.route("/api/v1.0/<start_date>/<end_date>")
def temp_start_end(start_date="2017-05-04", end_date="2017-05-18"):
    
    qry = session.query(Measures.date, Measures.tobs).filter(Measures.date >= start_date)\
        .filter(Measures.date <= end_date).group_by(Measures.date).all()
    
    df = pd.DataFrame({'temp': [result[1] for result in qry[:len(qry)]]})
    
    temp_df = pd.DataFrame({"Measure": ["Min Temp", "Avg Temp", "Max Temp"],
        "Temp": [df.min().values[0], df.mean().values[0], df.max().values[0]]})

    temp_dict = dict(zip(temp_df.Measure, temp_df.Temp))

    return jsonify(temp_dict)
####################################################################################################

####################################################################################################
if __name__ == "__main__":
    app.run(debug=True)