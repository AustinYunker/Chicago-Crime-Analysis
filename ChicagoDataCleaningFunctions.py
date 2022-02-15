"""
This file contains all the functions used to clean the data for the Chicago Analysis Project
"""

def crime_type_cleaner(df):
    """
    This function cleans the primary_type column in place. 
    
    df: DataFrame with primary_type column
    
    returns: None
    """
    df.loc[:, "primary_type"].replace(["CRIM SEXUAL ASSAULT"], "CRIMINAL SEXUAL ASSAULT", inplace = True)

    df.loc[:, "primary_type"].replace(["OTHER NARCOTIC VIOLATION"], "NARCOTICS", inplace = True)

    df.loc[:, "primary_type"].replace(["NON - CRIMINAL", "NON-CRIMINAL (SUBJECT SPECIFIED)"], "NON-CRIMINAL", inplace = True)

    df.loc[:, "primary_type"].replace(["RITUALISM"], "OTHER OFFENSE", inplace = True)
    
def location_imputer(df):
    """
    This function imputes missing values in the location_description column by setting the missing value to the value that 
    occurs most in the primary_type column in place
    
    df: DataFrame that contains the location_description column
    
    returns: None
    """
    mask = (df.loc[:, "primary_type"] == "DECEPTIVE PRACTICE") & (df.loc[:, "location_description"].isnull())
    df.loc[mask, ["location_description"]] = "RESIDENCE"
    
    mask = (df.loc[:, "primary_type"] == "THEFT") & (df.loc[:, "location_description"].isnull())
    df.loc[mask, ["location_description"]] = "STREET"
    
    crime_type = ["BURGLARY", "ROBBERY", "BATTERY", "CRIMINAL DAMAGE", "ARSON", "CRIMINAL SEXUAL ASSAULT", "OTHER OFFENSE"]
    mask = (df.loc[:, "primary_type"].isin(crime_type)) & (df.loc[:, "location_description"].isnull())
    df.loc[mask, ["location_description"]] = "RESIDENCE"

    
def location_cleaner(df):
    """
    This function cleans the location_description by merging categories together that are logically related in place.
    
    df: DataFrame that contains the location_description column
    
    returns: None
    """

    #Combine all values related to CTA
    CTA = ["CTA TRAIN", "CTA PLATFORM", "CTA BUS", "CTA BUS STOP", "CTA STATION", "CTA GARAGE / OTHER PROPERTY", 
           "CTA TRACKS - RIGHT OF WAY", "CTA PARKING LOT / GARAGE / OTHER PROPERTY", """CTA "L" PLATFORM""",
          "CTA PROPERTY", """CTA "L" TRAIN""", "CTA SUBWAY STATION"]
    df["location_description"].replace(CTA, "CTA", inplace = True)

    #Combine GANGWAY into ALLEY
    df["location_description"].replace(["GANGWAY"], "ALLEY", inplace = True)

    #Combine all values related to Sports/Clubs
    sports = ["ATHLETIC CLUB", "SPORTS ARENA/STADIUM", "SPORTS ARENA / STADIUM", "CLUB"]
    df["location_description"].replace(sports, "SPORTS", inplace = True)

    #Combine all values related to VACANT
    vacant = ["VACANT LOT/LAND", "VACANT LOT / LAND", "VACANT LOT"]
    df["location_description"].replace(vacant, "VACANT", inplace = True)

    #Combine the two Gas Station values
    df["location_description"].replace(["GAS STATION DRIVE/PROP."], "GAS STATION", inplace = True)

    #Combine all values related to Water/River/Lake
    water = ["LAKEFRONT/WATERFRONT/RIVERBANK", "POOL ROOM", "BOAT/WATERCRAFT", "LAKEFRONT / WATERFRONT / RIVERBANK", 
             "BOAT / WATERCRAFT", "RIVER BANK", "POOLROOM", "LAKE", "LAGOON"]
    df["location_description"].replace(water, "WATER", inplace = True)

    #Combine all values related to Banks/Credit Unions
    bank = ["ATM (AUTOMATIC TELLER MACHINE)", "CURRENCY EXCHANGE", "CREDIT UNION", "SAVINGS AND LOAN"]
    df["location_description"].replace(bank, "BANK", inplace = True)

    #Combine all values related to Roads/Streets/Highway
    street = ["HIGHWAY/EXPRESSWAY", "BRIDGE", "HIGHWAY / EXPRESSWAY", "EXPRESSWAY EMBANKMENT"]
    df["location_description"].replace(street, "STREET", inplace = True)

    #Combine all values related to Residence/Houses or items inside a House
    residence = ["RESIDENCE PORCH/HALLWAY", "RESIDENCE-GARAGE", "RESIDENCE - YARD (FRONT / BACK)", "RESIDENCE - PORCH / HALLWAY", 
           "RESIDENCE - GARAGE", "RESIDENTIAL YARD (FRONT/BACK)", "HOUSE", "ROOMING HOUSE", "PORCH", "YARD", "HALLWAY", "GARAGE",
          "VESTIBULE", "STAIRWELL", "BASEMENT", "LAUNDRY ROOM", "DRIVEWAY", "DRIVEWAY - RESIDENTIAL"]
    df["location_description"].replace(residence, "RESIDENCE", inplace = True)

    #Combine all values related to College
    college = ["COLLEGE/UNIVERSITY GROUNDS", "COLLEGE/UNIVERSITY RESIDENCE HALL", "COLLEGE / UNIVERSITY - GROUNDS", 
           "COLLEGE / UNIVERSITY - RESIDENCE HALL"]
    df["location_description"].replace(college, "COLLEGE", inplace = True)

    #Combine all values related to CTA into one CTA category
    veh = ["VEHICLE NON-COMMERCIAL", "VEHICLE-COMMERCIAL", "VEHICLE - OTHER RIDE SHARE SERVICE (E.G., UBER, LYFT)", 
           "VEHICLE - OTHER RIDE SERVICE", "VEHICLE - DELIVERY TRUCK", "VEHICLE - OTHER RIDE SHARE SERVICE (LYFT, UBER, ETC.)", 
           "VEHICLE - COMMERCIAL", "VEHICLE-COMMERCIAL - TROLLEY BUS", "VEHICLE-COMMERCIAL - ENTERTAINMENT/PARTY BUS", 
           "VEHICLE - COMMERCIAL: TROLLEY BUS", "VEHICLE - COMMERCIAL: ENTERTAINMENT / PARTY BUS", "TAXICAB", "",
          "AUTO / BOAT / RV DEALERSHIP", "AUTO", "DELIVERY TRUCK", "GARAGE/AUTO REPAIR", "TAXI CAB", "TRUCK", "TRAILER"]
    df["location_description"].replace(veh, "VEHICLE", inplace = True)

    #Combine all values related to Police/Fire Station/Protection
    police = ["POLICE FACILITY/VEH PARKING LOT", "POLICE FACILITY / VEHICLE PARKING LOT", "JAIL / LOCK-UP FACILITY",
             "FIRE STATION", "FOREST PRESERVE"]
    df["location_description"].replace(police, "POLICE", inplace = True)

    #Combine all values related to Parking
    parking = ["PARKING LOT/GARAGE(NON.RESID.)", "CHA PARKING LOT/GROUNDS", "PARKING LOT / GARAGE (NON RESIDENTIAL)", 
            "CHA PARKING LOT / GROUNDS", "PARKING LOT", "CHA PARKING LOT"]
    df["location_description"].replace(parking, "PARKING", inplace = True)

    #Combine all values related to Airports
    air = ["AIRPORT TERMINAL UPPER LEVEL - SECURE AREA", "AIRPORT TERMINAL LOWER LEVEL - NON-SECURE AREA", 
           "AIRPORT BUILDING NON-TERMINAL - NON-SECURE AREA", "AIRPORT VENDING ESTABLISHMENT", "AIRPORT/AIRCRAFT", "AIRCRAFT", 
           "AIRPORT PARKING LOT", "AIRPORT EXTERIOR - NON-SECURE AREA", "AIRPORT TERMINAL LOWER LEVEL - SECURE AREA", 
           "AIRPORT BUILDING NON-TERMINAL - SECURE AREA", "AIRPORT EXTERIOR - SECURE AREA", "AIRPORT TRANSPORTATION SYSTEM (ATS)",
           "AIRPORT TERMINAL MEZZANINE - NON-SECURE AREA", "AIRPORT TERMINAL UPPER LEVEL - NON-SECURE AREA"]
    df["location_description"].replace(air, "AIRPORT", inplace = True)

    #Combine all values related to School/Day Care
    school = ["SCHOOL, PUBLIC, BUILDING", "SCHOOL, PUBLIC, GROUNDS", "SCHOOL - PUBLIC BUILDING", "SCHOOL - PUBLIC GROUNDS", 
              "PUBLIC HIGH SCHOOL", "SCHOOL, PRIVATE, BUILDING", "SCHOOL, PRIVATE, GROUNDS", "SCHOOL - PRIVATE BUILDING", 
              "SCHOOL - PRIVATE GROUNDS", "SCHOOL YARD", "DAY CARE CENTER"]
    df["location_description"].replace(school, "SCHOOL", inplace = True)

    #Combine all values related to Bar/Tavern/Restaurant
    restaurant = ["BAR OR TAVERN", "TAVERN"]
    df["location_description"].replace(restaurant, "RESTAURANT", inplace = True)

    #Combine all values related to stores
    store = ["SMALL RETAIL STORE", "DEPARTMENT STORE", "GROCERY FOOD STORE", "CONVENIENCE STORE", "DRUG STORE", 
             "TAVERN/LIQUOR STORE", "CLEANING STORE", "APPLIANCE STORE", "TAVERN / LIQUOR STORE", "RETAIL STORE", 
             "LIQUOR STORE", "NEWSSTAND", "PAWN SHOP", "MOVIE HOUSE/THEATER", "MOVIE HOUSE / THEATER", "BARBERSHOP", 
             "CAR WASH", "COIN OPERATED MACHINE", "BOWLING ALLEY","KENNEL", "BARBER SHOP/BEAUTY SALON", "CLEANERS/LAUNDROMAT"]
    df["location_description"].replace(store, "STORE", inplace = True)

    #Combine all values related to hospitals or nursing homes
    hos = ["HOSPITAL BUILDING/GROUNDS", "HOSPITAL BUILDING / GROUNDS", "ANIMAL HOSPITAL", "NURSING HOME/RETIREMENT HOME", 
           "NURSING / RETIREMENT HOME", "NURSING HOME"]
    df["location_description"].replace(hos, "HOSPITAL", inplace = True)

    #Combine all values related to hotels/motels
    hotel = ["HOTEL/MOTEL", "HOTEL / MOTEL", "MOTEL"]
    df["location_description"].replace(hotel, "HOTEL", inplace = True)

    #Combine all values related to offices
    office = ["COMMERCIAL / BUSINESS OFFICE", "MEDICAL/DENTAL OFFICE", "MEDICAL / DENTAL OFFICE"]
    df["location_description"].replace(office, "OFFICE", inplace = True)

    #Combine all values related to buildings
    building = ["ABANDONED BUILDING", "GOVERNMENT BUILDING/PROPERTY", "FACTORY/MANUFACTURING BUILDING", 
                "GOVERNMENT BUILDING / PROPERTY", "FEDERAL BUILDING", "FACTORY / MANUFACTURING BUILDING", "GOVERNMENT BUILDING",
               "WAREHOUSE", "ELEVATOR", "YMCA"]
    df["location_description"].replace(building, "BUILDING", inplace = True)

    #Combine all values related to Chicago Housing Authority (CHA)
    cha = ["CHA APARTMENT", "CHA HALLWAY/STAIRWELL/ELEVATOR", "CHA HALLWAY / STAIRWELL / ELEVATOR", "CHA GROUNDS", 
           "CHA PLAY LOT", "CHA HALLWAY", "CHA ELEVATOR"]
    df["location_description"].replace(cha, "CHA", inplace = True)

    #Combine all values related to Church
    church = ["CHURCH/SYNAGOGUE/PLACE OF WORSHIP", "CHURCH / SYNAGOGUE / PLACE OF WORSHIP", "CHURCH PROPERTY"]
    df["location_description"].replace(church, "CHURCH", inplace = True)

    #Combine all other miscellaneous vaules
    other = ["OTHER (SPECIFY)", "OTHER RAILROAD PROP / TRAIN DEPOT", "OTHER COMMERCIAL TRANSPORTATION", 
             "OTHER RAILROAD PROPERTY / TRAIN DEPOT", "CEMETARY", "FARM", "HORSE STABLE", "RAILROAD PROPERTY",
             "WOODED AREA", "SEWER"]
    df["location_description"].replace(other, "OTHER", inplace = True)
    

def crime_month(df):
    """
    This function creates a new column that contains the month the crime occurred.
    
    df: DataFrame that has a column for the date the crime occurred.
    
    returns: None
    
    """
    df["Month"] = pd.Categorical(df.loc[:, "date"].dt.month, categories=range(1,13))
    
def crime_hour(df):
    """
    This function creates a new column that contains the hour the crime occurred.
    
    df: DataFrame that has a column for the date the crime occurred.
    
    returns: None
    
    """
    df["Hour"] = pd.Categorical(df.loc[:, "date"].dt.hour, categories = range(1, 13))
    
def community_cleaner(df):
    """
    This function cleans the community_name column by dropping those rows with missing values.
    
    df: DataFrame that contains the community_name column
    
    returns: None
    """
    df.dropna(subset=["community_name"], inplace = True)

    
def chicago_data_cleaner(df, clean_crime = True, impute_location = True, clean_location = True, add_month = True,
                                add_hour = True, clean_community = True, verbose = False):
    """
    This function is a wrapper over various functions to clean the columns in the Chicago data set in place
    
    The parameters are boolean values to decide if each individual function should be call on the data set
    
    returns: None
    """
    if verbose: print("Cleaning Started...\n")
    if clean_crime:
        crime_type_cleaner(df)
        if verbose: print("Successfully Cleaned Primary Type")
        
    if impute_location:
        location_imputer(df)
        if verbose: print("Successfully Imputed Location")
    
    if clean_location:
        location_cleaner(df)
        if verbose: print("Successfully Cleaned Location")  
    
    if add_month:
        crime_month(df)
        if verbose: print("Successfully Added Month Column")
        
    if add_hour:
        crime_hour(df)
        if verbose: print("Successfully Added Hour Column")
        
    if clean_community:
        community_cleaner(df)
        if verbose: print("Successfully Cleaned Community\n")
        
    df.reset_index(drop = True, inplace = True)
    
    if verbose: print("Data Set Successfully Cleaned!")

    
