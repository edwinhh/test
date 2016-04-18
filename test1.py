#coding=utf-8
'''
Created on 2016��4��15��

@author: Administrator
'''
import sys
import os
#sys.path.append("D:\\eclipse\\eclipse\\work\\Django\\d1") 
def setUp():
    print "function setup"

def tearDown():
    print "function teardown"
    
def Testfunc1():
    print "Testfunc1"
    assert True

def Testfunc2():
    print "Testfunc2"
    a=1
    b=1
    assert a==b
    
def f(a,b):
    return a+b

def k(a,b):
    return a*b
    

