#!/usr/bin/env python3
#coding:utf8
import memcache

try:
    mc = memcache.Client([('192.168.1.105:11211', 1)])
    # mc.set('k','value33333')
    ret = mc.get('k')
    print (ret)
except Exception,ex:
    print ex