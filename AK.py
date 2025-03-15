from tkinter import *
import pyautogui
import time
import webbrowser as wb
import os
import pyshorteners
import wikipedia
import yt_dlp as youtube_dl
import moviepy as mp
import cv2

root=Tk()
root.geometry("730x930")
root.title("Arun Kumar")

def screenshot1():
    time.sleep(4)
    name=time.time()
    name='C:/Users/Public/Pictures/Public Pictures {}.png'.format(name)
    img=pyautogui.screenshot()
    img.save(name)
    img.show()

    
def goto1(web1):
    #chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    #wb.get(chrome_path).open(web1)
    wb.open(web1)

def wordo():
    Wordpad_path='C:\\ProgramData\\Microsoft/Windows\\Start Menu\\Programs\\Accessories\\WordPad'
    os.startfile(Wordpad_path)

def excelo():
    excel_path="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
    os.startfile(excel_path)

def power():
    power_path="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
    os.startfile(power_path)

def screenshot():
    r=Tk()
    r.geometry("430x360")
    r.title("Screenshot")
    lblinfo=Label(r, font=('arial', 18, 'bold'), text="Screenshot Application", fg="black")
    lblinfo.grid(row=0, column=0,padx=40,pady=20)
    lblinfo=Label(r, font=('arial', 12, 'bold'), text="You have 4 second to open the window", fg="black")
    lblinfo.grid(row=1, column=0)
    lblinfo=Label(r, font=('arial', 12, 'bold'), text=" you want to take screenshot", fg="black")
    lblinfo.grid(row=2, column=0)
    button=Button(r,text="Take ScreenShot", command=screenshot1, bd=5, bg="white", fg="Blue", padx=12, pady=5)
    button.grid(row=3,column=0, pady=10)
    close=Button(r,text="Quit", command=r.destroy , bg="white", fg="Blue", bd=5, padx=10, pady=5)
    close.grid(row=5,column=0, pady=10)
    lblinfo=Label(r, font=('arial', 12, 'bold'), text='Your screenshot saved at path', fg="black")
    lblinfo.grid(row=6, column=0)
    lblinfo=Label(r, font=('arial', 12, 'bold'), text='C>Users>Public>Pictures', fg="black")
    lblinfo.grid(row=7, column=0)
    r.mainloop()


def chrome():
    r=Tk()
    r.geometry("550x450")
    r.title("Work Setup Automation")
    web1=StringVar()
    lblinfo=Label(r, font=('arial', 18, 'bold'), text="Work Setup Automation", fg="black")
    lblinfo.grid(row=0, column=0, sticky="w", padx=12, pady=20)
    lblinfo=Label(r, font=('arial', 15, 'bold'), text="Web browser", fg="black")
    lblinfo.grid(row=1, column=0, sticky="w", padx=15, pady=4)
    lblinfo=Label(r, font=('arial', 12, 'bold'), text="Enter the URL of website", fg="black")
    lblinfo.grid(row=2, column=0, sticky="w", padx=12, pady=3)
    web=Entry(r, font=('arial',12,'bold'), width=23 ,insertwidth=2, bd=5, justify='right' ,textvariable=web1)
    web.grid(row=3, sticky='ew' ,padx=(15,5), pady=0)
    goto=Button(r,text="go ✈",font=('arial',10,'bold') ,command=lambda: goto1(web.get()), bg="gray", fg="black", bd=2)
    goto.grid(row=3,column=1, sticky="w",padx=0, pady=0)
    lblinfo=Label(r, font=('arial', 15, 'bold'), text="Applicaton", fg="black")
    lblinfo.grid(row=4, column=0, sticky="w", padx=15, pady=(10,15))
    lblinfo=Label(r, font=('arial', 12, 'bold'), text="Enter to open Wordpad", fg="black")
    lblinfo.grid(row=5,column=0, sticky="ew", padx=(15,5), pady=0)
    btn=Button(r,text="Wordpad",font=('arial',10,'bold') ,command=wordo, bg="gray", fg="black", bd=2)
    btn.grid(row=5,column=1,padx=0, pady=9)
    lblinfo=Label(r, font=('arial', 12, 'bold'), text="Enter to open Excel", fg="black")
    lblinfo.grid(row=6,column=0, sticky="ew", padx=(15,5), pady=0)
    btn=Button(r,text="Excel",font=('arial',10,'bold') ,command=excelo, bg="gray", fg="black", bd=2)
    btn.grid(row=6,column=1,padx=0, pady=9)
    lblinfo=Label(r, font=('arial', 12, 'bold'), text="Enter to open Power Point", fg="black")
    lblinfo.grid(row=7,column=0, sticky="ew", padx=(15,5), pady=0)
    btn=Button(r,text="Power Point",font=('arial',10,'bold') ,command=power, bg="gray", fg="black", bd=2)
    btn.grid(row=7,column=1,padx=0, pady=9)
    r.mainloop()

def shortu():
    r=Tk()
    r.geometry("520x300")
    r.title("URL application")
    url=StringVar()
    short_url=Entry(r, font=('arial',12,'bold'), width=26, bd=3, justify='center')
    lblinfo=Label(r, font=('arial', 18, 'bold'), text="URL Shortener Application", fg="black")
    lblinfo.grid(row=0, column=0, sticky="w", padx=12, pady=20)
    lblinfo=Label(r, font=('arial', 12, 'bold'), text="Enter the URL", fg="black")
    lblinfo.grid(row=1, column=0, sticky="w", padx=12, pady=10)
    url=Entry(r, font=('arial',12,'bold'), width=26 ,insertwidth=2, bd=5, justify='right')
    url.grid(row=2, sticky='ew' ,padx=(15,5), pady=0)
    goto=Button(r,text="Done",font=('arial',10,'bold') ,command=lambda: update_url(url.get(),short_url), bg="gray", fg="black", bd=2)
    goto.grid(row=2,column=1, sticky="w",padx=0, pady=0)
    lblinfo=Label(r, font=('arial', 12, 'bold'), text="Shorted URL", fg="black")
    lblinfo.grid(row=3, column=0, sticky="w", padx=12, pady=10)
    short_url.grid(row=4,column=0, padx=(15,5), pady=0)
    gotou=Button(r,text="go ✈",font=('arial',10,'bold') ,command=lambda: goto1(short_url.get()), bg="gray", fg="black", bd=2)
    gotou.grid(row=4,column=1, sticky="w",padx=0, pady=0)
    r.mainloop()

def update_url(url1,short_url):
    urlss=pyshorteners.Shortener().tinyurl.short(url1)
    short_url.delete(0,END)
    short_url.insert(END,urlss)

def wiki():
    r=Tk()
    text=Text(r, font=('arial',12,'bold'), width=78, height=21, bd=5, wrap='word')
    r.geometry('900x780')
    r.title("Wikipedia Search App")
    ques=Label(r, text="Question", font=('arial', 18, 'bold'))
    ques.grid(row=0,column=0,pady=17,padx=380)
    get_q=Entry(r, bd=5, font=('arial', 14, 'bold'), insertwidth=5, width=20, justify='center')
    get_q.grid(row=1, column=0)
    submit=Button(r, text='Search', command=lambda: on_press(get_q,text),font=('arial',12,'bold'), bg='powder blue',padx=12,pady=6)
    submit.grid(row=2,column=0, pady=13)
    text.grid(columnspan=10, padx=15)
    btne=Button(r, text='Exit', command=r.destroy ,font=('arial',12,'bold'), bg='powder blue',padx=15,pady=8)
    btne.grid(row=4,column=0, pady=10)
    r.mainloop()


def on_press(get_q,text):
    text.delete("1.0",END)
    q=get_q.get()
    text.insert(INSERT,wikipedia.summary(q))

def yout():
    r=Tk()
    r.geometry("470x250")
    r.title("video Download")
    lblinfo=Label(r, font=('arial', 18, 'bold'), text="Youtube Video download", fg="black")
    lblinfo.grid(row=0, column=0, sticky="w", padx=20, pady=20)
    lblinfo=Label(r, font=('arial', 12, 'bold'), text="Enter the URL of youtube video", fg="black")
    lblinfo.grid(row=1,column=0, sticky='ew', pady=5,padx=0)
    youurl=Entry(r, font=('arial',13,'bold'), width=23 ,insertwidth=2, bd=5, justify='right')
    youurl.grid(row=2, sticky='ew', padx=10, pady=0)
    youd=Button(r,text="📥",font=('arial',12,'bold') ,command=lambda: youdo(youurl.get()), bg="powder blue", fg="black", bd=2, padx=0, pady=0)
    youd.grid(row=2,column=1, padx=(0,30))
    r.mainloop()


def youdo(urlyou):
    with youtube_dl.YoutubeDL() as ydl:
        ydl.download([urlyou])
  

def audioe():
    r=Tk()
    r.geometry("520x280")
    r.title("Audio extract")
    lblinfo=Label(r, font=('arial', 18, 'bold'), text="Audio Extractor", fg="black")
    lblinfo.grid(row=0, column=0, sticky="w", padx=20, pady=20)
    lblinfo=Label(r, font=('arial', 12, 'bold'), text="Enter the path for the video file: ", fg="black")
    lblinfo.grid(row=1,column=0, sticky='w', pady=5,padx=5)
    vidurl=Entry(r, font=('arial',13,'bold'), width=35 ,insertwidth=2, bd=5, justify='right')
    vidurl.grid(row=2, sticky='w', padx=10, pady=0)
    aud=Button(r,text="📥",font=('arial',12,'bold') ,command=lambda: aude(vidurl.get()), bg="powder blue", fg="black", bd=2, padx=0, pady=0)
    aud.grid(row=2,column=1, padx=(0,30))
    lblinfo=Label(r, font=('arial', 10, 'bold'), text="Note :- The path structure is like", fg="black")
    lblinfo.grid(row=3, column=0, sticky="w", padx=12, pady=0)
    lblinfo=Label(r, font=('arial', 10, 'bold'), text=r" C:\Users\Dell\Desktop\{video name}.mp4 ", fg="black")
    lblinfo.grid(row=4, column=0, sticky="w", padx=12, pady=0)
    lblinfo=Label(r, font=('arial', 10, 'bold'), text="Means enter the full path ", fg="black")
    lblinfo.grid(row=5, column=0, sticky="w", padx=19, pady=0)
    r.mainloop()

def aude(audurl):
    path=audurl
    videoclip=mp.VideoFileClip(path)
    audioclip=videoclip.audio
    audioclip.write_audiofile("audio.mp3")

def camra():
    r=Tk()
    r.geometry("640x370")
    r.title("IP Webcam")
    cam1=StringVar()
    lblinfo=Label(r, font=('arial', 16, 'bold'), text="IP webcam for smart phone connect camera", fg="black")
    lblinfo.grid(row=0, column=0, sticky="w", padx=30, pady=20)
    lblinfo=Label(r, font=('arial', 12, 'bold'), text="Enter the IP address", fg="black")
    lblinfo.grid(row=1,column=0, sticky='ew', pady=5,padx=0)
    web=Entry(r, font=('arial',12,'bold'), width=30 ,insertwidth=2, bd=5, justify='center' ,textvariable=cam1)
    web.grid(row=2, sticky='w', pady=0, padx=150)
    submit=Button(r, text='Start', command=lambda: cams(web.get()),font=('arial',12,'bold'), bg='powder blue',padx=12,pady=6)
    submit.grid(row=3,column=0, pady=13)
    lblinfo=Label(r, font=('arial', 12, 'bold'), text="Note :- The IP structure is like http://<your_phone_ip>:<port>", fg="black")
    lblinfo.grid(row=4, column=0, sticky="w", padx=12, pady=3)
    lblinfo=Label(r, font=('arial', 12, 'bold'), text="Press q for exit ", fg="black")
    lblinfo.grid(row=5, column=0, sticky="w", padx=12, pady=0)
    lblinfo=Label(r, font=('arial', 13, 'bold'), text="Install ip webcam app in your phone and click on start server", fg="black")
    lblinfo.grid(row=6, column=0, sticky="w", padx=12, pady=3)
    r.mainloop()


def cams(camip):
    address=camip.strip()+"/video"
    cap=cv2.VideoCapture(0)
    cap.open(address)
    print(address)
    while(True):
        ret, frame=cap.read()
        cv2.imshow('Frame',frame)
        if cv2.waitKey(20) & 0xFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


top=Frame(root,width=1000, height=90)
top.pack(side=TOP)
bottom=Frame(root,width=1000,height=910)
bottom.pack(fill=BOTH)
app_title=Label(top, font=('arial',35, 'bold'), text="Arun Kumar")
app_title.grid(row=0, column=1, pady=8)
app_title1=Label(top,font=('arial', 18), text="Python Projects" )
app_title1.grid(row=1,column=1)


lblb0=Label(bottom, text="")
lblb0.grid(row=0,column=0)
lbl1=Label(bottom, font=('arial',20,'bold'), text="1. Take Screenshot")
lbl1.grid(row=1,column=0,padx=20,sticky='w')
button1=Button(bottom, padx=16, pady=8, bd=10, fg="black", font=("arial",16,'bold'), width=8, text="Screenshot", bg="powder blue", command=screenshot)
button1.grid(row=1,column=1,padx=20, sticky='w')
lbl3=Label(bottom, font=('arial',20,'bold'), text="2. Work setup Auto.")
lbl3.grid(row=3,column=0, padx=20, sticky='w')
button3=Button(bottom, padx=16, pady=8, bd=10, fg="black", font=("arial",16,'bold'), width=8, text="Setup", bg="powder blue", command=chrome)
button3.grid(row=3,column=1, padx=20,pady=17, sticky='w')
lbl4=Label(bottom, font=('arial',20,'bold'), text="3. URL shortner app.")
lbl4.grid(row=4,column=0, padx=20, sticky='w')
button4=Button(bottom, padx=16, pady=8, bd=10, fg="black", font=("arial",16,'bold'), width=8, text="URL", bg="powder blue", command=shortu)
button4.grid(row=4,column=1, padx=20,pady=12, sticky='w')
lbl5=Label(bottom, font=('arial',20,'bold'), text="4. Wikipedia Seacrh app.")
lbl5.grid(row=5,column=0, padx=20, sticky='w')
button5=Button(bottom, padx=16, pady=8, bd=10, fg="black", font=("arial",16,'bold'), width=8, text="WIKI", bg="powder blue", command=wiki)
button5.grid(row=5,column=1, padx=20,pady=12, sticky='w')
lbl6=Label(bottom, font=('arial',20,'bold'), text="5. Youtube video Download")
lbl6.grid(row=6,column=0, padx=20, sticky='w')
button6=Button(bottom, padx=16, pady=8, bd=10, fg="black", font=("arial",16,'bold'), width=8, text="Download", bg="powder blue", command=yout)
button6.grid(row=6,column=1, padx=20,pady=12, sticky='w')
lbl7=Label(bottom, font=('arial',20,'bold'), text="6. Audio Extract")
lbl7.grid(row=7,column=0, padx=20, sticky='w')
button7=Button(bottom, padx=16, pady=8, bd=10, fg="black", font=("arial",16,'bold'), width=8, text="Extract", bg="powder blue", command=audioe)
button7.grid(row=7,column=1, padx=20,pady=12, sticky='w')
lbl8=Label(bottom, font=('arial',20,'bold'), text="7. IP Webcam")
lbl8.grid(row=8,column=0, padx=20, sticky='w')
button8=Button(bottom, padx=16, pady=8, bd=10, fg="black", font=("arial",16,'bold'), width=8, text="camera", bg="powder blue", command=camra)
button8.grid(row=8,column=1, padx=20,pady=12, sticky='w')


if __name__=="__main__":
    root.mainloop()