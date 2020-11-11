import pandas as pd
from acquire import acquire_logs
from acquire import acquire_cohorts

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

def prepare_merge_logs_all(df):
    '''
    Takes in a raw curriculum log dataframe and converts column headers to meaningful labels, and
    combines the separated date and time columns into a single column that is set as a datetime index.
    Missing cohort_id values are imputed with 0, representing users with an unknown cohort.
    Additionally, web pages that are not clearly curriculum are removed from the dataset.
    IMPORTANT: This will also merge the dataframe with the cohort data from the cohorts.csv file
    
    Parameters: df - dataframe to be cleaned
    
    Returns: df - dataframe
    '''
    cohorts = acquire_cohorts()
    cohorts.loc[46] = [0, 'Missing', '2014-02-04', '2021-05-04', 0]

    df.columns = ['date','time','page_viewed','user_id','cohort_id','ip']

    df['cohort_id'] = df.cohort_id.fillna(0)
    df['cohort_id'] = df.cohort_id.astype("int")

    df = pd.merge(df, cohorts, left_on='cohort_id', right_on='cohort_id')

    df.index = pd.to_datetime(df.date + " " + df.time)
    df.start_date = pd.to_datetime(df.start_date, format='%Y-%m-%d')
    df.end_date = pd.to_datetime(df.end_date, format='%Y-%m-%d')
    df = df.drop(columns=['date','time'], axis=1)

    df = df[df.cohort_id != 28]
    
    df = df[(df.page_viewed.str.contains('jpeg') != True) &
            (df.page_viewed.str.contains('json') != True) &
            (df.page_viewed.str.contains('jpg') != True) &
            (df.page_viewed != '/') & 
            (df.page_viewed != 'toc')]

    active = (df.index > df.start_date) & (df.index < df.end_date)
    df['active'] = active

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

def prepare_merge_logs_ds(df):
    '''
    Takes in a raw curriculum log dataframe and converts column headers to meaningful labels, and
    combines the separated date and time columns into a single column that is set as a datetime index.
    Missing cohort_id values are imputed with 0, representing users with an unknown cohort.
    Using the cohort_id, the returned dataframe is limited to only data science cohorts.
    Additionally, web pages that are not clearly curriculum are removed from the dataset.
    IMPORTANT: This will also merge the dataframe with the cohort data from the cohorts.csv file

    Parameters: df - dataframe to be cleaned
    
    Returns: df - dataframe
    '''
    cohorts = acquire_cohorts()
    cohorts.loc[46] = [0, 'Missing', '2014-02-04', '2021-05-04', 0]

    df.columns = ['date','time','page_viewed','user_id','cohort_id','ip']

    df['cohort_id'] = df.cohort_id.fillna(0)
    df['cohort_id'] = df.cohort_id.astype("int")

    df = pd.merge(df, cohorts, left_on='cohort_id', right_on='cohort_id')    

    df.start_date = pd.to_datetime(df.start_date, format='%Y-%m-%d')
    df.end_date = pd.to_datetime(df.end_date, format='%Y-%m-%d')
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

    active = (df.index > df.start_date) & (df.index < df.end_date)
    df['active'] = active

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

def prepare_merge_logs_wd(df):
    '''
    Takes in a raw curriculum log dataframe and converts column headers to meaningful labels, and
    combines the separated date and time columns into a single column that is set as a datetime index.
    Missing cohort_id values are imputed with 0, representing users with an unknown cohort.
    Using the cohort_id, the returned dataframe is limited to only data science cohorts.
    Additionally, web pages that are not clearly curriculum are removed from the dataset.
    IMPORTANT: This will also merge the dataframe with the cohort data from the cohorts.csv file
    
    Parameters: df - dataframe to be cleaned
    
    Returns: df - dataframe
    '''
    cohorts = acquire_cohorts()
    cohorts.loc[46] = [0, 'Missing', '2014-02-04', '2021-05-04', 0]

    df.columns = ['date','time','page_viewed','user_id','cohort_id','ip']

    df['cohort_id'] = df.cohort_id.fillna(0)
    df['cohort_id'] = df.cohort_id.astype("int")    

    df = pd.merge(df, cohorts, left_on='cohort_id', right_on='cohort_id')      

    df.start_date = pd.to_datetime(df.start_date, format='%Y-%m-%d')
    df.end_date = pd.to_datetime(df.end_date, format='%Y-%m-%d')
    df.index = pd.to_datetime(df.date + " " + df.time)

    df = df.drop(columns=['date','time'], axis=1)
    
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

    active = (df.index > df.start_date) & (df.index < df.end_date)
    df['active'] = active

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

def acquire_prepare_merge_logs():
    '''
    Combines the acquire and prepare functions to produce three dataframes 
    (a dataframe with both data science and web development students, 
    a dataframe consisting of only data science students,
    and a dataframe consisting of only web development students)

    IMPORTANT: The dataframes will also include the data from the cohorts.csv file
    
    Parameters: None
    
    Returns: combined, ds, wd - data science focused dataframe, web development focused dataframe
    '''
    df = acquire_logs()
    com_merged = prepare_merge_logs_all(df)
    ds_merged = prepare_merge_logs_ds(df)
    wd_merged = prepare_merge_logs_wd(df)

    return com_merged, ds_merged, wd_merged