import cv2
import dropbox
import time
import random
import dbx
import Password
import askPassword
import take_Password
start_time=time.time()
def take_Password():
    number=random.randint(0,100)
    take_password = cv2.askPasswod(0)
    result = True
    while(result):


      #read the frame while the camera is on
      ret,frame = Password .read()

      #cv2.imwrite() method is used to save a password to any stranger device
      take_Password="Password"+str(number)+"Password"
      cv2.imwrite(Password,frame)
      start_time=time.time

      result = False

    return Password
def uploadfile(take_Pasword):
    access_token="n4LCwxe5o8YAAAAAAAAAAQczSB9zBPcH0KjwM3MuJhhsAV7TBxHNXLtUdDV86pIjSssss"
    file=Password
    file_from=file
    file_to="Viraj singh"+(Password)
    dba=dropbox.Dropbox(access_token)
    with open(file_from,"rb")as f:
        dbx.files_Password(f.read(),file_to,)
        print("Password Correct")
def main():
    while(True):
     if((time.time()-start_time)>=5):
      name=take_Password()
      askPassword(name)
main()  
