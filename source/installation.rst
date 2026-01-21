Installation and setup instructions
===================================
Requirements
------------

The following are required:

* An HEASOFT installation (see below).

  Reltrans requires users to have a functioning `HEASOFT installation
  <https://heasarc.gsfc.nasa.gov/docs/software/lheasoft/>`_ (at least v6.30).
  This is a requirement regardless of whether you are compiling for use within
  or outside of XSPEC, as the models and libraries HEASOFT installs are
  dependencies of Reltrans.

* (Normalised) `XILLVER tables <https://sites.srl.caltech.edu/~javier/xillver/>`_.

  In particular, ``xillverCp_v3.4.fits``, ``xilverD-5.fits`` and
  ``xilver-a-Ec5.fits``. These can either be normalised yourself using a
  provided script (detailed below), or you can use the pre-normalised tables
  from `our test suite
  <https://github.com/reltrans/model-data/releases/latest>`_ (Note: these are
  not intended for science!).

  If you are normalising your own tables, set the ``RELTRANS_TABLES``
  environment variable to point to the directory with the tables.  The
  normalisation script additionally requires Python3, along with `numpy
  <https://numpy.org/>`_ and `astropy <https://www.astropy.org/>`:

  .. code-block:: bash

     export RELTRANS_TABLES="/directory/with/xillver/tables"
     make tables

  This will write the ``*_normalised.fits`` tables into the ``RELTRANS_TABLES``
  directory.

  Normalising tables can take some time and requires both several GB of memory
  and disc space. After these tables have been created, their un-normalised
  counterparts may be safely removed.


Installation
------------

Clone the source code repository and run ``make``:

 .. code-block:: bash

    git clone https://github.com/reltrans/reltrans
    cd reltrans
    make

This will compile Reltrans as a shared library into the ``build/lib``
directory. If you are using Reltrans in XSPEC, use the ``xspec`` target:

 .. code-block:: bash

    make xspec

This will generate the compile the requisite files and libraries for using
Reltrans in XSPEC to ``build/xspec``. It may then be loaded into XSPEC with

 .. code-block:: bash

    lmod xsreltrans ./build/xspec

You will now be be able to call the model identically to any other additive
model in Xspec.

.. _environmentvars:

Environmental variables
-----------------------

There are a number of environmental variables that are set across all model
flavours of reltrans. These relate both to the physics of the model, but also
makes model calling faster in some cases.

If environment variables are not set, the model uses default parameters.

* ``ION_ZONES`` [integer > 0; default 20]:

  It sets the number of radial zones of
  the disk to calculate the ionisation profile of the disk. The default value is
  50 zones, but the number used in previous works of the reltrans team is 20. If
  it is set to 1 the disk is considered to have the same ionisation and the same
  density everywhere.

* ``A_DENSITY`` [possible options 0 or 1; default 0]:

  It sets the type to density
  profile in the disk. There are two options:

  * ``A_DENSITY = 0`` -> constant density
  * ``A_DENSITY = 1`` -> Shakura & Suniev zone A density profile.

  Keep in mind that if you set the ION_ZONES = 1, it doesn't matter which
  density profile you choose because you have a single radial zone disk.

* ``MU_ZONES`` [integer > 0; default 5 ]:

  it sets the zones for the emitting angle (they are different from the radial
  zones). In previous work we noticed that the angle dependence does not change
  dramatically the spectrum, thus we have used MU_ZONES set to 1 to speed up the
  code.

* ``RELTRANS_TABLES`` [character string, NO default]:

  sets the path to where the Xillver tables to be used in the model are.

.. note::
   These tables should be the re-normalised tables produced by running the
   configuration file, NOT the tables that come directly from the website.

* ``RMF_SET`` and ``ARF_SET`` [character string; NO default]:

  they pre-set the path of the response matrix and the arf.
  This is not necessary if you are interested in the time-averaged energy
  spectrum since Xspec applies the response matrix automatically.
  If you work with either the real and imaginary part of the cross-spectrum or
  directly with the lag energy spectrum you may want to consider to pre-set the
  path of the response matrix and arf to avoid the code asking for it.
  If the two variables are not set the code will ask for the path: "Enter name
  the response file (with full path)"
  If users are modelling cross spectra from two different instruments (for
  example XMM and NuSTAR), then they also needs to specify the path to the
  second set of responses by additionally setting the RMF_SET2 and ARF_SET2.

* ``EMIN_REF`` and ``EMAX_REF`` [numbers > 0, NO default]:

  the minimum and maximum energies used to define the reference band used when
  calculating the model cross spectrum.
  If users are modelling cross spectra from two different instruments (for
  example XMM and NuSTAR), then they also need to specify the reference band of
  the second instrument by additionally setting EMIN_REF2 and EMAX_REF2.

* ``REV_VERB`` [integer > 0, default 0]:

  A verbosity switch to print information to terminal every time the model is
  run. Set to 0 during fits to avoid cluttering the terminal.

* ``BACKSCL`` [number > 0, default 1]:

  used to re-scale the background when running
  the simulation model flavours; it is identical to the BACKSCL parameter in the
  Xspec fakeit routine.

* ``SEED_SIML`` [number > 0, NO default]:

  the seed used to initialize the random
  number generator for the simulator model flavours.


An example file to initialize these quantites can be found in the Reltrans
repository (``example_set_reltrans_env``). If you want to use this file to
initialize the enviornment variables, edit the paths to the instrument responses
you're interested in to set RMF\_SET and ARF\_SET correctly, and then simply
source the file in your terminal.

Running the model outside of Xspec
----------------------------------

It is also possible to run the model outside of Xspec, using a Python wrapper
included in the repository (``f2py_interface.py``). The wrapper uses f2py
(``https://numpy.org/doc/stable/f2py/``) to call the Reltrans Fortran functions
directly in Python, by passing the need to e.g. interface with PyXspec.

The wrapper works as follows: it imports the compiled library file that
is created by the bash scripts, defines the appopriate C-types to interface
Python and C/Fortran arrays, and then defines the wrapper functions that Xspec
uses to differentiate model flavours:

.. code-block:: python

    import ctypes as ct
    import os.path
    import numpy as np

    # prepare a few pointer types for fortran
    type_double_p = ct.POINTER(ct.c_double)
    type_float_p = ct.POINTER(ct.c_float)
    type_int_p    = ct.POINTER(ct.c_int)


    #load the compiled library file
    lib = ct.cdll.LoadLibrary(os.path.dirname(__file__) + "/lib_reltrans.so")

    #define the function we want to call, and the types of its arguments
    #this is the standard Xspec model function input:
    #an energy array (ear), its size (ne), the model parameters (param), the
    #ifl spectrum flag, and the output spectrum (photar)
    wDCp = lib.tdreltransdcp_
    wDCp.argtypes = [type_float_p, type_int_p, type_float_p, type_int_p, type_float_p]
    wDCp.restype  = None

    #define a generic wrapper for all the possible model flavour wrappers
    def gen_wrap(ear, params, func):
        '''
        Takes:

        ear   : numpy array of energies
        params: array of parameters (double)

        Returns:

        photar: numpy.array (double)
        '''

        # to be extra sure you could put the following
        # but it could slow down the code
        #
        # ear    = numpy.array(ear)
        # params = numpy.array(params)

        ne = len(ear) - 1

        photar = np.zeros(ne, dtype = np.float32)

        func(ear.ctypes.data_as(type_float_p),
                   ct.byref(ct.c_int(ne)),
                   params.ctypes.data_as(type_float_p),
                   ct.byref(ct.c_int(1)),
                   photar.ctypes.data_as(type_float_p))

        return photar

    #define the function that we will use to call reltransDCp through the
    #generic wrapper
    def reltransDCp(ear, params):
        return gen_wrap(ear, params, wDCp)

.. note::
    The code above reads a library called lib_reltrans.so. This is because on
    some systems, the files produced by the Xspec compilation (libreltrans.so or
    libreltrans.dylib) may not play nicely with the f2py interface. If this is
    the case, we provide a makefile that is entirely independent of Xspec, and
    which can be used to produce the lib_reltrans.so library file by calling
    ``make revmakefile lib`` in the terminal.
