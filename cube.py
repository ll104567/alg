#!/usr/bin/python
# coding:utf-8

import pycuber as pc


s = pc.Formula()
cube = pc.Cube()

scramble = s.random()
print(scramble)
print(cube(scramble))
