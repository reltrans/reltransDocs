========================
Reltrans model flavours
========================

**Reltrans** is not just a single model, but is a library of different model
flavours that have slightly different physics. This page lists all the 
available models, briefly describes their differences, and lists their input
parameters.

.. note:: 
    This page might not be fully comprehensive currently as this documentation
    is under development.
    

=========================
Environmental variables
=========================
There are a number of environmental variables that are set across all model 
flavours of reltrans. These relate both to the physics of the model, but also
makes model calling faster in some cases.

If environment variables are not set, the model uses default parameters. 

#. ION_ZONES [number > 0; default 20]: 
It sets the number of radial zones of the disk to calculate the ionisation 
profile of the disk. The default value is 50 zones, but the number used in 
previous works of the reltrans team is 20. If it is set to 1 the disk is 
considered to have the same ionisation and the same density everywhere. 

#. A_DENSITY [possible options 0 or 1; default 0]: 
It sets the type to density profile in the disk. There are two options 
A_DENSITY = 0 -> constant density
A_DENSITY = 1 -> Shakura&Suniev zone A density profile. 
Keep in mind that if you set the ION_ZONES = 1, it doesn't matter which density
 profile you choose because you have a single radial zone disk. 

#. MU_ZONES [number > 0; default 5 ]: 
it sets the zones for the emitting angle (they are different from the radial 
zones). In previous work we noticed that the angle dependence does not change 
dramatically the spectrum, thus we have used MU_ZONES set to 1 to speed up the 
code. 

#. RMF_SET and ARF_SET [character string; NO default]: 
they pre-set the path of the response matrix and the arf. 
This is not necessary if you are interested in the time-averaged energy 
spectrum since xspec applies the response matrix automatically. 
If you work with either the real and imaginary part of the cross-spectrum or 
directly with the lag energy spectrum you may want to consider to pre-set the 
path of the response matrix and arf to avoid the code asking for it. 
If the two variables are not set the code will ask for the path: "Enter name 
of the response file (with full path)"

============================
Models
============================

------------
reltransDCp
------------

reltransDCp can be considered the "default" version of the lastest reltrans 
release. It assumes that the disk is illuminated by a nthcomp spectrum and the
disk is a variable density disk with a fixed high energy cutoff at 300keV. This
means that it used the xillverDCp tables.

^^^^^^^^^^^^^
Parameters
^^^^^^^^^^^^^

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
| 4                      | inc        |inclination  |
+------------------------+------------+-------------+
| 5                      | inc        |inclination  |
+------------------------+------------+-------------+
| 6                      | inc        |inclination  |
+------------------------+------------+-------------+
