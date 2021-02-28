import pyautogui as klavye
import time

def yaz():
    klavye.confirm('Uygulama çalışacak, emin misin?')
    time.sleep(1)
    sayi = 33
    while True:
        if sayi == 33:
            klavye.typewrite('a')
            klavye.press('enter')
            sayi += 1
            time.sleep(1)
        else:
            klavye.press('up')
            klavye.typewrite(chr(sayi))
            klavye.press('enter')
            sayi += 1
            time.sleep(1)

yaz()
