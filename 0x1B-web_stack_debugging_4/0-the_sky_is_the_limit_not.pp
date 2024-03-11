# Increase FD limits for Nginx web server

exec { 'increase-ulimit':
  command       => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path          => '/usr/local/bin/:/bin/',
}

# Restart Nginx web server
exec { 'nginx-restart':
  command       => '/etc/init.d/nginx restart',
  path          => '/etc/init.d/',
}
