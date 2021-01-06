
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

Tools for collecting light curve statistics for preliminary target sample size reduction or identification. Collected statistics include: _Rvar, Lomb-Scargle (LS) Periodogram top three power amplitudes with corresponding rotation periods, Box-Least-Squares (BLS) period, highest power amplitude, transit depth, transit duration, transit time_. <br/>
Can be used with light curve data (time, flux, flux_err arrays) from any instrument, but has been optimized for TESS 2-minute cadence targets with Teff <6500 K and data downloads are specifically for those targets only. A Light Curve is a time-series dataset of stellar flux observations. Contains example notebooks for downloading TESS 2-minute cadence data by sector and gathering stellar parameters from the TESS Input Catalog. Note that currently these tools are for preliminary sample reduction purposes only. Future updates will validate output statistic precisions. Current pipeline has suggested accuracy based on Kepler vetted catalogs as shown at bottom of the example notebook.

## Instructions
1. Follow guide in `download_data` notebook to obtain TESS 2-minute cadence light curve data
2. Download .py files and run.py files 
3. Use run.py files to calculate light curve statistics and save to a DataFrame
4. Evaluate statistical outputs for preliminary target reductions, see example usage 


## Example Usage

### Dependencies
- [astropy](https://www.astropy.org)
- [batman](https://www.cfa.harvard.edu/~lkreidberg/batman/)
- [glob](https://docs.python.org/3/library/glob.html?#module-glob)
- [lightkurve](https://docs.lightkurve.org/#)
- [matplotlib](https://matplotlib.org)
- [numpy](https://numpy.org)
- [os](https://docs.python.org/3/library/os.html?#module-os)
- [pandas](https://pandas.pydata.org)
- [scipy](https://www.scipy.org/install.html)
- [starspot](https://github.com/RuthAngus/starspot)
- [time](https://docs.python.org/3/library/time.html)
- [tqdm](https://pypi.org/project/tqdm/2.2.3/)


### License & attribution

&copy; 2020 Danielle Rowland;
The source code is made available under the MIT license. See `LICENSE` file for terms.
