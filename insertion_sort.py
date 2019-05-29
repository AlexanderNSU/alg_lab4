#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insertion_sort(a):
    for i in range(len(a)):
        j=i-1
        key=a[i]
        while a[j] > key and j >= 0:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return a
