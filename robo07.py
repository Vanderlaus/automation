import pyautogui as p

p.hotkey('win', 'r')
p.sleep(1)
p.write('C:/Users/vander.lauschner/Downloads/RPA.pbix')
p.sleep(1)
p.press("enter")
p.sleep(30)
p.click(x=704, y=97)
p.sleep(5)