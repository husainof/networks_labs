import requests
from bs4 import BeautifulSoup as b
from tkinter import *
from tkinter.messagebox import showerror


api = Tk()
WebsiteName = ""
Number = 0

foundLinks = []
checkedLinks = []


def btn_click():
    try:
        global Number
        Number = int(NumberPages.get())
        info1.delete(1.0, END)
        info2.delete(1.0, END)
        URL = UrlName.get()
        if("http://" not in URL):
            URL = "http://"+URL
        global linksForCheck
        global foundLinks
        global WebsiteName
        global checkedLinks
        checkedLinks = []  # проверенные ссылки
        foundLinks = []  # ссылки на сторонние сервера
        linksForCheck = []  # ссылки, которые нужно проверить
        WebsiteName = GetNameWebsite(URL)
        linksForCheck += [URL]
        Checklink()
    except:
        showerror(title="Ошибка", message="Некорректные данные")


def Checklink():
    global linksForCheck
    global foundLinks
    global checkedLinks
    k = 1
    try:
        while (linksForCheck != []) and (k <= Number):
            currentUrl = linksForCheck.pop(0)
            r = requests.get(currentUrl)
            if(r.status_code == 200):
                soup = b(r.text, 'html.parser')
                list1 = soup.find_all('a', href=True)
                list2 = str(list1)
                links = ""
                while ("href" in list2):
                    start = list2.find("href")
                    end = list2.find("\"", start + 6)
                    link = list2[start + 6:end]
                    list2 = list2.replace("href=\"" + link + "\"", "")
                    links += link + " "
                links = links.split()
                for c in links:
                    if ("http" in c):
                        c_short = GetNameWebsite(c)
                        if (c_short == WebsiteName) and (c not in checkedLinks) and (c not in linksForCheck) and (c != currentUrl):
                            linksForCheck += [c]
                        elif (c_short != WebsiteName) and (c_short not in foundLinks):
                            foundLinks += [c_short]
                    elif ("#" == c):
                        c = "http://" + WebsiteName + "/" + c
                        if (c not in checkedLinks) and (c not in linksForCheck) and (c != currentUrl):
                            linksForCheck += [c]
                    elif ("http" not in c):
                        c = "http://" + WebsiteName + c
                        if (c not in checkedLinks) and (c not in linksForCheck) and (c != currentUrl):
                            linksForCheck += [c]
                checkedLinks += [currentUrl]
                k += 1
        OutputLinks()
    except:
        showerror(title="Ошибка", message="При обработке данных произошла ошибка")


def GetNameWebsite(url):
    if("http://" in url):
        url = url.replace("http://", "")
    elif("https://" in url):
        url = url.replace("https://", "")
    if("www." in url):
        url = url.replace("www.", "")
    if(url.find("/") != -1):
        end = url.find("/")
        url = url[0: end]
    return url


def OutputLinks():
    if len(foundLinks) != 0:
        for c in checkedLinks:
            info2.insert(1.0, c+"\n\n")
        info2.insert(1.0, "Количество проверенных страниц: " +
                     str(len(checkedLinks))+"\n\n")
        for c in foundLinks:
            info1.insert(1.0, c+"\n\n")
        info1.insert(1.0, "Список найденных серверов:\n\n")


# api['bg'] = '#ffffff'
# api.title('LR №2')
# api.wm_attributes('-alpha', 1)
# api.geometry('1000x600')

# api.resizable(width=True, height=True)


# frame1 = Frame(api, bg='lightblue')
# frame1.place(relwidth=1, relheight=0.14)

# title = Label(frame1, text='Введите URL адрес и количество проверяемых страниц', bg='lightblue', font=28)
# title.pack()
# UrlName = Entry(frame1, bg='white', width=100, font=15)
# UrlName.pack()
# NumberPages =Entry(frame1, bg='white', width=20, font=15)
# NumberPages.pack()


# frame2 = Frame(api, bg='white')
# frame2.place(rely=0.15, relwidth=1, relheight=0.06)

# btn = Button(frame2, text='Поиск', bg='lightblue', font=20, command=btn_click)
# btn.pack()


# frame3 = Frame(api, bg='whitesmoke')
# frame3.place(rely=0.22,  relwidth=0.5, relheight=0.8)

# info1 = Text(frame3, font=8, width=100)
# #state=DISABLED
# info1.pack()

# frame4 = Frame(api, bg='whitesmoke')
# frame4.place(rely=0.22, relx=0.5,  relwidth=0.5, relheight=0.8)
# info2 = Text(frame4, font=8, width=100)
# info2.pack()

# api.mainloop()
