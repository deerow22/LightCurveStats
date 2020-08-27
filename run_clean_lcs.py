import time as imp_t
from tqdm import tqdm
import clean_lcs


#easiest tic_list comes from 'ONE' in download_data notebook, then ##code below can be used
## import pandas as pd
## sector_table = pd.read_csv('Filepath/all_targets_S0{}_v1.csv'.format(sector),skiprows=5)#from mit tess page sector target lists
## tic_list = sector_table['TICID'].to_numpy()

count = 0
def run_clean_lcs(sector, rawdatapath, tic_list, savepath):
    '''
    ~ Cleans files downloaded via custom curl script in download_data notebook. Cleaning involves
    TESS PDCSAP_FLUX choice, outlier removal, flux normalization, nan removal and stitching if multiple sectors~
    REQUIRES: clean_lcs, tqdm, time
    Args:
        sector        -(int) observation sector of light curve
        rawdatapath   -(str) path to raw data, assumes filename from custom curl
        tic_list      -(list or array) TIC IDs of target files to clean
        savepath      -(str) path to save cleaned light curves, automatically generates filename using tic
    Returns:
        total number of cleaned files (written files saved to savepath location)
    '''
    sectors_list = [sector]
    #cleans file(s) per tic & saves
    for tic in tqdm(tic_list):
        imp_t.sleep(1)
        allfilepaths = clean_lcs.locate_files(tic,path=rawdatapath) #search for all paths
        lcfile, secs_here = clean_lcs.sector_ordered_files(allfilepaths,sectors_list,tic) #only open files within sector_list
    ## sector_list ensures only one chosen
    ## for file in lcfiles: ## add in if stitching data from multiple sectors & change savepath to account for multiple sectors
        if lcfile != -99:
            realsec = lcfile[0].header()['SECTOR']
            savepath = '{}/{}/lc.fits'.format(savepath,tic)
            cleanlc = clean_lcs.clean_files(lcfile[0])
            clean_lcs.save_lc(cleanlc,savepath=savepath)
            print('save successful for TIC {}'.format(tic))
            count +=1
        else:
            pass

    return 'Cleaned {} files successfully'.format(count)