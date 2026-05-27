#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse

from inflammation import models, views, analysis
import os





def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    infiles = args.infiles
    if not isinstance(infiles, list):
        infiles = [args.infiles]

    for filename in infiles:
        inflammation_data = models.load_csv(filename)

        view_data = {
            "average": models.daily_mean(inflammation_data),
            "max": models.daily_max(inflammation_data),
            "min": models.daily_min(inflammation_data),
        }

        views.visualize(view_data)
    
    data_dir = os.path.dirname(infiles[0])

    _, extension = os.path.splitext(infiles[0])
    if extension == '.csv':
        data_source = analysis.CSVDataSource(data_dir=data_dir)
    elif extension == '.json': 
        data_source = analysis.JSONDataSource(data_dir=data_dir)

    data_source = analysis.CSVDataSource(data_dir=data_dir)
    data= data_source.load_inflammation_data()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A basic patient inflammation data management system"
    )

    parser.add_argument(
        "infiles",
        nargs="+",
        help="Input CSV(s) containing inflammation series for each patient",
    )

    args = parser.parse_args()

    main(args)
