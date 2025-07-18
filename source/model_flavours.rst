Reltrans model setup
========================

This section includes multiple notes on how to set up and run the model, and on 
the different assumptions that each model flavour makes

Reltrans model flavours
-----------------------

**Reltrans** is not just a single model, but is a library of different model
flavours that have slightly different physics. This page lists all the 
available models, briefly describes their differences, and lists their input
parameters.

.. note:: 
    This page might not be fully comprehensive currently as this documentation
    is under development.
    

Environmental variables
-----------------------

There are a number of environmental variables that are set across all model 
flavours of reltrans. These relate both to the physics of the model, but also
makes model calling faster in some cases.

If environment variables are not set, the model uses default parameters. 

* ION_ZONES [number > 0; default 20]\: 

  It sets the number of radial zones of
  the disk to calculate the ionisation profile of the disk. The default value is
  50 zones, but the number used in previous works of the reltrans team is 20. If
  it is set to 1 the disk is considered to have the same ionisation and the same
  density everywhere. 

* A_DENSITY [possible options 0 or 1; default 0]: 

  It sets the type to density 
  profile in the disk. There are two options: 
  
  * A_DENSITY = 0 -> constant density
  * A_DENSITY = 1 -> Shakura and Suniev zone A density profile. 
  
  Keep in mind that if you set the ION_ZONES = 1, it doesn't matter which 
  density profile you choose because you have a single radial zone disk.

* MU_ZONES [number > 0; default 5 ]: 

  It sets the zones for the emitting angle (they are different from the radial 
  zones). In previous work we noticed that the angle dependence does not change 
  dramatically the spectrum, thus we have used MU_ZONES set to 1 to speed up the 
  code. 

* RMF_SET and ARF_SET [character string; NO default]: 

  They pre-set the path of the response matrix and the arf. 
  This is not necessary if you are interested in the time-averaged energy 
  spectrum since xspec applies the response matrix automatically. 
  If you work with either the real and imaginary part of the cross-spectrum or 
  directly with the lag energy spectrum you may want to consider to pre-set the 
  path of the response matrix and arf to avoid the code asking for it. 
  If the two variables are not set the code will ask for the path: "Enter name 
  the response file (with full path)"

Models
------

reltransDCp
^^^^^^^^^^^

reltransDCp can be considered the "default" version of the lastest reltrans 
release. It assumes that the disk is illuminated by a nthcomp spectrum and the
disk is a variable density disk with a fixed high energy cutoff at 300keV. This
means that it used the xillverDCp tables.

**Parameters:**

+------------------------+------------+-------------+
| Parameter number       | Name       | Description |
+========================+============+=============+
| 1                      | h          |height of the|
|                        |            |corona from  |
|                        |            |the blackhole|
+------------------------+------------+-------------+
| 2                      | a          | spin        |
+------------------------+------------+-------------+
| 3                      | inc        |inclination  |
+------------------------+------------+-------------+
| 4                      | rin        |inner radius |
|                        |            |of the disk  |
+------------------------+------------+-------------+
| 5                      | rout       |outer radius |
|                        |            |of the disk  |
+------------------------+------------+-------------+
| 6                      | z          |redshift     |
+------------------------+------------+-------------+
| 7                      | Gamma      |slope        |
+------------------------+------------+-------------+
| 8                      | logxi      |ionisation   |
+------------------------+------------+-------------+
| 9                      | Afe        |iron         |
|                        |            |abundance    |
+------------------------+------------+-------------+
| 10                     | logNe      |disk density |
+------------------------+------------+-------------+
| 11                     | kTe        |electron     |
|                        |            |temperature  |
|                        |            |of the corona|
+------------------------+------------+-------------+
| 12                     | nH         |galactic     |
|                        |            |absorption   |
+------------------------+------------+-------------+
| 13                     | boost      |reflection   |
|                        |            |spectrum     |
|                        |            |normalisation|
+------------------------+------------+-------------+
| 14                     | Mass       |mass of the  |
|                        |            |black hole   |
+------------------------+------------+-------------+
| 15                     | fmin       |minimum      |
|                        |            |frequency of |
|                        |            |cross        |
|                        |            |spectrum     |
+------------------------+------------+-------------+
| 16                     | fmax       |maximum      |
|                        |            |frequency of |
|                        |            |cross        |
|                        |            |spectrum     |
+------------------------+------------+-------------+
| 17                     | ReIm       |flag for     |
|                        |            |outputs      |
+------------------------+------------+-------------+
| 18                     | phiA       |phase shift  |
|                        |            |of the       |
|                        |            |reference    |
|                        |            |band         |
+------------------------+------------+-------------+
| 19                     | phiAB      |phase        |
|                        |            |difference   |
|                        |            |between the  |
|                        |            |pivoting and |
|                        |            |normalisation|
|                        |            |of the       |
|                        |            |illuminating |
|                        |            |variability  |
+------------------------+------------+-------------+
| 20                     | g          |ratio of the |
|                        |            |normalisation|
|                        |            |between the  |
|                        |            |pivoting and |
|                        |            |normalisation|
|                        |            |of the       |
|                        |            |illuminating |
|                        |            |variability  |
+------------------------+------------+-------------+
| 21                     | RESP       |the number of|
|                        |            |instrument   |
|                        |            |responses    |
|                        |            |used         |
+------------------------+------------+-------------+


reltransPL
^^^^^^^^^^^

reltransPL is identical to reltransDCP except that it assumes that the disk is 
illuminated by a powerlaw spectrum. This means that it used the xillverDCp 
tables.

**Parameters:**


+------------------------+------------+-------------+
| Parameter number       | Name       | Description |
+========================+============+=============+
| 1                      | h          |height of the|
|                        |            |corona from  |
|                        |            |the blackhole|
+------------------------+------------+-------------+
| 2                      | a          | spin        |
+------------------------+------------+-------------+
| 3                      | inc        |inclination  |
+------------------------+------------+-------------+
| 4                      | rin        |inner radius |
|                        |            |of the disk  |
+------------------------+------------+-------------+
| 5                      | rout       |outer radius |
|                        |            |of the disk  |
+------------------------+------------+-------------+
| 6                      | z          |redshift     |
+------------------------+------------+-------------+
| 7                      | Gamma      |slope        |
+------------------------+------------+-------------+
| 8                      | logxi      |ionisation   |
+------------------------+------------+-------------+
| 9                      | Afe        |iron         |
|                        |            |abundance    |
+------------------------+------------+-------------+
| 10                     | logNe      |disk density |
+------------------------+------------+-------------+
| 11                     | Ecut       |observed     |
|                        |            |electron     |
|                        |            |temperature  |
|                        |            |of the corona|
+------------------------+------------+-------------+
| 12                     | nH         |galactic     |
|                        |            |absorption   |
+------------------------+------------+-------------+
| 13                     | boost      |reflection   |
|                        |            |spectrum     |
|                        |            |normalisation|
+------------------------+------------+-------------+
| 14                     | Mass       |mass of the  |
|                        |            |black hole   |
+------------------------+------------+-------------+
| 15                     | fmin       |minimum      |
|                        |            |frequency of |
|                        |            |cross        |
|                        |            |spectrum     |
+------------------------+------------+-------------+
| 16                     | fmax       |maximum      |
|                        |            |frequency of |
|                        |            |cross        |
|                        |            |spectrum     |
+------------------------+------------+-------------+
| 17                     | ReIm       |flag for     |
|                        |            |outputs      |
+------------------------+------------+-------------+
| 18                     | phiA       |phase shift  |
|                        |            |of the       |
|                        |            |reference    |
|                        |            |band         |
+------------------------+------------+-------------+
| 19                     | phiAB      |phase        |
|                        |            |difference   |
|                        |            |between the  |
|                        |            |pivoting and |
|                        |            |normalisation|
|                        |            |of the       |
|                        |            |illuminating |
|                        |            |variability  |
+------------------------+------------+-------------+
| 20                     | g          |ratio of the |
|                        |            |normalisation|
|                        |            |between the  |
|                        |            |pivoting and |
|                        |            |normalisation|
|                        |            |of the       |
|                        |            |illuminating |
|                        |            |variability  |
+------------------------+------------+-------------+
| 21                     | RESP       |the number of|
|                        |            |instrument   |
|                        |            |responses    |
|                        |            |used         |
+------------------------+------------+-------------+


rtransDbl
^^^^^^^^^^^

reltransDbl is identical to reltransDCP except that it assumes that there are 
2 illuminating sources. 

**Parameters:**


+------------------------+------------+-----------------------------+
| Parameter number       | Name       | Description                 |
+========================+============+=============================+
| 1                      | h1         |height of the                |
|                        |            |first                        |
|                        |            |corona from                  |
|                        |            |the blackhole                |
+------------------------+------------+-----------------------------+
| 2                      | h2         |height of the                |
|                        |            |second                       |
|                        |            |corona from                  |
|                        |            |the blackhole                |
+------------------------+------------+-----------------------------+
| 3                      | a          | spin                        |
+------------------------+------------+-----------------------------+
| 4                      | inc        |inclination                  |
+------------------------+------------+-----------------------------+
| 5                      | rin        |inner radius                 |
|                        |            |of the disk                  |
+------------------------+------------+-----------------------------+
| 6                      | rout       |outer radius                 |
|                        |            |of the disk                  |
+------------------------+------------+-----------------------------+
| 7                      | z          |redshift                     |
+------------------------+------------+-----------------------------+
| 8                      | Gamma      |slope                        |
+------------------------+------------+-----------------------------+
| 9                      | logxi      |ionisation                   |
+------------------------+------------+-----------------------------+
| 10                     | Afe        |iron                         |
|                        |            |abundance                    |
+------------------------+------------+-----------------------------+
| 11                     | logNe      |disk density                 |
+------------------------+------------+-----------------------------+
| 12                     | kTe        |electron                     |
|                        |            |temperature                  |
|                        |            |of the corona                |
+------------------------+------------+-----------------------------+
| 13                     | eta_0      |Time-averaged                |
|                        |            |normalization                |
|                        |            |ratio C1 \/                  |
|                        |            |C2 between                   |
|                        |            |the two                      |
|                        |            |lampposts and                |
|                        |            |sets continuum               |
|                        |            |cutoff and disk              |
|                        |            |disk ionization              |
+------------------------+------------+-----------------------------+
| 14                     | eta        |Fourier frequency dependent  |
|                        |            |normalization ratio C1(νc)\/ |
|                        |            |C2(νc)                       |
+------------------------+------------+-----------------------------+
| 15                     | beta_p     |propagation speed delay      |
|                        |            |between the two lampposts if |
|                        |            |they are coherent (0 if      |
|                        |            |incoherent)                  |
+------------------------+------------+-----------------------------+
| 16                     | nH         |galactic                     |
|                        |            |absorption                   |
+------------------------+------------+-----------------------------+
| 17                     | boost      |reflection                   |
|                        |            |spectrum                     |
|                        |            |normalisation                |
+------------------------+------------+-----------------------------+
| 18                     | Mass       |mass of the                  |
|                        |            |black hole                   |
+------------------------+------------+-----------------------------+
| 19                     | fmin       |minimum                      |
|                        |            |frequency of                 |
|                        |            |cross                        |
|                        |            |spectrum                     |
+------------------------+------------+-----------------------------+
| 20                     | fmax       |maximum                      |
|                        |            |frequency of                 |
|                        |            |cross                        |
|                        |            |spectrum                     |
+------------------------+------------+-----------------------------+
| 21                     | ReIm       |flag for                     |
|                        |            |outputs                      |
+------------------------+------------+-----------------------------+
| 22                     | phiA       |phase shift                  |
|                        |            |of the                       |
|                        |            |reference                    |
|                        |            |band of the bottom lamppost  |
+------------------------+------------+-----------------------------+
| 23                     | phiAB      |phase difference             |
|                        |            |between the pivoting and     |
|                        |            |normalisation of the         |
|                        |            |illuminating variability     |
|                        |            |for the bottom lamppost      |
+------------------------+------------+-----------------------------+
| 24                     | g          |ratio of the normalisation   |
|                        |            |between the pivoting and     |
|                        |            |normalisation of the         |
|                        |            |illuminating variability     |
|                        |            |of the bottom lamppost       |
+------------------------+------------+-----------------------------+
| 25                     | phiAB2     |phase difference             |
|                        |            |between the pivoting and     |
|                        |            |normalisation of the         |
|                        |            |illuminating variability     |
|                        |            |for the top lampost          |
+------------------------+------------+-----------------------------+
| 26                     | g2         |ratio of the normalisation   |
|                        |            |between the pivoting and     |
|                        |            |normalisation of the         |
|                        |            |illuminating variability     |
|                        |            |of the top lamppost          |
+------------------------+------------+-----------------------------+
| 27                     | alpha      |Cross-spectral               |
|                        |            |normalisation                |
|                        |            |constant                     |
|                        |            |set to unity                 |
|                        |            |for                          |
|                        |            |calculating                  |
|                        |            |lags                         |
+------------------------+------------+-----------------------------+
| 28                     | RESP       |the number of                |
|                        |            |instrument                   |
|                        |            |responses                    |
|                        |            |used                         |
+------------------------+------------+-----------------------------+


rtdist
^^^^^^^^^^^

rtdist is a variant of reltransDCp. It self-consistently calculates the disk
ionisation by calculating the geometric reltationship between the observer,
source of illuminating spectrum and the disk. It also features a change to
the previous boost normalisation factor for the reflection spectrum which is 
changed to 2 emissivity parameters which directs the emission in a 
manner that is more physical.

**Parameters:**

+------------------------+------------+-------------+
| Parameter number       | Name       | Description |
+========================+============+=============+
| 1                      | h          |height of the|
|                        |            |corona from  |
|                        |            |the blackhole|
+------------------------+------------+-------------+
| 2                      | a          | spin        |
+------------------------+------------+-------------+
| 3                      | inc        |inclination  |
+------------------------+------------+-------------+
| 4                      | rin        |inner radius |
|                        |            |of the disk  |
+------------------------+------------+-------------+
| 5                      | rout       |outer radius |
|                        |            |of the disk  |
+------------------------+------------+-------------+
| 6                      | z          |redshift     |
+------------------------+------------+-------------+
| 7                      | Gamma      |slope        |
+------------------------+------------+-------------+
| 8                      | Dkpc       |Distance to  |
|                        |            |source in kpc|
+------------------------+------------+-------------+
| 9                      | logxi      |ionisation   |
+------------------------+------------+-------------+
| 10                     | Afe        |iron         |
|                        |            |abundance    |
+------------------------+------------+-------------+
| 11                     | logNe      |disk density |
+------------------------+------------+-------------+
| 12                     | kTe        |electron     |
|                        |            |temperature  |
|                        |            |of the corona|
+------------------------+------------+-------------+
| 13                     | nH         |galactic     |
|                        |            |absorption   |
+------------------------+------------+-------------+
| 14                     | boost      |reflection   |
|                        |            |spectrum     |
|                        |            |normalisation|
+------------------------+------------+-------------+
| 15                     | Mass       |mass of the  |
|                        |            |black hole   |
+------------------------+------------+-------------+
| 16                     | b1         |emissivity   |
|                        |            |parameter    |
+------------------------+------------+-------------+
| 17                     | b2         |emissivity   |
|                        |            |parameter    |
+------------------------+------------+-------------+
| 18                     | fmin       |minimum      |
|                        |            |frequency of |
|                        |            |cross        |
|                        |            |spectrum     |
+------------------------+------------+-------------+
| 19                     | fmax       |maximum      |
|                        |            |frequency of |
|                        |            |cross        |
|                        |            |spectrum     |
+------------------------+------------+-------------+
| 20                     | ReIm       |flag for     |
|                        |            |outputs      |
+------------------------+------------+-------------+
| 21                     | phiA       |phase shift  |
|                        |            |of the       |
|                        |            |reference    |
|                        |            |band         |
+------------------------+------------+-------------+
| 22                     | phiAB      |phase        |
|                        |            |difference   |
|                        |            |between the  |
|                        |            |pivoting and |
|                        |            |normalisation|
|                        |            |of the       |
|                        |            |illuminating |
|                        |            |variability  |
+------------------------+------------+-------------+
| 23                     | g          |ratio of the |
|                        |            |normalisation|
|                        |            |between the  |
|                        |            |pivoting and |
|                        |            |normalisation|
|                        |            |of the       |
|                        |            |illuminating |
|                        |            |variability  |
+------------------------+------------+-------------+
| 24                     | Anorm      |normalisation|
|                        |            |of the model |
+------------------------+------------+-------------+
| 25                     | RESP       |the number of|
|                        |            |instrument   |
|                        |            |responses    |
|                        |            |used         |
+------------------------+------------+-------------+


Simulators
-----------

We also include a number of simulators for the different reltrans model
flavours. These are explicitly for simulating the timing products that reltrans
computes. This results in additional coherence, rms variability and time
exposure parameters. See :ref: 'environment'. There is no simulator for the 
reltransPL.

simrelt
^^^^^^^

simrelt is the simulator for the reltransDCp model. 

**Parameters:**

+------------------------+------------+-------------+
| Parameter number       | Name       | Description |
+========================+============+=============+
| 1                      | h          |height of the|
|                        |            |corona from  |
|                        |            |the blackhole|
+------------------------+------------+-------------+
| 2                      | a          | spin        |
+------------------------+------------+-------------+
| 3                      | inc        |inclination  |
+------------------------+------------+-------------+
| 4                      | rin        |inner radius |
|                        |            |of the disk  |
+------------------------+------------+-------------+
| 5                      | rout       |outer radius |
|                        |            |of the disk  |
+------------------------+------------+-------------+
| 6                      | z          |redshift     |
+------------------------+------------+-------------+
| 7                      | Gamma      |slope        |
+------------------------+------------+-------------+
| 8                      | logxi      |ionisation   |
+------------------------+------------+-------------+
| 9                      | Afe        |iron         |
|                        |            |abundance    |
+------------------------+------------+-------------+
| 10                     | logNe      |disk density |
+------------------------+------------+-------------+
| 11                     | kTe        |electron     |
|                        |            |temperature  |
|                        |            |of the corona|
+------------------------+------------+-------------+
| 12                     | nH         |galactic     |
|                        |            |absorption   |
+------------------------+------------+-------------+
| 13                     | boost      |reflection   |
|                        |            |spectrum     |
|                        |            |normalisation|
+------------------------+------------+-------------+
| 14                     | Mass       |mass of the  |
|                        |            |black hole   |
+------------------------+------------+-------------+
| 15                     | fmin       |minimum      |
|                        |            |frequency of |
|                        |            |cross        |
|                        |            |spectrum     |
+------------------------+------------+-------------+
| 16                     | fmax       |maximum      |
|                        |            |frequency of |
|                        |            |cross        |
|                        |            |spectrum     |
+------------------------+------------+-------------+
| 17                     | coh2       |coherence of |
|                        |            |the simulated|
|                        |            |signal       |
+------------------------+------------+-------------+
| 18                     | phiA       |phase shift  |
|                        |            |of the       |
|                        |            |reference    |
|                        |            |band         |
+------------------------+------------+-------------+
| 19                     | phiAB      |phase        |
|                        |            |difference   |
|                        |            |between the  |
|                        |            |pivoting and |
|                        |            |normalisation|
|                        |            |of the       |
|                        |            |illuminating |
|                        |            |variability  |
+------------------------+------------+-------------+
| 20                     | g          |ratio of the |
|                        |            |normalisation|
|                        |            |between the  |
|                        |            |pivoting and |
|                        |            |normalisation|
|                        |            |of the       |
|                        |            |illuminating |
|                        |            |variability  |
+------------------------+------------+-------------+
| 21                     | Anorm      |assumed flux |
|                        |            |normalisation|
|                        |            |of the model |
+------------------------+------------+-------------+
| 22                     | Texp       |exposure time|
|                        |            |of           |
|                        |            |observation  |
+------------------------+------------+-------------+
| 23                     | pow        |power        |
|                        |            |averaged over|
|                        |            |simulated    |
|                        |            |frequency    |
|                        |            |range        |
+------------------------+------------+-------------+
| 24                     | RESP       |the number of|
|                        |            |instrument   |
|                        |            |responses    |
|                        |            |used         |
+------------------------+------------+-------------+

simrtdbl
^^^^^^^^^^^

simrtdbl is the simulator for reltransDbl. 

**Parameters:**


+------------------------+------------+-----------------------------+
| Parameter number       | Name       | Description                 |
+========================+============+=============================+
| 1                      | h1         |height of the                |
|                        |            |first                        |
|                        |            |corona from                  |
|                        |            |the blackhole                |
+------------------------+------------+-----------------------------+
| 2                      | h2         |height of the                |
|                        |            |second                       |
|                        |            |corona from                  |
|                        |            |the blackhole                |
+------------------------+------------+-----------------------------+
| 3                      | a          | spin                        |
+------------------------+------------+-----------------------------+
| 4                      | inc        |inclination                  |
+------------------------+------------+-----------------------------+
| 5                      | rin        |inner radius                 |
|                        |            |of the disk                  |
+------------------------+------------+-----------------------------+
| 6                      | rout       |outer radius                 |
|                        |            |of the disk                  |
+------------------------+------------+-----------------------------+
| 7                      | z          |redshift                     |
+------------------------+------------+-----------------------------+
| 8                      | Gamma      |slope                        |
+------------------------+------------+-----------------------------+
| 9                      | logxi      |ionisation                   |
+------------------------+------------+-----------------------------+
| 10                     | Afe        |iron                         |
|                        |            |abundance                    |
+------------------------+------------+-----------------------------+
| 11                     | logNe      |disk density                 |
+------------------------+------------+-----------------------------+
| 12                     | kTe        |electron                     |
|                        |            |temperature                  |
|                        |            |of the corona                |
+------------------------+------------+-----------------------------+
| 13                     | eta_0      |Time-averaged                |
|                        |            |normalization                |
|                        |            |ratio C1 \/                  |
|                        |            |C2 between                   |
|                        |            |the two                      |
|                        |            |lampposts and                |
|                        |            |sets continuum               |
|                        |            |cutoff and disk              |
|                        |            |disk ionization              |
+------------------------+------------+-----------------------------+
| 14                     | eta        |Fourier frequency dependent  |
|                        |            |normalization ratio C1(νc)\/ |
|                        |            |C2(νc)                       |
+------------------------+------------+-----------------------------+
| 15                     | nH         |galactic                     |
|                        |            |absorption                   |
+------------------------+------------+-----------------------------+
| 16                     | boost      |reflection                   |
|                        |            |spectrum                     |
|                        |            |normalisation                |
+------------------------+------------+-----------------------------+
| 17                     | Mass       |mass of the                  |
|                        |            |black hole                   |
+------------------------+------------+-----------------------------+
| 18                     | fmin       |minimum                      |
|                        |            |frequency of                 |
|                        |            |cross                        |
|                        |            |spectrum                     |
+------------------------+------------+-----------------------------+
| 19                     | fmax       |maximum                      |
|                        |            |frequency of                 |
|                        |            |cross                        |
|                        |            |spectrum                     |
+------------------------+------------+-----------------------------+
| 20                     | coh2       |coherence of the simulated   |
|                        |            |signal                       |
+------------------------+------------+-----------------------------+
| 21                     | phiA       |phase shift                  |
|                        |            |of the                       |
|                        |            |reference                    |
|                        |            |band of the bottom lamppost  |
+------------------------+------------+-----------------------------+
| 22                     | phiAB      |phase difference             |
|                        |            |between the pivoting and     |
|                        |            |normalisation of the         |
|                        |            |illuminating variability     |
|                        |            |for the bottom lamppost      |
+------------------------+------------+-----------------------------+
| 23                     | g          |ratio of the normalisation   |
|                        |            |between the pivoting and     |
|                        |            |normalisation of the         |
|                        |            |illuminating variability     |
|                        |            |of the bottom lamppost       |
+------------------------+------------+-----------------------------+
| 24                     | phiAB2     |phase difference             |
|                        |            |between the pivoting and     |
|                        |            |normalisation of the         |
|                        |            |illuminating variability     |
|                        |            |for the top lampost          |
+------------------------+------------+-----------------------------+
| 25                     | g2         |ratio of the normalisation   |
|                        |            |between the pivoting and     |
|                        |            |normalisation of the         |
|                        |            |illuminating variability     |
|                        |            |of the top lamppost          |
+------------------------+------------+-----------------------------+
| 26                     | Texp       |exposure time of observation |
+------------------------+------------+-----------------------------+
| 27                     | pow        |power averaged over simulated|
|                        |            |frequency range              |
+------------------------+------------+-----------------------------+
| 28                     | RESP       |the number of                |
|                        |            |instrument                   |
|                        |            |responses                    |
|                        |            |used                         |
+------------------------+------------+-----------------------------+

simrtdist
^^^^^^^^^^^

simrtdist is the simulator for rtdist.

**Parameters:**

+------------------------+------------+-------------+
| Parameter number       | Name       | Description |
+========================+============+=============+
| 1                      | h          |height of the|
|                        |            |corona from  |
|                        |            |the blackhole|
+------------------------+------------+-------------+
| 2                      | a          | spin        |
+------------------------+------------+-------------+
| 3                      | inc        |inclination  |
+------------------------+------------+-------------+
| 4                      | rin        |inner radius |
|                        |            |of the disk  |
+------------------------+------------+-------------+
| 5                      | rout       |outer radius |
|                        |            |of the disk  |
+------------------------+------------+-------------+
| 6                      | z          |redshift     |
+------------------------+------------+-------------+
| 7                      | Gamma      |slope        |
+------------------------+------------+-------------+
| 8                      | Dkpc       |Distance to  |
|                        |            |source in kpc|
+------------------------+------------+-------------+
| 9                      | logxi      |ionisation   |
+------------------------+------------+-------------+
| 10                     | Afe        |iron         |
|                        |            |abundance    |
+------------------------+------------+-------------+
| 11                     | logNe      |disk density |
+------------------------+------------+-------------+
| 12                     | kTe        |electron     |
|                        |            |temperature  |
|                        |            |of the corona|
+------------------------+------------+-------------+
| 13                     | nH         |galactic     |
|                        |            |absorption   |
+------------------------+------------+-------------+
| 14                     | boost      |reflection   |
|                        |            |spectrum     |
|                        |            |normalisation|
+------------------------+------------+-------------+
| 15                     | Mass       |mass of the  |
|                        |            |black hole   |
+------------------------+------------+-------------+
| 16                     | b1         |emissivity   |
|                        |            |parameter    |
+------------------------+------------+-------------+
| 17                     | b2         |emissivity   |
|                        |            |parameter    |
+------------------------+------------+-------------+
| 18                     | fmin       |minimum      |
|                        |            |frequency of |
|                        |            |cross        |
|                        |            |spectrum     |
+------------------------+------------+-------------+
| 19                     | fmax       |maximum      |
|                        |            |frequency of |
|                        |            |cross        |
|                        |            |spectrum     |
+------------------------+------------+-------------+
| 17                     | coh2       |coherence of |
|                        |            |the simulated|
|                        |            |signal       |
+------------------------+------------+-------------+
| 20                     | ReIm       |flag for     |
|                        |            |outputs      |
+------------------------+------------+-------------+
| 21                     | phiA       |phase shift  |
|                        |            |of the       |
|                        |            |reference    |
|                        |            |band         |
+------------------------+------------+-------------+
| 22                     | phiAB      |phase        |
|                        |            |difference   |
|                        |            |between the  |
|                        |            |pivoting and |
|                        |            |normalisation|
|                        |            |of the       |
|                        |            |illuminating |
|                        |            |variability  |
+------------------------+------------+-------------+
| 23                     | g          |ratio of the |
|                        |            |normalisation|
|                        |            |between the  |
|                        |            |pivoting and |
|                        |            |normalisation|
|                        |            |of the       |
|                        |            |illuminating |
|                        |            |variability  |
+------------------------+------------+-------------+
| 24                     | Anorm      |assumed flux |
|                        |            |normalisation|
|                        |            |of the model |
+------------------------+------------+-------------+
| 25                     | Texp       |exposure time|
|                        |            |of           |
|                        |            |observation  |
+------------------------+------------+-------------+
| 26                     | pow        |power        |
|                        |            |averaged over|
|                        |            |simulated    |
|                        |            |frequency    |
|                        |            |range        |
+------------------------+------------+-------------+
| 27                     | RESP       |the number of|
|                        |            |instrument   |
|                        |            |responses    |
|                        |            |used         |
+------------------------+------------+-------------+