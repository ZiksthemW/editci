import pyautogui as klavye
import time

def yaz():
    yazi = str(input("Yazı: "))
    sure = float(input("Kaç saniye beklenecek: "))
    sayi = 0
    time.sleep(1)
    try:
        while True:
            klavye.press('up')
            klavye.typewrite(yazi[sayi])
            klavye.press('enter')
            sayi += 1
            time.sleep(sure)
            if yazi[sayi] == " ":
                klavye.press('up')
                klavye.typewrite(yazi[sayi])
                sayi += 1
                klavye.typewrite(yazi[sayi])
                klavye.press('enter')
                sayi += 1
                time.sleep(sure)
    except(IndexError):
        print("Başarıyla yazı gönderimi tamamlandı.")

yaz()
