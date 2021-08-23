from flask import Flask, render_template, jsonify, request

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt
import os
import numpy as np

# --------------------
# Database Setup
# --------------------
engine = create_engine(f"sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Date to be used in quieries, query_date specifies the last recent year, using last date in data set
query_date = dt.date(2017, 8, 23) - dt.timedelta(days=1) - dt.timedelta(weeks=52)

# Columns to select min, max, avg temperatures
sel = [func.min(Measurement.tobs).label("Min temp"),
       func.max(Measurement.tobs).label("Max temp"),
       func.avg(Measurement.tobs).label("Average temp")]

# Define function to convert string to date in format: year, month, day
def str_to_date(date_str):
    pass_param = [int(x) for x in date_str.split("&")]
    date = dt.date(pass_param[0], pass_param[1], pass_param[2],)
    return date

# --------------------
# Flask Setup
# --------------------
app = Flask(__name__)


# --------------------
# Flask Routes
# --------------------

# List all available api routes
@app.route("/")
def index():
    # Get base ulr root
    url_root = request.url_root;
    # Return html page with available routes, pass all required parameters
    return render_template('index.html', title = "Available Routes", url_root = url_root,
                            prcp = "api/v1.0/precipitation", prcp_title = "Precipitation",
                            stts = "api/v1.0/stations", stts_title = "Stations",
                            tobs = "api/v1.0/tobs", tobs_title = "Temperature observations for the last year of data",
                            start_date = "api/v1.0/startdate/2016&8&23", stdt_title = "Temperature: min, avg, max for Dates > Start Date",
                            end_date = "2017&8&23", steddt_title = "Temperature: min, avg, max for Start Date < Dates < End Date")

# List all precipitation values for the last year
@app.route("/api/v1.0/precipitation")
def prcp():
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Save query result into variable
    prcp_12_months = session.query(Measurement.date, Measurement.prcp).\
                        filter(Measurement.date>=query_date).\
                        filter(Measurement.prcp!=None).\
                        order_by(Measurement.date).all()
    # Close session
    session.close()

    # Convert the query result into a list of dictionaries
    all_prcp = []
    for date, prcp in prcp_12_months:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["percipitation"] = prcp
        all_prcp.append(prcp_dict)

    # Return JSON representation of result
    return jsonify(all_prcp)

# List all stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    # Query all stations
    stations = session.query(Station.station).\
            order_by(Station.station).all()
    
    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(stations))

    return jsonify(all_stations)

# List the dates and temperature observations of the most active station for the last year of data.
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    # Find the most active station
    act_stt = session.query(Station.station, func.count(Measurement.station)).\
            filter(Station.station == Measurement.station).\
            group_by(Station.station).order_by(func.count(Measurement.station).desc()).first()[0]

    # Join Measurement and Station tables to get temperatures
    tobs_12_months = session.query(Measurement.date, Measurement.tobs).\
                        filter(Station.station == Measurement.station).\
                        filter(Station.station == act_stt).\
                        filter(Measurement.date>=query_date).all()
    
    session.close()

    all_tobs = []
    for date, tobs in tobs_12_months:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["temperature"] = tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)

# List the minimum, the average, and the max temperature starting from a given start date
# To change the date user need to set date parameters in url path and reload the page
@app.route("/api/v1.0/startdate/<start_date_str>")
def start(start_date_str):
    session = Session(engine)

    # Convert string date value from url to date
    start_date = str_to_date(start_date_str)

    # Perform query
    temps = session.query(*sel).\
            filter(Station.station == Measurement.station).\
            filter(Measurement.date>=start_date).all()
    
    session.close()

    all_temp = list(np.ravel(temps))

    return jsonify(all_temp)

# List the minimum, the average, and the max temperature for a given start-end date range
@app.route("/api/v1.0/startdate/<start_date_str>/<end_date_str>")
def startend(start_date_str, end_date_str):
    session = Session(engine)

    # Convert start and end date value from url from string to date
    start_date = str_to_date(start_date_str)
    end_date = str_to_date(end_date_str)

    temps = session.query(*sel).\
            filter(Station.station == Measurement.station).\
            filter(Measurement.date>=start_date).\
            filter(Measurement.date<=end_date).all()
    
    session.close()

    all_temp = list(np.ravel(temps))

    return jsonify(all_temp)

if __name__ == '__main__':
    app.run(debug=True)