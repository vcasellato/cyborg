class mulher_gaviao { 

	file{"/etc/puppetlabs/puppet/puppet.conf":
	source => "puppet:///modules/mulher_gaviao/puppet.conf",
	ensure => present,
 


}

 	service{'puppet':
		ensure => running,
		enable => true,
		subscribe => File['/etc/puppetlabs/puppet/puppet.conf']
	}



}
