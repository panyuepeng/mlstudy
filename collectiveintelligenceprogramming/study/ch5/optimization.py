# coding: utf-8
# Author: pan
# Filename: 



import time
import random
import math

people = [
    ('Seymour', 'BOS'),
    ('Franny', 'DAL'),
    ('Zooey', 'CAK'),
    ('Walt', 'MIA'),
    ('Buddy', 'ORD'),
    ('Les', 'OMA')
]

# New York的LaGuardia机场
destination = 'LGA'

flights = {}
#
for line in file('schedule.txt'):
    origin, dest, depart, arrive, price = line.strip().split(',')
    flights.setdefault((origin, dest), [])

    # 将航班详情添加到航班列表中
    flights[(origin, dest)].append((depart, arrive, int(price)))


def getminutes(t):
    """
    计算某个时间在一天中的分钟数
    :param t:
    :return:
    """
    x = time.strptime(t, '%H:%M')
    # print x
    #
    return x[3] * 60 + x[4]


def printschedule(r):
    """
    格式化输出
    :param r:
    :return:
    """
    for d in range(len(r) / 2):
        name = people[d][0]
        origin = people[d][1]
        out = flights[(origin, destination)][int(r[d])]
        ret = flights[(destination, origin)][int(r[d + 1])]
        print '%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name, origin,
                                                      out[0], out[1], out[2],
                                                      ret[0], ret[1], ret[2])


def schedulecost(sol):
    totalprice = 0
    latestarrival = 0
    earlieastdep = 24 * 60
    for d in range(len(sol) / 2):
        # 得到往返程的航班
        origin = people[d][1]  # people的所在地
        outbound = flights[(origin, destination)][int(sol[2 * d])]
        # print 'outbound ', outbound
        returnf = flights[(destination, origin)][int(sol[2 * d + 1])]
        # print 'returnf ', returnf
        # 总价格等于所有往返成的价格只和
        totalprice += outbound[2]
        totalprice += returnf[2]

        # 记录最晚到达时间和最早离开时间
        if latestarrival < getminutes(outbound[1]): latestarrival = getminutes(outbound[1])
        if earlieastdep > getminutes(returnf[0]): earlieastdep = getminutes(returnf[0])
    # 每个人必须等待最后一个人到达机场，他们也必须在相同时间到达，并等候它们的返程航班
    totalwait = 0
    for d in range(len(sol) / 2):
        origin = people[d][1]
        outbound = flights[(origin, destination)][int(sol[2 * d])]
        # print 'outbound ' , outbound
        returnf = flights[(destination, origin)][int(sol[2 * d + 1])]
        # print 'returnf ' , returnf
        totalwait += latestarrival - getminutes(outbound[1])
        totalwait += getminutes(returnf[0]) - earlieastdep

    if latestarrival < earlieastdep: totalprice += 50

    return totalprice + totalwait


# 随机搜索
def randomoptimize(domain, costf):
    best = 99999999
    bestr = None
    for i in range(1000):
        # 创建一个随机解
        r = [random.randint(domain[j][0], domain[j][1]) for j in range(len(domain))]
        # print r
        # 得到成本
        cost = costf(r)
        # 和当前最优的解进行比较
        if cost < best:
            best = cost
            bestr = r
    return r


def hillclimb(domain, costf):
    """
    创建一个随机解，爬山
    :param domain:
    :param costf:
    :return:
    """
    sol = [random.randint(domain[j][0], domain[j][1]) for j in range(len(domain))]
    # print sol, 'Original', '\n\n'
    acount = 0
    totallist = []
    # 主循环
    while 1:
        # 创建相邻解的列表
        neighbors = []
        for j in range(len(domain)):
            # 在每个方向相对于原值偏离一点
            if sol[j] > domain[j][0]:
                neighbors.append(sol[0:j] + [sol[j] - 1] + sol[j + 1:])
            if sol[j] < domain[j][1]:
                neighbors.append(sol[0:j] + [sol[j] + 1] + sol[j + 1:])
        # 在相邻解中找到最优解
        current = costf(sol)
        best = current
        totallist.append(neighbors)
        for j in range(len(neighbors)):
            cost = costf(neighbors[j])
            if cost < best:
                best = cost
                # print cost
                sol = neighbors[j]
                acount += 1
                # print sol
        # 如果没有更好的解则退出
        if best == current:
            atemp = []
            # for llindex in totallist:
            #     for lindex in llindex:
            #         print lindex
            break
    # print acount
    return sol


def random_climb(domain, costf,optm=hillclimb, count=10):
    """
    设置多个随机初始解,随机重复爬山法
    :param domain:
    :param costf:
    :param count:
    :return:
    """
    if count < 1:
        raise Exception('count must be bigger than 1')
    bestresult = None
    bestcost = -1
    for i in range(count):
        tresult = optm(domain, costf)
        tmpcost = schedulecost(tresult)
        if bestcost == -1 or tmpcost < bestcost:
            bestcost = tmpcost
            bestresult = tresult
    return bestresult, bestcost


def annealingoptimize(domain, costf, T=100000.0, cool=0.99, step=1):
    # 随机初始化值
    vec = [float(random.randint(domain[i][0], domain[i][1])) for i in range(len(domain))]

    while T > 0.1:
        # 选择一个随机索引值
        i = random.randint(0, len(domain) - 1)
        # 选择一个改变索引值的方向
        dir = random.randint(-step, step)
        # print
        # print
        # print dir
        # print 'dir : ', dir

        # 创建一个代表题解的新列表，改变其中一个值
        vecb = vec[:]
        # print 'vecb: original ', vecb
        vecb[i] += dir
        # print 'vecb: after +d ', vecb

        #防止负数对于维度数据的向下溢出
        if vecb[i] < domain[i][0]:
            vecb[i] = domain[i][0]
            # print  '1 if           ', vecb
        # 防止数对于维度数据的向上溢出
        elif vecb[i] > domain[i][1]:
            vecb[i] = domain[i][1]
            # print  '1 elif         ', vecb
        # print 'vecb: target  ', vecb
        # 计算当前成本和新的成本
        ea = costf(vec)
        eb = costf(vecb)
        # 是否是更好的解， 或者是趋向最优解的可能的临界临界解吗
        if (eb < ea or random.random() < pow(math.e, -(eb - ea) / T)):
            vec = vecb
        # 降低温度
        T = T * cool
    return vec


def pytest(target=2306):
    a = None
    while True:
        a= random_climb(domain,schedulecost,optm=hillclimb, count=500)
        b= random_climb(domain,schedulecost, optm=annealingoptimize)
        if a==b and a[1] == target:
            break
    return a


def geneticoptimeze(domain, costf, popsize=50, step=1,mutprob=0.2, elite = 0.2, maxiter = 100):
    """

    :param domain:
    :param costf:
    :param popsize: 种群大小，可选
    :param step:
    :param mutprob: 种群新成员由变异而非交叉得来的概率。可选
    :param elite: 种群中被认为是最优解且被传入下一代的部分，可选
    :param maxiter: 运行的代数，可选
    :return:
    """
    # 变异操作
    pass

if __name__ == '__main__':
    # [(0, 9), (0, 9), (0, 9), (0, 9), (0, 9), (0, 9), (0, 9) , (0, 9), (0, 9), (0, 9), (0, 9), (0, 9)]
    domain = [(0, 9)] * (len(people) * 2)
    # print domain
    # s = randomoptimize(domain,schedulecost)
    # print schedulecost(s)
    # print printschedule(s)
    # print '======================='
    # ss = hillclimb(domain, schedulecost)
    # print '-----------------'
    # print schedulecost(ss)
    # printschedule(ss)
    #
    # print random_climb(domain,schedulecost,optm=hillclimb, count=100)
    # # print annealingoptimize(domain,schedulecost)
    # print random_climb(domain,schedulecost, optm=annealingoptimize)
    pytest()
