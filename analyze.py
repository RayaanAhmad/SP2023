import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

water_df = pd.read_csv("BKB_WaterCleaned.csv") # Initialize the DataFrame on launch

# Notes:
# Site : [ A, B, C, D, Bay ]
# Size of DF: [ 156, 164, 100, 194, 661 ]

# Function that first shrinks the water_df to a single site we look at
# @ Param: string: site_name - Which site we look at, possible values are
#          {'Bay', 'D', 'B', 'C', 'A'}
# @ Returns: DataFrame: site_df - Dataframe of only 1 site
def filter_site(site_name):
    site_df = water_df.loc[ water_df["Site_Id"] == site_name]
    return site_df


# Function that takes a site, and filters into the given parameters to compare
# @ Param: DataFrame: site_df - DataFrame from filter_site()
#          string: param1 - Value we are comparing # 1 (X-Axis)
#          string: param2 - Value we are comparing # 2 (Y-Axis)
# @ Returns: DataFrame: paramed_df - Dataframe keeping the two given params
def pick_two(site_df, param1, param2):
    paramed_df = site_df[ [param1, param2] ]
    return paramed_df


# Function: takes given parameters and puts into a graph
# @ Param: DataFrame: paramed_df - Dataframe with first column as X-Axis and second as Y-Axis
#          string: site_name - Name of the chosen site
# @ Returns: string: graph_name - name of the graph as .png file
#                    corr_equations - line of best fit and r^2 values
#            pyplot: null_img - return this to clear the graph
def create_graph(paramed_df, site_name):
    headers = paramed_df.columns # The headers in the dataframe
    x_ax = headers[0].split(' ')[0]
    y_ax = headers[1].split(' ')[0] # Get labels of the X and Y axis w/o units
    title = x_ax + ' vs. ' + y_ax   # Title of the graph

    null_img = plt.figure() # Placeholder
    plt.xlabel(headers[0]) # X-Axis = param1 from pick_two()
    plt.ylabel(headers[1]) # Y-Axis = param2 from pick_two()

    x_values = paramed_df[headers[0]]
    y_values = paramed_df[headers[1]]
    plt.plot(x_values, y_values, '.') # Plots one vs the other at points, no connecting lines

    m, b = np.polyfit(x_values, y_values, 1)
    plt.plot(x_values, m*x_values + b) # Add line of best fit with equation of degree 1

    matrix = np.corrcoef(x_values, y_values)
    corr = matrix[0, 1]
    r_squared = corr ** 2 # Getting the value of r^2

    corr_equations = 'y = ' + '{:.3f}'.format(m) + 'x + ' + '{:.3f}'.format(b) \
                     + '\nr^2 = ' + '{:.3f}'.format(r_squared)

    # Write the equation and value of r^2 at the bottom left

    name = site_name + "_" + x_ax + "_" + y_ax + ".png" # Create custom name of png
    plt.title(title)
    plt.savefig(name)
    return name, corr_equations, null_img # Return us the name of the graph

# Arbritary Testing ## LEAVE COMMENTED OR ELSE BREAKS INTERFACE.PY
# site = filter_site("A")
# params = pick_two(site, "Salinity (ppt)", "pH (standard units)")
# im, na = create_graph(params, "A")
