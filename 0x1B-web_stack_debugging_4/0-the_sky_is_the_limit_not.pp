# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Ensure the directory exists
file { '/etc/default/':
  ensure => directory,
}

# Create an empty nginx file if it doesn't exist
file { '/etc/default/nginx':
  ensure  => present,
  content => '', # Add content if needed
}

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin',
  require => [File['/etc/default/nginx'], Package['nginx']],
}

# Restart Nginx
exec { 'nginx-restart':
  command   => '/etc/init.d/nginx restart',
  path      => '/etc/init.d/',
  subscribe => Exec['fix--for-nginx'],}

