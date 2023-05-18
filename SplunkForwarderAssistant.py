import os
import logging

# logging module
logging.basicConfig(level=logging.INFO, format='%(message)s')

#logger instance
logger = logging.getLogger(__name__)

# separate logger for outputconf_1
outputconf_logger = logging.getLogger("outputconf")

# stored in variables
HostAddress = input("Enter the host IP Address: ")
HostPortNumber = input("Enter the port number: ")
ServerName = input("Enter the server name (Press Enter for default-autolb-group): ")

#  strings into their types
HostAddressFinal = str(HostAddress)
PortNumberFinal = str(HostPortNumber)
ServerNameFinal = ServerName or "default-autolb-group"  # Set default value if no entry is provided

# Log the host address, port number, and server name
logger.info("The host address you entered is: %s", HostAddressFinal)
logger.info("The port number you entered is: %s", PortNumberFinal)
logger.info("The server name you entered is: %s", ServerNameFinal)

# Confirm the inputted variables
confirm = input("\nAre the inputted variables correct? (yes/no): \n")

if confirm.lower() not in ['yes', 'y']:
    logger.info("Please re-run the program and provide the correct input.")
else:
    # Prompt to save configuration files
    save_files = input("Would you like to save the configuration files? (yes/no): \n")

    if save_files.lower() in ['yes', 'y']:
        desktop_path = os.path.expanduser("~/Desktop")  # Path to the desktop directory
        outputconf_file = os.path.join(desktop_path, "output.conf")
        deploymentclient_file = os.path.join(desktop_path, "deploymentclient.conf")

        with open(outputconf_file, 'w') as file:
            file.write("[tcpout]\ndefaultGroup=%s\n\n[tcpout:%s]\n" % (ServerNameFinal, ServerNameFinal))
            file.write("server=%s:%s\n" % (HostAddressFinal, PortNumberFinal))
            file.write("[tcpout-server://%s:%s]" % (HostAddressFinal, PortNumberFinal))

        with open(deploymentclient_file, 'w') as file:
            file.write("[target-broker:deploymentServer]\ntargetUri = %s:%s" % (HostAddressFinal, PortNumberFinal))

        logger.info("Configuration files saved successfully on the desktop.")
        logger.info("Please copy the configuration files from the desktop to 'C:\\program files\\SplunkUniversalFowarder\\etc\\system\\local'.")
    else:
        def outputconf_1():
            outputconf_logger.info("[tcpout]\ndefaultGroup=%s\n\n[tcpout:%s]\n", ServerNameFinal, ServerNameFinal)
            outputconf_logger.info("server=%s:%s", HostAddressFinal, PortNumberFinal)
            outputconf_logger.info("\n[tcpout-server://%s:%s]", HostAddressFinal, PortNumberFinal)


        def deploymentclient():
            logger.info("[target-broker:deploymentServer]\ntargetUri = %s:%s", HostAddressFinal, PortNumberFinal)


        logger.info("The output.conf file should look like this: ")
        outputconf_1()
        logger.info("\nThe deploymentclient.conf file should look like this: \n")
        deploymentclient()
