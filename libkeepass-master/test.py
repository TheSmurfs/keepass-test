#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:FCQ
# datetime:2018/7/18 19:20
# software: PyCharm

import libkeepass

with libkeepass.open('新数据库.kdbx', password='123456', unprotect=False) as kdb:
    # print parsed element tree as xml
    print(kdb.pretty_print())

    # decrypt the password fields
    kdb.unprotect()
    print(kdb.pretty_print())