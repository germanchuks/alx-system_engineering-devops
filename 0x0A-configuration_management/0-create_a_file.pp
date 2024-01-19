# File: 0-create_a_file.pp

file { '/tmp/school':
    ensure  => 'file',          # Ensure it is a file
    mode    =>  '0744',         # File permissions
    owner   =>  'www-data',     # File owner
    group   =>  'www-data',     # File group
    content =>  'I love Puppet', # File content
}
