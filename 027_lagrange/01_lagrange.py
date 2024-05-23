from scipy.optimize import minimize
import numpy as np 

#目标函数：
def func(args):
    fun = lambda x: 60 - 10*x[0] - 4*x[1] + x[0]**2 + x[1]**2 - x[0]*x[1]
    #fun = lambda x: 10 - x[0]**2 - x[1]**2
    return fun
 
#约束条件，包括等式约束和不等式约束
def con(args):
    cons = ({'type': 'eq', 'fun': lambda x: x[0]+x[1]-8})
    #cons = ({'type': 'ineq', 'fun': lambda x: x[1]-x[0]**2},
    #        {'type': 'eq', 'fun': lambda x: x[0]+x[1]})
    return cons 

if __name__ == "__main__":
    args = ()
    args1 = ()
    cons = con(args1)
    x0 = np.array((2.0, 1.0))  #设置初始值，初始值的设置很重要，很容易收敛到另外的极值点中，建议多试几个值
    
    #求解#
    res = minimize(func(args), x0, method='SLSQP', constraints=cons)
    print(res.success)
    print("x1=",res.x[0],";  x2=",res.x[1])
    print("最优解为：",res.fun)
