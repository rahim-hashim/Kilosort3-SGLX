# Kilosort3-SGLX: One-stop shop for implementing CatGT, Kilosort3, and phy2 extract-wavforms on multiple probes from SpikeGLX output

For more information on packages included:   

* [Kilosort 3](https://github.com/MouseLand/Kilosort)
* [SpikeGLX / CatGT](https://billkarsh.github.io/SpikeGLX/)
* [phy](https://phy.readthedocs.io/en/latest/)



## General description

Welcome to Kilosort3, a MATLAB package for spike sorting electrophysiological data up to 1024 channels. In many cases, and especially for Neuropixels probes, the automated output of Kilosort3 requires minimal manual curation. The main change from v2.5 is a completely new and much more sophisticated clustering algorithm, which we will document soon. To learn about Kilosort2.5, the primary reference is the Neuropixels 2.0 [paper](https://www.biorxiv.org/content/10.1101/2020.10.27.358291v1). The Github wiki still refers to Kilosort2, and it will be updated. 

Kilosort2.5 improves on Kilosort2 primarily in the type of drift correction we use. Where Kilosort2 modified templates as a function of time/drift (a drift **tracking** approach), Kilosort2.5 corrects the raw data directly via a sub-pixel registration process (a drift **correction** approach). Kilosort2.5 has not been as broadly tested as Kilosort2, but is expected to work out of the box on Neuropixels 1.0 and 2.0 probes, as well as other probes with vertical pitch <=40um. For other recording methods, like tetrodes or single-channel recordings, you should test empirically if v2.5 or v2.0 works better for you (use the "releases" on the github page to download older versions). 

Kilosort2 can still be accessed by downloading the release "Kilosort 2.0". It improves on the original Kilosort primarily by employing drift correction, which changes the templates continuously as a function of drift. Drift correction does not depend on a particular probe geometry, but denser spacing of sites generally helps to better track neurons, especially if the probe movement is large. Kilosort2 has been primarily developed on awake, head-fixed recordings from Neuropixels 1.0 data, but has also been tested in a few other configurations. To get a sense of how probe drift affects spike sorting, check out our "eMouse" simulation [here](https://github.com/MouseLand/Kilosort2/tree/master/eMouse_drift) and [its wiki page](https://github.com/MouseLand/Kilosort2/wiki/4.-eMouse-simulator-with-drift).

To aid in setting up a Kilosort2/2.5 run on your own probe configuration, we have developed a [graphical user interface](https://github.com/MouseLand/Kilosort/wiki/1.-The-GUI) where filepaths can be set and data loaded and visually inspected, to make sure Kilosort2/2.5 sees it correctly. The picture above is another GUI visualization: it shows the templates detected by Kilosort2 over a 60ms interval from a Neuropixels recording. The final output of Kilosort2/2.5 can be visualized and curated in the [Phy GUI](https://github.com/kwikteam/phy), which must be installed separately. Since Phy is in Python, you will also need the [npy-matlab](https://github.com/kwikteam/npy-matlab) package.

## Installation

Requirements:

* MATLAB >= R2016b
* MATLAB Toolboxes:
  * Parallel Computing Toolbox
  * Signal Processing Toolbox
  * Statistics and Machine Learning Toolbox
* NVIDIA GPU and CUDA capabilities
* phy2 installed on computer

You must run and complete successfully `mexGPUall.m` in the `CUDA` folder. This requires mexcuda support, which comes with the parallel computing toolbox. To set up mexcuda compilation, install the exact version of the CUDA toolkit compatible with your MATLAB version (see [here](https://www.mathworks.com/help/distcomp/gpu-support-by-release.html)). On Windows, you must also install a CPU compiler, for example the freely available [Visual Studio Community](https://www.visualstudio.com/vs/older-downloads/). You may need to check that the version of Visual Studio you install is compatible with your version of CUDA. If you had previously used a different CPU compiler in MATLAB, you must switch to the CUDA-compatible compiler using `mex -setup C++`. For more about mexcuda installation, see these [instructions](http://uk.mathworks.com/help/distcomp/mexcuda.html).

### General instructions for running Kilosort3-SGLX

#### MATLAB

Add all folders and subfolders to a MATLAB environment, navigate to `main-kilosort3.m`, update all paths pointing to your local data, channel map files, set Kilosort parameters (see: **Parameters** section for more information), and hit Run.

### Parameters

`probes`: imec probes included from SpikeGLX

* if empty (`[]`), includes all found folders 

`sessionNum`

* if empty (`[]`), includes all sessions (g0, g1,...)

`dest_folder`:

`runCatGT`:

* 0=don't run

* **1=run (default)** 

`cat_prb_fld`:

* only relevant with runCatGT = 1

* see CatGT ReadMe for more details (default '0:3')

`includeCatGT`:

* 0=do not include

* 1=both non-CatGT+CatGT

* **2=only CatGT (default 2)**

`extract_waveforms`: perform phy extract-waveforms (not performed in typical kilosort-3 runs)

* **0=dont run extract-waveforms (default 0)**

* 1=run extract-waveforms

`deleteCATbin`: delete CAT bin file after running CatGT to save space

* 0=save

* **1=delete (default 1)**

`deleteTemp`: delete temp_wh.dat after running Kilosort to save space

* 0=save

* **1=delete (default 1)**

## Credits

SpikeGLX by Bill Karsh

Kilosort3 by Marius Pachitariu / Nick Steinmetz  

phy2 by UCL Cortex Lab
 

## Questions

Please create an issue for bugs / installation problems.
