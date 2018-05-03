# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:23:55 2018

@author: Harry
"""

import smech_prog_assg2_prob_1_functions王冠珵105022529 as smf
import smech_prog_assg2_prob_2_functions王冠珵105022529 as smf2
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime 
now = datetime.now()

def err(a,b):
    '''
    a = experiment; b = theoretics
    '''
    err = (b-a)/b *100
    err = round(err,2)
    return err

num_dice = 10
num_face = 6

#=====prob1(1)==========================================
print('\nProblem 1(1)')
face_l = 1
face_h = 8
trials = 1000
N = 100
nd1 = smf.N_dice( face_l, face_h, trials, N )
tnd1 = smf.TheoN_dice( face_l, face_h, trials, N )
print('Mean, theoretical mean : ', nd1[0], tnd1[0], ' Error: ', err(nd1[0], tnd1[0]) ,'%')
print('Variance, theo-variance : ', nd1[1], tnd1[1], ' Error: ', err(nd1[1], tnd1[1]), '%')
print('Std, theo-std : ', nd1[2], tnd1[2], ' Error: ', err(nd1[2], tnd1[2]), '%')


#=====prob1(2)==========================================
#(a)
print('\nProblem 1(2a)')
face_l = 1
face_h = 10
trials = 100
N = 6
nd1 = smf.N_dice( face_l, face_h, trials, N )
tnd1 = smf.TheoN_dice( face_l, face_h, trials, N )
print('Mean, theoretical mean : ', nd1[0], tnd1[0], ' Error: ', err(nd1[0], tnd1[0]) ,'%')
print('Variance, theo-variance : ', nd1[1], tnd1[1], ' Error: ', err(nd1[1], tnd1[1]), '%')
print('Std, theo-std : ', nd1[2], tnd1[2], ' Error: ', err(nd1[2], tnd1[2]), '%')

#(b)
print('\nProblem 1(2b)')
face_l = 1
face_h = 20
trials = 1000
N = 10
nd1 = smf.N_dice( face_l, face_h, trials, N )
tnd1 = smf.TheoN_dice( face_l, face_h, trials, N )
print('Mean, theoretical mean : ', nd1[0], tnd1[0], ' Error: ', err(nd1[0], tnd1[0]) ,'%')
print('Variance, theo-variance : ', nd1[1], tnd1[1], ' Error: ', err(nd1[1], tnd1[1]), '%')
print('Std, theo-std : ', nd1[2], tnd1[2], ' Error: ', err(nd1[2], tnd1[2]), '%')

#=====prob1(3)==========================================
print('\nProblem 1(3)')
face_l = 1
face_h = 2
trials = 100
N = np.arange(1,100)
varton = np.ndarray([len(N),1])
for i in range(0, len(N)):
    varton[i] = smf.N_dice( face_l, face_h, trials, i+1 )[1]
#print(stdton)
fit = N
plt.plot(varton/ max(varton))
plt.plot(fit/ max(fit))
plt.title('The Variance to the Sides-of-die graph. ')
plt.legend(['the Variance', 'y = Nx'])
plt.show()

#=====prob2(1)==========================================
hist = smf2.statistics(2,[1,1],[4,6],100000)
plt.bar(hist[1], hist[0]/np.max(hist[0]))
plt.title('Histogram/ Probability distribution of 2 dice with 4, 6 sides.\n(Bin value at its left edge.)')
plt.show()
#=====prob2(2)==========================================
hist = smf2.statistics(3,[1,1,1],[6,6,6],100000)
plt.bar(hist[1], hist[0]/np.max(hist[0]))
plt.title('Histogram/ Probability distribution of 3 dice with 6, 6, 6 sides.\n(Bin value at its left edge.)')
plt.show()

hist = smf2.statistics(3,[1,1,1],[4,6,12],100000)
plt.bar(hist[1], hist[0]/np.max(hist[0]))
plt.title('Histogram/ Probability distribution of 3 dice with 4, 6, 12 sides.\n(Bin value at its left edge.)')
plt.show()


dur = datetime.now()-now
print('Run duration : ', dur)