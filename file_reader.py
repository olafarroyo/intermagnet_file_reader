#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:01:00 2018

@author: olaf
"""

a=open('tuc20181021vsec.sec','r')
b=a.read()

c=b.split('\n')

print(c[0:10])
