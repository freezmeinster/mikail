import cherrypy
import db
import loader

def view():
  username = cherrypy.session.get('username')
  id_user = cherrypy.session.get('id_user')
  d = db.query_select("select * from user where id_user = "+str(id_user)+"")
  return """
          <div id="rightside">
            <table >
             <tr><td>Nama</td><td>:</td><td>"""+d[3]+"""</td></tr>
             <tr><td>Email</td><td>:</td><td>"""+d[4]+"""</td></tr>
             <tr><td>No Telp</td><td>:</td><td>"""+d[5]+"""</td></tr>
             <tr><td>Alamat</td><td>:</td><td>"""+str(d[8])+"""</td></tr>
             <tr><td>Point</td><td>:</td><td>"""+str(d[9])+"""</td></tr>
            </table>
            <form action="/libuser/upload" method="POST" enctype="multipart/form-data">
             <input type="hidden" name="id_user" value=\""""+str(id_user)+"""\">
             <input type="file" name="photo">
             <input type="submit" class="btn" value="Upload">
            </form>
          </div>
	 """