# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  
    config.vm.box = "ubuntu/bionic64"
  
    config.vm.define "control", primary: true do |control|
      control.vm.network "private_network", ip: "192.168.33.10"
      control.vm.hostname = "controller"
      control.vm.synced_folder ".//ansible_data", "/home/vagrant/ansible_data"
      control.vm.provider "virtualbox" do |vb| 
        vb.memory = 512
        vb.customize ["modifyvm", :id, "--audio", "none"]
      end
      
      control.vm.provision :shell, :inline => <<"EOF"   
if [ ! -f "/home/vagrant/.ssh/id_rsa" ]; then
  ssh-keygen -t rsa -N "" -f /home/vagrant/.ssh/id_rsa
fi
cp /home/vagrant/.ssh/id_rsa.pub /vagrant/control.pub

cat << 'SSHEOF' > /home/vagrant/.ssh/config
Host *
  StrictHostKeyChecking no
SSHEOF

chown -R vagrant:vagrant /home/vagrant/.ssh/

sudo apt-get update -y
sudo apt-get -y install python3-apt
sudo apt-add-repository ppa:ansible/ansible
sudo apt install ansible -y

# Add admin group to vagrant users, and give users in the admin group the privilege to sudo without a password 
usermod -a -G admin vagrant
cp /etc/sudoers /etc/sudoers.orig
sed -i -e '/Defaults\s\+env_reset/a Defaults\texempt_group=admin' /etc/sudoers
sed -i -e 's/%admin ALL=(ALL) ALL/%admin ALL=NOPASSWD:ALL/g' /etc/sudoers 

EOF
    end

    config.vm.define "load-balancer" do |loadbalancer|
      loadbalancer.vm.network "private_network", ip: "192.168.33.11"
      loadbalancer.vm.hostname = "load-balancer"
      loadbalancer.vm.network "forwarded_port", guest: 80, host: 8080
      loadbalancer.vm.provider "virtualbox" do |vb| 
        vb.memory = 512
        vb.customize ["modifyvm", :id, "--audio", "none"]
      end

      loadbalancer.vm.provision :shell, :inline => <<'EOF'
cat /vagrant/control.pub >> /home/vagrant/.ssh/authorized_keys

  sudo apt-get update -y
  sudo apt-add-repository ppa:ansible/ansible
  sudo apt install ansible -y

  # Add admin group to vagrant users, and give users in the admin group the privilege to sudo without a password 
  usermod -a -G admin vagrant
  cp /etc/sudoers /etc/sudoers.orig
  sed -i -e '/Defaults\s\+env_reset/a Defaults\texempt_group=admin' /etc/sudoers
  sed -i -e 's/%admin ALL=(ALL) ALL/%admin ALL=NOPASSWD:ALL/g' /etc/sudoers
EOF
     end


      config.vm.define "server-1" do |server_1|
      server_1.vm.network "private_network", ip: "192.168.33.12"
      server_1.vm.hostname = "server-1"
      server_1.vm.provider "virtualbox" do |vb| 
        vb.memory = 512
        vb.customize ["modifyvm", :id, "--audio", "none"]
      end
  
      server_1.vm.provision :shell, :inline => <<'EOF'
cat /vagrant/control.pub >> /home/vagrant/.ssh/authorized_keys

sudo apt-get update -y
sudo apt-add-repository ppa:ansible/ansible
sudo apt install ansible -y

# Add admin group to vagrant users, and give users in the admin group the privilege to sudo without a password 
usermod -a -G admin vagrant
cp /etc/sudoers /etc/sudoers.orig
sed -i -e '/Defaults\s\+env_reset/a Defaults\texempt_group=admin' /etc/sudoers
sed -i -e 's/%admin ALL=(ALL) ALL/%admin ALL=NOPASSWD:ALL/g' /etc/sudoers
EOF
     end


      config.vm.define "server-2" do |server_2|
      server_2.vm.network "private_network", ip: "192.168.33.13"
      server_2.vm.hostname = "server-2"
      server_2.vm.provider "virtualbox" do |vb| 
        vb.memory = 512
        vb.customize ["modifyvm", :id, "--audio", "none"]
      end
      
      server_2.vm.provision :shell, :inline => <<'EOF'
cat /vagrant/control.pub >> /home/vagrant/.ssh/authorized_keys

sudo apt-get update -y
sudo apt-add-repository ppa:ansible/ansible
sudo apt install ansible -y

# Add admin group to vagrant users, and give users in the admin group the privilege to sudo without a password 
usermod -a -G admin vagrant
cp /etc/sudoers /etc/sudoers.orig
sed -i -e '/Defaults\s\+env_reset/a Defaults\texempt_group=admin' /etc/sudoers
sed -i -e 's/%admin ALL=(ALL) ALL/%admin ALL=NOPASSWD:ALL/g' /etc/sudoers
EOF
     end
end