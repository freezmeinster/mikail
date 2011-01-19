import cherrypy
import db
import loader
import os.path

class info:
  
  @cherrypy.expose
  def index(self):
      raise cherrypy.HTTPRedirect('/user/login')
  
  @cherrypy.expose
  def upload(self,photo,id_user):
      prefix = loader.setting.hashing(id_user)
      size = 0
      mime = ['image/png','image/jpeg']
      alldata =''
      while True:
         data = photo.file.read()
         
         if not data:
            break
         alldata += data
         size += len(data)
         
       
      if photo.type not in mime:
           return "Maaf File yang anda upload tidak di izinkan"
      elif photo.type in mime:
	   if photo.type == 'image/png':
	      suffix = '.png'
	   elif photo.type == 'image/jpeg':
	      suffix = '.jpg'
          
      photo_dir = os.path.join(os.path.dirname(__file__), "../asset/photo/"+prefix+""+suffix+"")
      saved_file = open(photo_dir, 'wb')
      saved_file.write(alldata)
      saved_file.close()
      db.query_insert("update user set photo = '/asset/photo/"+prefix+""+suffix+"' where id_user = "+id_user+"")
      
      raise cherrypy.HTTPRedirect('/admin/detil_admin')