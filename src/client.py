import paramiko


class client:
    def __init__(self, address, name, pw):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(address, username=name, password=pw)
        print("SSH connected")
        self.data = []

    def clear_output(self):
        self.stdin.write('X\n')
        self.stdin.flush()
        while self.stdout.channel.recv_ready():
            self.data = self.stdout.read(1)

    def input(self, cmd):
        self.clear_output()

        self.stdin, self.stdout, self.stderr = self.client.exec_command(cmd)
        self.stdin.flush()

    def read_output(self):
        self.data = self.stdout.read()

        return self.data

    def close(self):
        self.client.close()
