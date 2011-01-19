import cherrypy

def view():
  l = cherrypy.session.get('level')
  if l == '0':
    level = 'admin'
  elif l == '1':
    level = 'user'
  else :
    raise cherrypy.HTTPRedirect('/')
    level = 'mbuh'
    
  return """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>Mikail - Beranda</title>
	<link href="/asset/styles/layout.css" rel="stylesheet" type="text/css" />
	<link href="/asset/styles/wysiwyg.css" rel="stylesheet" type="text/css" />
	<link href="/asset/themes/blue/styles.css" rel="stylesheet" type="text/css" />
        <script type="text/javascript" SRC="/asset/scripts/enhance.js"></script>	
	<script type='text/javascript' SRC="/asset/scripts/excanvas.js"></script>
	<script type='text/javascript' SRC="/asset/scripts/jquery.min.js"></script>
	<script type='text/javascript' SRC="/asset/scripts/jquery.qtip.js"></script>
        <script type='text/javascript' SRC="/asset/scripts/jquery-ui.min.js"></script>
	<script type='text/javascript' SRC="/asset/scripts/jquery.wysiwyg.js"></script>
        <script type='text/javascript' SRC="/asset/scripts/visualize.jQuery.js"></script>
        <script type="text/javascript" SRC="/asset/scripts/functions.js"></script>

	</head>
	<body id="homepage">
	    <div id="header">
	      <a href="/"""+level+"""" title=""><img SRC="/asset/img/cp_logo.png" alt="Control Panel" class="logo" /></a>
	      <div id="searcharea"><a href="http://glue.bramandityo.com" target="blank"><button class="btn">Glue Network Developer</button></a></div>
            </div>
        
    <!-- Top Breadcrumb Start -->
    <div id="breadcrumb">
    	<ul>	
        	<li><img SRC="/asset/img/icons/icon_breadcrumb.png" alt="Location" /></li>
        	<li><strong>Location:</strong></li>
            <li><a href="#" title="">Sub Section</a></li>

            <li>/</li>
            <li class="current">Control Panel</li>
        </ul>
    </div>
         """