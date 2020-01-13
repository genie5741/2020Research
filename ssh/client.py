import paramiko


class client:
    def __init__(self, addrtess, name, pw):
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
        self.stdin, self.stdout, self.stderr = self.client.exec_command(cmd)
        self.stdin.write(cmd)
        self.stdin.flush()
        self.data = self.stdout()

        self.clear_output()

    def close(self):
        self.client.close()