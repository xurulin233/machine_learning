import numpy
from matplotlib import pyplot

# 基因序列长度
DNA_SIZE = 10
# 初始种群数量
POP_SIZE = 100
# 交叉配对的概率
CROSS_RATION = 0.5
# 变异概率
MUTATION_RATION = 0.01
#繁衍代数
GENERATION = 500

def fx(x):
    return numpy.sin(10*x)*x+numpy.cos(2*x)*x
    # return x*x*x*3+x*x*2
    # return 10*numpy.sin(5*x)+7*numpy.cos(4*x)

def draw_primal():
    data = []
    xindex = []
    i = 1
    while i <= 10:
        data.append(fx(i))
        xindex.append(i)
        i+=0.1
    pyplot.plot(xindex,data)
    pyplot.show()

def otob(data):
    temp = []
    while data!=0:
        temp.append(data%2)
        data = int(data/2)
    temp.reverse()
    return temp

#DNA翻译，讲二进制转换为十进制并将其缩放到（0,10）内
def btoo(data):
    sum = 0
    for i in range(len(data)):
        sum = sum + data[i]*2**(len(data)-i-1)
    return sum/(2**DNA_SIZE-1)*10

#归一化处理
def guiyi(data):
    data = (data-numpy.min(data))/(numpy.max(data)-numpy.min(data))
    return data

#定义适合度函数，此时使用原数值即可
def fitness(data):
    return data-numpy.min(data)+1e-5

#适者生存，从种群中挑选出指定数量的优质个体（依据适合度）
'''
    replace=True表示可以取出相同的值，默认为False
'''
def select(pop,fitness_score):
    temp = fitness_score/numpy.sum(fitness_score)
    p = []
    for data in temp:
        p.append(data[0])
    #轮渡算法，按照概率挑选个体
    index = numpy.random.choice(numpy.arange(POP_SIZE),size=POP_SIZE,replace=True,p=p)
    return pop[index]

#繁衍，父母DNA配对生成新的个体（新的个体会替代原来的个体），通过交叉功能实现，交叉位置随机
def cross(parent,pop):
    if numpy.random.rand() <= CROSS_RATION:
        # 为parent随机寻找一个样本进行配对
        index = numpy.random.randint(0, POP_SIZE)
        # 在随机位置进行交叉
        cross_index = numpy.random.randint(0, 2, size=DNA_SIZE).astype(numpy.bool_)
        parent[cross_index] = pop[index][cross_index]
    return parent

#繁衍，父母DNA配对生成新的个体（新的个体会替代原来的个体），通过交叉功能实现，交叉位置随机
def cross_fitness(pop,fitness_score):
    temp = fitness_score / numpy.sum(fitness_score)
    p = []
    for data in temp:
        p.append(data[0])
    #优秀的个体其繁衍概率应该更大
    parent1_index = numpy.random.choice(numpy.arange(POP_SIZE),p=p)
    parent2_index = numpy.random.choice(numpy.arange(POP_SIZE),p=p)
    parent1 = pop[parent1_index]
    parent2 = pop[parent2_index]
    if numpy.random.rand() <= CROSS_RATION:
        #两个体在随机位置交叉，生成新的个体，此处使用True和False数组表示
        cross_index = numpy.random.randint(0, 2, size=DNA_SIZE).astype(numpy.bool_)
        parent1[cross_index] = parent2[cross_index]
    return parent1

#变异，在繁衍过程中有小概率出现变异的情况
def mutation(child):
    for i in range(DNA_SIZE):
        if numpy.random.rand() <= MUTATION_RATION:
            if child[i] == 0:
                child[i] = 1
            else:
                child[i] = 0
    return child

if __name__ == '__main__':
    #生成初始种群
    pop = numpy.random.randint(0,2,size=(POP_SIZE,DNA_SIZE))
    # print(pop)
    #繁衍GENERATION次
    for i in range(GENERATION):
        #讲二进制转换为十进制
        pop_value = []
        for j in range(POP_SIZE):
            temp = []
            temp.append(btoo(pop[j]))
            pop_value.append(temp)
        # print(pop_value)
        #计算个体适合度得分，此问题中希望fx的取值尽量大，此时就通过fx的值计算适合度
        pop_value_fitness = []
        for temp_data in pop_value:
            temp = []
            temp.append(fx(temp_data[0]))
            pop_value_fitness.append(temp)
        pop_value_fitness = fitness(pop_value_fitness)
        # print(pop_value_fitness)

        #适者生存，从中群众挑选出优质的个体
        pop = select(pop,pop_value_fitness)
        # 讲二进制转换为十进制
        pop_value = []
        for j in range(POP_SIZE):
            temp = []
            temp.append(btoo(pop[j]))
            pop_value.append(temp)
        # print(pop_value)
        # 计算个体适合度得分，此问题中希望fx的取值尽量大，此时就通过fx的值计算适合度
        pop_value_fitness = []
        for temp_data in pop_value:
            temp = []
            temp.append(fx(temp_data[0]))
            pop_value_fitness.append(temp)
        pop_value_fitness = fitness(pop_value_fitness)
        #繁衍，种群中的个体进行配对
        new_pop = []
        # for parent in pop:
        #     child = cross(parent,pop)
        #     #在繁衍的过程中子代可能出现变异
        #     child = mutation(child)
        #     #将新产生的个体重新放回种群
        #     new_pop.append(child)
        for i in range(POP_SIZE):
            child = cross_fitness(pop,pop_value_fitness)
            child = mutation(child)
            new_pop.append(child)
        pop = numpy.array(new_pop)

    # 绘制原始曲线
    data = []
    xindex = []
    i = 1
    while i <= 10:
        data.append(fx(i))
        xindex.append(i)
        i += 0.1
    pyplot.plot(xindex, data)
    # 绘制经过N次繁衍后剩下种群散点分布
    # print(pop)
    data2 = []
    xindex2 = []
    for i in range(len(pop)):
        xindex2.append(btoo(pop[i]))
        data2.append(fx(btoo(pop[i])))
    print(xindex2)
    pyplot.scatter(xindex2, data2, color='red')
    pyplot.show()
    print(f"最大值为{numpy.max(data2)}")



