# Add a custom HTTP header

# Update Package Lists
exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}
->
# Install Nginx
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
# Custom HTTP Header
file_line { 'add Header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
# Custom Root Page
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}
->
# Custom Error Page
file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
}
->
# Start Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
