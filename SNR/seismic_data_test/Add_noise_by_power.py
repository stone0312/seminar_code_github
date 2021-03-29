#!/usr/bin/env python3

'''
for SNR test
cal SNR by power
2021-03-14
copyright by sy
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

#def par

set_cmp = 'viridis_r'
set_title = 'SNR=0'
snr = -10
#-----------check snr----------------
print('snr:',snr)

#==================================================================
def ReadDat(fn, shape=[], dtype="float32" ) -> np.ndarray:
    if ( len(shape) == 0 ):# {{{
        pass
    if ( -1 in shape):
        n_elem = -1
    else:
        n_elem = np.prod(shape)
        pass

    arr = np.fromfile(fn, dtype, count=n_elem)
    arr = arr.reshape(shape, order="F")
    return arr# }}}

#==================================================================
def get_gaussian_noise(signal,SNR):
    noise = np.random.randn(*signal.shape)# {{{
    noise = noise - np.mean(noise)
    signal_power = (1/np.size(signal))*np.sum(np.power(signal,2))
    noise_variance = signal_power/np.power(10,(SNR/10))
    noise = (np.sqrt(noise_variance)/np.std(noise))*noise
    return noise # }}}

#==================================================================
def plot_image():
    plt.figure(1)# {{{
    ax1 = plt.subplot(1, 1, 1)

    nz, nx  = 750, 497
    data_fn = "/Users/stone/Seismic_data/mar_v_dx12.5m_dz4m_750x497.dat"
    data    = ReadDat(data_fn, shape=[nz, nx])
    data_with_noise = data+get_gaussian_noise(data,snr)
    im1 = plt.imshow(data_with_noise, cmap=set_cmp)
    plt.title(set_title, fontsize=16, fontweight='bold')

    #------------check snr----------

    Ps = (np.linalg.norm(data))**2
    Pn = (np.linalg.norm(data_with_noise-data))**2
    check_SNR = 10*np.log10(Ps/Pn)
    print('check_SNR:',check_SNR)

    #----------Add colorbar---------
    ax1_divider = make_axes_locatable(ax1)

    cax1 = ax1_divider.append_axes("right", size="3%", pad="2%")

    cb1 = plt.colorbar(im1, cax=cax1)
   
    #---------pick one trace--------

    plt.figure(2)
    trace_original   = data[:,250]
    trace_with_noise = data+get_gaussian_noise(data,snr)
    trace_with_noise = trace_with_noise[:,250]
    plt.title('trace', color='r')

    plt.plot(trace_original, color='b', label='original')
    plt.plot(trace_with_noise, color='r', label='with_noise')
    
    plt.legend()

    plt.show()

    #---------save date-------------
    data1 = data.reshape((-1,1),order = 'F')
    data1.tofile('save.dat')
    return 
# }}}
#==================================================================
def real_main():
    
    plot_image()

#==================================================================
if __name__ == "__main__":
    real_main()
