import pandas as pd
from acquire import acquire_logs 

def prepare_logs_all(df):
    '''
    Takes in a raw curriculum log dataframe and converts column headers to meaningful labels, and
    combines the separated date and time columns into a single column that is set as a datetime index.
    Missing cohort_id values are imputed with 0, representing users with an unknown cohort.
    Additionally, web pages that are not clearly curriculum are removed from the dataset.
    
    Parameters: df - dataframe to be cleaned
    
    Returns: df - dataframe
    '''
    df.columns = ['date','time','page_viewed','user_id','cohort_id','ip']

    df.index = pd.to_datetime(df.date + " " + df.time)

    df = df.drop(columns=['date','time'], axis=1)

    df['cohort_id'] = df.cohort_id.fillna(0)
    df['cohort_id'] = df.cohort_id.astype("int")

    df = df[df.cohort_id != 28]
    
    df = df[(df.page_viewed.str.contains('jpeg') != True) &
            (df.page_viewed.str.contains('json') != True) &
            (df.page_viewed.str.contains('jpg') != True) &
            (df.page_viewed != '/') & 
            (df.page_viewed != 'toc')]
            
    return df

def prepare_logs_ds(df):
    '''
    Takes in a raw curriculum log dataframe and converts column headers to meaningful labels, and
    combines the separated date and time columns into a single column that is set as a datetime index.
    Missing cohort_id values are imputed with 0, representing users with an unknown cohort.
    Using the cohort_id, the returned dataframe is limited to only data science cohorts.
    Additionally, web pages that are not clearly curriculum are removed from the dataset.
    
    Parameters: df - dataframe to be cleaned
    
    Returns: df - dataframe
    '''
    df.columns = ['date','time','page_viewed','user_id','cohort_id','ip']

    df.index = pd.to_datetime(df.date + " " + df.time)

    df = df.drop(columns=['date','time'], axis=1)

    df['cohort_id'] = df.cohort_id.fillna(0)
    df['cohort_id'] = df.cohort_id.astype("int")

    df = df[(df.cohort_id == 30) |
            (df.cohort_id == 34) |
            (df.cohort_id == 55) |
            (df.cohort_id == 59)]
    
    df = df[(df.page_viewed.str.contains('jpeg') != True) &
            (df.page_viewed.str.contains('json') != True) &
            (df.page_viewed.str.contains('jpg') != True) &
            (df.page_viewed != '/') & 
            (df.page_viewed != 'toc')]
            
    return df

def prepare_logs_wd(df):
    '''
    Takes in a raw curriculum log dataframe and converts column headers to meaningful labels, and
    combines the separated date and time columns into a single column that is set as a datetime index.
    Missing cohort_id values are imputed with 0, representing users with an unknown cohort.
    Using the cohort_id, the returned dataframe is limited to only data science cohorts.
    Additionally, web pages that are not clearly curriculum are removed from the dataset.
    
    Parameters: df - dataframe to be cleaned
    
    Returns: df - dataframe
    '''
    df.columns = ['date','time','page_viewed','user_id','cohort_id','ip']

    df.index = pd.to_datetime(df.date + " " + df.time)

    df = df.drop(columns=['date','time'], axis=1)

    df['cohort_id'] = df.cohort_id.fillna(0)
    df['cohort_id'] = df.cohort_id.astype("int")    
    
    # Note: Cohort_id #28 is designated as 'Staff' and will also be excluded
    df = df[(df.cohort_id != 28) &
               (df.cohort_id != 30) & 
               (df.cohort_id != 34) & 
               (df.cohort_id != 55) & 
               (df.cohort_id != 59)]

    df = df[(df.page_viewed.str.contains('jpeg') != True) &
            (df.page_viewed.str.contains('json') != True) &
            (df.page_viewed.str.contains('jpg') != True) &
            (df.page_viewed != '/') & 
            (df.page_viewed != 'toc')]
    
    return df

def acquire_prepare_logs():
    '''
    Combines the acquire and prepare functions to produce three dataframes 
    (a dataframe with both data science and web development students, 
    a dataframe consisting of only data science students,
    and a dataframe consisting of only web development students)
    
    Parameters: None
    
    Returns: combined, ds, wd - data science focused dataframe, web development focused dataframe
    '''
    df = acquire_logs()
    combined = prepare_logs_all(df)
    ds = prepare_logs_ds(df)
    wd = prepare_logs_wd(df)

    return combined, ds, wd