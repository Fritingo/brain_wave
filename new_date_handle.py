import numpy as np
record_1d = []
# record_1d_2 = []
# record_1d_3 = []
# record_1d_4 = []

for record_num in range(0,3,1):
    record_name = 're-relax_'+str(record_num)+'.npy'
    record=np.load(record_name)
    print(record_num)


    for time_step in range(0,512,1):
        for slicestart in range(3500,4500,1):#一維去頭去尾之train first 2650 test 2650 3650 p3650 5350#3500 test 3500 4500 p 4500 5350
            for ch in range(0,16,1):  #ch
                record_1d.append(record[ch][slicestart + time_step])
    # elif 10 < record_num < 21:
    #     print("b")
    #     for time_step in range(0, 512, 1):
    #         for slicestart in range(100, 1000, 1):  # 一維去頭去尾之512_t1
    #             for ch in range(0, 16, 1):  # ch
    #                 record_1d_2.append(record[ch][slicestart + time_step])
    # elif 20 < record_num < 31:
    #     print("c")
    #     for time_step in range(0, 512, 1):
    #         for slicestart in range(100, 1000, 1):  # 一維去頭去尾之512_t1
    #             for ch in range(0, 16, 1):  # ch
    #                 record_1d_3.append(record[ch][slicestart + time_step])
    # elif 30 < record_num < 41:
    #     print("d")
    #     for time_step in range(0, 512, 1):
    #         for slicestart in range(100, 1000, 1):  # 一維去頭去尾之512_t1
    #             for ch in range(0, 16, 1):  # ch
    #                 record_1d_4.append(record[ch][slicestart + time_step])
                # record[ch] = record[ch][100:73841]
record_1d_arr = np.asarray(record_1d)
print(np.shape(record_1d_arr))
record_3d = record_1d_arr.reshape(-1, 512, 16)
# record_1d_arr2 = np.asarray(record_1d_2)
# record_3d2 = record_1d_arr2.reshape(-1, 512, 16)
# record_1d_arr3 = np.asarray(record_1d_3)
# record_3d3 = record_1d_arr3.reshape(-1, 512, 16)
# record_1d_arr4 = np.asarray(record_1d_4)
# record_3d4 = record_1d_arr4.reshape(-1, 512, 16)
print(np.shape(record_3d))
# findata = np.concatenate((record_3d,record_3d2,record_3d3,record_3d4),axis=0)#,c_3d,d_3d,e_3d    ,c_3d,d_3d,e_3d
# # print(findata)
# print(np.shape(findata))
np.save('re3-test_r.npy',record_3d)

# np.save('re_r_train.npy',record_3d)
# record_r1 = np.load('record_t5.npy')
# print(record_r1)
# print(np.shape(record_r1))
# record_r2 = np.load('record2_t.npy')

# record_r3 = np.load('record_r3.npy')
# record_r4 = np.load('record_r4.npy')
# record_r5 = np.load('record2_r.npy')
# print(np.shape(record_r2))
# print(np.shape(record_r3))
# print(np.shape(record_r4))
# print(np.shape(record_r5))
# np.set_printoptions(threshold=np.nan)  #print all of the data

# a = []
# b = []
# # c = []
# # d = []
# # e = []
#
# for time_step in range(0,512,1):
#     for slicestart in range(100,73300,1):#一維去頭去尾之512_t1
#         for ch in range(0,16,1):  #ch
#
# #
#             a.append(record_r1[ch][slicestart+time_step])
#             # print(record_r1)
#             # print(np.shape(record_r1))
#             # b.append(record_r2[ch][slicestart+time_step])
#             # c.append(record_r3[ch][slicestart+time_step])
#             # d.append(record_r4[ch][slicestart+time_step])
#             # e.append(record_r5[ch][slicestart+time_step])
# for time_step in range(0,512,1):
#     for slicestart in range(800,1000,1):#一維去頭去尾之512_t1
#         for ch in range(0,16,1):  #ch
#             b.append(record_r2[ch][slicestart + time_step])
#
# a_arr = np.asarray(a)
# b_arr = np.asarray(b)
# # c_arr = np.asarray(c)
# # d_arr = np.asarray(d)
# # e_arr = np.asarray(e)
#
# a_3d = a_arr.reshape(-1,512,16)#3Dshape(深度,行,列); "-1" will auto catch the length
# print(a_3d)
# print(np.shape(a_3d))
# b_3d = b_arr.reshape(-1,512,16)
# print(b_3d)
# print(np.shape(b_3d))
# # c_3d = c_arr.reshape(-1,512,16)
# # print(c_3d)
# # print(np.shape(c_3d))
# # d_3d = d_arr.reshape(-1,512,16)
# # print(d_3d)
# # print(np.shape(d_3d))
# # e_3d = e_arr.reshape(-1,512,16)
# # print(e_3d)
# # print(np.shape(e_3d))
#
# findata = np.concatenate((a_3d,b_3d),axis=0)#,c_3d,d_3d,e_3d    ,c_3d,d_3d,e_3d
# print(findata)
# print(np.shape(findata))
# np.save('tight_test.npy',findata)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import numpy as np
# text1 = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
# text2 = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
# text3 = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
# text4 = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
# text5 = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
#
#
#
# # record_1d = []
# # for record_num in range(1,6,1):
# #     # record_name = 'text'+str(record_num)
# #     # record=np.load(record_name)
# #
# #     for time_step in range(0,3,1):
# #         for slicestart in range(0,6,1):#一維去頭去尾之512_t1
# #             for ch in range(0,3,1):  #ch
# #                 record_1d.append('text'+str(record_num)[ch][slicestart + time_step])
# #                 print(record_1d)
# # record_1d_arr = np.asarray(record_1d)
# # record_3d = record_1d_arr.reshape(-1, 512, 16)
# # print(record_3d)
# # print(np.shape(record_3d))
# # # for
# a = np.zeros((16, 1))
# a = a.tolist()
#
# # a = []
# # b = []
# # c = []
# # d = []
# # e = []
# # #一維去頭去尾之512
# for j in range(0,3,1):
#     for i in range(0, 6, 1):
#         for k in range(0, 3, 1):
#             a[k].append(text1[k][i+j])
#             print(a)
#             # b.append(text2[k][i+j])
#             # c.append(text3[k][i+j])
#             # d.append(text4[k][i+j])
#             # e.append(text5[k][i+j])
#     # for i in range(3, 6, 1):  # 一維去頭去尾之512
#     #     j = i + 3
#     #     a.append(text2[k,i:j])
# for j in range(0,3,1):
#     for i in range(0, 6, 1):
#         for k in range(0, 3, 1):
#             a[k].append(text2[k][i+j])
#             print(a)
# np.transpose(a)
# print(a)
# a_arr = np.asarray(a)
# a_3d = a_arr.reshape(-1,6,3)
# print(a_3d)
# print(np.shape(a_3d))
# # a_arr=np.asarray(a)
# #
# # b_arr=np.asarray(b)
# # c_arr=np.asarray(c)
# # d_arr=np.asarray(d)
# # e_arr=np.asarray(e)
# #
# # a_3d = a_arr.reshape(-1,6,3)
# # print(a_3d)
# # print(np.shape(a_3d))
# # b_3d = b_arr.reshape(-1,6,3)
# # c_3c = c_arr.reshape(-1,6,3)
# # d_3d = d_arr.reshape(-1,6,3)
# # e_3d = e_arr.reshape(-1,6,3)
# # findata = np.concatenate((a_3d,b_3d,c_3c,d_3d,e_3d),axis=0)
# # print(findata)
# # print(np.shape(findata))
# # print(np.shape(findata[0:3940, :, :]))