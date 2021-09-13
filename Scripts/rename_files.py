import os

dir = 'F:/faces94/dataset'
os.chdir(dir)
files=os.listdir(dir)
for i in range(len(files)):
    os.rename(files[i],str(i))
    i=i+1
