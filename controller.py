import pafy

def download(url, mycb):
    try:   
        v = pafy.new(url,  callback=None)  #создаем объект   
        file_name = v.title
        print(v.title)
        streams = v.getbest() #получаем видеопотоки, содержащие звуковую дорожку
        file_name = streams.download(quiet=True, callback=mycb)
        print('Скачалось!')
    except:
        print('Не работает')
    

def mycb(total, recvd, ratio, rate, eta):
    print(total, recvd, ratio, eta)   
