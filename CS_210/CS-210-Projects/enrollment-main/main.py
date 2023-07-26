"""Enrollment analysis:  Summary report of majors enrolled in a class.
CS 210 project, Spring 2022.
Author:  John Moore
Credits: Soundcloud Rap music to electirc guitar background for focus.
"""

import doctest
import csv

def read_csv_column(path: str, field: str) -> list[str]:
    """Read one column from a CSV file with headers into a list of strings."""
    
    with open('C:\\Users\\johnm\\dev\\UO CS Work\\CS 210\\CS-210-Projects\\enrollment-main\\data\\test_roster.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            print(line)
            