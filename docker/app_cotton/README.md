# app_cotton

This is a practice Dockerfile.

The point of this practice was to have Vault installed and create
a Vault user to run everything related to it.

If you type in ```/bin/bash vault.start``` it should auto
start the Vault-Dev process, which will create a vault.info file
containing the root/vault keys.

To Do:
* Have the vault-dev process start as a systemd service.
