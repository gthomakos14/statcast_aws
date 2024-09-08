import pybaseball
import polars as pl
import warnings

warnings.simplefilter('ignore')

def statcast_polars(start_dt):
    df = pl.from_pandas(pybaseball.statcast(start_dt))

    return df