# -*- coding: utf-8 -*-
"""
Created on Tue May 29 23:19:37 2018

@author: 1000091
"""

Group_A = [10,20,30,40,50]

Group_B = [5,10,15,20,25]

var_A = sum([(a - (float(sum(Group_A)) / len(Group_A))) ** 2 for a in Group_A]) / (len(Group_A) - 1)

print("Variance for group A is =", format(var_A,'.0f'))

var_B = sum([(b - (float(sum(Group_B)) / len(Group_B))) ** 2 for b in Group_B]) / (len(Group_B) - 1)

print("Variance for group B is =", format(var_B,'.0f'))

F_Test = var_A / var_B

print("The F Test as calculated is =", format(F_Test,'.0f'))