import BLS
import LS

def test_open_mylcs():
    tic1= 7582633; sector1=14
    t1,f1,fe1 = LS.open_mylcs(tic1,sector1,path='mypath') #passes
    assert len(t1)==len(f1)==len(fe1) #passes
    tic2 = 1234; sector2 = 1
    print('Expecting print statement about tic 1234 sector 1 Error:')
    t2,f2,fe2 = LS.open_mylcs(tic2,sector2,path='WrongFolder/Wrongfilename.fits')
    assert t2 == 'None'
    
def test_rvar():
    time,flux,fluxerr = BLS.fake_data()
    r_var = LS.rvar(flux)
    assert r_var <1.
    assert isinstance(r_var, np.float64)
    
def test_ls_measure():
    time,flux,fluxerr = BLS.fake_data()
    periods, powers = LS.ls_measure(time,flux)
    assert len(periods)==3
    assert len(powers)==3
    
test_open_mylcs()
test_rvar()
test_ls_measure()