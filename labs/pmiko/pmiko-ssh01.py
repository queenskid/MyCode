import paramiko
client = paramiko.SSHClient()
clien.set_missing_host_key_policy(paramiko.WarningPolicy())
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect('localhost', username='student', password='alta3')
cmd = 'ls'
stdin, stdout, stderr = client.exec_command(cmd)
print('result ' + cmd)
for line in stdout:
    print('' + line.strip('\n'))
exit()
