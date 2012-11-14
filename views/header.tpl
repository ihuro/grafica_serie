<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Graficador de series</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Graficador de Series">
    <meta name="author" content="Cesar Roldan">

    <!-- Le styles -->
    <link href="media/css/bootstrap.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
      % setdefault('extra_css', '')
      {{extra_css}}
    </style>
    <link href="media/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <link rel="shortcut icon" href="ico/favicon.ico">
  </head>

  <body>

    % setdefault('about', False)
    %if about:
    <a href="https://github.com/ihuro/grafica_serie">
      <img style="position: absolute; top: 40px; right: 0; border: 0;"
           src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png"
           alt="Fork me on GitHub">
    </a>
    %end
    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="#">Graficador de Series</a>
          <div class="nav-collapse">
            <ul class="nav">
              <li \\
              %if not about:
                  class="active"\\
              %end
              ><a href="/">Graficar</a></li>
              <li \\
              %if about:
                  class="active"\\
              %end
              ><a href="/about">Acerca de</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>
