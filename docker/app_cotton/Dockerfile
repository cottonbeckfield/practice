FROM centos
MAINTAINER Courtney Cotton
RUN yum update

# Unzip is needed for installing Vault.
RUN yum install -y unzip wget

# Install Vault
RUN wget https://releases.hashicorp.com/vault/0.6.2/vault_0.6.2_linux_amd64.zip
