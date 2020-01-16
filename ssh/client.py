import paramiko


class client:
    def __init__(self, address, name, pw):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(address, username=name, password=pw)
        self.result = []

    def clear_output(self):
        self.stdin.write('X\n')
        self.stdin.flush()
        while self.stdout.channel.recv_ready():
            self.data = self.stdout.read(1)

    def input(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        stdin.write(cmd)
        stdin.flush()
        data = stdout.read()

        self.clear_output()

        return data

    def close(self):
        self.client.close()
