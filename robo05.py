import rpa as r
import pyautogui as p

r.init()

r.url('https://www.google.com.br/')


r.wait(2.0)
r.type('//*[@name="q"]', 'RPA Python[enter]')
r.wait(2.0)

r.snap('page', 'rpa_page.png')
r.wait(2.0)
r.close()