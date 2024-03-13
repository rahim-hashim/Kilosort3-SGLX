import os
import numpy as np
import pandas as pd
from pathlib import Path
import argparse
import matplotlib.pyplot as plt
from matplotlib import gridspec, rcParams
from kilosort import run_kilosort

def plot_results(settings):

  # outputs saved to results_dir
  results_dir = Path(settings['data_dir']).joinpath('kilosort4')
  ops = np.load(results_dir / 'ops.npy', allow_pickle=True).item()
  camps = pd.read_csv(results_dir / 'cluster_Amplitude.tsv', sep='\t')['Amplitude'].values
  contam_pct = pd.read_csv(results_dir / 'cluster_ContamPct.tsv', sep='\t')['ContamPct'].values
  chan_map =  np.load(results_dir / 'channel_map.npy')
  templates =  np.load(results_dir / 'templates.npy')
  chan_best = (templates**2).sum(axis=1).argmax(axis=-1)
  chan_best = chan_map[chan_best]
  amplitudes = np.load(results_dir / 'amplitudes.npy')
  st = np.load(results_dir / 'spike_times.npy')
  clu = np.load(results_dir / 'spike_clusters.npy')
  firing_rates = np.unique(clu, return_counts=True)[1] * 30000 / st.max()
  dshift = ops['dshift']

  rcParams['axes.spines.top'] = False
  rcParams['axes.spines.right'] = False
  gray = .5 * np.ones(3)

  fig = plt.figure(figsize=(10,10), dpi=100)
  grid = gridspec.GridSpec(3, 3, figure=fig, hspace=0.5, wspace=0.5)

  ax = fig.add_subplot(grid[0,0])
  ax.plot(np.arange(0, ops['Nbatches'])*2, dshift);
  ax.set_xlabel('time (sec.)')
  ax.set_ylabel('drift (um)')

  ax = fig.add_subplot(grid[0,1:])
  t0 = 0 
  t1 = np.nonzero(st > ops['fs']*5)[0][0]
  ax.scatter(st[t0:t1]/30000., chan_best[clu[t0:t1]], s=0.5, color='k', alpha=0.25)
  ax.set_xlim([0, 5])
  ax.set_ylim([chan_map.max(), 0])
  ax.set_xlabel('time (sec.)')
  ax.set_ylabel('channel')
  ax.set_title('spikes from units')

  ax = fig.add_subplot(grid[1,0])
  nb=ax.hist(firing_rates, 20, color=gray)
  ax.set_xlabel('firing rate (Hz)')
  ax.set_ylabel('# of units')

  ax = fig.add_subplot(grid[1,1])
  nb=ax.hist(camps, 20, color=gray)
  ax.set_xlabel('amplitude')
  ax.set_ylabel('# of units')

  ax = fig.add_subplot(grid[1,2])
  nb=ax.hist(np.minimum(100, contam_pct), np.arange(0,105,5), color=gray)
  ax.plot([10, 10], [0, nb[0].max()], 'k--')
  ax.set_xlabel('% contamination')
  ax.set_ylabel('# of units')
  ax.set_title('< 10% = good units')

  for k in range(2):
      ax = fig.add_subplot(grid[2,k])
      is_ref = contam_pct<10.
      ax.scatter(firing_rates[~is_ref], camps[~is_ref], s=3, color='r', label='mua', alpha=0.25)
      ax.scatter(firing_rates[is_ref], camps[is_ref], s=3, color='b', label='good', alpha=0.25)
      ax.set_ylabel('amplitude (a.u.)')
      ax.set_xlabel('firing rate (Hz)')
      ax.legend()
      if k==1:
          ax.set_xscale('log')
          ax.set_yscale('log')
          ax.set_title('loglog')

  # 
  probe = ops['probe']
  # x and y position of probe sites
  xc, yc = probe['xc'], probe['yc']
  nc = 16 # number of channels to show
  good_units = np.nonzero(contam_pct <= 0.1)[0]
  mua_units = np.nonzero(contam_pct > 0.1)[0]

  gstr = ['good', 'mua']
  for j in range(2):
      print(f'~~~~~~~~~~~~~~ {gstr[j]} units ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
      print('title = number of spikes from each unit')
      units = good_units if j==0 else mua_units 
      fig = plt.figure(figsize=(12,3), dpi=150)
      grid = gridspec.GridSpec(2,20, figure=fig, hspace=0.25, wspace=0.5)

      for k in range(40):
          wi = units[np.random.randint(len(units))]
          wv = templates[wi].copy()  
          cb = chan_best[wi]
          nsp = (clu==wi).sum()
          
          ax = fig.add_subplot(grid[k//20, k%20])
          n_chan = wv.shape[-1]
          ic0 = max(0, cb-nc//2)
          ic1 = min(n_chan, cb+nc//2)
          wv = wv[:, ic0:ic1]
          x0, y0 = xc[ic0:ic1], yc[ic0:ic1]

          amp = 4
          for ii, (xi,yi) in enumerate(zip(x0,y0)):
              t = np.arange(-wv.shape[0]//2,wv.shape[0]//2,1,'float32')
              t /= wv.shape[0] / 20
              ax.plot(xi + t, yi + wv[:,ii]*amp, lw=0.5, color='k')

          ax.set_title(f'{nsp}', fontsize='small')
          ax.axis('off')
      plt.show()

def run_kilosort4(save_path=None, n_channels=385, probe_name='neuropixels_NHP_channel_map_linear_v1.mat'):

  settings = {'data_dir': save_path, 'n_chan_bin': n_channels}

  ops, st, clu, tF, Wall, similar_templates, is_ref, est_contam_rate = \
      run_kilosort(settings=settings, probe_name=probe_name)
  
  plot_results(settings)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Run Kilosort4 on a dataset')
  parser.add_argument('--save_path', type=str, help='Path to the folder containing the data to be processed')
  parser.add_argument('--n_channels', type=int, help='Number of channels in the probe')
  parser.add_argument('--map_file', type=str, help='Name of the channel map file in the data folder')
  args = parser.parse_args()
  run_kilosort4(save_path=args.save_path, n_channels=args.n_channels, probe_name=args.map_file)