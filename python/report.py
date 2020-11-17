import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from csv import writer



BEST_FITNESS = 'best_fitness'
TIME = 'time'
ITER = 'iteration'


def add_to_csv(filename, best_fitness, iteration):
    filename = 'csv/' + filename + '.csv'
    with open(filename, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow([iteration, best_fitness, time.time()])