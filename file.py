import os
import os.path

def FileMenu():
    print('''Input 0 to exit
Input 1 delete file
Input 2 to rename file
Input 3 to add content to this file
Input 4 to rewrite content of this file
Input 5 for return to the parent directory''')

def DirMenu():
    print('''Input 0 to exit
Input 1 to rename directory
Input 2 to print number of files in it
Input 3 to print number of directories in it
Input 4 to list content of the directory 
Input 5 to add file to this directory
Input 6 to add new directory to this directory
Input 7 to return to work with file''')    
os.system('cls')
programm=True
InFile=True
cnt2=0
print("You now working with file\n")
while programm==True:
    while InFile ==True :
     if cnt2 == 0:
         Folderpath=input("Input path of directory: ")
         filelist = os.listdir(Folderpath)
         print(filelist)
         IsExist=False
         while IsExist ==False:
             currentFile= input("Write full file name you want to work:")
             pathoffile=os.path.join(Folderpath,currentFile)
             os.system('cls')
 
             if os.path.isfile(pathoffile):
                 IsExist=True
             else:
                 os.system('cls')
                 print ("File not exist")
         cnt2+=1        
     FileMenu()
     command=int(input())
     os.system('cls')
     if command == 0:
         exit()
     if command == 1:
         
         os.remove(pathoffile)
         os.system('cls')
         print("File has been deleted\n")
         
     elif command ==2:
         newname = input('Write new file name: ')
         newname = os.path.join(os.path.split(pathoffile)[0], newname) + os.path.splitext(pathoffile)[1]
         os.rename(pathoffile, newname)
         pathoffile=newname
         os.system('cls')
         print("File has been renamed")

     elif command == 3 :
         print("Write what you want to add:")
         edittext=str(input())+"\r\n"
         f=open(pathoffile,"a")       
         f.write(edittext)
         f.close()
         os.system('cls')    
         print("file context has been changed\n")   

     elif command == 4:
         print("Write what you want to rewrite:")
         edittext=str(input())+"\r\n"
         f=open(pathoffile,"wt")
         f.write(edittext)
         f.close()
         os.system('cls')    
         print("file context has been rewrited\n")  
         
     elif command==5:
         InFile=False
         os.system('cls')
         cnt2=0

    while InFile == False :
     DirMenu()
     command=int(input())
     os.system('cls')
     if command == 0:
         exit()
     if command == 1:
         Folderpath=input("Input path of directory: ")
         currentdir = os.path.join(Folderpath, input('Enter directory name: '))
         newdir = os.path.join(Folderpath, input('Enter new name: '))
         os.system('cls')  
         try :
             os.rename(currentdir, newdir)
             print('Directory successfully renamed\n')
         except : print("There is no file",Folderpath)  
        
     if command == 2:
         cnt = 0
         Folderpath=input("Input path of directory: ")
         for item in os.scandir(Folderpath):
            if item.is_file():
                cnt += 1
         os.system('cls')
         print(str(cnt)+" files in "+str(Folderpath)+'\n')
        
     if command == 3: 
         Folderpath=input("Input path of directory: ")
         os.system('cls')
         print(str(len(next(os.walk(Folderpath))[1]))+"directories in"+str(Folderpath)+'\n')

     if command == 4 : 
         Folderpath=input("Input path of directory: ")
         filelist = os.listdir(Folderpath)    
         os.system('cls')
         print(filelist,'\n')

     if command==5 :
         Folderpath=input("Input path of directory: ")
         nameofnewfile=str(input("Write new name of file: "))+".txt"
         filepath = os.path.join(Folderpath, nameofnewfile)
         if not os.path.exists(filepath):
             f = open(filepath, "a")
             f.close()
         os.system('cls')
         print("File has been created\n") 

     if command == 6 :
         Folderpath=input("Input path of directory: ")
         newdirectory = input("Write name of new directory: ") 
         filepath = os.path.join(Folderpath, newdirectory)
         if not os.path.isdir(filepath):
             os.makedirs(filepath)
             os.system('cls')
             print("New directory has been created\n")
         else :
             os.system('cls')
             print("Directory already exist\n")

     if command == 7 :
         InFile=True
         os.system('cls')
