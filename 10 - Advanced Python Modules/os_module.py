import os
import shutil


f = open("practice.txt", "w+")
f.write("This is a test string")
f.close()

print(os.getcwd())
print(os.listdir("C:\\Users"))

# shutil.move("practice.text", "")
