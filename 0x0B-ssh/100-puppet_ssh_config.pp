#!/usr/bin/env bash
#using a puppet file

$content = '\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication\no'
exec {'ssh_config':
  path    => '/usr/bin',
  command => "echo '${content}' >> /etc/ssh/ssh_config"
}
