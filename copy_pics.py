import os
import shutil
import rempropensity as rp

#config 1 paths
c1_train_eeg1_nrem_path = 'B:\\dset_A_2\\picData\\config1\\eeg1\\train\\nrem'
c1_train_eeg1_rem_path = 'B:\\dset_A_2\\picData\\config1\\eeg1\\train\\rem'
c1_train_eeg1_wake_path = 'B:\\dset_A_2\\picData\\config1\\eeg1\\train\\wake'

c1_train_eeg2_nrem_path = 'B:\\dset_A_2\\specData\\config1\\eeg2\\train\\nrem'
c1_train_eeg2_rem_path = 'B:\\dset_A_2\\specData\\config1\\eeg2\\train\\rem'
c1_train_eeg2_wake_path = 'B:\\dset_A_2\\specData\\config1\\eeg2\\train\\wake'


c1_val_eeg1_nrem_path = 'B:\\dset_A_2\\picData\\config1\\eeg1\\val\\nrem'
c1_val_eeg1_rem_path = 'B:\\dset_A_2\\picData\\config1\\eeg1\\val\\rem'
c1_val_eeg1_wake_path = 'B:\\dset_A_2\\picData\\config1\\eeg1\\val\\wake'

c1_val_eeg2_nrem_path = 'B:\\dset_A_2\\specData\\config1\\eeg2\\val\\nrem'
c1_val_eeg2_rem_path = 'B:\\dset_A_2\\specData\\config1\\eeg2\\val\\rem'
c1_val_eeg2_wake_path = 'B:\\dset_A_2\\specData\\config1\\eeg2\\val\\wake'

picpath = 'B:\\allconfig\\specData'
recpath = 'B:\\AC_data2'

recordings = os.listdir(picpath)
recordings2 = sorted(recordings)[::5]

for rec in recordings2:
	M,S = rp.load_stateidx(recpath, rec)
	#eeg1path = os.path.join(picpath, rec, 'eeg1')
	eeg2path = os.path.join(picpath, rec, 'eeg2')
	#emgpath = os.path.join(picpath, rec, 'emg')
	allpics = os.listdir(eeg2path)
	remcnt=0
	nremcnt=0
	wakecnt=0

	for pic in allpics:
		ind = int(pic.split('.')[0])
		state = M[ind]
		if state==0:
			pass
		elif state==1:
			remcnt+=1
			if remcnt%5==1:
				#shutil.copyfile(os.path.join(eeg1path, pic), os.path.join(c1_val_eeg1_rem_path, rec+'_'+pic))
				shutil.copyfile(os.path.join(eeg2path, pic), os.path.join(c1_val_eeg2_rem_path, rec+'_'+pic))
				#shutil.copyfile(os.path.join(emgpath, pic), os.path.join(c1_val_emg_rem_path, rec+'_'+pic))
			else:
				#shutil.copyfile(os.path.join(eeg1path, pic), os.path.join(c1_train_eeg1_rem_path, rec+'_'+pic))
				shutil.copyfile(os.path.join(eeg2path, pic), os.path.join(c1_train_eeg2_rem_path, rec+'_'+pic))
				#shutil.copyfile(os.path.join(emgpath, pic), os.path.join(c1_train_emg_rem_path, rec+'_'+pic))
		elif state==2:
			wakecnt+=1
			if wakecnt%5==1:
				#shutil.copyfile(os.path.join(eeg1path, pic), os.path.join(c1_val_eeg1_wake_path, rec+'_'+pic))
				shutil.copyfile(os.path.join(eeg2path, pic), os.path.join(c1_val_eeg2_wake_path, rec+'_'+pic))
				#shutil.copyfile(os.path.join(emgpath, pic), os.path.join(c1_val_emg_wake_path, rec+'_'+pic))
			else:
				#shutil.copyfile(os.path.join(eeg1path, pic), os.path.join(c1_train_eeg1_wake_path, rec+'_'+pic))
				shutil.copyfile(os.path.join(eeg2path, pic), os.path.join(c1_train_eeg2_wake_path, rec+'_'+pic))
				#shutil.copyfile(os.path.join(emgpath, pic), os.path.join(c1_train_emg_wake_path, rec+'_'+pic))
		else:
			nremcnt+=1
			if nremcnt%5==1:
				#shutil.copyfile(os.path.join(eeg1path, pic), os.path.join(c1_val_eeg1_nrem_path, rec+'_'+pic))
				shutil.copyfile(os.path.join(eeg2path, pic), os.path.join(c1_val_eeg2_nrem_path, rec+'_'+pic))
				#shutil.copyfile(os.path.join(emgpath, pic), os.path.join(c1_val_emg_nrem_path, rec+'_'+pic))
			else:
				#shutil.copyfile(os.path.join(eeg1path, pic), os.path.join(c1_train_eeg1_nrem_path, rec+'_'+pic))
				shutil.copyfile(os.path.join(eeg2path, pic), os.path.join(c1_train_eeg2_nrem_path, rec+'_'+pic))
				#shutil.copyfile(os.path.join(emgpath, pic), os.path.join(c1_train_emg_nrem_path, rec+'_'+pic))
	print('pictures for ' + rec + ' all copied')					



