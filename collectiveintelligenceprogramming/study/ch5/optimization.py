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
    return x[3]*60+x[4]


def printschedule(r):
    for d in range(len(r) / 2):
        name = people[d][0]
        origin = people[d][1]


if __name__ == '__main__':
    pass