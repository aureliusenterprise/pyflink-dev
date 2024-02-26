#!/bin/bash

# Install dependencies
poetry install

# Ensure binaries are executable and add them to the PATH
chmod +x -R $PWD/bin
echo 'export PATH="$PATH:$PWD/bin"' >> ~/.bashrc
source ~/.bashrc

# Prompt the user to set their git username and email if not already set
if [ -z "$(git config --global user.name)" ]; then
    read -p "Enter your Git username (full name): " git_username
    git config --global user.name "$git_username"
fi

if [ -z "$(git config --global user.email)" ]; then
    read -p "Enter your Git email: " git_email
    git config --global user.email "$git_email"
fi
