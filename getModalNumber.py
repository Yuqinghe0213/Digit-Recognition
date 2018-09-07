import numpy as np
import random
import csv

def loadCSVfile2(filename):
    tmp = np.loadtxt(filename, dtype=np.str, delimiter=",")
    data = tmp[1:,1:].astype(np.float)
    newdata = np.squeeze(data)
    return newdata

def mode(l):
    count_dict = {}
    for i in l:
        if count_dict.has_key(i):
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    max_appear = 0
    for v in count_dict.values():
        if v > max_appear:
            max_appear = v
    if max_appear == 1:
        return
    mode_list = []
    for k, v in count_dict.items():
        if v == max_appear:
            mode_list.append(k)
    return mode_list

def productresult(data1, data2, data3):
    tt = np.zeros([3,len(data2)])
    final = np.zeros(len(data2))
    tt[0,:] = data1
    tt[1,:] = data2
    tt[2,:] = data3
    new_t = tt.T
    for i in range(0, len(data1)):
        number_max = np.zeros(3)
        number_max= mode(new_t[i])
        if (number_max == None):
            index = random.randint(0, 2)
            final[i] = new_t[i,index]
        else:
            index = [0]
            new_a = np.delete(number_max, index)
            if len(new_a)==1:
                final[i] = number_max[0]
            else:
                index2 = random.randint(0, len(number_max)-1)
                final[i] = number_max[index2]
    return final


data1 = loadCSVfile2("result_10000.csv")
data2 = loadCSVfile2("result_30000.csv")
data3 = loadCSVfile2("result_kares.csv")

final_result = productresult(data1, data2, data3)
with open('final_result.csv', 'w') as csvfile:
    wr = csv.writer(csvfile)
    wr.writerow(("Id","Label"))
    for index in range(len(final_result)):
        wr.writerow(((index+1),final_result[index]))