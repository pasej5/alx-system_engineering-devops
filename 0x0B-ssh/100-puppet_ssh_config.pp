#!/usr/bin/env bash
# puppet file testing

file { 'etc/ssh/_config':
  ensure => present,

content =>"
  host*
  IdentityFile ~/.ssh/school
  PasswordAuthentication no",
}
