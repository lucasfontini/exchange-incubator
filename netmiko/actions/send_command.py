from netmiko import ConnectHandler
import sys
from st2common.runners.base_action import Action


def connect(hostname, username, password, device_type, port):
    try:
        device = {
            'device_type': device_type,
            'ip': hostname,
            'username': username,
            'password': password,
            'port': port,

        }
        connection = ConnectHandler(**device)
        return connection
    except Exception as e:
        print(e)
        return None


class main(Action):

    def run(self, hostname, device_type, port, command):
        credentials = self.config
        USER = credentials['user']
        PASSWORD = credentials['password']

        if credentials:
            connection = connect(hostname, USER, PASSWORD,
                                 device_type=device_type, port=port)
            if connection is not None:
                output = connection.send_command(command)
                connection.disconnect()
                print(output)
                return output
            else:
                print("Connection failed")
                return sys.exit(1)
        else:
            print(
                "No credentials found, please check your config file /opt/stackstorm/configs/pack_name")
            return sys.exit(1)
