#Import necessary packages

import numpy as np
import scipy.signal
import numpy as np
import scipy.io as so
import scipy.stats as stats
import os.path
import numpy as np
import re
import multiprocessing
import matplotlib.pyplot as plt
import time
import pathlib
import rempropensity as rp

def load_stateidx(ppath, name, ann_name=''):
	""" load the sleep state file of recording (folder) $ppath/$name
	@Return:
		M,K         sequence of sleep states, sequence of 
					0'1 and 1's indicating non- and annotated states
	"""
	ddir = os.path.join(ppath, name)
	ppath, name = os.path.split(ddir)

	if ann_name == '':
		ann_name = name

	sfile = os.path.join(ppath, name, 'remidx_' + ann_name + '.txt')
	
	f = open(sfile, 'r')
	lines = f.readlines()
	f.close()
	
	n = 0
	for l in lines:
		if re.match('\d', l):
			n += 1
			
	M = np.zeros(n)
	K = np.zeros(n)
	
	i = 0
	for l in lines :
		
		if re.search('^\s+$', l) :
			continue
		if re.search('\s*#', l) :
			continue
		
		if re.match('\d+\s+-?\d+', l) :
			a = re.split('\s+', l)
			M[i] = int(a[0])
			K[i] = int(a[1])
			i += 1
			
	return M,K


def make_eeg1_spec(startInd, lsplit, Mlength, M, savepath ,eeg1):
	ind1 = startInd
	limit = ind1 + lsplit

	if Mlength-10 < limit:
		limit = Mlength-10

	while ind1 < limit:
		if ind1>0:
			start = ind1 - 1
			end = ind1 + 2
			eeg_start = start*2500
			eeg_end = end*2500
			subarrays = []
			for substart in np.arange(eeg_start, eeg_end, 250):
				seqstart = substart - 500
				seqend = substart + 1000
				sup = list(range(seqstart, seqend+1))
				Pow,F = rp.power_spectrum(eeg1[sup],1000,1/1000)
				ifreq = np.where((F>=0)&(F<=20))
				subPow = Pow[ifreq]
				subarrays.append(subPow)
			totPow = np.stack(subarrays, axis=1)

			fig1 = plt.figure(figsize=(3.0,2.1),dpi=100)
			plt.subplots_adjust(top=1,bottom=0,right=1,left=0,hspace=0,wspace=0)
			plt.imshow(totPow,cmap='hot',interpolation='nearest',origin='lower')
			plt.gca().set_axis_off()
			plt.margins(0,0)
			plt.axis('off')
			plt.gca().xaxis.set_major_locator(plt.NullLocator())
			plt.gca().yaxis.set_major_locator(plt.NullLocator())
			curr = M[ind1]
			fig1.savefig(savepath+str(ind1)+'.png')
			plt.close(fig1)
		ind1+=1

def make_eeg2_spec(startInd, lsplit, Mlength, M, savepath ,eeg2):
	ind1 = startInd
	limit = ind1 + lsplit

	if Mlength-10 < limit:
		limit = Mlength-10

	while ind1 < limit:
		if ind1>0:
			start = ind1 - 1
			end = ind1 + 2
			eeg_start = start*2500
			eeg_end = end*2500
			subarrays = []
			for substart in np.arange(eeg_start, eeg_end, 250):
				seqstart = substart - 500
				seqend = substart + 1000
				sup = list(range(seqstart, seqend+1))
				Pow,F = rp.power_spectrum(eeg2[sup],1000,1/1000)
				ifreq = np.where((F>=0)&(F<=20))
				subPow = Pow[ifreq]
				subarrays.append(subPow)
			totPow = np.stack(subarrays, axis=1)

			fig2 = plt.figure(figsize=(3.0,2.1),dpi=100)
			plt.subplots_adjust(top=1,bottom=0,right=1,left=0,hspace=0,wspace=0)
			plt.imshow(totPow,cmap='hot',interpolation='nearest',origin='lower')
			plt.gca().set_axis_off()
			plt.margins(0,0)
			plt.axis('off')
			plt.gca().xaxis.set_major_locator(plt.NullLocator())
			plt.gca().yaxis.set_major_locator(plt.NullLocator())
			curr = M[ind1]
			fig2.savefig(savepath+str(ind1)+'.png')
			plt.close(fig2)
		ind1+=1


def make_emg_spec(startInd, lsplit, Mlength, M, savepath ,emg):
	ind1 = startInd
	limit = ind1 + lsplit

	if Mlength-10 < limit:
		limit = Mlength-10

	while ind1 < limit:
		if ind1>0:
			start = ind1 - 1
			end = ind1 + 2
			eeg_start = start*2500
			eeg_end = end*2500
			subarrays = []
			for substart in np.arange(eeg_start, eeg_end, 250):
				seqstart = substart - 500
				seqend = substart + 1000
				sup = list(range(seqstart, seqend+1))
				Pow,F = rp.power_spectrum(emg[sup],1000,1/1000)
				ifreq = np.where((F>=0)&(F<=20))
				subPow = Pow[ifreq]
				subarrays.append(subPow)
			totPow = np.stack(subarrays, axis=1)

			fig3 = plt.figure(figsize=(3.0,2.1),dpi=100)
			plt.subplots_adjust(top=1,bottom=0,right=1,left=0,hspace=0,wspace=0)
			plt.imshow(totPow,cmap='hot',interpolation='nearest',origin='lower')
			plt.gca().set_axis_off()
			plt.margins(0,0)
			plt.axis('off')
			plt.gca().xaxis.set_major_locator(plt.NullLocator())
			plt.gca().yaxis.set_major_locator(plt.NullLocator())
			curr = M[ind1]
			fig3.savefig(savepath+str(ind1)+'.png')
			plt.close(fig3)
		ind1+=1

if __name__ == "__main__":
	#ppath = input("Enter PPATH without quotation marks: ")
	ppath = 'B:\\AC_data2'
	recordings = os.listdir(ppath)

	for rec in recordings:
		starttime = time.time()
		M,K = load_stateidx(ppath, rec)
		split = int(len(M)/8)
		mlength = len(M)
		eeg1 = np.squeeze(so.loadmat(os.path.join(ppath, rec, 'EEG.mat'))['EEG'])
		eeg2 = np.squeeze(so.loadmat(os.path.join(ppath, rec, 'EEG2.mat'))['EEG2'])
		emg = np.squeeze(so.loadmat(os.path.join(ppath, rec, 'EMG.mat'))['EMG'])

		opath = 'B:\\allconfig\\specData'

		os.makedirs(opath+'\\'+rec)
		os.makedirs(opath+'\\'+rec+'\\eeg1')
		os.makedirs(opath+'\\'+rec+'\\eeg2')
		os.makedirs(opath+'\\'+rec+'\\emg')

		outpath1 = opath+'\\'+rec+'\\eeg1\\'
		outpath2 = opath+'\\'+rec+'\\eeg2\\'
		outpath3 = opath+'\\'+rec+'\\emg\\'

		p1 = multiprocessing.Process(target=make_eeg1_spec, args=(0*split, split, mlength, M, outpath1,eeg1,))
		p2 = multiprocessing.Process(target=make_eeg1_spec, args=(1*split, split, mlength, M, outpath1,eeg1,))
		p3 = multiprocessing.Process(target=make_eeg1_spec, args=(2*split, split, mlength, M, outpath1,eeg1,))
		p4 = multiprocessing.Process(target=make_eeg1_spec, args=(3*split, split, mlength, M, outpath1,eeg1,))
		p5 = multiprocessing.Process(target=make_eeg1_spec, args=(4*split, split, mlength, M, outpath1,eeg1,))
		p6 = multiprocessing.Process(target=make_eeg1_spec, args=(5*split, split, mlength, M, outpath1,eeg1,))
		p7 = multiprocessing.Process(target=make_eeg1_spec, args=(6*split, split, mlength, M, outpath1,eeg1,))
		p8 = multiprocessing.Process(target=make_eeg1_spec, args=(7*split, split, mlength, M, outpath1,eeg1,))

		p1.start()
		p2.start()
		p3.start()
		p4.start()
		p5.start()
		p6.start()
		p7.start()
		p8.start()

		p1.join()
		p2.join()
		p3.join()
		p4.join()
		p5.join()
		p6.join()
		p7.join()
		p8.join()

		print('EEG1 pics for ' + rec + ' made.')

		

		p9 = multiprocessing.Process(target=make_eeg2_spec, args=(0*split, split, mlength, M, outpath2,eeg2,))
		p10 = multiprocessing.Process(target=make_eeg2_spec, args=(1*split, split, mlength, M, outpath2,eeg2,))
		p11 = multiprocessing.Process(target=make_eeg2_spec, args=(2*split, split, mlength, M, outpath2,eeg2,))
		p12 = multiprocessing.Process(target=make_eeg2_spec, args=(3*split, split, mlength, M, outpath2,eeg2,))
		p13 = multiprocessing.Process(target=make_eeg2_spec, args=(4*split, split, mlength, M, outpath2,eeg2,))
		p14 = multiprocessing.Process(target=make_eeg2_spec, args=(5*split, split, mlength, M, outpath2,eeg2,))
		p15 = multiprocessing.Process(target=make_eeg2_spec, args=(6*split, split, mlength, M, outpath2,eeg2,))
		p16 = multiprocessing.Process(target=make_eeg2_spec, args=(7*split, split, mlength, M, outpath2,eeg2,))

		p9.start()
		p10.start()
		p11.start()
		p12.start()
		p13.start()
		p14.start()
		p15.start()
		p16.start()

		p9.join()
		p10.join()
		p11.join()
		p12.join()
		p13.join()
		p14.join()
		p15.join()
		p16.join()

		print('EEG2 pics for ' + rec + ' made.')

		p17 = multiprocessing.Process(target=make_emg_spec, args=(0*split, split, mlength, M, outpath3,emg,))
		p18 = multiprocessing.Process(target=make_emg_spec, args=(1*split, split, mlength, M, outpath3,emg,))
		p19 = multiprocessing.Process(target=make_emg_spec, args=(2*split, split, mlength, M, outpath3,emg,))
		p20 = multiprocessing.Process(target=make_emg_spec, args=(3*split, split, mlength, M, outpath3,emg,))
		p21 = multiprocessing.Process(target=make_emg_spec, args=(4*split, split, mlength, M, outpath3,emg,))
		p22 = multiprocessing.Process(target=make_emg_spec, args=(5*split, split, mlength, M, outpath3,emg,))
		p23 = multiprocessing.Process(target=make_emg_spec, args=(6*split, split, mlength, M, outpath3,emg,))
		p24 = multiprocessing.Process(target=make_emg_spec, args=(7*split, split, mlength, M, outpath3,emg,))

		p17.start()
		p18.start()
		p19.start()
		p20.start()
		p21.start()
		p22.start()
		p23.start()
		p24.start()

		p17.join()
		p18.join()
		p19.join()
		p20.join()
		p21.join()
		p22.join()
		p23.join()
		p24.join()
		
		print('Done!')
		print(time.time()-starttime)        
