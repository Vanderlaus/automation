import pyautogui as p

p.moveTo(x=42, y=350, duration=1)
p.doubleClick(x=42, y=350)

p.moveTo(x=273, y=17, duration=1)
p.click(x=273, y=17)

p.moveTo(x=161, y=52, duration=1)
p.click(x=161, y=52)
p.typewrite('github')
p.hotkey('enter')

p.moveTo(x=1311, y=109, duration=1)
p.sleep(1)
p.click(x=1311, y=109)
p.sleep(2)
p.typewrite('vanderlaus@hotmail.com')
p.moveTo(x=678, y=367, duration=1)
p.click(x=678, y=367)
p.typewrite('*********')
p.moveTo(x=804, y=411, duration=1)
p.sleep(2)
p.click(x=804, y=411)

p.moveTo(x=279, y=173, duration=1)
p.sleep(1)
p.click(x=279, y=173)

p.moveTo(x=628, y=331, duration=1)
p.sleep(1)
p.click(x=628, y=331)
p.typewrite('automation_chalenge')

p.moveTo(x=446, y=671, duration=1)
p.sleep(1)
p.click(x=446, y=671)
p.hotkey('enter')

#repositorio já criado
#p.moveTo(x=1532, y=105, duration=1)
#p.sleep(2)
#p.click(x=1532, y=105)

#p.moveTo(x=1462, y=279, duration=1)
#p.sleep(2)
#p.click(x=1462, y=279)

#p.moveTo(x=561, y=316, duration=1)
#p.sleep(2)
#p.click(x=561, y=316)

#get endereço clone
p.moveTo(x=1052, y=285, duration=1)
p.sleep(2)
p.click(x=1052, y=285)

p.moveTo(x=1046, y=461, duration=1)
p.sleep(2)
p.click(x=1046, y=461)

p.moveTo(x=459, y=881, duration=1)
p.sleep(2)
p.click(x=459, y=881)

p.moveTo(x=82, y=191, duration=1)
p.sleep(2)
p.click(x=82, y=191)
p.sleep(1)
p.rightClick(x=82, y=191)

p.moveTo(x=186, y=320, duration=1)
p.sleep(2)
p.click(x=186, y=320)

p.sleep(2)
p.typewrite('git clone ')
#p.hotkey('shift','insert')
p.hotkey('ctrl', 'v')
p.sleep(2)
p.hotkey('enter')
p.sleep(1)
p.typewrite('cd automation_chalenge')
p.sleep(2)
p.hotkey('enter')
p.sleep(2)
p.typewrite('code .')
p.hotkey('enter')
p.sleep(2)

#Vscode
p.moveTo(x=1242, y=78, duration=1)
p.sleep(1)
p.click(x=1242, y=78)
p.moveTo(x=132, y=81, duration=1)
p.sleep(2)
p.click(x=132, y=81)
p.typewrite('teste.py')
p.hotkey('enter')
p.sleep(2)

p.typewrite('print("Hello World")')
p.moveTo(x=1486, y=53, duration=1)
p.click(x=1486, y=53)
p.sleep(2)

p.moveTo(x=704, y=881, duration=1)
p.click(x=704, y=881)
p.sleep(2)
p.typewrite('git add .')
p.hotkey('enter')
p.sleep(2)
p.typewrite('git commit -m "subindo commit automation"')
p.hotkey('enter')
p.sleep(2)
p.typewrite('git push')
p.hotkey('enter')
p.sleep(2)

p.moveTo(x=656, y=883, duration=1)
p.sleep(2)
p.click(x=656, y=883)

p.moveTo(x=271, y=160, duration=1)
p.sleep(3)
p.doubleClick(x=271, y=160)