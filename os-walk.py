import os
 
rootDir = '/home/cyrrup/Downloads/PM'
for dirName, subdirList, fname in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in [f for f in fname if f.endswith(".jpg")]:
    	
        print('\t%s' % fname)
    # Remove the first entry in the list of sub-directories
    # if there are any sub-directories present
    #if len(subdirList) > 0:
        #del subdirList[0]