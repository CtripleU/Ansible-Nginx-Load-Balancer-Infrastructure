Vagrant.configure("2") do |config|

    config.vm.box = "ubuntu/bionic64"


    config.vm.define "load-balancer" do |loadbalancer|
      loadbalancer.vm.provider "virtualbox" do |vb|
        vb.memory = "512"
      end

      loadbalancer.vm.network "private_network", ip: "192.168.33.10"
      loadbalancer.vm.hostname = 'load-balancer'

      loadbalancer.vm.provision "ansible" do |ansible|
        ansible.verbose = "v"
        ansible.playbook = "loadbalancer.yml"
        ansible.become = true
        ansible.limit = "loadbalancer"
        ansible.inventory_path = "vagrant-hosts"
      end

  #   nodejsapp_nginx.vm.provision "shell", inline: <<-SHELL
  #     echo "Adding SSH Key"
  #     echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDA5Xv55ZTwhBiXvTpsLUyrIghNs1wudPGLDeJ5pUTingJwwPizczSNwui+1FYKRs0UGjAGruUHYboiUOhJ37DZIWWJR8wKg10b+V/Uxv3b0xbV87dd7suZiUgPnK7y24IyCfelGD//dRmePQVbaszcOhctJyeJNgKigqc0MUEYaJWBQPfwN6TuBBSMsX4eDvdjJ0WQYCCzXU0SScZnwxtyozstizA+AzzsWmcZsXzfkNsxgNtKwLNTJ3z8/IQZlVIMt9RyRIF7U8EuuPfRYsmm63KIU2keBSvNb/02m4MDitvu3WXI7UdidXBYdwU0LZiuHGXRAsSILvPIAJv1zQYT' >> /home/vagrant/.ssh/authorized_keys
  #   SHELL
  # end

  # config.vm.define "nodejsapp_backend_1" do |nodejsapp_backend_1|
  #   nodejsapp_backend_1.vm.provider "virtualbox" do |vb|
  #      vb.memory = "512"
  #   end
  # Configure app servers
    config.vm.define "server-1" do |server_1|
      server_1.vm.provider "virtualbox" do |vb|
        vb.memory = "512"
      end

      server_1.vm.network "private_network", ip: "192.168.33.11"
      server_1.vm.hostname = 'server-1'

      server_1.vm.provision "ansible" do |ansible|
        ansible.verbose = "v"
        ansible.playbook = "webservers.yml"
        ansible.become = true
        ansible.limit = "webservers"
        ansible.inventory_path = "vagrant-hosts"
      end

  #   nodejsapp_backend_1.vm.provision "shell", inline: <<-SHELL
  #     echo "Adding SSH Key"
  #     echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDA5Xv55ZTwhBiXvTpsLUyrIghNs1wudPGLDeJ5pUTingJwwPizczSNwui+1FYKRs0UGjAGruUHYboiUOhJ37DZIWWJR8wKg10b+V/Uxv3b0xbV87dd7suZiUgPnK7y24IyCfelGD//dRmePQVbaszcOhctJyeJNgKigqc0MUEYaJWBQPfwN6TuBBSMsX4eDvdjJ0WQYCCzXU0SScZnwxtyozstizA+AzzsWmcZsXzfkNsxgNtKwLNTJ3z8/IQZlVIMt9RyRIF7U8EuuPfRYsmm63KIU2keBSvNb/02m4MDitvu3WXI7UdidXBYdwU0LZiuHGXRAsSILvPIAJv1zQYT' >> /home/vagrant/.ssh/authorized_keys
  #   SHELL
  # end

    config.vm.define "server-2" do |server_2|
      server_2.vm.provider "virtualbox" do |vb|
        vb.memory = "512"
      end

      server_2.vm.network "private_network", ip: "192.168.33.12"
      server_2.vm.hostname = 'server-2'

      server_2.vm.provision "ansible" do |ansible|
        ansible.verbose = "v"
        ansible.playbook = "webservers.yml"
        ansible.become = true
        ansible.limit = "webservers"
        ansible.inventory_path = "vagrant-hosts"
      end

  #   nodejsapp_backend_2.vm.provision "shell", inline: <<-SHELL
  #     echo "Adding SSH Key"
  #     echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDA5Xv55ZTwhBiXvTpsLUyrIghNs1wudPGLDeJ5pUTingJwwPizczSNwui+1FYKRs0UGjAGruUHYboiUOhJ37DZIWWJR8wKg10b+V/Uxv3b0xbV87dd7suZiUgPnK7y24IyCfelGD//dRmePQVbaszcOhctJyeJNgKigqc0MUEYaJWBQPfwN6TuBBSMsX4eDvdjJ0WQYCCzXU0SScZnwxtyozstizA+AzzsWmcZsXzfkNsxgNtKwLNTJ3z8/IQZlVIMt9RyRIF7U8EuuPfRYsmm63KIU2keBSvNb/02m4MDitvu3WXI7UdidXBYdwU0LZiuHGXRAsSILvPIAJv1zQYT' >> /home/vagrant/.ssh/authorized_keys
  #   SHELL
  # end

    config.vm.provision "shell", inline: <<-SHELL   
      apt-get update
      
      # Create group admin, add admin group to vagrant users, and give users in the admin group the privilege to sudo without a password 
      groupadd -r admin
      usermod -a -G admin vagrant
      cp /etc/sudoers /etc/sudoers.orig
      sed -i -e '/Defaults\s\+env_reset/a Defaults\texempt_group=admin' /etc/sudoers
      sed -i -e 's/%admin ALL=(ALL) ALL/%admin ALL=NOPASSWD:ALL/g' /etc/sudoers 
  
  SHELL
end
