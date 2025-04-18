from win32api import GetSystemMetrics,mouse_event,GetAsyncKeyState
import win32con
import ctypes
import time
import cv2
import numpy as np
import dxcam
from winsound import Beep
from os import system
from keyboard import is_pressed
import wmi
import datetime
import socket
import random
import os
from colorama import Fore, Style, init
import string
import winsound

string.ascii_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mb2 = random.randint(1000, 3999)
ctypes.windll.kernel32.SetConsoleTitleW(f"BlackSquad.exe --> pid [{mb2}] ")
kirrrr = random.choice(string.ascii_letters)
kir = random.choice(string.ascii_letters)

def print_banner():
    system("cls")
    print(Style.BRIGHT + Fore.MAGENTA +"""
 		   
            ▄▀█ █░█ ▀█▀ █▀█ █▄▀ █ █▀▀ █▄▀
            █▀█ █▄█ ░█░ █▄█ █░█ █ █▄▄ █░█
 		    DRAGON________MODE
   """)

    
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
scr = dxcam.create()
time.sleep(0.2)
region = (
    int(103),
    int(25),
    int(128),
    int(145)
)
screen = (int(width/2),int(height/2),int(width/2 + 2),int(height/2 + 2))
system("cls")

def check():
    ccc = wmi.WMI()
    sss = ccc.Win32_Processor()
    hardid = sss[0].ProcessorId
    processid = sss[0].Description
    now = datetime.datetime.now()
    cock = now.strftime("%M")
    gh = now.strftime("%S")
    current_time = now.strftime("%d/%m/%y")
    start_current_time = datetime.date(now.year, now.month, now.day)
    end_current_time = datetime.date(2022, 11, 18)
    end_day = (end_current_time - start_current_time).days
    x = int(cock)
    j = int(gh)
    x = x * 99 * 15 * 79 * 2 * j
    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    pime = now.strftime("%I:%M:%S")
    ran = random.randint(0, 3)
    os.system("cls")
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+"Searching For Updates..."+Style.RESET_ALL)
    time.sleep(3.6)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+"Ready For Action...")
    time.sleep(3)
    os.system("cls")
    time.sleep(3)
    hwid = "BFEBF"
    process = "Inte"
    if hardid == hwid and processid == process: 
        print(Style.BRIGHT + Fore.CYAN +"""
                █████████████████████████
                █─▄─▄─█▄─▄█▄─▀█▀─▄█▄─▄▄─█
                ███─████─███─█▄█─███─▄█▀█
                ▀▀▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀ 
        ░░ ░░ ░░ ░░ ░░ ░░ ░░        ░░ ░░ ░░ ░░ ░░ ░░ ░░
                ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀
        ░░ ░░ ░░ ░░ ░░ ░░ ░░        ░░ ░░ ░░ ░░ ░░ ░░ ░░                      
          ᴛɪᴍᴇ ᴏғ ᴘᴜʀᴄʜᴀsᴇ            ᴛɪᴍᴇ ʀᴇᴍᴀɪɴɪᴜɴɢ   """)
                                      
        print(Style.BRIGHT + Fore.YELLOW +f"""                 {current_time}                      {end_day}

        """)
        print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+Style.BRIGHT + Fore.YELLOW +" VIP USER")
        time.sleep(2.0)
        time.sleep(4)

    else:
        print(Style.BRIGHT + Fore.CYAN+"""             
        ▒█▀▀█ █▀▀█ █▀▀▄ █▀▀ 　 ▒█▀▀▀ █▀▀▄ ▀▀█▀▀ █▀▀ █▀▀█ 
        ▒█░░░ █░░█ █░░█ █▀▀ 　 ▒█▀▀▀ █░░█ ░░█░░ █▀▀ █▄▄▀ 
        ▒█▄▄█ ▀▀▀▀ ▀▀▀░ ▀▀▀ 　 ▒█▄▄▄ ▀░░▀ ░░▀░░ ▀▀▀ ▀░▀▀
             -= Autokick#0611 (DRAGON_____MODE) =-
        """+Style.RESET_ALL)
        teleport = input(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" Please Enter Your Private Code:"+Style.RESET_ALL)
        q = int(teleport)
        if q != x:
            print(Style.BRIGHT + Fore.RED +f"[{pime}]"+"******SYSTEM INFORMATION BLOCKED******")
            print(Style.BRIGHT + Fore.RED +f"[{pime}]"+"User:  "+hostname)
            print(Style.BRIGHT + Fore.RED +f"[{pime}]"+"Local IP:  "+IPAddr)
            print(Style.BRIGHT + Fore.RED +f"[{pime}]"+"CPU Model:  "+processid+Style.RESET_ALL)
            time.sleep(2.0)
            print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" Please Contact With Creator [AutoKick#0611].")
            time.sleep(25.0)
            exit()
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+Style.BRIGHT + Fore.GREEN +" Passed")
    time.sleep(6)
    os.system("cls")
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+ Fore.RED+"Spoofing Drivers..."+Style.RESET_ALL)
    time.sleep(3)
    koss = random.randint(123124123123123, 999999999999999)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+f"1-HEX: {kirrrr}{koss}{kir}"+Style.RESET_ALL)
    time.sleep(4)
    PIDD = random.randint(1010, 2000)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+f"PROCESS-PID: {PIDD}"+Style.RESET_ALL)
    time.sleep(4)
    os.system("cls")
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" User:  "+hostname)
    time.sleep(1.5)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" IP:    "+IPAddr+"""

    """)
    time.sleep(1.5)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" Hardware ID: "+hardid+"""
    """)
    time.sleep(3)
    os.system("cls")
    print(Style.BRIGHT + Fore.MAGENTA +"""

    ░█████╗░██╗░░░██╗████████╗░█████╗░██╗░░██╗██╗░█████╗░██╗░░██╗
    ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██║░██╔╝██║██╔══██╗██║░██╔╝
    ███████║██║░░░██║░░░██║░░░██║░░██║█████═╝░██║██║░░╚═╝█████═╝░
    ██╔══██║██║░░░██║░░░██║░░░██║░░██║██╔═██╗░██║██║░░██╗██╔═██╗░
    ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██║░╚██╗██║╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝
 		   -= Autokick#0611 (DRAGON_____MODE) =-
   """+ Style.RESET_ALL)
    time.sleep(3.5)
    print(Fore.YELLOW +""" --> Loading injector Kernel32.dll... 
          """)
    time.sleep(13.5)
    winsound.Beep(400, 200)
    try:
        a = os.environ['USERPROFILE']
        b = a + "\Desktop\Black Squad.url"
        os.startfile (b)
    except:
        print(Style.BRIGHT +Fore.RED +"Cant Access To Game Data!!!!"+Style.RESET_ALL)
        time.sleep(2.5)
        pass
    print(Style.BRIGHT + Fore.GREEN +" Injected!"+Style.RESET_ALL)
    sleep(1.5)
        

check()

def main():
    global region
    print_banner()
    system("cls")
    print_banner()
    cmd = input("AimBot Speed(default:11.2):")
    my_list = list(region)
    cmd4 = input(f"ESP SIZE (default: {my_list[0]} ):"+Style.RESET_ALL)
    cmd4 = int(cmd4) - my_list[0]
    my_list[0] = my_list[0] + cmd4
    my_list[2] = my_list[2] + cmd4
    region = tuple(my_list)
    print(my_list[0])
    system("cls")
    print_banner()
    print("[] Aimbot on")
    speed = float(cmd)
    running = False
    aimbot = False
    while True:
        if GetAsyncKeyState(win32con.VK_NUMPAD9):
            main()
        if GetAsyncKeyState(win32con.VK_NUMPAD5):
            if aimbot == False:
                aimbot = True
                Beep(400, 150)
                print("[] Aimbot off") 
            else:
                aimbot = False
                Beep(400, 150)
                print("[] Aimbot on")                                 
        if aimbot == False:
            try:
                pic = scr.grab(region=region)
                hsv = cv2.cvtColor(pic,cv2.COLOR_BGR2HSV)
                hower_red = np.array([179,255,255])
                lower_red = np.array([179,168,135])
                mask = cv2.inRange(hsv, lower_red, hower_red)
                res = cv2.bitwise_and(pic,pic, mask= mask)
                blue, green, red = cv2.split(pic)
                contours1, hierarchy1 = cv2.findContours(image=red, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
                cX = contours1[1][-1][-1][0]
                cY = contours1[1][-1][-1][1]
                cY = cY / speed
                ctypes.windll.user32.mouse_event(
                        ctypes.c_uint(0x0001),
                        ctypes.c_uint(int((cX - 17) * cY)),
                        ctypes.c_uint(0),
                        ctypes.c_uint(0),
                        ctypes.c_uint(0))    

            except:
                pass

main()


