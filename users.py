import os, sys, json
import web, jinja2
from web.contrib.template import render_jinja

import main as main_module

render = render_jinja(
	'templates',   # 设置模板路径.
	encoding = 'utf-8', # 编码.
)

def add(x, y):
	return x + y

render._lookup.filters['add'] = add

class HttpBase:
	def __init__(self):		
		print("request start")
	def __del__(self):
		print("request end")

class Index(HttpBase):
	def GET(self):
		return render.index()

class Page(HttpBase):
	def GET(self):
		return render.page(name = 'admin', arr = [1, 2, 3], d = { "a": "A", "b": "B", "c": "C" })

class Getparams(HttpBase):
	def GET(self):
		a = web.input(name = None)
		if a.name == None:
			a.name = "ozg"
		return 'Hello, ' + a.name + '!'

class Getparams2(HttpBase):
	def GET(self, name, name2):
		return 'Hello, ' + name + ' and ' + name2 + '!'

class Getjson(HttpBase):
	def GET(self):
		web.header('content-type', 'text/json')
		return json.dumps({'a': 'A', 'b': 'B', 'c': 'C'})

class Sess(HttpBase):
	def GET(self):
		main_module.session.user = {
			"a": "A",
			"b": "B",
			"c": "C"
		}
		
		#删除
		#main_module.session.user = None
		
		web.header('content-type', 'text/json')
		return json.dumps(main_module.session.user)
