# Automatic Backup Script

This script automates the process of copying confidential files like passwd, shadow from a remote host to a local directory periodically, allowing for automatic data exfiltrations.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your/repository.git
   ```

2. Navigate to the directory containing the script:

   ```bash
   cd repository-directory
   ```

3. Ensure you have the necessary permissions to execute the script:

   ```bash
   chmod +x backup_script.sh
   ```

4. Modify the script variables as needed:
   - `remote_user`: The username used to connect to the remote host.
   - `remote_host`: The IP address or hostname of the remote host.
   - `remote_directory`: The directory on the remote host containing the files to be backed up.
   - `local_directory`: The local directory where the files will be copied.
   - `remote_home_directory`: The home directory of the remote user.
   - `ssh_key`: (Optional) The path to your SSH private key file for authentication.

## Usage

This can be injected into another file and make this execution really quiet.
To start the automatic exfiltration process, simply execute the script:

```bash
./backup_script.sh
```
