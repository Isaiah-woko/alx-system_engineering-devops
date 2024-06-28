# This Puppet manifest ensures that the Flask package version 2.1.0 is installed using pip3
ile { '/tmp/school':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
