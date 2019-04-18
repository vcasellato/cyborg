class canario_negra {
	case $::osfamily {
		"redhat":{
			$pacote = ["epel-release","git","vim","fortune-mod","figlet","fish"]
		}

		
		"debian":{
			exec{"Atualizando Repositorio":
				command => "/usr/bin/apt update"

		}
			$pacote = ["git","fortunes-br","figlet","fish"]
		}

}

	package{$pacote:
		ensure => present,
		
		
}	
		file{'/root/.bashrc':
		source => "puppet:///modules/canario_negra/bashrc_base",
		ensure => present,




	}
	file{'/root/.bash_logout':
		source => "puppet:///modules/canario_negra/bash_logout",
		ensure => present,
	} 


	user {"devops":
		ensure => present,
		managehome => true,
		shell => "/usr/bin/fish",
}

}
