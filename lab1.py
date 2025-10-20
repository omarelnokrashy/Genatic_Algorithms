# import re
# password = input("Enter your password: ")

# if(re.search(r'[A-Z]+',password)and re.search(r'[a-z]+',password) and re.search(r'[0-9]+',password) and len(password)>=8 and re.search(r'[@$!%*#?&]+',password)):
#     print("Strong Password")
# else:
#     print("Weak Password")

from scipy.optimize import linprog

obj = [-2,-5]
lhs_ineq = [[1,2],
             [5,3]]

rhs_ineq = [16,45]

bnd = [(0,float("inf")),
       (0,float("inf"))]    

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd)
print(opt)