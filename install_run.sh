#!/bin/bash

#Shell Script to install all dependencies required for the project
pip install -r requirements.txt
echo "Make sure all your required credentials are filled properly in .env file"
read -p "Do you want to run the Program ? (y/n): " reply

if [ "$reply" = "y" ];
then
    python3 cloudflare_dns_entry.py 
fi

echo "Executed Successfully !"