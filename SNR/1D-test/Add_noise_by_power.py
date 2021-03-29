#!/usr/bin/env python3

'''
for SNR test
cal SNR by power
2021-03-14
copyright by sy
'''

import numpy as np
import matplotlib.pyplot as plt


#def par



#==================================================================
x = np.linspace(1,6,2000)
signal = np.sin(x)

#==================================================================
def get_gaussian_noise(signal,SNR):
    noise = np.random.randn(*signal.shape)
    noise = noise - np.mean(noise)
    signal_power = (1/signal.shape[0])*np.sum(np.power(signal,2))
    noise_variance = signal_power/np.power(10,(SNR/10))
    #noise_variance = signal_power/np.power(10,(SNR/20))
    noise = (np.sqrt(noise_variance)/np.std(noise))*noise
    return noise 

#==================================================================
def real_main():
    plt.figure(1)
    plt.suptitle('cal by power', fontsize=16, fontweight='bold')
    plt.subplots_adjust(left=0.2, wspace=0.8, top=0.8)
    #subplot 1
    plt.subplot(3, 1, 1)
    plt.plot(x, signal, label="sin(x)")
    plt.title('original signal', color='r')
    plt.legend()
    #subplot 2
    plt.subplot(3, 1, 2)
    plt.plot(x, signal+get_gaussian_noise(signal,-20), label="snr=-20")
    plt.title('add noise', color='r')
    plt.legend()
    #subplot 3
    plt.subplot(3, 1, 3)
    plt.plot(x, signal+get_gaussian_noise(signal,20), label="snr=20")
    plt.title('add noise', color='r')
    plt.legend()
    plt.show()


#==================================================================
if __name__ == "__main__":
    real_main()
