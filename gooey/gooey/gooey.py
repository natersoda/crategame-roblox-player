import pyautogui, time

count = 0

def slow(name, confident):
    notepadloc = pyautogui.locateOnScreen(f'{name}.png', confidence=confident)
    notepadpoint = pyautogui.center(notepadloc)
    x, y = notepadpoint
    pyautogui.moveTo(x, y)
    time.sleep(1.2)
    pyautogui.click(x,y)

def fast(name, confident):
    notepadloc = pyautogui.locateOnScreen(f'{name}.png', confidence=confident)
    notepadpoint = pyautogui.center(notepadloc)
    x, y = notepadpoint
    pyautogui.moveTo(x, y)
    pyautogui.click(x,y)

fast("mouse",.9)
fast("mouse2",.9)
fast("roblox",.9)
time.sleep(.6)

try:
  while True:
    try:
       slow("check",.95)
       count = 0;
       print("\nafk checked")
    except pyautogui.ImageNotFoundException:
       print(f"\nthis has run {count} times before an afk check")
    try:
       slow("crate",.85)
       try:
          notepadloc = pyautogui.locateOnScreen(f'maxx.png', confidence=.95)
          slow("inventory", .95)
          pyautogui.moveTo(1000, 1000)
          time.sleep(.5)
          slow("sell", .95)
          time.sleep(.5)
          slow("button2", .95)
          time.sleep(.5)
          slow("mini", .95)
       except pyautogui.ImageNotFoundException:
          print(f"")
       time.sleep(5.1)
    except pyautogui.ImageNotFoundException:
       print('\ncrate not found :(')
    try:
       slow("button",.9)
    except pyautogui.ImageNotFoundException:
       print('\nbutton not found :(')
    count = count + 1
     
except KeyboardInterrupt:
     print('h')
