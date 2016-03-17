import requests
from bs4 import BeautifulSoup


#Establish the session with linkedin
client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html)
csrf = soup.find(id="loginCsrfParam-login")['value']


login_information = {
    'session_key':'email@email.com',
    'session_password':'password',
    'loginCsrfParam': csrf,
}


t=client.post(LOGIN_URL, data=login_information)
#=============completed============

#create the content file
file_info=['https://www.linkedin.com/profile/view?id=AAEAAAFC4L8BEl6gJ1SFGybSHLcIlztVe9TxfYk&authType=name&authToken=ZAvg&trk=prof-sb-browse_map-name']#seed link
length=1
f=open('Link.txt','w')
for content in file_info:
    page=client.get(content)
    soup=BeautifulSoup(page.text)
    connections_link= soup.find_all("a",{"class":"browse-map-photo"})
    for item in connections_link:
        next_link= item.get("href")
        if str(next_link) not in file_info:
            file_info.append(str(next_link))
            f.write(str(next_link))
            f.write('\n')
            length = length +1 # This is a depth first so I add for all the links
            print(str(next_link))
    if length >100:
        break
f.close()
#=================Completed========

#================Start reading the link and collecting information=================
file_read=open('Link.txt','r')
file_info=[]
for things in file_read:
    file_info.append(things)
file_read.close()
length=0
tmp_txt=[]
for it in file_info:
    tmp_txt=[]
    details=client.get(it)
    details_soup=BeautifulSoup(details.text)
    flag=0
    print('------------------------------------------------')
    print('\n')
    for tag in details_soup.find_all(['h4','time','li']):
        if flag ==1:
            if 'Interests' in tag.text.strip() or 'Received' in tag.text.strip() or 'Given' in tag.text.strip() or 'See'in tag.text.strip() or 'You' in  tag.text.strip():
                file_output.close()
                break
            if tag.text.strip() not in tmp_txt:#and starts with a number then li
                print(tag.text.strip())
                file_output.write(tag.text.strip().encode('utf8'))
                file_output.write('\n')
                tmp_txt.append(tag.text.strip())
        if 'Public Profile' in tag.text.strip():
            flag =1
            profile = 'profile'+ str(length)+ '.txt'
            file_output=open(profile,'w')
            length=length+1
    
   
    
#==========================Completed===========================================
    
    




        
            
        
   
       
            
        
