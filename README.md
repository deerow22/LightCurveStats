
<hr>
     <br />
            <div align="center">
                <h1>LightCurveStats</h1>
                     <div><div align="center" width=100px>
                           <h3>tools for collecting light curve statistics to narrow target sample searches</h3>
                             <img align="center" src="Images/lc-ex2.png" width="400" /> 
                             <img align='left' src="Images/lc-ex1.png" width="400" /> 
<!-- 
<img align='left' src="Images/ls.png" width="400" /> 
<img align='right' src="Images/lc-ex3.png" width="400" /> 
 -->
                     </div></div>
			</div>
    <br />
<hr>


# Description

Tools for collecting light curve statistics for preliminary target sample size reduction or identification. Collected statistics include: _Rvar, Lomb-Scargle (LS) Periodogram top three power amplitudes with corresponding rotation periods, Box-Least-Squares (BLS) orbital period, highest power amplitude, transit depth, transit duration, transit time_. <br/>
Can be used with light curve data (time, flux, flux_err arrays) from any instrument, but has been optimized for TESS 2-minute cadence targets with Teff <6500 K. A Light Curve is a time-series dataset of stellar flux observations. Contains example notebooks for downloading TESS 2-minute cadence data by sector and gathering stellar parameters from the TESS Input Catalog. Note that currently these tools are for preliminary sample reduction purposes only. Future updates will validate output statistic precisions. Current pipeline has suggested accuracy based on Kepler vetted catalogs as shown at bottom of the example notebook.

## Instructions
1. Follow guide in `download_data` notebook to obtain TESS 2-minute cadence light curve data
2. Download .py files and run.py files 
3. Use run.py files to calculate light curve statistics and save to a DataFrame
4. Evaluate statistical outputs for preliminary target reductions, see example usage 


## Example Usage
To narrow a search for planet hosting stars while avoiding eclipsing binaries: 
Use collected statistics to isolate targets with high BLS power amplitudes but low R_var with different period values from BLS and LS, to increase potential sample of magnetically stable stars with transit detections. 

### Dependencies
- astropy
- glob
- lightkurve
- matplotlib
- numpy
- os
- pandas
- scipy
- starspot
- time
- tqdm


### License & attribution

Copyright 2020 Danielle Rowland.
The source code is made available under the terms of the MIT license.
If you make use of this code, please cite this package and its dependencies.