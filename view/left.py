import cherrypy
import loader
import db

def view():
  username = cherrypy.session.get('username')
  id_user = cherrypy.session.get('id_user')
  a = db.query_select("select * from user where id_user = "+str(id_user)+"")
  if a[7] == None:
    avatar = "/asset/img/avatar.png"
  else :
    avatar = a[7]
  return """
         <div id="leftside">

    	<div class="user">
        	<img SRC="%s" width="44" height="44" class="hoverimg" alt="Avatar" />
            <p>Masuk sebagai:</p>
            <p class="username">%s</p>
            <p class="userbtn"><a href="/user/detil_user" title="">Profile</a></p>
            <p class="userbtn"><a href="/libuser/logout" title="">Log out</a></p>
        </div>

        <div class="notifications">
        	<p class="notifycount"><a href="" title="" class="notifypop">10</a></p>
            <p><a href="" title="" class="notifypop">New Notifications</a></p>
            <p class="smltxt">(Click to open notifications)</p>
        </div>
        
        <ul id="nav">

            <li>
                <a class="expanded heading">Aset Anda</a>
                 <ul class="navigation">
                    <li><a href="#" title="">Daftar Aset Anda</a></li>
                    <li><a href="#" title="">Buat Awan Baru</a></li>
                    <li><a href="#" title="">Section link here</a></li>
                </ul>
           
        </ul>
    </div>

         """ % (avatar,username)