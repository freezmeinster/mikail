import cherrypy
import loader

class info:

	@cherrypy.expose
	def index(self):
	    head = loader.head.view()
	    right = loader.right.view()
	    adminleft = loader.adminleft.view()
	    notification = loader.notification.view()
	    final = head+right+adminleft+notification
	    return final
	
	@cherrypy.expose
	def list_user(self):
	    head = loader.head.view()
	    right = loader.admin_listuser.view()
	    adminleft = loader.adminleft.view()
	    notification = loader.notification.view()
	    final = head+right+adminleft+notification
	    return final
	    
	@cherrypy.expose
	def detil_admin(self):
	    head = loader.head.view()
	    right = loader.detil_admin.view()
	    adminleft = loader.adminleft.view()
	    notification = loader.notification.view()
	    final = head+right+adminleft+notification
	    return final
	    
