import cherrypy
import loader

class info:
  
  @cherrypy.expose
  def index(self):
    head = loader.head.view()
    right = loader.right.view()
    left = loader.left.view()
    notification = loader.notification.view()
    final = head+right+left+notification
    user = cherrypy.session.get('username')
    return final
    
  @cherrypy.expose
  def detil_user(self):
    head = loader.head.view()
    right = loader.detil_user.view()
    left = loader.left.view()
    notification = loader.notification.view()
    final = head+right+left+notification
    return final
	
  @cherrypy.expose
  def login(self):
      a = loader.login.view()
      return a
