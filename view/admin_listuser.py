import db

def view():
  
  a = db.query_select('select * from user where id_user not like 1','all')
  data = ''
  for b in a:
    if b[6] == 0:
       clas = "<a href=\"#\" class=\"notifypop\"><span class=\"usagetxt redtxt\">Administrator</span></a>"
    else :
       clas = "<a href=\"#\" class=\"notifypop\"><span class=\"usagetxt greentxt\">Pengguna</span></a>"
       
    if b[10] == 0:
       stat = "<a href=\"#\" class=\"notifypop\"><span class=\"usagetxt greentxt\">Aktif</span></a>"
    else :
       stat = "<a href=\"#\" class=\"notifypop\"><span class=\"usagetxt redtxt\">Di Blok</span></a>"
    but = "<button class=\"btn\">Edit</button> <button class=\"btn\">Hapus</button>"
      
    data += "<tr><td>"+b[1]+"</td><td>"+b[3]+"</td><td>"+b[4]+"</td><td>"+b[5]+"</td><td>"+clas+"</td><td><button class=\"btn notifypop\">"+str(b[9])+"</button></td><td>"+stat+"</td><td>"+but+"</td></tr>" 
  
  return """
          <div id="rightside">
                  <div class="contentcontainer">
            <div class="headings">

                <h2>Pengguna yang terdaftar pada Mikail</h2>
            </div>
            <div class="contentbox">
             <table widht="100%">
              <tr><th>Username</th><th>Nama</th><th>Email</th><th>No Telp</th><th>Level</th><th>Point</th><th>Status</th><th>Aksi</th></tr>
              """+data+"""
             </table>   
             <div style="clear: both;"></div>
            </div>

        </div>

          </div>
	 """