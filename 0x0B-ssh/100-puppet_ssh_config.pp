# Puppet script to create an ssh config file
file_line { 'Turn off the password authentication':
	ensure => 'present',
	path   => '/etc/ssh/ssh_config',
	line   => '	PasswordAuthentication no',
	}

file_line { 'the identity file':
	ensure => 'present',
	path   => '/etc/ssh/ssh_config',
	line   => '	IdentityFile ~/.ssh/school',
	}
