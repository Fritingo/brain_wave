import numpy as np

record_t1 = np.load('record_t1.npy')

#try===================================================================================================
# text = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
# text2 = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]])
#
#
#
#
#
# a = text[0,1:4]
# for k in range(0,3,1):
#
#     for i in range(1,8,1):#一維去頭去尾之512
#         j = i+3
#         a = np.concatenate((a,text[k,i:j]))
#     for x in range(1, 8, 1):  # 一維去頭去尾之512
#         y = x + 3
#         a = np.concatenate((a,text2[k,x:y]))
#
# b = text[0,1:4]
# a = np.delete(a,b)
# print(a)
#
# b = a.reshape(21,3,2)
# print(b)
# # #try===================================================================================================
r_shape = np.shape(record_t1)
print(r_shape)




a = record_t1[0,52:564]
# print(a)
for k in range(0,15,1):  #ch

    for i in range(52,1588,1):#一維去頭去尾之512
        j = i+512
        a = np.concatenate((a,record_t1[k,i:j]))
    # for x in range(1, 8, 1):  # 一維去頭去尾之512
    #     y = x + 3
    #     a = np.row_stack((a,record[k,x:y]))
    # for x2 in range(1, 8, 1):  # 一維去頭去尾之512
    #     y2 = x2 + 3
    #     a = np.row_stack((a,record[k,x2:y2]))
    # for x3 in range(1, 8, 1):  # 一維去頭去尾之512
    #     y3 = x3 + 3
    #     a = np.row_stack((a,record[k,x3:y3]))
    # for x4 in range(1, 8, 1):  # 一維去頭去尾之512
    #     y4 = x4 + 3
    #     a = np.row_stack((a,record[k,x4:y4]))
b = record_t1[0,52:564]
a = np.delete(a, b)
print(a)

a_shape = np.shape(a)
print(a_shape)
# b = a.reshape(16,,)
# print(b)