import os
import sys
import subprocess

def error(message):
    print(f"Error: {message}")
    sys.exit(1)

def run_command(command, shell=False, capture_output=False):
    try:
        result = subprocess.run(command, check=True, text=True, shell=shell, capture_output=capture_output)
        return result.stdout.strip() if capture_output else None
    except subprocess.CalledProcessError as e:
        error(f"Command failed: {e}")

class php_mysql:
    def __init__(self, version):
        self.version = version

    def run(self):
        self.command = [
            ("=======Updating the server=======","sudo apt update && sudo apt upgrade -y",True),
            ("=======Installing PHP=======", f"sudo apt install php{self.version} -y", True),
            ("=======Installing MySQL=======", "sudo apt install mysql-server -y", True),
            ("=======Starting MySQL=======", "sudo systemctl start mysql", True),
            ("=======Enabling MySQL=======", "sudo systemctl enable mysql", True),
        ]

        for des, cmd, shell in self.command:
            try:
                print(f"{des}...............")
                run_command(cmd, shell=shell)
                print(f"----> Success {des}........[OK]")
            except Exception as e:
                print(f"----> Failed {des}........[FAILED]")
                error(f"Command failed: {e}")

def main():
    v = input("==> Enter which version of PHP you want to install (e.g., 8.1): ")
    i = php_mysql(v)
    i.run()
    php_v = run_command(["php", "--version"], capture_output=True)
    Mysql_v = run_command(["mysql", "--version"], capture_output=True)
    print(f"==>  PHP Version: {php_v}")
    print(f"==>  MySQL Version: {Mysql_v}")

if __name__ == "__main__":
    main()
