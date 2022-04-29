import paramiko
import getpass
import time

HOST = 'IP address of nodegrid'
user = input("username= ")
password = getpass.getpass("Pass= ")

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect(hostname=HOST, username=user, password=password)

commands = ['cd access/', 'ls', 'connect ttyS2-15', 'show version']
print("Successful connected to: ", HOST)

DEVICE_ACCESS = session.invoke_shell()
for command in commands:
    DEVICE_ACCESS.send(f'{command}\n')
    time.sleep(4)
    output = DEVICE_ACCESS.recv(65000)
    output2=(output.decode('ascii'))
    final_host = output2.split(">")[0]
    print(final_host)

session.close()