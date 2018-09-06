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
    print x
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
        origin = people[d][1]
        outbound = flights[(origin, destination)][int(sol[2 * d])]
        returnf  = flights[(destination, origin)][int(sol[2*d + 1])]

        # 总价格等于所有往返成的价格只和
        totalprice += outbound[2]
        totalprice += returnf[2]

        # 记录最晚到达时间和最早离开时间


if __name__ == '__main__':

    s = [1,4,3,2,7,3,6,3,2,4,5,3]
    printschedule(s)

    pass