#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time         :       200603
# @Author       :       Senson
# @File         :       men_disk.py
# Used for seeking memory and disk status of vm

import psutil

def memstatus():
    print('Mem status:')
    mem = psutil.virtual_memory()
    # Unit: MB
    memtotal = mem.total/1024/1024
    memused = mem.used/1024/1024
    mempercent = str(memused/memtotal*100) + '%'

    print('%.2fMB' % memused)
    print('%.2fMB' % memtotal)
    print(mempercent)

def diskstatus():
    print('Disk status:')
    disk = psutil.disk_partitions()
    diskuse = psutil.disk_usage('/')
    # Unit: GB
    diskused = diskuse.used / 1024 / 1024 / 1024
    disktotal = diskuse.total / 1024 / 1024 / 1024
    diskpercent = diskused / disktotal * 100
    print('%.2fGB' % diskused)
    print('%.2fGB' % disktotal)
    print('%.2f' % diskpercent)



memstatus()

diskstatus()
