Reltrans model flavours
=======================

**Reltrans** is not just a single model, but is a library of different model
flavours that have slightly different physics. This page lists all the 
available models, briefly describes their differences, and lists their input
parameters.

.. note:: 
    This page might not be fully comprehensive currently as this documentation
    is under development.
    

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

