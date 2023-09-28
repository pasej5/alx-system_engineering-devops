#puppet to save time and effort

package { 'nginx'
  ensure => installed,
}

file_line { 'install:'
  ensure => 'present'
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 deafault_server;',
  line   => 'rewrite ^/redirect_me https:www.github.com/pasej5 permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  reguire => package['nginx'],
}
