# 100-puppet_ssh_config.pp

# Ensure the SSH client configuration file exists
file { '/etc/ssh/ssh_config':
  ensure => file,
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
}

# Ensure there is only one IdentityFile line
file_line { 'Remove old IdentityFile lines':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^.*IdentityFile.*$',
  ensure => absent,
}

# Add the new IdentityFile line
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/school',
}

# Turn off password authentication
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => '    PasswordAuthentication no',
  match => '^.*PasswordAuthentication.*$',
}
