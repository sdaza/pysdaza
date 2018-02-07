import pandas
import numpy
import glob

# read files
def read_files(dir):
    filenames = glob.glob(dir)
    return pandas.concat([pandas.read_csv(i) for i in filenames],
                     ignore_index=True)

# missing data
def count_missing(df):
    m = df.isnull().sum()/len(df)
    m = m[m>0.00]
    if ( len(m) > 0):
        return m.sort_values(ascending=False)
    else:
        print('No missing data!')

# impute values
def impute_values(data, group_vars):
    df = data.copy()
    group= df.groupby(group_vars)

    def impute_median(series):
        return series.fillna(series.median())

    def impute_mode(series):
        return series.fillna(series.mode()[0])

    # get list of variables with missing values
    m = df.isnull().sum()/len(df)
    variables = list(m[m>0.00].index)

    # impute
    for v in variables:
        if (df[v].dtypes == numpy.dtype('int')) | (df[v].dtypes == numpy.dtype('float')):
            df[v] = group[v].transform(impute_median)
        elif (df[v].dtypes == numpy.dtype('object')):
            df[v] = group[v].transform(impute_mode) # most frequent category
    return df

# transform variables
def transform_variables(data, variables, kind='log'):
    d = data.copy()
    for name in variables:
        if kind=='log':
            values = [numpy.log(v) if v >0.0 else numpy.log(0.01) for v in d[name]]
            values = (values - numpy.mean(values)) # centering
        elif kind=='z':
            values = (d[name] - numpy.mean(d[name])) / numpy.std(d[name]) # z-score
        d[kind+'_'+name] = values
    return d