#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
__author__ = 'wp'



temp = "小强"

print temp

temp_unicode = temp.decode('utf-8')

temp_gbk = temp_unicode.encode('gbk')

print(temp_unicode)

print(temp_gbk)
