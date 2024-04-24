import subprocess

class NetUtils:
    @staticmethod
    def get_local_ip():
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # Connect to an external IP to get the local IP of the host machine
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    @staticmethod
    def server(ipv4_address, SERVER_PORT, FOLDER_MAIN="./"):
        # Starting a simple HTTP server on a specified port and directory
        subprocess.Popen(['python', '-m', 'http.server', str(SERVER_PORT), '--directory', FOLDER_MAIN], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        SERVER_STARTED = True  # Assuming the server started successfully
        with open('server.prop.state', 'w') as f:
            f.write('1')
        print(f'Server started at http://{ipv4_address}:{SERVER_PORT}')


