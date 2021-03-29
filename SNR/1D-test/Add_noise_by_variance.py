#!/usr/bin/env python3

'''
for SNR test 
cal SNR by variance
2021-03-14
copyright by sy
'''

import numpy as np
import matplotlib.pyplot as plt


#def par
snr1 = -5
snr2 = 0
snr3 = 5
snr4 = 10

#===========================================================================
x = np.linspace(1,6,2000)
signal = np.sin(x)

#===========================================================================
def get_gaussian_noise(signal,SNR):
    noise = np.random.randn(*signal.shape)
    noise = noise - np.mean(noise)
    #signal_power = (1/signal.shape[0])*np.sum(np.power(signal,2))
    signal_power = np.linalg.norm( signal - signal.mean() )**2 / signal.size
    noise_variance = signal_power/np.power(10,(SNR/10))
    noise = (np.sqrt(noise_variance)/np.std(noise))*noise
    return noise 

#===========================================================================
def normalized(x):
    y = x - np.mean(x)
    y = y / np.max(np.abs(y))
    return y

#===========================================================================
def real_main():
    plt.figure(1)
    plt.suptitle('cal by variance', fontsize=16, fontweight='bold')
    plt.subplots_adjust(left=0.1, wspace=0.8, top=0.8)
    #subplot 1
    plt.subplot(5, 1, 1)
    plt.plot(x, signal, label="sin(x)")
    plt.title('original signal', color='r')
    plt.legend()
    #subplot 2
    plt.subplot(5, 1, 2)
    plt.plot(x, normalized(signal+get_gaussian_noise(signal,snr1)), label=snr1)
    plt.title('add noise', color='r')
    plt.legend()
    #subplot 3
    plt.subplot(5, 1, 3)
    plt.plot(x, normalized(signal+get_gaussian_noise(signal,snr2)), label=snr2)
    #plt.plot(x, signal+get_gaussian_noise(signal,5), label="snr=5")
    plt.title('add noise', color='r')
    plt.legend()
    #subplot 4
    plt.subplot(5, 1, 4)
    plt.plot(x, normalized(signal+get_gaussian_noise(signal,snr3)), label=snr3)
    #plt.plot(x, signal+get_gaussian_noise(signal,10), label="snr=10")
    plt.title('add noise', color='r')
    plt.legend()
    #subplot 5
    plt.subplot(5, 1, 5)
    plt.plot(x, normalized(signal+get_gaussian_noise(signal,snr4)), label=snr4)
    #plt.plot(x, signal+get_gaussian_noise(signal,15), label="snr=15")
    plt.title('add noise', color='r')
    plt.legend()
    plt.show()


#===========================================================================
if __name__ == "__main__":
    real_main()
