import LS
import time as imp_t
from tqdm import tqdm
import pandas as pd
import numpy as np


def run_LS(sector, targetsfilepath, saveresultspath):
	'''
	~ runs Lomb-Scargle analysis on TESS light curves for 2-minute cadence targets and
	  writes values and final stat table to file~
	REQUIRES: time, tqdm, pandas, numpy, LS
	Args:
		sector               -(int) sector of observation for saving 
		targetsfilepath      -(str) full path and file name of mit tess page sector target lists
		saveresultspath      -(str) full path to location for saved arrays
	Returns:
		DataFrame of tic, Rvar, highest 3 power amplitudes with corresponding rotation periods
	'''
	sector_table = pd.read_csv(targetsfilepath,skiprows=5)#from mit tess page sector target lists
	tic_list = sector_table['TICID'].to_numpy()

	rvars=[]; ls_1=[]; ls_2=[]; ls_3=[]; lsamp_1=[]; lsamp_2=[]; lsamp_3=[];tics=[];missingtics=[]
	arrpath = saveresultspath

	for tic in tqdm(tic_list):
		imp_t.sleep(1)
		time,flux,fluxerr = LS.open_mylcs(tic,sector,path='mypath')
		if len(flux) != 4: #4 b/c len('None')==4
			Rvar = LS.rvar(flux)
			periods,powers = LS.ls_measure(time,flux,fluxerr)
			rvars.append(Rvar)
			np.save(arrpath+'rvar',rvars)
			ls_1.append(periods[0])
			np.save(arrpath+'ls_1',ls_1)
			ls_2.append(periods[1])
			np.save(arrpath+'ls_2',ls_2)
			ls_3.append(periods[2])
			np.save(arrpath+'ls_3',ls_3)
			lsamp_1.append(powers[0])
			np.save(arrpath+'lsamp_1',lsamp_1)
			lsamp_2.append(powers[1])
			np.save(arrpath+'lsamp_2',lsamp_2)
			lsamp_3.append(powers[2])
			np.save(arrpath+'lsamp_3',lsamp_3)
			tics.append(tic)
			np.save(arrpath+'tics',tics)
		else:
			missingtics.append(tic)
			np.save(arrpath+'missing_tics',missingtics)

	data = {'TIC':tics,'rvar':rvars,'ls-1':ls_1,'ls-2':ls_2,'ls-3':ls_3,
			'lsamp-1':lsamp_1,'lsamp-2':lsamp_2,'lsamp-3':lsamp_3}
	stats = pd.DataFrame(data)
	stats.to_csv(arrpath+'ls_stats.csv',index=False)
	print('F I N I S H E D')

	return stats


