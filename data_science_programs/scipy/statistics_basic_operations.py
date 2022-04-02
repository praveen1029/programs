import math

array=[1,2,3,4,5,6,7]

def minimum(array):
    temp = array[0]
    for i in array:
        if i < temp:
            temp = i
    return temp

def maximum(array):
    temp = array[0]
    for i in array:
        if i > temp:
            temp = i
    return temp

def data_range(array):
   min = minimum(array)
   max = maximum(array)
   return max-min

def mean(array):
    temp=0
    for i in array:
        temp += i
    return temp/len(array)


def variance(array):
    avg = mean(array)
    temp=0
    for i in array:
        temp += (i-avg)**2
    return temp/len(array)


def standard_deviation(array):
    var = variance(array)
    std = math.sqrt(var)
    return std


def covariance(array,a):
    mean1 = mean(array)
    mean2 = mean(a)
    cov1 = []
    cov2 = []
    cov = 0
    total_num = len(a)
    for i in array:
        cov1.append(i-mean1)
    for i in a:
        cov2.append(i-mean2)
    for i in range(total_num):
        cov += (cov1[i]*cov2[i])
    cov /= len(a)
    return cov


a =[1,4,9,16,25,36,49]

def correlation_coeffcient(array,a):
    cov = covariance(array,a)
    std1 = standard_deviation(array)
    std2 = standard_deviation(a)
    result = cov/(std1*std2)
    return result

def percentile(array,num):
    count = 0
    array = array.sort()
    for i in array:
        if i == num:
            break
        else:
            count += 1
    per = (count/len(array))*100
    return int(per)

def postion_using_percentile(per,num):
    position = (per/100)*num
    return math.ceil(position)

ab = [2,2,3,3,3,4,4,1,1,1]


def mode(array):
    # frequency = 0
    # num = 0
    # temp = 1
    # for i in range(1,len(array)):
    #     if array[i] != array[i-1]:
    #         if temp > frequency:
    #             frequency = temp
    #             num = array[i-1]
    #             temp = 1
    #         else:
    #             temp = 1
    #     else:
    #         temp += 1

    #     if i == len(array)-1:
    #         if temp > frequency:
    #             num = array[i-1]

    counts = {x:array.count(x) for x in array}
    print(counts)
    max = 0
    mode_list = []
    key_list = list(counts.keys())
    value_list = list(counts.values())
    for i in range(len(counts)):
        if value_list[i] > max:
            mode_list = []
            max = value_list[i]
            mode_list.append(key_list[i])

        elif value_list[i] == max:           
            mode_list.append(key_list[i])

    return mode_list
    
result = mode(ab)
print(result)