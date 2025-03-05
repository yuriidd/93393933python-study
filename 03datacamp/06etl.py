#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Mon Feb 24 18:12:58 2025 @author: yurii"""


# %%####################################

#   EXTRACT
#   TRANSFORM
#   LOAD
#   LOGGING


# %%###################################         SQL
# #####################################             EXTRACT
# #####################################
import sqlalchemy
# Create a connection to the sales database
db_engine = sqlalchemy.create_engine("postgresql+psycopg2://repl:password@localhost:5432/sales")
# Query the sales table
raw_sales_data = pd.read_sql("SELECT * FROM sales;", db_engine)
print(raw_sales_data)


##

def extract():
    connection_uri = "postgresql+psycopg2://repl:password@localhost:5432/sales"
    db_engine = sqlalchemy.create_engine(connection_uri)

def extract():
    connection_uri = "postgresql+psycopg2://repl:password@localhost:5432/sales"
    db_engine = sqlalchemy.create_engine(connection_uri)
    raw_data = pd.read_sql("SELECT * FROM sales WHERE quantity_ordered = 1", db_engine)
    # Print the head of the DataFrame
    print(raw_data.head())
    # Return the extracted DataFrame
    return raw_data

## 
def extract(file_name):
    print(f"Extracting data from {file_name}")
    return pd.read_csv(file_name)

# parquet
sales_data = pd.read_parquet("sales_data.parquet", engine="fastparquet")

##
def extract():
    connection_uri = "postgresql+psycopg2://repl:password@localhost:5432/sales"
    db_engine = sqlalchemy.create_engine(connection_uri)


















# %%###################################         
# #####################################             TRANSFORM
# #####################################

# convert units

.to_datetime()
# "timestamps" column currectly looks like: "20230101085731"
# Convert "timestamps" column to type datetimecleaned
["timestamps"] = pd.to_datetime(cleaned["timestamps"], format="%Y%m%d%H%M%S")
# >> Timestamp('2023-01-01 08:57:31')


# "timestamps" column currently looks like: 1681596000011
# Convert "timestamps" column to type datatimecleaned
["timestamps"] = pd.to_datetime(cleaned["timestamps"], unit="ms")
# >> Timestamp('2023-04-15 22:00:00.011000')

print(df.nsmallest(10, ['timestamps']))
print(df.nlargest(10, ['timestamps']))


# 
def transform(source_table, target_table):      # f string for tables !! cool
  data_warehouse.execute(f"""
  CREATE TABLE {target_table} AS
      SELECT
          CONCAT("Product ID: ", product_id),
          quantity * price
      FROM {source_table};
  """)

def transform(data_frame):
  return data_frame.loc[:, ["industry_name", "number_of_firms"]]

#
#    for JSON TRANSFORM
'''Look at 02deinpy.py           JSON >> python'''
'''Look at 03pandas.py           API / JSON'''

def transform(raw_data):
	raw_data.fillna(
    	value={
			# Fill NaN values with column mean
			"math_score": raw_data["math_score"].mean(),
			"reading_score": raw_data["reading_score"].mean(),
			"writing_score": raw_data["writing_score"].mean()
		}, inplace=True
	)
	return raw_data




# %%###################################         
# #####################################             LOAD
# #####################################

#
def load(data_frame, file_name):
  # Write the data_frame to a CSV
  data_frame.to_csv('file_name')

###
# Custom CSV

df.to_csv("./stock.csv", 
          header=True,      # save header or not
          index=True,
          sep="|"           # default is ","
          )
df.to_parquet()
df.to_json()
df.to_sql()

###
# Check wheather file exists with `os` module
import os

stock_df.to_csv('stock.csv')

file_exists = os.path.exists('stock.csv')
print(file_exists)

##
def load(clean_data, file_path):
    clean_data.to_csv(file_path, header=False, index=False)   # Write the data to a file

    file_exists = os.path.exists(file_path)  # Check to make sure the file exists
    if not file_exists:
        raise Exception(f"File does NOT exists at path {file_path}")

# Load the transformed data to the provided file path
load(clean_sales_data, "transformed_sales_data.csv")


##





# %%###################################         
# #####################################             LOGGING
# #####################################

import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

# Create different types of logs
logging.debug(f"Variable has value {path}")
logging.info("Data has been transformed and will be loaded.")
logging.warning("Unexpected number of rows detected.")
logging.error("{ke} arose in execution.")

try:
    # execute some code here
except:
    # logging about failures that occured
    # logic to execute upon exception

##
try:
    # Try to filter by price_change
    clean_stock_data = transform(raw_stock_data)
    logging.info("Successfully filtered DataFrame by 'price_change'")
except: KeyError as ke:
    # Handle the error, create new column, transform
    logging.warning(f"{ke}: Cannot filter DataFrame by 'price_change'")
    raw_stock_data["price_change"] = raw_stock_data["close"] - raw_stock_data["open"]
    clean_stock_data = transform(raw_stock_data)


##
def extract(file_path):
    return pd.read_parquet(file_path)
try:  # Update the pipeline to include a try block
    raw_sales_data = extract("sales_data.parquet")  # Attempt to read in the file
except FileNotFoundError as file_not_found:  # Catch the FileNotFoundError
	logging.error(file_not_found)  # Write an error-level log
# >> ERROR: [Errno 2] No such file or directory: 'sales_data.parquet'


##




# %%###################################         
# #####################################             TESTING data pipelines
# #####################################

# ### validate loaded data
raw_tax_data = extract("raw_tax_data.csv")
clean_tax_data = transform(raw_tax_data)
load(clean_tax_data, "clean_tax_data.parquet")

print(f"Shape of raw_tax_data: {raw_tax_data.shape}")
print(f"Shape of clean_tax_data: {clean_tax_data.shape}")

to_validate = pd.read_parquet("clean_tax_data.parquet")
print(clean_tax_data.head(3))
print(to_validate.head(3))

print(to_validate.equals(clean_tax_data))  # Check that the DataFrames are equal


# ###
isinstance(clean_tax_data, pd.DataFrame)
assert isinstance(clean_tax_data, str)

# ###
import pytest

@pytest.fixture()           # Create a pytest fixture
def raw_tax_data():
	raw_data = extract("raw_tax_data.csv")
	return raw_data    # Return the raw DataFrame


# ###
@pytest.fixture()
def clean_tax_data():
    raw_data = pd.read_csv("raw_tax_data.csv")
    clean_data = transform(raw_data)
    return clean_data

# Pass the fixture to the function
def test_tax_rate(clean_tax_data):
    # Assert values are within the expected range
    assert (clean_tax_data["tax_rate"].max() <= 1 
            and clean_tax_data["tax_rate"].min() >= 0)


# ###
Running a data pipeline end-to-end
import logging
from pipeline_utils import extract, transform, load

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

try:
    # Extract, transform, and load data    
    raw_stock_data = extract("raw_stock_data.csv")
    clean_stock_data = transform(raw_stock_data)
    load(clean_stock_data)
    logging.info("Successfully extracted, transformed and loaded data.")  # Log success message
    
# Handle exceptions, log messages
except Exception as e:
    logging.error(f"Pipeline failed with error: {e}")








# %%###################################         
# #####################################             T
# #####################################













