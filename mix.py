import numpy as np
x=np.load('xtran_data.npy')
print(np.shape(x))
tight_data = np.load('t_xtran.npy')
print(np.shape(tight_data))
relax_data = np.load('r_xtran.npy')
print(np.shape(relax_data))

reduce = [1060,13201,1984,1240,1598,1815,1260,2241,1107,1195,12682,1141,1373,2938,58,14]
add = [-579,-6518,-1266,-618,-903,-841,-594,-975,-639,-724,-6912,-625,-771,-772,-15,16]

for ch_num in range(0,16):
    tight_data[:,:,ch_num] = ((tight_data[:, :, ch_num])-add[ch_num]) / (reduce[ch_num])
    relax_data[:,:,ch_num] = ((relax_data[:, :, ch_num])-add[ch_num]) / (reduce[ch_num])

brain_wave_data = np.append(tight_data,relax_data,axis=0)
print(np.shape(brain_wave_data))
print(np.amax(brain_wave_data),np.amin(brain_wave_data))
np.save('xtran_data.npy', brain_wave_data)
