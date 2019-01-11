#! /usr/bin/env python
"""
Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Hank Preston <hapresto@cisco.com>"
__contributors__ = "Bryan Byrne <brybyrne@cisco.com>"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"


from device_info import ios_xe1
from ncclient import manager

if __name__ == '__main__':

    # NETCONF Config Template to use
    netconf_template = open("config-temp-ietf-interfaces.xml").read()

    # Build the XML Configuration to Send
    netconf_payload = netconf_template.format(int_name="GigabitEthernet2",
                                              int_desc="Configured by NETCONF",
                                              ip_address="10.255.255.1",
                                              subnet_mask="255.255.255.0"
                                              )
    print("Configuration Payload:")
    print("----------------------")
    print(netconf_payload)

    with manager.connect(host=ios_xe1["address"], port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False) as m:

        # Send NETCONF <edit-config>
        netconf_reply = m.edit_config(netconf_payload, target="running")

        # Print the NETCONF Reply
        print(netconf_reply)
