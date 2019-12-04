# Title: UMD Energy Usage

## Introduction

In this project I analyzed a dataset of energy use by buildings at the
University of Maryland available from the [TerpFootprints]. Specifically I was
interested in seeing what buildings use the most energy per square foot.

## Data

The TerpFootprints website makes information for individual buildings available
but does not make the entire dataset easily available. I wrote a scraping
program that downloads the data one at at time and aggregates it as a series of
CSV files. The ones that I use here are:

- buildings.csv: metadata about the buildings, including name and area (square feet)
- energy.csv: time series data about the energy use by building

These two files are included as part of the directory of files you are looking
aat here.

## Run

To run my program you will need to have [Pandas] installed.

    pip3 install pandas

After that you should be able to run my program:

    python3 analyze.py

This will print out the buildings and their average energy use per square foot.
The results are also stored in a CSV file for additional processing.

## Credits

This project was created by Ed Summers who did the data collection, analysis and
documentation.

[TerpFootprints]: https://terpfootprints.umd.edu/
[Pandas]: https://pandas.pydata.org/





