This script is a reverse shell written in PowerShell. It allows you to establish a remote shell connection to a specified IP address and port.

## Installation

1. Ensure you have PowerShell installed on your system. This script should work with PowerShell on Windows.
2. Copy the script code into a text editor and save it with a `.ps1` extension, for example, `script.ps1`.
3. Optionally, you may need to adjust the IP address (`$a`) and port (`$p`) variables within the script to match your target configuration.

## Usage

1. Open PowerShell.
2. Navigate to the directory where you saved the `script.ps1` script.
3. Execute the script by running the following command:

   ```powershell
   .\script.ps1
   ```

4. Once the script is executed, it will attempt to establish a connection to the specified IP address (`$a`) and port (`$p`).
5. If the connection is successful, you will have a remote shell session established.
6. You can interact with the remote shell session via the PowerShell prompt. Any commands entered will be executed on the remote system.

**Note:**

- Ensure that the target system is reachable and allows connections on the specified port.
- This script assumes that you have appropriate permissions and access rights to establish a remote connection.
