# Ansible-Nginx-Load-Balancer-Infrastructure

#### This infrastructure deploys a flask web app that returns a random anime quote using the API - https://github.com/RocktimSaikia/anime-chan

Setup Requirements
-----
The solution was built with the following versions of software installed on vagrant host. 
- Virtualbox 6.1.26
- Vagrant 2.2.18 

You do not need Ansible installed on the vagrant host, as it wil be installed on the control machine. 


### Why Ansible?
There are three VMs, so installing, configuring, and maintaining each of them manually will be difficult and not efficient as it would take a lot of time and repeated work. Therefore, a way to automate processes is required. I chose Ansible over other tools such as Chef and Puppet because of its simplicity. It is easy to write, apply, and manage.

Roles initialized with Ansible Galaxy: 
- common : This role contains common configurations for all the servers.
- apps: This role contains common configurations for all the web servers.
- loadbalancer: This role contains configurations for the Nginx load balancer.

To duplicate the solution on your machine:
-----
  * Clone this repository
  * Run `vagrant up --provision`
  * SSH into the control server where ansible is installed `vagrant ssh control`
  * Cd into the synced folder `cd ansible_data`
  * Deploy the load balancer by runnin `ansible-playbook site.yml`


*Note*: The VMs were provisioned to ensure that all users in the admin group can sudo without a password.


Possible Improvements
-----
* Make use of roles to organize tasks, handlers, and templates better.
* Since I have to create two web servers running `ubuntu/bionic64`, I can refactor the Vagrantfile to use a single configuration block to create them instead of repeating the same thing twice. 
* I did not consider security as this is for a test environment. So there are no firewalls or backup scripts for the box. It would be recommended to secure the system if this were to be moved from a test environment to production.

#### Completion time  
It took about six hours for me to complete this task.


