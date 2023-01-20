#-------------------------write in a file-----------------------
# with open("Creat.txt","w") as f:
#     line=["Rohit is so awesome","\nRohit can do anything","\nMy name is rohit motwani"]
#     f.writelines(line)
#-----------------------read the written file---------------------
with open("Creat.txt","r") as f:
    line="\n"
    content=f.read()
    line_no=1
    characters="abcdefghijklmnopqrstuvwxyz"
    words=" "
    word_count=0
    characters_count=0
    for i in content:
        if(i==line):
            line_no+=1
        for j in words:
            if(i==j):
                word_count+=1
        for j in characters:
            if(i==j):
                characters_count+=1
    print("Total number of lines is : {}".format(line_no))
    print("Total number of words is : {}".format((word_count+line_no)))
    print("Total number of characters is : {}".format((characters_count+word_count+line_no)))