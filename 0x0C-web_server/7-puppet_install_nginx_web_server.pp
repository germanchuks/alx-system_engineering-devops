# Puppet manifest to install nginx

# update software packages list
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# install nginx
package { 'nginx':
  ensure     => 'installed',
}

# Allow HTTP
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

# Create index file
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

file_line { 'Default config file':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

# Restart nginx
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# start service nginx
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
