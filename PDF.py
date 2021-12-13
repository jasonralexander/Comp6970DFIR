'''12-2-2021 copyright Jason Alexander and Jennifer Johnson
Project 2 COMP 6350
Professor Jason Cuneo
Auburn University
'''

import re
import hashlib

dd_file = 'Project2.dd'
#opening file and write as a python object
with open(dd_file, "rb") as f:
    content = f.read()
    f.close()

#signatures
PDF_SOF = b'\x25\x50\x44\x46'
PDF_EOF = b'\x0A\x25\x25\x45\x4F\x46'
#creating a list of matches for Start of file signature so further work can be done to deduce if its an actual file
SOF_list = [match.start() for match in re.finditer(re.escape(PDF_SOF), content)]
EOF_list = [match.start() for match in re.finditer(re.escape(PDF_EOF), content)]

'''This code validates that the start of a file should be less than the end of a file. EG: a file can't start at byte 100
and end at byte 98 that would be impossible. It also validates if there are more objects in the SOF list than the EOF 
list it will delete the extra false positive start of file signatures in the list'''

header_count = len(SOF_list)
footer_count = len(EOF_list)

#if no files found exit
if header_count == 0:
    exit()

for index in range(header_count):

    file_start = int(SOF_list[index])

    if index == (header_count - 1):
        # the number of bytes in the footer are added to the file
        # to carve until the end of the footer
        file_end = int(EOF_list[footer_count - 1]) + 6
    else:
        footer_iterator = 0
        while EOF_list[footer_iterator] < SOF_list[index + 1]:
            footer_iterator += 1
        file_end = int(EOF_list[footer_iterator - 1]) + 6

    if index == 0:
        file_end += 2
    else:
        file_end += 1
#file carve
    subdata = content[file_start:file_end]
    carve_filename=str(file_start)+""+str(file_end)+".pdf"
    print("Found PDF starting offset", str(file_start),"End offset",str(file_end))
    carve_obj = open(carve_filename, 'wb')
    carve_obj.write(subdata)
    carve_obj.close()
    print("carving it to " + carve_filename)
#calculate sha256
    with open(carve_filename, "rb") as f:
        bytes = f.read()  # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
        print("SHA256:",readable_hash,"\n")