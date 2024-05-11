import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError('List must contain nine numbers.')
  else:
    a = np.array(list).reshape((3, 3))
    mean_list = [np.mean(a, axis=0).tolist(), np.mean(a, axis=1).tolist(), np.mean(a)]
    var_list = [np.var(a, axis=0).tolist(), np.var(a, axis=1).tolist(), np.var(a)]
    std_list = [np.std(a, axis=0).tolist(), np.std(a, axis=1).tolist(), np.std(a)]
    max_list = [np.max(a, axis=0).tolist(), np.max(a, axis=1).tolist(), np.max(a)]
    min_list = [np.min(a, axis=0).tolist(), np.min(a, axis=1).tolist(), np.min(a)]
    sum_list = [np.sum(a, axis=0).tolist(), np.sum(a, axis=1).tolist(), np.sum(a)]
  
    calculations = {
      'mean': mean_list,
      'variance': var_list,
      'standard deviation': std_list,
      'max': max_list,
      'min': min_list,
      'sum': sum_list
    }
    return calculations