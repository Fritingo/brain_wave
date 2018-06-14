from keras.models import load_model
import numpy as np

record = np.load('re-relax_2.npy')
print(np.shape(record))
# print(np.shape(record))
# print(record)
new_record = []
# reduce=max-min
# add=min
# v_max = [7704.0, 1599.0, 2393.0, 1605.0, 7327.0, 4925.0, 1657.0, 7424.0, 6834.0, 7291.0, 6656.0, 8191.0, 1355.0, 6894.0, 29.0, 52.0]#re2
# v_min = [-7288.0, -1728.0, -4523.0, -1398.0, -7824.0, -1403.0, -1154.0, -7083.0, -6609.0, -7484.0, -3489.0, -7913.0, -930.0, -6861.0, 14.0, -20.0]#re2
v_max = [7704.0, 7817.0, 7797.0, 7870.0, 7776.0, 7812.0, 7815.0, 7815.0, 7816.0, 7816.0, 7809.0, 8191.0, 7745.0, 7772.0, 31.0, 55.0]#re3
v_min = [-7659.0, -7954.0, -7978.0, -7921.0, -7943.0, -7938.0, -7976.0, -7997.0, -7874.0, -8061.0, -7916.0, -8047.0, -7891.0, -7969.0, 0.0, -20.0]#re3

model = load_model('re3-model.h5')

for time_step in range(0, 512, 1):
    for slicestart in range(4500, 5350, 1):  # 一維去頭去尾之512_t1
        for ch in range(0, 16, 1):  # ch
            new_record.append(record[ch][slicestart+time_step])

new_record_arr = np.asarray(new_record)
new_record_3d = new_record_arr.reshape(-1, 512, 16)
# print(new_record_3d)

# ===================================================================================================
# for ch_num in range(0, 16):
#     new_record_3d[:, :, ch_num] = ((new_record_3d[:, :, ch_num]) - add[ch_num]) / (reduce[ch_num]) * 0.7
# reduce = [-33.0, -3.0, -71.0, -33.0, 69.0, -5.0, -19.0, 11.0, -21.0, 6.0, -19.0, -53.0, -18.0, -45.0, 22.0, 22.0]
# add = [-62.0, -91.0, -6563.0, -47.0, -19.0, -57.0, -24.0, -66.0, -89.0, -16.0, -2489.0, -6594.0, -378.0, -53.0, 22.0, 22.0]
# for i in range(0,16,1):
#     reduce.append(np.amax(record[:,i]))
#     add.append(np.amin(record[:,i]))
# print(reduce)
# print(add)
#
for ch_num in range(0,16):
    if (v_max[ch_num]-v_min[ch_num]) == 0:
        new_record_3d[:, :, ch_num] = ((new_record_3d[:, :, ch_num]) - v_min[ch_num])
        # relax_data[:, :, ch_num] = ((relax_data[:, :, ch_num]) - add[ch_num])
    else:
        new_record_3d[:,:,ch_num] = ((new_record_3d[:, :, ch_num])-v_min[ch_num]) / (v_max[ch_num]-v_min[ch_num])
        # relax_data[:,:,ch_num] = ((relax_data[:, :, ch_num])-add[ch_num]) / (reduce[ch_num]-add[ch_num])
# for ch_num in range(0,16):
#     new_record_3d[:,:,ch_num] = ((new_record_3d[:, :, ch_num])-add[ch_num]) / (reduce[ch_num]-add[ch_num]) #* 0.7
    # relax_data[:,:,ch_num] = ((relax_data[:, :, ch_num])-add[ch_num]) / (reduce[ch_num]-add[ch_num]) #* 0.7
                    # =================================================================================================

prediction = model.predict(new_record_3d)
                    # winsound.PlaySound("*",winsound.SND_ALIAS)

                    # if prediction[0, 0] > prediction[0, 1]:  # change to 1,0   0,1
                    #     prediction[0, 0] = 1
                    #     prediction[0, 1] = 0
                    #
                    # else:
                    #     prediction[0, 0] = 0
                    #     prediction[0, 1] = 1
print(np.round(prediction))
print(np.shape(prediction))
right_count=0
wrong_count=0

for x in range (len(prediction)):
    # print(np.round(prediction[x][0]))
    if np.round(prediction[x][0]) == 1.0:
        right_count+=1
    else:
        wrong_count+=1
print(right_count)
print(wrong_count)
print(right_count/(right_count+wrong_count))

# text=model.predict(record)
# print(text)


# print(text[0,0])
# print(text[0,1])

# print(text[0:1][0][1])

# if text[0,0] > text[0,1]:#change to 1,0   0,1
#     text[0,0] = 1
#     text[0,1] = 0
#
# else:
#     text[0,0] = 0
#     text[0,1] = 1
#
# print(text)