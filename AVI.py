'''12-2-2021 copyright Jason Alexander and Jennifer Johnson
Project 2 COMP 6350
Professor Jason Cuneo
Auburn University
'''

#imports
import re
import hashlib

#Opening the project file
dd_file = 'Project2.dd'

#reading project file as into a python object for further manipulation
with open(dd_file, "rb") as f:
    content = f.read()
    f.close()

#Signature for AVI
AVI_SOF = b'\x52\x49\x46\x46'

#creating a list of matches for Start of file signature so further work can be done to deduce if its an actual file
SOF_list = [match.start() for match in re.finditer(re.escape(AVI_SOF), content)]
EOF_list = []

'''For every object in the list, we're going to be calculating the file size in little endian order and qualify it
 as a valid AVI file, '''
for SOF in SOF_list:
    byte_offset = int(SOF / 2)
    size_start = byte_offset + 4
    size_end = size_start + 4
    size_bytes = content[size_start:size_end]
    size_int = int.from_bytes(size_bytes, "little")
    file_end = byte_offset + size_int + 8
    EOF_list.append(file_end)

'''This code validates that the start of a file should be less than the end of a file. EG: a file can't start at byte 100
and end at byte 98 that would be impossible. It also validates if there are more objects in the SOF list than the EOF 
list it will delete the extra false positive start of file signatures in the list'''
if len(SOF_list)!=len(EOF_list):
    i = 0
    while i<len(EOF_list):
        if SOF_list[i]>EOF_list[i]:
            del EOF_list[i]
        i = i + 1

i = 0
'''
This code takes the start of file list and carves the files using the already figured out start and end of file. 
'''
for SOF in SOF_list:
    subdata=content[SOF:EOF_list[i]+2]
    carve_filename = str(SOF)+"_"+str(EOF_list[i])+".avi"
    carve_obj = open(carve_filename, 'wb')
    carve_obj.write(subdata)
    carve_obj.close()
    i = i + 1
    print("Found an avi and carving it to " + carve_filename)
    with open(carve_filename, "rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha256(bytes).hexdigest()
        print("SHA256:", readable_hash,"\n")

'''
This section will return the SHA256 hash value of the recovered file. 
'''


