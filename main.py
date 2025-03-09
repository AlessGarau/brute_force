from file_handler import FileHandler
from brute_force import BruteForce
from concurrent.futures import ThreadPoolExecutor
from queue import Empty, Queue
from threading import Event
import signal
import sys

def signal_handler(sig, frame):
    print("\nCaught SIGINT (Ctrl + C)")
    sys.exit(0)

def main():
    file_handler = FileHandler('./files/naja.zip')
    brute_force = BruteForce('passwords.txt', file_handler)
    queue = Queue()
    password_length = [1,2,3,4]
    success = Event()

    signal.signal(signal.SIGINT, signal_handler)
    try:
        with ThreadPoolExecutor(max_workers=8) as thread:
            generate_password_futures = [thread.submit(brute_force.generate_password, length) for length in password_length]
            for future in generate_password_futures:
                queue.put(future.result())

            while not queue.empty() and not success.is_set():
                    passwords = queue.get(timeout=0.1)
                    for password in passwords:
                        test = brute_force.file.verify_password(password)
                        if test == True:
                            print(f"Password found: {password}")
                            brute_force.file.extract_content(password, './extract')
                            success.set()
                            break
    except KeyboardInterrupt:
        print("\nCaught KeyboardInterrupt")
        pass

if __name__ == '__main__':
    main()