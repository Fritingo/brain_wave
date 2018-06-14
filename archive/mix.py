import numpy as np
# x=np.load('xtran_data.npy')
# print(np.shape(x))
tight_data = np.load('re3-train_t.npy')
print(np.shape(tight_data))
relax_data = np.load('re3-train_r.npy')
print(np.shape(relax_data))
v_max = []
v_min = []
v_max = [7704.0, 7817.0, 7797.0, 7870.0, 7776.0, 7812.0, 7815.0, 7815.0, 7816.0, 7816.0, 7809.0, 8191.0, 7745.0, 7772.0, 31.0, 55.0]#re3
v_min = [-7659.0, -7954.0, -7978.0, -7921.0, -7943.0, -7938.0, -7976.0, -7997.0, -7874.0, -8061.0, -7916.0, -8047.0, -7891.0, -7969.0, 0.0, -20.0]#re3

# v_max = [7704.0, 1599.0, 2393.0, 1605.0, 7327.0, 4925.0, 1657.0, 7424.0, 6834.0, 7291.0, 6656.0, 8191.0, 1355.0, 6894.0, 29.0, 52.0]#re2
# v_min = [-7288.0, -1728.0, -4523.0, -1398.0, -7824.0, -1403.0, -1154.0, -7083.0, -6609.0, -7484.0, -3489.0, -7913.0, -930.0, -6861.0, 14.0, -20.0]#re2
# for i in range(0,16,1):
#     v_max.append(max(np.amax(tight_data[:,:,i]),np.amax(relax_data[:,:,i])))
#     v_min.append(min(np.amin(tight_data[:,:,i]),np.amin(relax_data[:,:,i])))
print(v_max)
print(v_min)

for ch_num in range(0,16):
    if (v_max[ch_num]-v_min[ch_num]) == 0:
        tight_data[:, :, ch_num] = ((tight_data[:, :, ch_num]) - v_min[ch_num])
        relax_data[:, :, ch_num] = ((relax_data[:, :, ch_num]) - v_min[ch_num])
    else:
        tight_data[:,:,ch_num] = (((tight_data[:, :, ch_num])-v_min[ch_num]) / (v_max[ch_num]-v_min[ch_num]))
        relax_data[:,:,ch_num] = (((relax_data[:, :, ch_num])-v_min[ch_num]) / (v_max[ch_num]-v_min[ch_num]))

brain_wave_data = np.concatenate((tight_data,relax_data),axis=0)
# print(i)
print(np.shape(brain_wave_data))
print(brain_wave_data)
print(np.amax(brain_wave_data),np.amin(brain_wave_data))
np.save('re3-train.npy', brain_wave_data)

