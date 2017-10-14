import pandas as pd

def read_ts(source_url):
    """Read pandas time series from *source_url*"""
    df = pd.read_csv(source_url, converters={0: pd.to_datetime}, index_col=0)
    return df.iloc[:,0] 

usd_er = read_ts('http://mini-kep.herokuapp.com/ru/series/USDRUR_CB/d/2017/')
assert usd_er['2017-09-28'] == 58.01022


# This app has three URLs that relay annual, quarterly and monthly macroeconomic time series from mini-kep parser.
URL = {'a': 'http://mini-kep.herokuapp.com/annual',
    'q': 'http://mini-kep.herokuapp.com/quarterly',
    'm': 'http://mini-kep.herokuapp.com/monthly'}

def read_csv(source):
    return pd.read_csv(source, converters={0: pd.to_datetime}, index_col=0)

dfa, dfq, dfm = (read_csv(URL[freq]) for freq in 'aqm')
