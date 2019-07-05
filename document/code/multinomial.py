from random import random
import numpy as np
import matplotlib.pyplot as plt

def va():
    x = random()
    if x < 1/6.:
        return 10.
    if x < 2/6.:
        return 11.
    if x < 3/6.:
        return 12.
    if x < 4/6.:
        return 13.
    if x < 5/6.:
        return 14.
    return 15.

def iv_():
    attack = va()
    defense = va()
    stamina = va()
    return (attack, defense, stamina), round((attack+defense+stamina)/45.*100.,2)

def number_trials_before_100():
    num_trials = 0
    iv, score = iv_()
    while not((iv[0] == 15) & (iv[1] == 15) & (iv[2] == 15)):
        num_trials += 1
        iv, score = iv_()
    return num_trials


def iv_success_simulate_once(num_trials=100):
    trials = []
    for i in range(num_trials):
        iv, score = iv_()
        trials.append(score)
        #if score == 100.:
        #    print i
    #print 'percentage 100:', len(np.where(np.array(trials)==100.)[0])
    #print 'percentage 97.8:', len(np.where(np.array(trials)>=97.)[0])-len(np.where(np.array(trials)==100.)[0])
    #print 'esperance:', np.mean(trials)
    #print 'ecart type:', np.std(trials)
    return len(np.where(np.array(trials)==100.)[0])
    #plt.hist(trials, normed=True, bins=100)
    #plt.title("Trials")
    #plt.show()


def iv_success_simulate(num_trials=100):
    a = 0.
    for i in range(1000):
        if iv_success_simulate_once(num_trials) == 0.:
            a += 1
    return a/1000.

#esperance: 1/p, variance: (1-p)/p^2 = (1-1/216.)/(1/216.)**2 avec p = 1/216
def iv_100_simulate():
    trials = []
    for i in range(100):
        trials.append(number_trials_before_100())
    print 'esperance:', np.mean(trials), 216.
    print 'ecart type:', np.std(trials), np.sqrt((1-1/216.)/(1/216.)**2)
    plt.hist(trials, normed=True, bins=100)
    plt.title("Trials")
    plt.show()

def shiny(shinyrate = 1/20.):
    x = random()
    if x < shinyrate:
        return 1.
    return 0.

def number_trials_before_shiny(shinyrate= 1/20.):
    num_trials = 1
    x = shiny()
    while not(x):
        x = shiny(shinyrate)
        num_trials += 1
    return num_trials

def shiny_simulate(shinyrate = 1/20.):
    trials = []
    for i in range(10000):
        trials.append(number_trials_before_shiny(shinyrate))
    print 'esperance:', np.mean(trials), 1./shinyrate
    print 'ecart type:', np.std(trials), np.sqrt((1-shinyrate)/(shinyrate)**2)
    plt.hist(trials, normed=True, bins=10)
    plt.title("Trials")
    plt.show()




