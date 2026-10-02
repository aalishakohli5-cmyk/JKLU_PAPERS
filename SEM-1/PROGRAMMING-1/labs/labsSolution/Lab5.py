#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:17:16 2026

@author: aalishakohli1
"""
'''for i in range(2, 10, 3):
    print(i, end=" ")'''

'''n = 205
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count) '''


n = 84
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
print(rev)
