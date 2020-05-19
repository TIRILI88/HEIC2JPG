import os

dir = input('Hier das Verzechnis mit den Bilder eingeben und Enter druecken: ')
counter = 0
for i in os.listdir(dir):
    files = os.path.join(dir,i)
    split= os.path.splitext(files)
    if split[1]=='.HEIC':
       os.rename(files,split[0]+'.JPG')
       counter += 1

print(str(counter) + " Dateien erfolgreich umgewandelt.")