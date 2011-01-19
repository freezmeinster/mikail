import cherrypy
import db
import loader

class info:
  
  @cherrypy.expose
  def index(self):
      raise cherrypy.HTTPRedirect('/user/login')