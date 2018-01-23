#!/usr/bin/env python
from netmiko import ConnectHandler

cisco_wlc = {
'device_type': 'cisco_ios',
'ip': '***',
'username': '***',
'password': '***',
'global_delay_factor': 4,
}
#device = ConnectHandler(cisco_wlc)

platform = 'cisco_wlc'
host = '***'
username = '***'
password = '***'
global_delay_factor= 4
device = ConnectHandler(device_type=platform, ip=host, username=username, password=password, global_delay_factor=global_delay_factor)
output = device.send_command("show version")

print ">>>>>>>>>>>> START <<<<<<<<<<<"
print output
print ">>>>>>>>>>>> END <<<<<<<<<<<"

device.disconnect()
