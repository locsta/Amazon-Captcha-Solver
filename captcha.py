import os
from os import listdir
from os.path import isfile, join
import subprocess
import time
import pyautogui

# This function helps to label captchas manually faster, original filenames looks like "Captcha_zdfbhsfgfbg"

def captcha():
    def is_authorized(letter):
        authorized_letters = ["A", "B", "C", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "R", "T", "U", "X", "Y"]
        return letter in authorized_letters

    mypath = "/datasets/captchas"
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file in files:
        if file.startswith("Captcha"):
            try:
                # open captchat in Image Viewer
                os.system(f"xdg-open {mypath}/{file}")

                # get processus id of the Image Viewer opened
                ps_id = subprocess.check_output("pgrep eog", shell=True).strip()

                # Wait for the file to open and click where the terminal is located
                time.sleep(0.5)
                terminal_location_on_screen = (3807, 445)
                pyautogui.click(terminal_location_on_screen)

                # Get the solved captcha
                captcha_solved = str(input("Entrer the captcha letters:")).upper()

                # Check if the captcha entered is 6 letters long and if the letter is in the authorized letters list
                while len(captcha_solved) != 6 or sum([is_authorized(l) for l in captcha_solved]) != 6:
                    captcha_solved = str(input("Entrer the captcha letters:")).upper()

                # Close the Image Viewer
                os.system(f"kill {int(ps_id)}")

                # Rename the captcha filename to its value
                os.rename(f"{mypath}/{file}", f"{mypath}/{captcha_solved}.jpg")
                print(file)
            except:
                pass

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    captcha()