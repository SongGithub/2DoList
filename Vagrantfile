# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "precise64"
  # port for POSTGRESQL database
  config.vm.network :forwarded_port, guest: 5432, host: 9900
end
