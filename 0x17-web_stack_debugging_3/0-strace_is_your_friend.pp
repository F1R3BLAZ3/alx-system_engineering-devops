# Puppet manifest to fix an issue with Wordpress not initializing

exec { 'fix_phpp':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}
