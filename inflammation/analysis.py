"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np
import argparse

from inflammation import models, views


class CSVDataSource:
    def __init__(self,data_dir):
        self.data_dir = data_dir

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir,'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.data_dir}")
        data = map(models.load_csv, data_file_paths)
        
        return data


class JSONDataSource:
    """Loads all inflammation*.json files inside a directory
    """
    def __init__(self,data_dir):
        self.data_dir = data_dir

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir,'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data JSON files found in path {self.data_dir}")
        data = map(models.load_json, data_file_paths)
        return data
        

def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    data = data_source.load_inflammation_data()

    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    graph_data = {
        'standard deviation by day': daily_standard_deviation
    }
    views.visualize(graph_data)

    return daily_standard_deviation

if __name__ == '__main__':
    # Initialize the parser
    parser = argparse.ArgumentParser(
        description="Calculate standard deviation by day between datasets."
    )
    
    # Add the data_dir argument
    parser.add_argument(
        'data_dir', 
        type=str, 
        help="Path to the directory containing the inflammation CSV files."
    )
    
    # Parse the arguments from the command line
    args = parser.parse_args()
    
    # Run the function using the provided argument
    analyse_data(args.data_dir)
