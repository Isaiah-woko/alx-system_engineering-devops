# using Puppet to make changes to our configuration file

file { '/etc/ssh/ssh_config':
    ensure  => present,
    content => @("EOF"),
    Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
    | EOF
    mode    => '0744',
    owner   => 'test',
    group   => 'test',
}
