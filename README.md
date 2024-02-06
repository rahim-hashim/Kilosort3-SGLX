# Kilosort3-SGLX: One-stop shop for implementing CatGT, Kilosort3, and phy2 extract-wavforms on multiple probes from SpikeGLX output

For more information on packages included:   

* [Kilosort 3](https://github.com/MouseLand/Kilosort)
* [SpikeGLX / CatGT](https://billkarsh.github.io/SpikeGLX/)
* [phy](https://phy.readthedocs.io/en/latest/)



## General description

Running `extract-waveforms` allows for visualization of individual waveforms in WaveformView and makes possible the FeatureView, which is very helpful visualization for merging/splitting decision-making at the phy2 manual curation steps post-kilosort run.  

## Installation

Requirements:

* MATLAB >= R2016b
* MATLAB Toolboxes:
  * Parallel Computing Toolbox
  * Signal Processing Toolbox
  * Statistics and Machine Learning Toolbox
* NVIDIA GPU and CUDA capabilities
* Kilosort-3 installed on computer
* phy2 installed on computer
* Anaconda installed on computer

Setup for Kilosort-3 is identical to what has been outlined in the original [repository](https://github.com/MouseLand/Kilosort). This script will not work without Kilosort installed properly. [CatGT]([CatGT: Tshift, CAR, Gfix - SpikeGLX (billkarsh.github.io)](https://billkarsh.github.io/SpikeGLX/help/catgt_tshift/catgt_tshift/)) is also embedded in this repository under the directory CatGT-win. Lastly, make sure to setup the [phy](https://github.com/cortex-lab/phy/) environment appropriately in order to run extract-waveforms, which also relies on [Anaconda](www.anaconda.org) to also be installed on your computer.

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
