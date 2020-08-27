import BLS 
import pandas as pd
from astropy.io import ascii
from astropy.table import Table
import time as imp_t
from tqdm import tqdm
import numpy as np



def run_BLS(sector,tics,datapath,saveresultspath):
	'''
	~ Runs Box-least-squares analysis on TESS light curves for 2-minute cadence targets and
	  writes values and final stat table to file~
	REQUIRES: time, tqdm, pandas, numpy, astropy, BLS
	Args:
		sector               -(int) sector of observation for saving 
		tics                 -(list or array) tic ids for targets
		datapath             -(str) full path and file name of mit tess page sector target lists
		saveresultspath      -(str) full path to location for saved arrays
	Returns:
		Astropy Table of tic, highest power amplitude with corresponding orbital period, transit depth, transit duration, transit time
	'''


	##bls needs
	pgrid =  BLS.period_grid(log='on') 
	dgrid = BLS.duration_grid(start=.01,stop=.29,N=5)
	Secids=[];Secpowers=[];Secperiods=[];Secdepths=[];Secdurs=[];Sectts=[]

	count = 0
	for tic in tqdm(tics):
		imp_t.sleep(1)
		# print('starting {} out of {}'.format(count,len(kics)))
		lc = BLS.open_mylcs(tic,sector,filepath=datapath) #open data
		flat_time, flat_flux, flat_fluxerr = BLS.flatten_lc(lc[0],lc[1],lc[2]) #flatten [time,flux,fluxerr]
		# print('starting bls')
		periodogram, stats = BLS.bls(pgrid,dgrid,flat_time, flat_flux, flat_fluxerr)
		fn = saveresultspath
		np.save('{}/bls_pg_period'.format(fn,tic),periodogram.period)
		np.save('{}/bls_pg_power'.format(fn,tic),periodogram.power)
		Secids.append(tic)
		Secpowers.append(stats[0]);Secperiods.append(stats[1]);Secdepths.append(stats[2]);
		Secdurs.append(stats[3]);Sectts.append(stats[4])
		#save arrays as they come in case of crash - but all in final table
		
		np.save('{}/BLS_powers'.format(fn),Secpowers)
		np.save('{}/BLS_periods'.format(fn),Secperiods)
		np.save('{}/BLS_depths'.format(fn),Secdepths)
		np.save('{}/BLS_durations'.format(fn),Secdurs)
		np.save('{}/BLS_transit_times'.format(fn),Sectts)
	#make a table
	print('making final table: Sec{}_bls_stats.csv'.format(sector))
	sec_table = Table([Secids,Secperiods,Secpowers,Secdepths,Secdurs,Sectts],
		names=('TIC','period_bls','power_bls','depth_bls','dur_bls','tt_bls'))

	ascii.write(sec_table, '{}/Sec{}_bls_stats.csv'.foramt(fn,sector),format='csv', overwrite=True) 
	print(' F  I  N  I  S  H  E  D') 

	return sec_table