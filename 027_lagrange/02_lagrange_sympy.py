#导入sympy包，用于求导，方程组求解等等
from sympy import * 
 
#设置变量
x1 = symbols("x1")
x2 = symbols("x2")
alpha = symbols("alpha")
#beta = symbols("beta")
 
#构造拉格朗日等式
L = 60 - 10*x1 - 4*x2 + x1*x1 + x2*x2 - x1*x2 - alpha * (x1 + x2 - 8)
 
#求导，构造KKT条件
difyL_x1 = diff(L, x1)  #对变量x1求导
difyL_x2 = diff(L, x2)  #对变量x2求导
difyL_alpha = diff(L, alpha) #对alpha求导
 
#求解KKT等式
aa = solve([difyL_x1, difyL_x2, difyL_alpha], [x1, x2, alpha])
print(aa)
x1=aa.get(x1)
x2=aa.get(x2)
alpha=aa.get(alpha)
print("最优解为：",60 - 10*x1 - 4*x2 + x1*x1 + x2*x2 - x1*x2 - alpha * (x1 + x2 - 8))
