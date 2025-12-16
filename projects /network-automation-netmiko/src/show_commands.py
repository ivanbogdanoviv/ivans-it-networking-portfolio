from netmiko import ConnectHandler
import json
import getpass

def load_devices(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def main():
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    devices = load_devices("../sample-data/devices.json")

    show_commands = [
        "show ip interface brief",
        "show version"
    ]

    for device in devices:
        print(f"\nConnecting to {device['name']} ({device['host']})")

        device["username"] = username
        device["password"] = password

        try:
            connection = ConnectHandler(**device)

            for command in show_commands:
                output = connection.send_command(command)
                print(f"\n--- {command} ---")
                print(output)

            connection.disconnect()

        except Exception as e:
            print(f"Failed to connect to {device['name']}: {e}")

if __name__ == "__main__":
    main()
