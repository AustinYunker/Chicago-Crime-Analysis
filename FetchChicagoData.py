import pandas as pd
from pandas.io import gbq

def fetch_chicago_data(query_string, project_id, excel_file, verbose = True):
    """
    This function fetches the data from Google BigQuery. First a query is made based on the specified query string and
    project id. Next, an excel file with the Chicago districts are read in and joined with the original data. Finally, 
    a duplicate column is dropped.
    
    query_string: String with the specific query to be passed to Google BigQuery
    project_id: Corresponding project id in Google BigQuery
    excel_file: Path to the excel file containing chicago districts
    
    returns: pandas dataframe with the queried and joined data
    """
    
    if verbose: print("Fetching Chicago Data Started...\n")
        
    #Read the data in from Google BigQuery
    chicago_data = gbq.read_gbq(query_string, project_id=project_id)
    if verbose: print("Successfully queried Google BigQuery.")
        
    #Read in an Excel file with a one to one mapping between Chicago community areas and districts
    chicago_districts = pd.read_excel(excel_file)
    if verbose: print("Sucessfully read in excel file.")
        
    #Data type can't be joined on an int
    chicago_districts.community_area = chicago_districts["community_area"].astype("string")
    chicago_data.community_area = chicago_data["community_area"].astype("string")
        
    #Outer join the two data sets
    chicago = chicago_data.merge(chicago_districts, how="outer", left_on="community_area", right_on="community_area")
    if verbose: print("Sucessfully joined Chicago districts to main data.")
    
    #Drop the community area variable since we have a community name variable
    chicago.drop("community_area", axis = 1, inplace = True)
    if verbose: print("Successfully dropped duplicate column")
        
    if verbose: print("\nSucccessfully fetched Chicago Data")
        
    return chicago