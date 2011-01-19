import cherrypy
import db
import loader

def view():
  username = cherrypy.session.get('username')
  id_user = cherrypy.session.get('id_user')
  a = db.query_select("select * from user where id_user = "+str(id_user)+"")
  return """
         <div id="leftside">

    	<div class="user">
        	<img SRC="%s" width="44" height="44" class="hoverimg" alt="Avatar" />
            <p>Selamat Datang:</p>
            <p class="admin">%s</p>
            <p class="userbtn"><a href="/admin/detil_admin" title="">Profile</a></p>
            <p class="userbtn"><a href="/libuser/logout" title="">Log out</a></p>
        </div>

        <div class="notifications">
        	<p class="notifycount"><a href="" title="" class="notifypop">10</a></p>
            <p><a href="" title="" class="notifypop">New Notifications</a></p>
            <p class="smltxt">(Click to open notifications)</p>
        </div>
        
        <ul id="nav">

            <li>
                <a class="expanded heading">Awan</a>
                 <ul class="navigation">
                    <li><a href="#" title="">Daftar Awan</a></li>
                    <li><a href="#" title="">Daftar Pesanan Awan</a></li>
                    <li><a href="#" title="">Buat Awan Baru</a></li>
                </ul>
           </li>
           
             <li>
                <a class="expanded heading">Pengguna</a>
                 <ul class="navigation">
                    <li><a href="/admin/list_user" title="">Daftar Pengguna</a></li>
                    <li><a href="#" title="">Daftarkan Pengguna Baru</a></li>
                    <li><a href="#" title="">Pesan Dari Pengguna</a></li>
                </ul>
           </li>
           
           <li>
                <a class="expanded heading">Server</a>
                 <ul class="navigation">
                    <li><a href="#" title="">Daftar Server</a></li>
                    <li><a href="#" title="">Tambahkan Jenis Server</a></li>
                    <li><a href="#" title="">Daftarkan Server Baru</a></li>
                    
                </ul>
           </li>
        </ul>
    </div>

         """ % (a[7],username)