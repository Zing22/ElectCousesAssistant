from distutils.core import setup
import py2exe

setup(
	windows=[
		{"script":"main.py","icon_resources":[(1,"logo.ico"),]}],
	options={
		"py2exe":{"includes":["sip"],"dll_excludes":["MSVCP90.dll"]}},
	data_files=[
		("image", ["image/logo.png", "image/code.jpg"])]
	)