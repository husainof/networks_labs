import requests
from bs4 import BeautifulSoup as b

WebsiteName = ""
Number = 0

foundLinks = []
checkedLinks = []


def getUrls(num, url):
    try:
        global Number
        Number = int(num)
        
        URL = url
        if("http://" not in URL):
            URL = "http://"+URL
        global linksForCheck
        global foundLinks
        global WebsiteName
        global checkedLinks
        checkedLinks = []  
        foundLinks = [] 
        linksForCheck = [] 
        WebsiteName = GetNameWebsite(URL)
        linksForCheck += [URL]
        Checklink()
    except:
        print("Некорректные данные")
    return checkedLinks, foundLinks


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
    except:
        print("При обработке данных произошла ошибка")
   


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
