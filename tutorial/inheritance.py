#!/usr/bin/python3
from Chef import Chef
from Chinese_chef import Chinese_chef

myChef = Chef()
myChineseChef = Chinese_chef()

myChef.make_chicken()
myChef.make_special_dish()

print("")

myChineseChef.make_chicken()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()
