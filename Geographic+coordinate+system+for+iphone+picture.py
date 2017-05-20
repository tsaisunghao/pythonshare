
# coding: utf-8

# In[1]:

import PIL.Image



# In[2]:

direc = 'your file directory'


# In[3]:

head = ('file','latitude','longitude')
outputFile = open(r'your file directory','w',newline = '')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(head)


# In[4]:

for i in range(1,7):
    direcs = direc + str(i)+ '.jpg'
    img = PIL.Image.open(direcs)
    exif_data = img._getexif()
    coordi = exif_data[34853]
    latitude = coordi[2][0][0] #latitude
    longitude = coordi[4][0][0] # longitude
    coordination = (str(i)+ '.jpg',latitude,longitude)
    print (coordination)
    
    outputWriter.writerow(coordination)


# In[42]:

print (coordi)


# In[43]:

outputFile.close()


# In[ ]:



