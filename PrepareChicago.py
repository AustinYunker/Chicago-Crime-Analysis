def prepare_chicago(df, attribs):
    """
    This function is just a convenient wrapper around the ColumnTransformer method for OneHotEncoding categorical features
    specific to the test data
    
    df: DataFrame
    attribs: Columns specified to be transformed. Expected data structure is a list
    
    returns: X(Sparse Matrix): y(Series)
    """
    cat_encoder = OneHotEncoder()
    X = cat_encoder.fit_transform(df[attribs])
    
    y = (df["arrest"] == True).astype(np.int)
    return X, y