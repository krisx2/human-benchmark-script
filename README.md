# Automation scripts for [human benchmark](https://humanbenchmark.com/) tests

This is a group of scripts used to get 100% in the humanbenchmark test(s).

## Some requirements
- Python libraries used for this project
  - PyAutoGUI
  - win32
  - selenium
  - keyboard
- Supports only 1920x1080 resolution 
- Make sure to download the needed libraries with ***pip install*** 
- Make sure to have your browser fullscreen and be set  to the top of the page, also make sure to have the display size of your browser set to 100% (default)
- Win32 is exclusive to windows meaning if you want to simulate mouse clicks on other OS's you would have to use pynput or pyautogui's methods (im using win32 here because is faster)

### Why don't I use selenium for everything?

- I've decided to use pyautogui on some task because I want to practice using  different libraries and different approaches to solving the same problems.
