# Change the OS configuration so holberton user can login and open a file
# without any error message.

exec { 'increase-holberton-user-hard-file-limit':
  command       => 'sed -i "/^holberton hard/s/5/50000/" /etc/security/limits.conf',
  path          => '/usr/local/bin/:/bin/'
}

exec { 'increase-holberton-user-soft-file-limit':
  command       => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path          => 'usr/local/bin/:/bin/'
}
