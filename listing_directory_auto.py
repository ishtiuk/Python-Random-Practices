import os

pth = 'C:\\Windows\\System32'

directory_lst = os.listdir(pth)

# print(directory_lst)

serching_element = 'cmd.exe'

for i in directory_lst:
    if serching_element in directory_lst:
        indx = directory_lst.index(serching_element)
        pr = directory_lst[indx]
        print(type(pr), pr)
        
        # path making my own way  😎😎

        full_path = pth+'\\'+pr

        # path using 'OS' module 😏😏

        full_anotehr_path = os.path.join(pth, serching_element)

        print(full_anotehr_path)
        print(full_path)
        break

os.startfile(full_path)

os.startfile(full_anotehr_path)
