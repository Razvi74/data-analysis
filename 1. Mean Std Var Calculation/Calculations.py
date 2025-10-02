import numpy as np

#Defining calculating functions (mean, variance, standard deviation, max, min, and sum)
def calc_mean(arr):
    arr_mean = np.mean(arr,axis=0,dtype=float)
    return arr_mean
def calc_var(arr):
    arr_var = np.var(arr,axis=0,dtype=float)
    return arr_var
def calc_std(arr):
    arr_std = np.std(arr,axis=0,dtype=float)
    return arr_std
def calc_max(arr):
    arr_max = np.max(arr,axis=0)
    return arr_max
def calc_min(arr):
    arr_min = np.min(arr,axis=0)
    return arr_min
def calc_sum(arr):
    arr_sum = np.sum(arr,axis=0)
    return arr_sum

#Defining the main calculation function

def calculate(l):
    length_list = len(l)
    #initialize an empty dictionary with the given keys
    Dict_result = {}
    Dict_result = dict({'mean': [], 'variance': [], 'standard deviation': [], 'max': [], 'min': [], 'sum': []})

    if (len(l) != 9):
        raise ValueError('List must contain nine numbers.')

    arr = np.array(l)
    arr = arr.reshape(3, 3)
    arr_T = arr.T

    Dict_result['mean'].append(list(calc_mean(arr)))
    Dict_result['mean'].append(list(calc_mean(arr_T)))
    Dict_result['mean'].append(calc_mean(l))

    Dict_result['variance'].append(list(calc_var(arr)))
    Dict_result['variance'].append(list(calc_var(arr_T)))
    Dict_result['variance'].append(calc_var(l))

    Dict_result['standard deviation'].append(list(calc_std(arr)))
    Dict_result['standard deviation'].append(list(calc_std(arr_T)))
    Dict_result['standard deviation'].append(calc_std(l))

    Dict_result['max'].append(list(calc_max(arr)))
    Dict_result['max'].append(list(calc_max(arr_T)))
    Dict_result['max'].append(calc_max(l))

    Dict_result['min'].append(list(calc_min(arr)))
    Dict_result['min'].append(list(calc_min(arr_T)))
    Dict_result['min'].append(calc_min(l))

    Dict_result['sum'].append(list(calc_sum(arr)))
    Dict_result['sum'].append(list(calc_sum(arr_T)))
    Dict_result['sum'].append(calc_sum(l))

    calculations = Dict_result
    return calculations
l=(0,1,2,3,4,5,6,7,8)
res=calculate(l)
print(res)

