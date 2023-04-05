f = open("test.txt" , "w+")
for i in range(5):
    str = input()
    f.write(str+'\n')
f.close()