# Puppet manifest to fix Nginx "Too many open files" issue

# Increase ULIMIT in /etc/default/nginx
exec { 'increase_ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['restart_nginx'],
}

# Restart Nginx
exec { 'restart_nginx':
  command     => 'nginx restart',
  path        => '/etc/init.d/',
  refreshonly => true,
}
