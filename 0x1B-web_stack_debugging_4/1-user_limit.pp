# Enable holberton to login without Error

# Increase the Hard file limit for Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard/s/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}

# Increase soft file limit for Holberton user.
exec { 'increase-soft-file-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
