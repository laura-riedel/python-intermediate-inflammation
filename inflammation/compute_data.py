"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views

class CSVDataSource():
    """
    Class for loading the data csvs.

    :param data_path: name of directory containing csv files
    """
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_data(self):
        """
        Automatically loads all inflammation csvs from directory.
        """
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.data_dir}")
        return list(map(models.load_csv, data_file_paths))
    
def compute_standard_deviation_by_day(data):
    """
    Computes the mean inflammation value for each day across all datasets,
    then computes the daily standard deviation
    """
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    return daily_standard_deviation

def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the standard deviation of mean inflammation values 
    for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    data = data_source.load_data()

    daily_standard_deviation = compute_standard_deviation_by_day(data)

    # graph_data = {
    #     'standard deviation by day': daily_standard_deviation,
    # }
    # views.visualize(graph_data)
    return daily_standard_deviation
