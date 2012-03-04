#!/usr/bin/env python
import sys
sys.path.append('/dabuzz/')

import time, os
import web

urls = (
  '/', 'hello',
  '/(static)/(.*)', 'static'
)

class hello:
  def GET(self):
    web.header("Content-Type","text/html; charset=utf-8")
    return """
    <!--[if lt IE 9]>
  <script src="static/js/html5.js"></script>
<![endif]-->
<link rel="icon" href="static/img/favicon.ico" type="image/x-icon"> 
<link rel="shortcut icon" href="static/img/favicon.ico" type="image/x-icon"> 
    <link rel="stylesheet" href="static/css/bootstrap.min.css">
    <style type="text/css">
      html, body {
        background-color: #eee;
        background-image: url("static/img/stripe.png");
      }
      body {
        padding-top: 40px;
      }
      .container > footer p {
        text-align: center;
      }
      .container {
      }

      .content {
        background-color: #fff;
        padding: 40px;
        padding-top: 20px;
        padding-bottom: 10px;
        margin: 0 -40px; /* negative indent the amount of the padding to maintain the grid system */
        -webkit-border-radius: 0 0 6px 6px;
           -moz-border-radius: 0 0 6px 6px;
                border-radius: 0 0 6px 6px;
        -webkit-box-shadow: 0px 0px 80px 80px #333333;
           -moz-box-shadow: 0px 0px 80px 80px #333333;
                box-shadow: 0px 0px 80px 80px #333333;
      }

      .wrapper {
        min-height: 500px;
      }

      /* Page header tweaks */
      .page-header {
        background-color: #f5f5f5;
        padding: 20px 20px 10px;
        margin: -20px -20px 20px;
      }

      .content .span4 {
        margin-left: 10px;
        padding-left: 9px;
        border-left: 1px solid #eee;
        display: block;
      }

      .topbar .btn {
        border: 0;
      }
      
      #footer {
        text-align: center;
        margin: 10px;
        padding: 5px;
      }
    </style>
</head><html><body><div class="container"><div class="content"><center><h1>Hello World</h1></center></div></div></body></html>
    """

  def POST(self):
    web.header("Content-Type","text/html; charset=utf-8")
    return self.GET()

if __name__ == "__main__":
  print "starting local webserver on localhost on port " + sys.argv[1]
  app = web.application(urls, globals(), autoreload=True)
  app.internalerror = web.debugerror
  app.run()

sys.stdout = sys.stderr # mod_wsgi flips out if this isn't here
app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()
