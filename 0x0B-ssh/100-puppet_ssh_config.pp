#!/usr/bin/env bash
#puppet file

exec { 'append_ssh_config':
  command => "echo -e '\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no' >> /etc/ssh/ssh_config",
  path    => '/usr/bin',
  unless  => "grep -q 'IdentityFile ~/.ssh/school' /etc/ssh/ssh_config && grep -q 'PasswordAuthentication no' /etc/ssh/ssh_config",
  require => File['/etc/ssh/ssh_config'],
}
