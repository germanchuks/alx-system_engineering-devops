#!/usr/bin/env bash
# Automate the creation of custom HTTP header response using Puppet

exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell'
}

package { 'nginx':
  ensure => present,
}

file { '/var/www/html':
  ensure => directory
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!'
}

file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page"
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => '
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      add_header X-Served-By $hostname;
      root /var/www/html;
      index index.html index.htm;

      location /redirect_me {
        return 301 https//youtube.com/;
      }

      error_page 404 /404.html;
      location /404 {
        root /var/www/html;
        internal;
      }
    }
  '
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
  enable  => true
}
