import cherrypy
import db
import loader

class info:
  
  @cherrypy.expose
  def index(self):
      raise cherrypy.HTTPRedirect('/user/login')
    
  @cherrypy.expose
  def user_status(self,id_user):
      a = db.query_select("select * from user where id_user = "+str(id_user)+"")
      if a[10] == 0:
	 stat = "Akiktif"
      elif a[10] == 1:
	 stat = "Kena Blok"
      return stat