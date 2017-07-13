#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: Xiannian Tang
@contact: taxini@live.com
@file: list_test.py
@time: 2017/6/26 17:07
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
bicycles.append('line')
print(bicycles)
del bicycles[4]
print(bicycles)
bicycles.insert(4,'line')
print(bicycles)
add = bicycles.pop(4)
print(bicycles)
print(add)
too_expensive = 'trek'
bicycles.remove(too_expensive)
print(bicycles)


