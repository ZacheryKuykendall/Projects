#!/bin/bash

# Step 1: Update package information
sudo apt-get update

# Step 2: Install required packages
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release -y

# Step 3: Add Docker’s official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Step 4: Add Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Step 5: Update the package list again
sudo apt-get update

# Step 6: Install Docker
sudo apt-get install docker-ce docker-ce-cli containerd.io -y

# Step 7: Add your user to the docker group
sudo usermod -aG docker $USER
