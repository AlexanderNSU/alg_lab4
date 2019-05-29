#!/usr/bin/env python
# -*- coding: utf-8 -*-

def selection_sort(a):
    n=-1
    for j in a:
        n+=1
        minim=j
        m=n-1
        change=n
        for i in a[n:]:
            m+=1
            if i < minim:
                minim=i
                change=m
        a[change]=a[n]
        a[n]=minim
    return a
