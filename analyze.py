import pandas as pd
import matplotlib.pyplot as plt

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
# @ Returns: string: graph_name - name of the graph as .png file
#            pyplot: image - the graph comparing the variables
def create_graph(paramed_df):
    name = "temp.png"
    headers = paramed_df.columns # The headers in the dataframe

    image = plt.figure() # The graph
    plt.xlabel(headers[0]) # X-Axis = param1 from pick_two()
    plt.ylabel(headers[1]) # Y-Axis = param2 from pick_two()

    x_values = paramed_df[headers[0]]
    y_values = paramed_df[headers[1]]
    plt.plot(x_values, y_values) # Plots one vs the other

    plt.title("Comparison")
    plt.savefig(name)
    return image, name

# Arbritary Testing
site = filter_site("A")
params = pick_two(site, "Salinity (ppt)", "pH (standard units)")
im, na = create_graph(params)
