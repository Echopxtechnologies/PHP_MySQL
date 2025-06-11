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

class ask:
    def __init__(self):
        self.php_mysql = input("Do you want to install Php and MySQL ? [y/n]: ")
        self.webmin = input("Do you want to install Webmin? [y/n]: ")
    def php_mysql_in(self):
        return self.php_mysql.lower() == "y"

    def webmin_in(self):
        return self.webmin.lower() == "y"

class Install:
    def Webmin(self):
        print("Installing Webmin!....")
        cmds = [
            # (description, command, shell)
            ("Adding Webmin GPG key", "wget -q -O- http://www.webmin.com/jcameron-key.asc | sudo gpg --dearmor -o /usr/share/keyrings/webmin.gpg", True),
            ("Adding Repository", "sudo sh -c 'echo \"deb [signed-by=/usr/share/keyrings/webmin.gpg] http://download.webmin.com/download/repository sarge contrib\" > /etc/apt/sources.list.d/webmin.list'", True),
            ("Updating...", "sudo apt update", True),
            ("Installing Webmin", "sudo apt install -y webmin", True),
            ("Enabling Firewall", "sudo ufw allow 10000/tcp", True),
        ]

        for desc, cmd, shell in cmds:
            try:
                print(f"==> {desc}")
                result = subprocess.run(cmd, shell=shell, check=True, text=True, capture_output=True)
                print(f"==> Success: {desc}.................................[OK]\n")
            except subprocess.CalledProcessError as e:
                print(f"==> Error in {desc}: {e.stderr}")
                exit(1)  # Exit if any critical step fails
    

def main():
    q = ask()
    if q.php_mysql_in():
        print("---------------------------------------------------------------------\n")
        v = input("==> Enter which version of PHP you want to install (e.g., 8.1): ")
        print("---------------------------------------------------------------------\n")
        i = php_mysql(v)
        i.run()
        php_v = run_command(["php", "--version"], capture_output=True)
        Mysql_v = run_command(["mysql", "--version"], capture_output=True)
        print("---------------------------------------------------------------------\n")
        print(f"==>  PHP Version: {php_v}")
        print(f"==>  MySQL Version: {Mysql_v}")
        print("---------------------------------------------------------------------\n")

    if q.webmin_in():
        try:
            installer = Install()
            installer.Webmin()
        except Exception as e:
            print(f"Error Unable to install webmin: {e}")

    

if __name__ == "__main__":
    main()
