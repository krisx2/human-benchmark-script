# Automation scripts for [human benchmark](https://humanbenchmark.com/) tests

This is a group of scripts used to get 100% in the humanbenchmark test(s).

## Some requirements
- Python libraries used for this project
  - PyAutoGUI
  - ~~win32~~ (replaced by pynput)
  - selenium
  - keyboard
- Supports only 1920x1080 resolution (for now)
- Make sure to download the needed libraries with ***pip install*** 
- Make sure to have your browser fullscreen and be set to the top of the page, also make sure to have the display size of your browser set to 100% (default)
- ~~Win32 is exclusive to windows meaning if you want to simulate mouse clicks on other OS's you would have to use pynput or pyautogui's methods (im using win32 here because is faster)~~ (replaced by pynput)
- The reaction time test and the aim trainer tests don't use selenium for speed , every script uses "ESC" key to start and "b" to stop the browser aswell as "q" for stopping the loop
### Updates in the future
- I'm going to optimize some of the tests either support more resolutions or remove the need, also make a separate script that just runs the test all at once (meaning you don't have to run all of them individually)
- Finally I'm planning to implement some gui to make it more user friendly

