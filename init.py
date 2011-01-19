#!/usr/bin/env python

import cherrypy
import os.path
import loader


class Root:
  
    @cherrypy.expose
    def index(self): 
      user = cherrypy.session.get('id_user')
      if user == None:
	raise cherrypy.HTTPRedirect('/user/login')
      else :
	raise cherrypy.HTTPRedirect('/user/')

root = Root()
root.user = loader.User.info()
root.libuser = loader.Libuser.info()
root.admin = loader.Admin.info()
root.libadmin = loader.Libadmin.info()
root.ajax = loader.Ajax.info()
mikail_config = os.path.join(os.path.dirname(__file__), 'mikail.conf')

if __name__ == '__main__':
    cherrypy.quickstart(root, config=mikail_config)
else:
    cherrypy.tree.mount(root, config=mikail_config)
