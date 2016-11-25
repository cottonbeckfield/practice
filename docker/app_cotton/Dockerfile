FROM centos
MAINTAINER Courtney Cotton
RUN yum update

# Unzip is needed for installing Vault.
RUN yum install -y \
  unzip \
  wget

# To run it, you will need a user + env variables
RUN useradd -ms /bin/bash vault
USER vault
WORKDIR /home/vault

# Install Vault
RUN wget -P /home/vault https://releases.hashicorp.com/vault/0.6.2/vault_0.6.2_linux_amd64.zip \
  -O vault_dev.zip; \
  unzip vault_dev.zip; \
  rm vault_dev.zip

# Start the Vault-Dev funsies
RUN echo "VAULT_ADDR=http://127.0.0.1:8200" >> /home/vault/.bash_profile
RUN touch vault.start \
  && echo "nohup /home/vault/vault server -dev > /home/vault/vault.info 2>&1 &" \
  >> vault.start

# Vault-Dev runs on 127.0.0.1:8200
EXPOSE 8200
