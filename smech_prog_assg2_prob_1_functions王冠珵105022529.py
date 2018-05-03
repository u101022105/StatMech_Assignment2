# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:44:37 2018

@author: SonicsMacRetina
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime 


#def error_calc(exp, theo, ind):
#    err = (exp-theo)/ theo
#    if ind == 0:
#        print('The error between the \'mean\' and its theoretical value is ', err*100 , '%')
#    elif ind == 1:
#        print('The error between the \'standard deviation\' and its theoretical value is ', err* 100 , '%')
#    if np.abs(err) < 0.01:
#        print('This error is less than 1%')
#    return err
#
#def error_lite(exp, theo):
#    err = (exp-theo)/ theo
#    if np.abs(err) < 0.01:
#        print('This error is less than 1%')
#    return err
#
#def a_die(face_l, face_h, trials):
#    die = np.random.randint(face_l, face_h + face_l, trials)
#    mean = np.average(die)
#    std = np.std(die)
#    rel_dev = std/ trials
#    result = [mean, std, rel_dev, die]
#    #numf = int(face_h - face_l + 1)
#    #th = theory_die(numf, trials)
#    #errM = error_lite(mean, th[0])
#    #errS = error_lite(std, th[1])
#    return result
#
#def theory_die(face_l, face_h, trials):
#    #num_f = len(face)
#    num_f = int(face_h - face_l + 1)
#    lst = np.arange(1, num_face + 1)
#    prob = 1 / num_f
#    #q = 1 - prob
#    mean = sum(lst) * prob 
#    #std = ((sum((lst - mean)**2))/ trials)**(1/2)
#    std = (1/12 * (num_f**2 -1))**(1/2)
#    rel_dev = std/ trials
#    result = [mean, std, rel_dev] 
#    return result
#=====================================================
def N_dice(face_l, face_h, trials, N):
    '''
    #die = [[die1 die2... dieN](trial1), [die1...N](trial2), ....,[die1...N](trials)]
    return [meanlst, var, stdlst, sumlst, die]
    '''
    die = np.ndarray([trials, N])
    bigdie = np.ndarray([trials])
    #meanlst = np.array([])
    #varlst = np.array([])
    #stdlst = np.array([])
    #sumlst = np.array([])
    for i in range(0, trials):
        die[i] = np.random.randint(face_l, face_h + face_l, N)
        bigdie[i] = np.sum(die[i])
        #meanlst = np.append(meanlst, np.average(die[i]))
        #varlst = np.append(varlst, np.var(die[i]))
        #stdlst = np.append(stdlst, np.std(die[i]))
        #sumlst = np.append(sumlst, np.sum(die[i]))
    #print(die)
    mean = np.average(bigdie)
    var = np.var(bigdie)
    std = np.std(bigdie)
    result = [mean, var, std, bigdie, die]
    return result

def TheoN_dice(face_l, face_h, trials, N):
    '''
    return [mean, var, std] 
    '''
    num_f = int(face_h - face_l + 1)
    #mean = (1 + num_f )*N/2
    #var = 1/12*(N*(num_f +1)*( 4* num_f -3*N* num_f -3*N +2 ))
    mean = (1+num_f)/2*N
    var = (1/12 * (num_f**2 -1))*N
    std = (1/12 * (num_f**2 -1))**(1/2)* (N**(1/2))
    result = [mean, var, std] 
    return result
#=====================================================
#def hist(data, *arg):
#    bn = arg[0]
#    histlst = np.histogram(data, bn)
#    return histlst
#    
#def draw(data, bns, face, *args):
#    '''
#    args0 = face_list
#    args1 = trials
#    '''
#    fig = plt.subplot()
#    if type(bns) != int:
#        bns = 'auto'
#    fig.hist(data, bins = bns, range = (face[0],face[-1]), edgecolor='black', linewidth=1.2)
#    if len(args)>0:
#        fig.set_title('Histogram of the Die roll, faces of '+ str(len(face)) + ', trials of ' + str(args[0]))
#    plt.show()
#    return 0
#    
#def draw2(data):
#    fig = plt.subplot()
#    fig.plot(np.arange(1,len(data)+1),data)
#    plt.show()
#    return 0
#
#
#
#    
#timer = datetime.now()
##=======operation=====
##face = [1,6]
##num_face = face[1] - face[0] + 1
#
#num_face = 16
#face = np.arange(1, num_face + 1)
#trials = 10000
#bins = ''
#
#if type(bins)!= int:
#    bins = 'auto'
#atmp1 = a_die(face[0],face[-1], trials)
#thm1 = theory_die(face[0],face[-1], trials)
#histl = np.histogram(atmp1[-1], num_face)[0]
#prob = histl/ trials
#
##plt.plot(prob,'b.')
##plt.show()
#print('S = ', str(num_face), ' faces')
#print('\nProbability of faces \n'+ str(tuple(face)) + '\n' + str(prob) + '\n' )
#print('Theoretical mean, ', thm1[0], '\nVariance, ', thm1[1]**2,'\nstandard deviation, ', thm1[1],'\nrelative deviation, ', thm1[2], '\n')
#print('mean, ', atmp1[0], '\nVariance, ', atmp1[1]**2,'\nstandard deviation, ', atmp1[1],'\nrelative deviation, ', atmp1[2],'\nhistory, ', atmp1[3],'\n')
#print('faces/trials : ', num_face/trials)
#
#errM = error_calc(atmp1[0], thm1[0], 0)
#errS = error_calc(atmp1[1], thm1[1], 1)
#print('\n1/ sqrt N is : ', str( 1/trials**0.5))
##print('hislst', histl)
##draw(atmp1[3], bins, face, trials)
##draw2(histl)
##=====================
#duration = datetime.now() - timer
#print('\ntime spent : ', duration)