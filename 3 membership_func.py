# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 10:47:56 2018

@author: VP LAB
"""

import matplotlib.pyplot as plt
import numpy as np


def gamma():
    a = int(input())
    b = int(input())
    x=np.linspace(-10.0,10.0,1024);
    y = np.zeros(x.shape)
    for i in range(len(x)):
        if x[i]<a:
            y[i]=0
        elif x[i]>=b:
            y[i]=1
        else:
            y[i]=(x[i]-a)/(b-a)
    plt.plot(x,y)
    plt.show()

def s():
    a = int(input())
    b = int(input())
    x = np.linspace(-10,10,1000)
    y = np.zeros(x.shape)
    for i in range(len(x)):
        if x[i]<a:
            y[i]=0
        elif x[i]<(a+b)/2.0:
            y[i]=2*((x[i]-a)/(b-a))**2
        elif x[i]<b:
            y[i]=1-2*((x[i]-b)/(b-a))**2
        else:
            y[i]=1
    plt.plot(x,y)
    plt.show()

def bell():
    a = int(input())
    b = int(input())
    c = int(input())
    x = np.linspace(-10,10,1000)
    y = 1/(1+((x-c)/a)**(2*b))
    plt.plot(x,y)
    plt.show()

def triangular():
    a = int(input())
    b = int(input())
    m = int(input())
    x = np.linspace(-10,10,1000)
    y = np.zeros(x.shape)
    for i in range(len(x)):
        if x[i]<=a or x[i]>=b:
            y[i]=0.0
        elif x[i]<=m:
            y[i]=(x[i]-a)/(m-a)
        elif x[i]<b:
            y[i]=(b-x[i])/(b-m)
    plt.plot(x,y)
    plt.show()

def l():
    a = int(input())
    b = int(input())
    x = np.linspace(-10,10,1000)
    y = np.zeros(x.shape)
    for i in range(len(x)):
        if x[i]<a:
            y[i]=1
        elif x[i]<b:
            y[i]=(b-x[i])/(b-a)
        else:
            y[i]=0
    plt.plot(x,y)
    plt.show()

def trapezoidal():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    x = np.linspace(-10,10,1000)
    y = np.zeros(x.shape)
    for i in range(len(x)):
        if x[i]<a or x[i]>d:
            y[i]=0
        elif x[i]<=b:
            y[i]=(x[i]-a)/(b-a)
        elif x[i]<c:
            y[i]=1
        else:
            y[i]=(d-x[i])/(d-c)
    plt.plot(x,y)
    plt.show()

def gaussian():
    x = np.linspace(-10,10,1000)
    mu = np.mean(x)
    std = np.std(x)
    y = np.exp(-((x-mu)**2)/(2*std**2))
    plt.plot(x,y)
    plt.show()

s()
bell()
triangular()
l()
trapezoidal()
gaussian()
