'''12-2-2021 copyright Jason Alexander and Jennifer Johnson
Project 2 COMP 6350
Professor Jason Cuneo
Auburn University
'''

import re
import hashlib

dd_file = 'Project2.dd'

with open(dd_file, "rb") as f:
    content = f.read()
    f.close()

#signatures
DOCX_SOF = b'\x50\x4B\x03\x04\x14\x00\x06\x00'
DOCX_EOF = b'\x50\x4B\x05\x06'

#creating a list of matches for Start of file signature so further work can be done to deduce if its an actual file
SOF_list = [match.start() for match in re.finditer(re.escape(DOCX_SOF), content)]
EOF_list = [match.start() for match in re.finditer(re.escape(DOCX_EOF), content)]

'''This code validates that the start of a file should be less than the end of a file. EG: a file can't start at byte 100
and end at byte 98 that would be impossible. It also validates if there are more objects in the SOF list than the EOF 
list it will delete the extra false positive start of file signatures in the list'''
if len(SOF_list) != len(EOF_list):
    i = 0
    while i<len(EOF_list):
        if SOF_list[i]>EOF_list[i]:
            del EOF_list[i]
        i = i + 1

i = 0
for SOF in SOF_list:
    subdata=content[SOF:EOF_list[i]]
    carve_filename=str(SOF)+"_"+str(EOF_list[i])+".docx"
    print("Found DOCX starting offset", str(SOF), "End offset", str(EOF_list[i]))
    carve_obj = open(carve_filename, 'wb')
    carve_obj.write(subdata)
    carve_obj.close()
    i = i + 1
    print("carving it to " + carve_filename)
    # calculating sha256
    with open(carve_filename, "rb") as f:
        bytes = f.read()  # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
        print("SHA256:", readable_hash, "\n")
    if i == (len(EOF_list) or len(SOF_list)): #this fixes an error where i can go out of bounds and cause an error.
        break


