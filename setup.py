# -*- coding: utf-8 -*-

##############################################
# Filename: setup.py
# Mtime: 2015/7/20 16:33
# Description:
#    用于生成exe文件
# Author: Zing
##############################################

from distutils.core import setup
import py2exe

setup(
    windows=[
        {"script":"main.py","icon_resources":[(1,"logo.ico"),]}],
    options={
        "py2exe":{"includes":["sip"],"dll_excludes":["MSVCP90.dll"]}},
    data_files=[
        ("image", ["image/logo.png", "image/code.jpg", "image/loading.png"\
        	, "image/nodata.png", "image/please.png", "image/s_nodata.png"])]
    )