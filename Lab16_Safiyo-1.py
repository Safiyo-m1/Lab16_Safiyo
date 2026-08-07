"""
Program Name: Lab16_Safiyo-1.py
Author: Safiyo Mohamed
Purpose: Reads Ohio's unemployment rate data and creates
a time series line plot of the unemployment rate using matplotlib.
Starter Code: No external starter code was used.
Date: 08/09/2026
"""
import csv
import matplotlib.pyplot as plt
from datetime import datetime 

class UnemploymentDataset:
    """Holds and loads Ohio unemployment data from a CSV file."""

    def __init__(self, filename):
        self.filename = filename
        self.dates = []
        self.rates = [] 


    def load(self):
        """Reads the CSV file, converts each row, and stores valid entries."""
        with open(self.filename, newline='') as csv_file:
            csv_reader = csv.reader(csv_file)

            for index, row in enumerate(csv_reader):
                # Row 0 is the header row; skip it after inspecting. 
                if index == 0:
                    continue

                date_str, rate_str = row[0], row[1]

                try:
                    current_date = datetime.strptime(date_str, "%Y-%m-%d")
                    current_rate = float(rate_str)
                except ValueError:
                    print(f"Skipping row {index}: invalid data {row}")
                    continue

                self.dates.append(current_date)
                self.rates.append(current_rate)

        return self 

 