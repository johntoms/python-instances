#!/usr/bin/env python
# coding=utf-8
"""
__Author__ = 'JohnToms'
__CreateTime__ = '2019/7/25'
"""
# BuiltIn Packages
# Part3   Packages
# Project Packages


class Employee():
    empCount = 0

    def __init__(self, salary, name):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: %s , Salary: %s" % (self.name, self.salary))

if __name__ == '__main__':
    employee = Employee('johntoms', '4000')
    employee1 = Employee('kangkang', '2000')
    employee1.displayEmployee()
    employee1.displayCount()
    employee.displayCount()
    employee.displayEmployee()
