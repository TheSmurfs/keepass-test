#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:FCQ
# datetime:2018/7/18 19:31
# software: PyCharm

import libkeepass

with libkeepass.open('新数据库.kdbx', password='123456', unprotect=False) as kdb:
    # print parsed element tree as xml
    #print(kdb.pretty_print())

    # decrypt the password fields
    kdb.unprotect()

    str1 = kdb.pretty_print()

    with open('xml.xml', 'wb+') as f:
        f.write(str1)
        #print(kdb.pretty_print(),f)
