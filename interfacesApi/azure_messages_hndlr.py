import json
import sys
from azure.iot.hub import IoTHubRegistryManager

CONNECTION_STRING = "HostName=cloudiothub.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=OXIljDPW9fw4cdODJE2NNcWgmtmb/UyVFAIoTNcHQGo="
DEVICE_ID = "device1"

def send_request_messagses(data,messageType):
    try:
        # Create IoTHubRegistryManager
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)

        props={}
        # optional: assign system properties
        props.update(messageId = messageType)

        props.update(contentType = "application/json")

        registry_manager.send_c2d_message(DEVICE_ID, data, properties=props)

    except Exception as ex:
        print ( "Unexpected error" )
        return



