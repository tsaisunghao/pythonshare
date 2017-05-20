
# coding: utf-8

# In[1]:

import PIL.Image
import csv


# In[2]:

direc = 'C:/Users/Vincent/Desktop/IMG_'


# In[3]:

head = ('檔案','緯度','經度')
outputFile = open(r'D:\black\file.csv','w',newline = '')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(head)


# In[4]:

for i in range(1,7):
    direcs = direc + str(i)+ '.jpg'
    img = PIL.Image.open(direcs)
    exif_data = img._getexif()
    coordi = exif_data[34853]
    latitude = coordi[2][0][0] #緯度
    longitude = coordi[4][0][0] # 經度
    coordination = (str(i)+ '.jpg',latitude,longitude)
    print (coordination)
    
    outputWriter.writerow(coordination)


# In[42]:

print (coordi)


# In[43]:

outputFile.close()


# In[ ]:



