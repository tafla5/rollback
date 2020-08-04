import re
#interacje sa uzywane do liczenia wystapien "ssh"
def no_object(line):
    single_object[interation].append('no '+line)
def no_object_group(line):
    object_group[interation].append('no '+line)
def no_access_list(line):
    #szuka line i cyfr a nastepnie jest zamienia na pusty znak
    without_line = re.sub(' line [0-9]+','',line)
    access_list[interation].append('no '+without_line)


file_name = input('Provide source file name: ')

single_object = [[],[]]
object_group = [[],[]]
access_list = [[],[]]
ssh = [[],[]]
a = -1
interation = -1

with open(file_name+'.txt', 'r+') as file_object:
    for line in file_object:
        if line.startswith('ssh'):
            interation+=1
            ssh[interation].append(line)
        elif line.startswith('conf'):
            ssh[interation].append(line)
        elif line.startswith('object-group'):
            no_object_group(line)
        elif line.startswith('object '):
            no_object(line)
        elif line.startswith('access-list'):
            no_access_list(line)


with open(file_name+'.txt', 'a') as file_object:
    file_object.write('\n\n###########################\n\n\n\n')
    while a < interation:
        a+=1
        for i in ssh[a]:
            file_object.write(str(i)+'\n')
        for i in access_list[a]:
            file_object.write(str(i))
        file_object.write('\n')
        for i in object_group[a]:
            file_object.write(str(i))
        file_object.write('\n')
        for i in single_object[a]:
            file_object.write(str(i))
        file_object.write("\nend \nwr\n\n")
