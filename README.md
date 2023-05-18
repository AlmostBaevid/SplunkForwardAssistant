# Splunk Forwarder Configuration Helper Script

## Purpose
This script is designed to assist novice users in correctly setting up configuration files for Splunk Enterprise forwarders. As a novice installing Splunk Enterprise and the forwarders, it can be challenging to configure the necessary files accurately. This script aims to simplify the process by providing a guided approach to generate the required configuration files.

## How to Use
1. Run the script in a Python environment.
2. Follow the prompts to provide the necessary inputs, such as the host IP address, port number, and server name (with an option for a default value).
3. Review the displayed sample output configurations for the `output.conf` and `deploymentclient.conf` files.
4. Confirm if the inputted variables are correct.
5. Choose whether to save the generated configuration files.
6. If saving, the script will create `output.conf` and `deploymentclient.conf` files on the desktop. Copy these files to `C:\Program Files\SplunkUniversalForwarder\etc\system\local` directory to configure Splunk forwarders correctly.

Please note that this script assumes a basic understanding of Splunk Enterprise and forwarder configuration. It aims to simplify the process for novice users, but it is still essential to have a fundamental understanding of Splunk and its concepts.

## Compatibility
This script is compatible with Python 3.x versions.

## Disclaimer
This script is provided as-is, without any warranties or guarantees. Use it at your own risk. The authors and contributors of this script are not responsible for any issues or damages arising from the use of this script.


## Contributions
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please submit them through the [issue tracker](https://github.com/yourusername/splunk-forwarder-config-helper/issues) or create a pull request.
