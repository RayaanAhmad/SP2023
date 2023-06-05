import pandas as pd

water_df = pd.read_csv("BKB_WaterCleaned.csv")

# Function that first shrinks the water_df to a single site we look at
# @ Param: string: site_name - Which site we look at, possible values are
#          {'Bay', 'D', 'B', 'C', 'A'}
# @ Returns: DataFrame: shrunk_df - Dataframe of only 1 site
def filter_site(site_name):
    shrunk_df = water_df.loc[ water_df["Site_Id"] == site_name]
    return shrunk_df
