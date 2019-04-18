# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
 
#DEVOPS
  config.vm.define "devops" do |devops|
    devops.vm.hostname = "devops"
    devops.vm.box = "ubuntu/xenial64"
    devops.vm.box_check_update = false
    devops.vm.network "private_network", ip: "192.168.99.10", dns: "8.8.8.8"
  
    devops.vm.provider "virtualbox" do |dev|
    dev.memory = "3072"
   end
  end 

#DOCKER
  config.vm.define "docker" do |docker|
    docker.vm.hostname = "docker"
    docker.vm.box = "ubuntu/xenial64"
    docker.vm.box_check_update = false
    docker.vm.network "private_network", ip: "192.168.99.20", dns: "8.8.8.8"
  
    docker.vm.provider "virtualbox" do |doc|
    doc.memory = "2048"
   end
  end 

#AUTOMATION
  config.vm.define "automation" do |automation|
    automation.vm.hostname = "automation"
    automation.vm.box = "centos/7"
    automation.vm.box_check_update = false
    automation.vm.network "private_network", ip: "192.168.99.30", dns: "8.8.8.8"
  
    automation.vm.provider "virtualbox" do |aut|
    aut.memory = "2048"
   end
  end

  config.vm.provision "shell", inline: <<-SHELL
    mkdir -p /root/.ssh/
    cat /vagrant/infraagil.pem > /root/.ssh/id_rsa
    cat /vagrant/infraagil.pub > /root/.ssh/authorized_keys
    chmod 600 /root/.ssh/id_rsa
  SHELL
end
