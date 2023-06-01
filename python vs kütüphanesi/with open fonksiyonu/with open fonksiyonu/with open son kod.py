with open("alper copy.jpg","rb")as okunacak:
    with open("python2.jpg","wb")as yazilacak:
        for satir in okunacak:
            yazilacak.write(satir)
