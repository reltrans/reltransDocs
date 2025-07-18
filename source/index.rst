.. Reltrans documentation master file, created by
   sphinx-quickstart on Thu Jul 17 11:20:52 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Reltrans's documentation!
====================================

Welcome to the Reltrans documentation! 

Reltrans is a publicly available, semi-analytical model for X-ray reverberation mapping of accreting black holes in both AGN and X-ray binaries. It can be used to compute both time-averaged spectra and energy-dependent, Fourier domain cross spectra. In order to perform relativistic ray-tracing, Reltrans assumes the lamp-post model for the coronal geoemtry, with some potential tweaks depending on the model flavour. For example, it is possible to include a second lamp-post self consistently, or to modify the angular dependence of the source emissivity. 

Features
--------
Reltrans used the `YNOGK <https://github.com/bjricketts/YNOGK>`_ code to perform ray-tracing and calculate both energy shifts and light travel times, and then convolves the resulting kernel with the `Xillver <https://sites.srl.caltech.edu/~javier/xillver/>`_ rest-frame reflection spectrum model. 

The model accounts for multiple sources of lags self-consistently. Light-travel time lags from the corona to the disk are included naturally from the relativistic ray-tracing. Continuum lags driven by the variability of the corona are implemented through a pivoting power-law. Finally, the model accounts self-consistently for lags driven by changes in the reflection spectrum, which themselves are driven by variability in the power-law; in particular, the model computes the ionization changes in the disk due to changes in the corona luminosity, and the changes in the reflection spectrum due to the changes in the coronal photon index.

Reltrans is designed to be compatible with Xspec. If users are computing a time-averaged spectrum, it is then convolved with the instrument response identically to any other additive model in the software. If users are calculating a cross spectrum instead, then the convolution with the instrument response is handled internally by the model. 

Reporting issues
----------------
If you find any issues with the code, we encourage you to contact the developers by opening an issue on the Github `issues <https://github.com/reltrans/reltrans/issues>`_ page.

Documentation contents
======================

.. toctree::
   :maxdepth: 1
   
   installation 
   model_flavours

Citing Reltrans
===============

If you use Reltrans in your research, we ask that you please cite the following papers:

.. raw:: html

    <script type="text/javascript">
        function copyIngramBib() {
            var bibtex = `@ARTICLE{2019MNRAS.488..324I,
                author = {{Ingram}, Adam and {Mastroserio}, Guglielmo and {Dauser}, Thomas and {Hovenkamp}, Pieter and {van der Klis}, Michiel and {Garc{\'\i}a}, Javier A.},
                 title = "{A public relativistic transfer function model for X-ray reverberation mapping of accreting black holes}",
               journal = {\mnras},
              keywords = {black hole physics, methods: data analysis, galaxies: active, X-rays: binaries, Astrophysics - High Energy Astrophysical Phenomena},
                  year = 2019,
                 month = sep,
                volume = {488},
                number = {1},
                 pages = {324-347},
                   doi = {10.1093/mnras/stz1720},
         archivePrefix = {arXiv},
                eprint = {1906.08310},
          primaryClass = {astro-ph.HE},
                adsurl = {https://ui.adsabs.harvard.edu/abs/2019MNRAS.488..324I},
               adsnote = {Provided by the SAO/NASA Astrophysics Data System}
               }`;
            const el = document.createElement('textarea');
            el.value = bibtex;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
       
        }
        
        function copyGulloBib() {
            var bibtex = `@ARTICLE{2021MNRAS.507...55M,
                author = {{Mastroserio}, Guglielmo and {Ingram}, Adam and {Wang}, Jingyi and {Garc{\'\i}a}, Javier A. and {van der Klis}, Michiel and {Cavecchi}, Yuri and {Connors}, Riley and {Dauser}, Thomas and {Harrison}, Fiona and {Kara}, Erin and {K{\"o}nig}, Ole and {Lucchini}, Matteo},
                 title = "{Modelling correlated variability in accreting black holes: the effect of high density and variable ionization on reverberation lags}",
               journal = {\mnras},
              keywords = {accretion, accretion discs, black hole physics, relativistic processes, X-rays: binaries, X-rays: galaxies, Astrophysics - High Energy Astrophysical Phenomena},
                  year = 2021,
                 month = oct,
                volume = {507},
                number = {1},
                 pages = {55-73},
                   doi = {10.1093/mnras/stab2056},
         archivePrefix = {arXiv},
                eprint = {2107.06893},
          primaryClass = {astro-ph.HE},
                adsurl = {https://ui.adsabs.harvard.edu/abs/2021MNRAS.507...55M},
               adsnote = {Provided by the SAO/NASA Astrophysics Data System}
               }`;
            const el = document.createElement('textarea');
            el.value = bibtex;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);       
        }        
    </script>

    <ul>
        <li>Ingram et al., 2019 MNRAS, 488, 324
            [<a href="https://doi.org/10.1093/mnras/stz1720">DOI</a>]
            [<a href="https://ui.adsabs.harvard.edu/abs/2019MNRAS.488..324I">ADS</a>]
            [<a onclick="copyIngramBib()">Copy BibTeX to clipboard</a>]</li>
            
        <li>Mastroserio et al., 2021 MNRAS, 507, 55M
            [<a href="https://doi.org/10.1093/mnras/stab2056">DOI</a>]
            [<a href="https://ui.adsabs.harvard.edu/abs/2021MNRAS.507...55M/">ADS</a>]
            [<a onclick="copyGulloBib()">Copy BibTeX to clipboard</a>]</li>
    </ul>
   
Additionally, if you use the RTDist flavour we ask that you also cite: 

.. raw:: html

    <script type="text/javascript">
        function copyRTdistBib() {
            var bibtex = `@ARTICLE{2022MNRAS.509..619I,
                author = {{Ingram}, Adam and {Mastroserio}, Guglielmo and {van der Klis}, Michiel and {Nathan}, Edward and {Connors}, Riley and {Dauser}, Thomas and {Garc{\'\i}a}, Javier A. and {Kara}, Erin and {K{\"o}nig}, Ole and {Lucchini}, Matteo and {Wang}, Jingyi},
                 title = "{On measuring the Hubble constant with X-ray reverberation mapping of active galactic nuclei}",
               journal = {\mnras},
              keywords = {black hole physics, methods: data analysis, galaxies: active, cosmological parameters, Astrophysics - High Energy Astrophysical Phenomena, Astrophysics - Cosmology and Nongalactic Astrophysics},
                  year = 2022,
                 month = jan,
                volume = {509},
                number = {1},
                 pages = {619-633},
                   doi = {10.1093/mnras/stab2950},
         archivePrefix = {arXiv},
                eprint = {2110.15651},
          primaryClass = {astro-ph.HE},
                adsurl = {https://ui.adsabs.harvard.edu/abs/2022MNRAS.509..619I},
               adsnote = {Provided by the SAO/NASA Astrophysics Data System}
               }`;
            const el = document.createElement('textarea');
            el.value = bibtex;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);       
        }
    </script>

    <ul>
        <li>Ingram et al., 2022 MNRAS, 509, 619
            [<a href="https://doi.org/10.1093/mnras/stab2950">DOI</a>]
            [<a href="https://ui.adsabs.harvard.edu/abs/2022MNRAS.509..619I">ADS</a>]
            [<a onclick="copyRTdistBib()">Copy BibTeX to clipboard</a>]</li>
    </ul>

Finally, if you use the double lamp post flavour, we ask that you also cite:

.. raw:: html

    <script type="text/javascript">
        function copydoubleLPBib() {
            var bibtex = `@ARTICLE{2023ApJ...951...19L,
                author = {{Lucchini}, Matteo and {Mastroserio}, Guglielmo and {Wang}, Jingyi and {Kara}, Erin and {Ingram}, Adam and {Garcia}, Javier and {Dauser}, Thomas and {van der Klis}, Michiel and {K{\"o}nig}, Ole and {Lewin}, Collin and {Nathan}, Edward and {Panagiotou}, Christos},
                 title = "{Investigating the Impact of Vertically Extended Coronae on X-Ray Reverberation Mapping}",
               journal = {\apj},
              keywords = {Accretion, Black hole physics, Reverberation mapping, 14, 159, 2019, Astrophysics - High Energy Astrophysical Phenomena},
                  year = 2023,
                 month = jul,
                volume = {951},
                number = {1},
                   eid = {19},
                 pages = {19},
                   doi = {10.3847/1538-4357/acd24f},
         archivePrefix = {arXiv},
                eprint = {2305.05039},
          primaryClass = {astro-ph.HE},
                adsurl = {https://ui.adsabs.harvard.edu/abs/2023ApJ...951...19L},
               adsnote = {Provided by the SAO/NASA Astrophysics Data System}
               }`;
            const el = document.createElement('textarea');
            el.value = bibtex;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);       
        }
    </script>
    
    <ul>
        <li>Lucchini et al., 2023 ApJ, 951, 19
            [<a href="https://doi.org/10.3847/1538-4357/acd24f">DOI</a>]
            [<a href="https://ui.adsabs.harvard.edu/abs/2023ApJ...951...19L">ADS</a>]
            [<a onclick="copydoubleLPBib()">Copy BibTeX to clipboard</a>]</li>
    </ul>
