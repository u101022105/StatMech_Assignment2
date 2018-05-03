# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 17:21:41 2018

@author: Harry
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime 
now = datetime.now()

def a_die(face_l, face_h, trials):
    die = np.random.randint(face_l, face_h + face_l, trials)
    mean = np.average(die)
    std = np.std(die)
    rel_dev = std/ trials
    result = [mean, std, rel_dev, die]
    #numf = int(face_h - face_l + 1)
    #th = theory_die(numf, trials)
    #errM = error_lite(mean, th[0])
    #errS = error_lite(std, th[1])
    return result

def bincalc(nod, face_l, face_h):
    #psudie =[]
    #for i in range(0, nod):
     #   psudie = np.append(psudie, np.arange(face_l[i], face_h[i]))
    mins  = np.sum(face_l)
    maxes = np.sum(face_h)
    bins = np.arange(mins, maxes + 1 )
    return bins
    
def statistics(nod, face_l, face_h, trials):
    '''
    nod = number of die
    face_l/h needs to be a list, in corresponse with nod
    if two dice, one with 4 faces another with 6, then face_l = [0,0], face_h = [4, 6]
    the returned 'hist' is with rightmost bin edges, so I excluded the last value in order to match the st numbers,
    '''
    face_l = np.array(face_l)
    face_h = np.array(face_h)
    diehistory = np.empty([nod, trials])
    bins = bincalc(nod, face_l, face_h)
    for i in range(0, nod):
        diehistory[i] = a_die(face_l[i], face_h[i], trials)[3]
    #print(diehistory)
    #print(np.shape(diehistory))
    sum_vec = np.ones_like(np.arange(0,nod))
    #print(sum_vec)
    summ = np.dot(sum_vec, diehistory )
    hist = np.histogram(summ, bins = bins)
    hist= [hist[0], hist[1][:-1]]
    return hist

def st_general(data):
    mean = np.average(data)
    var = np.var(data)
    std = np.std(data)
    return [mean, var, std]

def st_theo(nod, face_l, face_h, trials):
    num_f = int(face_h - face_l + 1)
    lst0 = np.arange(1, num_f + 1)
    lst= []
    for i in range(0, nod):
        lst = np.append(lst, lst0)
    prob = 1 / num_f
    #q = 1 - prob
    mean = sum(lst) * prob 
    var = (1/12 * (num_f**2 -1))
    std = var**(1/2)
    #std = (1/12 * (num_f**2 -1))**(1/2)
    #rel_dev = std/ trials
    return [mean, var, std]
#st1 = statistics(2, [1,1], [4,6], 10000)
#print('[numbers-(y), bins-(x)] : \n',st1)
#
#st2 = statistics(3, [1,1,1], [6,6,6], 10000)
#print('[numbers-(y), bins-(x)] : \n',st2)
#
#st3 = statistics(3, [1,1,1], [4,6,10], 10000)
#print('[numbers-(y), bins-(x)] : \n',st3)
#
#plt.bar(st1[1], st1[0])
#plt.show()
#
#plt.bar(st2[1], st2[0])
#plt.show()
#
#plt.bar(st3[1], st3[0])
#plt.show()
#
#dur = datetime.now()-now
#print('Run duration : ', dur)
