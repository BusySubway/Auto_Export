import pyautogui
import pyperclip
pyautogui.moveTo(x=3330, y=126, duration=3.0)
pyautogui.click()
f = open("Dictation Mistakes in Chapter5.txt")
while True:
    line = f.readline()
    if line:
        pyperclip.copy(line)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.moveTo(x=2947, y=293, duration=0.3)
        pyautogui.click()
        pyautogui.moveTo(x=3148, y=127, duration=0.5)
        pyautogui.click()
        pyautogui.moveTo(x=2910, y=671, duration=0.3)
        pyautogui.click()
        pyautogui.moveTo(x=2857, y=127, duration=0.3)
        pyautogui.click()
        pyautogui.moveTo(x=3330, y=126, duration=0.2)
        pyautogui.click()
    else:
    	break

f.close()