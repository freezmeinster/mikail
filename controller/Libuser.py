import cherrypy
import db,os
import loader

class info:

   @cherrypy.expose
   def index(self):
      raise cherrypy.HTTPRedirect('/user/login')
      
   @cherrypy.expose
   def checklogin(self,username=None,password=None):
      if username != '' and password != '': 
	user = loader.setting.sanitize(username)
	pw = loader.setting.sanitize(password)
	enc_pass = loader.setting.hashing(pw)
	query = "select * from user where username like \"%s\" and password like \"%s\"" % (user,enc_pass)
	a = db.query_select(query)
	if a == None:
	  raise cherrypy.HTTPRedirect('/user/login')
	elif a[6] == 0:
	  cherrypy.session['id_user'] = a[0]
	  cherrypy.session['username'] = a[1]
	  cherrypy.session['level'] = '0'
	  raise cherrypy.HTTPRedirect('/admin')
	elif a[6] == 1:
	  cherrypy.session['id_user'] = a[0]
	  cherrypy.session['username'] = a[1]
	  cherrypy.session['level'] = '1'
	  raise cherrypy.HTTPRedirect('/user')
	else:
	  return query
      else:
	 raise cherrypy.HTTPRedirect('/user/login')
   
   @cherrypy.expose
   def logout(self):
     cherrypy.session['id_user'] = ''
     cherrypy.session['username'] = ''
     cherrypy.session['level'] = ''
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
      
      raise cherrypy.HTTPRedirect('/user/detil_user')

	
	