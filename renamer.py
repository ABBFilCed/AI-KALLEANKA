# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
# Function to rename multiple files 
#Ändra från annotations till mappen du vill ändra namnen i.
def main(): 
    x=267  
    for filename in os.listdir("testing_images"):
        arr=filename.split(".")
        if arr[1]=="JPEG":
            dst = str(x) +"."+ arr[1]
            src ='testing_images/'+ filename 
            dst ='testing_images/'+ dst 
            
            # rename() function will 
            # rename all the files 
            os.rename(src, dst) 
            x+=1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 