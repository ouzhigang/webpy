#!/usr/bin/python3

import os, sys, web

urls = (
	'/getparams2/(\w+)/(\w+)', 'users.Getparams2',
	'/getparams', 'users.Getparams',
	'/getjson', 'users.Getjson',
	'/page', 'users.Page',	
	'/sess', 'users.Sess',
	'^/gotoindex$', 'redirect /page',
	'/', 'users.Index'
)

app = web.application(urls, globals())
web.config.debug = False

session = web.session.Session(app, web.session.DiskStore('sessions'))

if __name__ == "__main__":
	app.run()
