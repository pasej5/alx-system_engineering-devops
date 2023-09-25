#!/usr/bin/env bash
# puppet file testing

file { 'etc/ssh_cofig':
  ensure => present,

content =>"
  host*
  IdentityFile ~/.ssh/school
  PasswordAuthentication no",
}
