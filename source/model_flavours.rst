Reltrans model flavours
=======================

**Reltrans** is not just a single model, but is a library of different model
flavours that have slightly different physics. This page lists all the 
available models, briefly describes their differences, and lists their input
parameters.

.. note:: 
    This page might not be fully comprehensive currently as this documentation
    is under development.
    
Models
-------

.. note::
    reltrans is a library of spectral timing models which means that all variants
    of the model include parameters related to which spectral timing product the 
    model returns. These include:

    * fmin and fmax: these two parameters define the frequency range of the 
      cross-spectrum to be evaluated. Setting both of these values to 0 will
      cause the model to always return the time-averaged spectrum.
    * ReIm: this parameter flags the model to output different timing products
      or components of the cross-spectrum. 
        * 0: The time-averaged spectrum.
        * 1: Real part of the cross spectrum.
        * 2: Imaginary part of the cross spectrum.
        * 3: Modulus of the cross spectrum.
        * 4: Lag-energy spectrum.
        * 5: Modulus of the folded cross spectrum.
        * 6: Lag-energy spectrum calculated from the folded cross spectrum.
    
reltransDCp
^^^^^^^^^^^

reltransDCp can be considered the "default" version of the lastest reltrans 
release. It assumes that the disk is illuminated by an nthcomp spectrum with electron
temperature kTe, and the disk density is a parameter. This means that it uses the
xillverDCp tables.

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
illuminated by an exponentially cut-off powerlaw spectrum, and the disk density
is hardwired to $10^{15}~cm^{-3}$. This means that it uses the xillver tables.

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
| 10                     | Ecut       |observed     |
|                        |            |exponential  |
|                        |            |cut off      |
|                        |            |energy       |
+------------------------+------------+-------------+
| 11                     | nH         |galactic     |
|                        |            |absorption   |
+------------------------+------------+-------------+
| 12                     | boost      |reflection   |
|                        |            |spectrum     |
|                        |            |normalisation|
+------------------------+------------+-------------+
| 13                     | Mass       |mass of the  |
|                        |            |black hole   |
+------------------------+------------+-------------+
| 14                     | fmin       |minimum      |
|                        |            |frequency of |
|                        |            |cross        |
|                        |            |spectrum     |
+------------------------+------------+-------------+
| 15                     | fmax       |maximum      |
|                        |            |frequency of |
|                        |            |cross        |
|                        |            |spectrum     |
+------------------------+------------+-------------+
| 16                     | ReIm       |flag for     |
|                        |            |outputs      |
+------------------------+------------+-------------+
| 17                     | phiA       |phase shift  |
|                        |            |of the       |
|                        |            |reference    |
|                        |            |band         |
+------------------------+------------+-------------+
| 18                     | phiAB      |phase        |
|                        |            |difference   |
|                        |            |between the  |
|                        |            |pivoting and |
|                        |            |normalisation|
|                        |            |of the       |
|                        |            |illuminating |
|                        |            |variability  |
+------------------------+------------+-------------+
| 19                     | g          |ratio of the |
|                        |            |normalisation|
|                        |            |between the  |
|                        |            |pivoting and |
|                        |            |normalisation|
|                        |            |of the       |
|                        |            |illuminating |
|                        |            |variability  |
+------------------------+------------+-------------+
| 20                     | RESP       |the number of|
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
| 23                     | phiAB1     |phase difference             |
|                        |            |between the pivoting and     |
|                        |            |normalisation of the         |
|                        |            |illuminating variability     |
|                        |            |for the bottom lamppost      |
+------------------------+------------+-----------------------------+
| 24                     | g1         |ratio of the normalisation   |
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
| 27                     | RESP       |the number of                |
|                        |            |instrument                   |
|                        |            |responses                    |
|                        |            |used                         |
+------------------------+------------+-----------------------------+


rtdist
^^^^^^^^^^^

rtdist is a variant of reltransDCp. It self-consistently calculates the disk
ionisation by calculating the geometric relationship between the observer,
source of illuminating spectrum and the disk, thus logxi is not a parameter 
of this model flavour, since it has been replaced by the distance between 
the observer and the source. It also features a change to
the previous boost normalisation factor for the reflection spectrum. The 
source is no longer assumed to be isotropic. Instead, the angular
dependence is specified by the parameters b1, b2 and qboost (referred to as
as boost but defined differently from other reltrans flavours). b1 and b2 are
linear and quadratic coefficients of the :math:`\text{mu}= \cos(\theta)` dependence
and qboost skews the relation where :math:`qboost = \frac{I(\text{mu}=-1)}{I(\text{mu}=1)}`. 
The disk scale height also has become a free parameter.

For a comprehensive explanation of the model, please see the model paper:
https://ui.adsabs.harvard.edu/abs/2022MNRAS.509..619I/abstract.

.. note::
    **IMPORTANT!**

    If you are using rtdist in reltrans, the xspec norm parameter must be frozen
    to 1 as Anorm replaces xspec norm's function.

    * For the DC component, the xspec norm parameter must be frozen to norm=1.
    * For the lag spectrum, the xspec norm parameter must (as usual) be frozen to
      norm=1.
    * For the Re/Im/amp spectra, the xspec norm becomes the average power in that
      frequency range in squared fractional rms units (this is the case if the
      data really is the cross-spectrum and not the complex covariance).

    The reason for this is that Anorm is A0 from the RELTRANS 2.0 paper.
    Previously, A0 was input as the norm parameter of the DC component. Now we
    need A0 for all calls because we use it to calculate logxi(r). It is
    therefore its own model parameter. The model therefore already multiplies
    the DC component by Anorm and the AC components by Anorm^2  before sending
    then to xspec.

.. note::
    :math:`h/r > 0`` is currently not used in the calculation of mu_e and mu_i. 
    These are the cosines of the angles between the incident/emitted ray and 
    the z-axis, NOT the disc normal. This may have implications when inferring
    information about the geometry of the disk.

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
| 14                     | honr       |scale height |
|                        |            |of the disk  |
+------------------------+------------+-------------+
| 14                     | Mass       |mass of the  |
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
exposure parameters. See :ref:`environmentvars` for additional parameters 
pertaining to the simulation such as seeding the simulation. There is no 
simulator for the reltransPL.

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
