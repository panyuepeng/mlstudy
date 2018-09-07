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
    origin, dest, depart,arrive,price = line.strip().split(',')
    flights.setdefault((origin, dest),[])

    #将航班详情添加到航班列表中
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
    return x[3]*60+x[4]


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
    for d in range(len(sol)/2):
        #得到往返程的航班
        origin = people[d][1] # people的所在地
        outbound = flights[(origin, destination)][int(sol[2 * d])]
        # print 'outbound ', outbound
        returnf  = flights[(destination, origin)][int(sol[2*d + 1])]
        # print 'returnf ', returnf
        # 总价格等于所有往返成的价格只和
        totalprice += outbound[2]
        totalprice += returnf[2]

        # 记录最晚到达时间和最早离开时间
        if latestarrival < getminutes(outbound[1]): latestarrival = getminutes(outbound[1])
        if earlieastdep > getminutes(returnf[0]): earlieastdep =getminutes(returnf[0])
    # 每个人必须等待最后一个人到达机场，他们也必须在相同时间到达，并等候它们的返程航班
    totalwait = 0
    for d in range(len(sol)/2):
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
        #创建一个随机解
        r = [random.randint(domain[j][0], domain[j][1]) for j in range(len(domain))]
        # print r
        #得到成本
        cost = costf(r)
        #和当前最优的解进行比较
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
    sol = [random.randint(domain[j][0],domain[j][1]) for j in range(len(domain))]
    print sol, 'Original', '\n\n'
    acount = 0
    totallist = []
    #主循环
    while 1:
        # 创建相邻解的列表
        neighbors = []
        for j in range(len(domain)):
            #在每个方向相对于原值偏离一点
            if sol[j] > domain[j][0]:
                neighbors.append(sol[0:j] + [sol[j]-1] + sol[j+1:])
            if sol[j] < domain[j][1]:
                neighbors.append(sol[0:j] + [sol[j] + 1] + sol[j+1:])
        # 在相邻解中找到最优解
        current = costf(sol)
        best = current
        totallist.append(neighbors)
        for j in range(len(neighbors)):
            cost = costf(neighbors[j])
            if cost < best:
                best = cost
                print cost
                sol= neighbors[j]
                acount +=1
                print sol
        #如果没有更好的解则退出
        if best == current:
            atemp = []
            # for llindex in totallist:
            #     for lindex in llindex:
            #         print lindex
            break
    print acount
    return sol


if __name__ == '__main__':

#[(0, 9), (0, 9), (0, 9), (0, 9), (0, 9), (0, 9), (0, 9), (0, 9), (0, 9), (0, 9), (0, 9), (0, 9)]
    domain = [(0,9)] * (len(people)*2)
    # print domain
    # s = randomoptimize(domain,schedulecost)
    # print schedulecost(s)
    # print printschedule(s)
    print '======================='
    ss = hillclimb(domain, schedulecost)
    print '-----------------'
    print schedulecost(ss)
    printschedule(ss)
    pass