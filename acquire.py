import pandas as pd

def acquire_logs():
    '''
    Convert txt file of curriculumn web logs to a raw dataframe
    
    Parameters: None
    
    Returns: df - dataframe
    '''
    df = pd.read_csv('anonymized-curriculum-access.txt',
                      engine='python',
                     header=None,
                     index_col=False,
                     sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
                     na_values='"-"',
                     )

    return df

def acquire_cohorts():
    '''
    Reads the cohorts.csv file into a pandas dataframe
    
    Parameters: None
    
    Returns: df - dataframe
    '''
    df = pd.read_csv('cohorts.csv')
    return df    