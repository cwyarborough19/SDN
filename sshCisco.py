import os
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import AuthenticationException, SSHException, NetMikoTimeoutException

USERNAME = input("Please enter your SSH username: ")
PASS = getpass("Please enter your SSH password: ")

device = {
    'ip': '192.168.108.11',
    'username': USERNAME,
    'password': PASS,
    'device_type': 'cisco_ios'
}

c = ConnectHandler(**device)

output = c.send_command('show run')

f = open('backup.conf', 'x')

f.write(output)

f.close()
