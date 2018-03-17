# import numpy as np
# #
# # record_t = []
# # record_t.append(np.load('record_t1.npy'))
# # record_t2 = np.load('record_t2.npy')
# # record_t3 = np.load('record_t3.npy')
# # record_t4 = np.load('record_t4.npy')
# # record_t5 = np.load('record_t5.npy')
# #
# # # #try===================================================================================================
# text = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
# text2 = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
#
#
#
#
#
# a = []
# b = []
# for k in range(0,3,1):
#
#     for i in range(3,6,1):#一維去頭去尾之512
#         j = i+3
#         a.append(text[k,i:j])
#         b.append(text2[k,i:j])
#     # for i in range(3, 6, 1):  # 一維去頭去尾之512
#     #     j = i + 3
#     #     a.append(text2[k,i:j])
#
# a_arr=np.asarray(a)
# b_arr=np.asarray(b)
# a_3d = a_arr.reshape(3,-1,3)
# b_3d = b_arr.reshape(3,-1,3)
#
# findata = np.concatenate((a_3d,b_3d),axis=1)
# print(findata)
# print(np.shape(findata))
# # # #try===================================================================================================
# r_shape = np.shape(record_t1)
# print(r_shape)




# a = []
# # print(a)
# for k in range(0,15,1):  #ch
#
#     for i in range(51,1650,1):#一維去頭去尾之512
#         j = i+512
#         a.append(record_t1[k,i:j])
#         print(len(a))
#     # for x in range(50,1850,1):  # 一維去頭去尾之512
#     #     y = x + 512
#     #     a.append((a,record_t2[k,x:y]))
#     # for x2 in range(50,1850,1):  # 一維去頭去尾之512
#     #     y2 = x2 + 512
#     #     a.append((a,record_t3[k,x2:y2]))
#     # for x3 in range(50,1850,1):  # 一維去頭去尾之512
#     #     y3 = x3 + 512
#     #     a.append((a,record_t4[k,x3:y3]))
#     # for x4 in range(50,1850,1):  # 一維去頭去尾之512
#     #     y4 = x4 + 512
#     #     a.append((a,record_t5[k,x4:y4]))


# a_arr = np.asarray(a)
# a_shape = np.shape(a_arr)
# print(a_shape)
# b = a_arr.reshape(16,1440,512)
# print(b)

# ******************************************************************************************************************
import numpy as np

record_t1 = np.load('record_t1.npy')
record_t2 = np.load('record_t2.npy')
record_t3 = np.load('record_t3.npy')
record_t4 = np.load('record_t4.npy')
record_t5 = np.load('record_t5.npy')
# np.set_printoptions(threshold=np.nan)  #print all of the data

a = []
b = []
c = []
d = []
e = []

for ch in range(0,16,1):  #ch
    for slicestart in range(50,838,1):#一維去頭去尾之512_t1
        sliceend = slicestart+512
        a.append(record_t1[ch, slicestart:sliceend])
        b.append(record_t2[ch, slicestart:sliceend])
        c.append(record_t3[ch, slicestart:sliceend])
        d.append(record_t4[ch, slicestart:sliceend])
        e.append(record_t5[ch, slicestart:sliceend])

a_arr = np.asarray(a)
b_arr = np.asarray(b)
c_arr = np.asarray(c)
d_arr = np.asarray(d)
e_arr = np.asarray(e)

a_3d = a_arr.reshape(16,-1,512)#3Dshape(深度,行,列); "-1" will auto catch the length
b_3d = b_arr.reshape(16,-1,512)
c_3d = c_arr.reshape(16,-1,512)
d_3d = d_arr.reshape(16,-1,512)
e_3d = e_arr.reshape(16,-1,512)


findata = np.concatenate((a_3d,b_3d,c_3d,d_3d,e_3d),axis=1)
print(findata)
print(np.shape(findata))
np.save('tight_data.npy',findata)