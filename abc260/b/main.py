import numpy as np
N, X, Y, Z = input().split()
ls_success = []
math_ls = list(map(int, input().split()))
eng_ls = list(map(int, input().split()))

result_math_and_eng =  np.array([math_ls, eng_ls]).T

for i in range(X):
    math_max_value = max(math_ls)
    math_max_index = math_ls.index(math_max_value)
    ls_success.push(math_max_index)
    math_ls.pop(math_max_index)
    eng_ls.pop(math_max_index)
    result_math_and_eng = np.delete(result_math_and_eng, 1, axis = math_max_index)

for j in range(Y):
    eng_ls_value = max(eng_ls)
    eng_ls_index = eng_ls_index(eng_ls_value)
    ls_success.push(eng_ls_index)
    eng_ls.pop(eng_ls_index)
    math_ls.pop(eng_ls_index)
    result_math_and_eng = np.delete(result_math_and_eng, 1, axis = eng_ls_index)


for h in range(Z):
    
