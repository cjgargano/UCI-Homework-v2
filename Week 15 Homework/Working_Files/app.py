# Import Dependencies
##################################################
import numpy as np
import pandas as pd

from flask import Flask, render_template, jsonify, request, redirect

##################################################
# Flask Setup
##################################################
app = Flask(__name__)

##################################################
# Read in CSV files
##################################################

samples_db = pd.read_csv("data/belly_button_biodiversity_samples.csv")
metadata_db = pd.read_csv("data/Belly_Button_Biodiversity_Metadata.csv")
otu_db = pd.read_csv("data/belly_button_biodiversity_otu_id.csv")

##################################################
# Flask Routes
##################################################

@app.route("/")
def index():
    return render_template("index.html")

##################################################

@app.route("/api/v1.0/names")
# List of Sample Names
def sample_names():
    sample_names_list = list(samples_db.columns.values)[1:]
    return jsonify(sample_names_list)

##################################################

@app.route("/api/v1.0/otu")
# List of OTU Descriptions

def otu_descriptions():
    otu_desc = list(otu_db['lowest_taxonomic_unit_found'])
    return jsonify(otu_desc)

##################################################

@app.route("/api/v1.0/metadata/<sample>")
# MetaData for a given sample.

def meta_sample(sample):

    try:
        meta_id = int(sample[3:len(sample)])
        i = metadata_db.loc[metadata_db["SAMPLEID"] == meta_id].index[0]

        meta_dict = {"Sample ID": sample,
                     "BB Type": metadata_db.loc[metadata_db["SAMPLEID"] == meta_id,"BBTYPE"][i],
                     "Age": metadata_db.loc[metadata_db["SAMPLEID"] == meta_id,"AGE"][i],
                     "Gender": metadata_db.loc[metadata_db["SAMPLEID"] == meta_id,"GENDER"][i],
                     "Ethnicity": metadata_db.loc[metadata_db["SAMPLEID"] == meta_id,"ETHNICITY"][i],
                     "Wash Frequency": metadata_db.loc[metadata_db["SAMPLEID"] == meta_id,"WFREQ"][i],
                     "Location": metadata_db.loc[metadata_db["SAMPLEID"] == meta_id,"LOCATION"][i]
                    }
        return jsonify(meta_dict)

    except (ValueError, IndexError):
        return (f"Data Unavailable for sample {sample}.  Please select another sample.")

##################################################

@app.route("/api/v1.0/wfreq/<sample>")
# Weekly Washing Frequency as a number.

def wash_freq(sample):

    try:
        meta_id = int(sample[3:len(sample)])
        i = metadata_db.loc[metadata_db["SAMPLEID"] == meta_id].index[0]
        wash_freq = int(metadata_db.loc[metadata_db['SAMPLEID'] == meta_id, 'WFREQ'][i])
        return jsonify(wash_freq)

    except ValueError:
        return (f"Data Unavailable for sample {sample}.  Please select another sample.")

##################################################

@app.route("/api/v1.0/samples/<sample>")
# OTU IDs and Sample Values for a given sample.

def sample_list(sample):

    try:
        otu_id = list(samples_db["otu_id"])
        sample_value = list(samples_db[sample])
        otu_desc = list(otu_db['lowest_taxonomic_unit_found'])

        n = len(otu_desc)
        
        otu_list = []
        value_list = []
        desc_list = []

        for i in range(0, n-1):

            if (sample_value[i] != 0 and pd.isnull(sample_value[i]) != True):
            
                otu_list.append(int(otu_id[i]))
                value_list.append(int(sample_value[i]))
                desc_list.append(otu_desc[i])
                
        sample_dict = {"otu_ids": otu_list,
                        "sample_values": value_list,
                        "otu_desc": desc_list
                        }

        return jsonify(sample_dict)

    except (ValueError):
        return (f"Value Error")

    except (TypeError):
        return (f"Type Error")


##################################################

if __name__ == "__main__":
    app.run(debug=True)