from sklearn.preprocessing import OneHotEncoder
def prepare_chicago_features(df, attribs):
    """
    This function is just a convenient wrapper around the ColumnTransformer method for OneHotEncoding categorical features
    specific to the test data
    
    df: DataFrame
    attribs: Columns specified to be transformed. Expected data structure is a list
    
    returns: X(Sparse Matrix)
    """
    cat_encoder = OneHotEncoder()
    X = cat_encoder.fit_transform(df[attribs])
    
    return X