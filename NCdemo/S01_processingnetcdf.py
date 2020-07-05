"""
Script goal, 

Open the ndvi, precipitation and temperature netcdf then convert them to a csv 
that R can read in.  


"""

# ==============================================================================

__title__ = "Process Netcdf"
__author__ = "Arden Burrell"
__version__ = "v1.0(23.06.2020)"
__email__ = "aburrell@whrc.org"

# ==============================================================================

# ========== Import packages ==========
import os
import sys
import numpy as np
import pandas as pd
# import datetime as dt
# import warnings as warn
import xarray as xr
# import dask
# import bottleneck as bn
from collections import OrderedDict, defaultdict

# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import seaborn as sns

# ==============================================================================
def main():
	# ========== Set the filenames ==========
	fnNDVI  = "./AUSdemo_GIMMS_ndvi.nc"
	fnPPT   = "./AUSdemo_TERRACLIMATE_ppt.nc"
	fnTMEAN = "./AUSdemo_TERRACLIMATE_tmean.nc"

	# ========== Loop over the three datasets ==========
	for dsname, dsdesc in zip([fnNDVI, fnPPT, fnTMEAN], ["ndvi", "ppt", "tmean"]):

		# ========== Read the dataset in ==========
		dsin = xr.open_dataset(dsname)

		# ========== Stack the dataset ==========
		ds_stack = dsin.stack(cord=('longitude', 'latitude'))

		# ========== Convert to a pandas datadrame ==========
		df_out =  pd.DataFrame(ds_stack[dsdesc].values.T, index=ds_stack.cord.values, columns=ds_stack.time.values)

		# ========== Create a file name out ==========
		fnout = "./demo_dataframe_%s.csv" % (dsdesc)

		# ========== Save the file out ==========
		df_out.to_csv(fnout)


	breakpoint()

# ==============================================================================
if __name__ == '__main__':
	main()