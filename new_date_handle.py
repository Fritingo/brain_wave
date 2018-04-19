import numpy as np

record_r1 = np.load('record_t5.npy')
# print(record_r1)
# print(np.shape(record_r1))
# record_r2 = np.load('record_r2.npy')
#
# record_r3 = np.load('record_r3.npy')
# record_r4 = np.load('record_r4.npy')
# record_r5 = np.load('record_r5.npy')
# print(np.shape(record_r2))
# print(np.shape(record_r3))
# print(np.shape(record_r4))
# print(np.shape(record_r5))
# np.set_printoptions(threshold=np.nan)  #print all of the data

a = []
# b = []
# c = []
# d = []
# e = []

for time_step in range(0,512,1):
    for slicestart in range(100,101,1):#一維去頭去尾之512_t1
        for ch in range(0,16,1):  #ch

#
            a.append(record_r1[ch][slicestart])
            # b.append(record_r2[ch][slicestart])
            # c.append(record_r3[ch][slicestart])
            # d.append(record_r4[ch][slicestart])
            # e.append(record_r5[ch][slicestart])

a_arr = np.asarray(a)
# b_arr = np.asarray(b)
# c_arr = np.asarray(c)
# d_arr = np.asarray(d)
# e_arr = np.asarray(e)

a_3d = a_arr.reshape(-1,512,16)#3Dshape(深度,行,列); "-1" will auto catch the length
print(a_3d)
print(np.shape(a_3d))
# b_3d = b_arr.reshape(-1,512,16)
# print(b_3d)
# print(np.shape(b_3d))
# c_3d = c_arr.reshape(-1,512,16)
# print(c_3d)
# print(np.shape(c_3d))
# d_3d = d_arr.reshape(-1,512,16)
# print(d_3d)
# print(np.shape(d_3d))
# e_3d = e_arr.reshape(-1,512,16)
# print(e_3d)
# print(np.shape(e_3d))

# findata = np.concatenate((a_3d,b_3d,c_3d,d_3d,e_3d),axis=0)#,c_3d,d_3d,e_3d
# print(findata)
# print(np.shape(findata))
np.save('t_test.npy',a_3d)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import numpy as np
# text = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
# text2 = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
# text3 = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
# text4 = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
# text5 = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
#
#
#
#
#
#
#
#
# a = []
# # b = []
# # c = []
# # d = []
# # e = []
# # #一維去頭去尾之512
# for j in range(0,3,1):
#
#     for i in range(0, 6, 1):
#         for k in range(0, 3, 1):
#             a.append(text[k][i+j])
#             print(a)
#             # b.append(text2[k][i+j])
#             # c.append(text3[k][i+j])
#             # d.append(text4[k][i+j])
#             # e.append(text5[k][i+j])
#     for i in range(3, 6, 1):  # 一維去頭去尾之512
#         j = i + 3
#         a.append(text2[k,i:j])
#
# a_arr=np.asarray(a)
# #
# # b_arr=np.asarray(b)
# # c_arr=np.asarray(c)
# # d_arr=np.asarray(d)
# # e_arr=np.asarray(e)
# #
# a_3d = a_arr.reshape(-1,6,3)
# print(a_3d)
# print(np.shape(a_3d))
# # b_3d = b_arr.reshape(-1,6,3)
# # c_3c = c_arr.reshape(-1,6,3)
# # d_3d = d_arr.reshape(-1,6,3)
# # e_3d = e_arr.reshape(-1,6,3)
# findata = np.concatenate((a_3d,b_3d,c_3c,d_3d,e_3d),axis=0)
# print(findata)
# print(np.shape(findata))
# print(np.shape(findata[0:3940, :, :]))