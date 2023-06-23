# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import desc

from datetime import datetime
from dateutil.relativedelta import relativedelta
from sqlalchemy import and_
from matplotlib import style
import matplotlib.pyplot as plt

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement, Station = Base.classes.measurement, Base.classes.station

# Create our session (link) from Python to the DB
session_link = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    print("Welcome, here are avaiable API Routes")
    return (
        f"List of Available API Routes </h1><br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>
        f"/api/v1.0/<start>/<end>"
    )

    #adding Session Link
    session_link = Session(engine)
    
    
