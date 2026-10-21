# f=open("neha.txt","r")
# content=f.read()
# print(content)
# f.close()
with open("neha.txt","r") as f:
    content=f.read()
    print(content)
    # with the help of using with no need to close the file explicitly, it will be closed automatically when the block is exited