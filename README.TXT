12-2-2021 copyright Jason Alexander and Jennifer Johnson
Project 2 COMP 6350
Professor Jason Cuneo
Auburn University


Please ensure the file is called 'Project2.dd'

Please ensure that all the python files and the project file are in the same directory.

After running the main.py, it will recover all the files it finds into the same directory.
    Please note that some files found didn't open correctly on the linux machine, but opened perfectly when having Microsoft office
    or VLC player installed. The files are recovered in a working format, but you need to ensure you are opening it with the correct program.

This code was written and translated for execution using Pycharm community edition on a Sift workstation (Ubuntu)

Several websites were used to help develop this code and included in the written report.

This software is under the FOSS and under the GNU GPl licensing, basically use it if it works for you but don't charge anyone for its use.

Sources used:
(1)https://www.jefflawler.net/post/hunting-for-file-signatures
(2)https://www.thehexninja.com/2018/01/practical-exercise-image-carving-ii.html
    This second source was instrumental in helping me understand python usage to figure out one part of the puzzle but
    it doesn't include various checks(SHA256) or inbounds/out-of-bounds for specific files and
    other requirements that are needed for this project.


Expected output:

/home/sansforensics/PycharmProjects/Forensics/venv/bin/python /home/sansforensics/PycharmProjects/Forensics/main.py
Found an avi and carving it to 245760_537264139.avi
SHA256: 2f8011429d5062e8d8a7f16a9ed3e1065edd962d0b40474601e55c28f372fe65

Found an avi and carving it to 37908480_1816640197.avi
SHA256: 86fe0ef4a232a0b4bf865d6cca95bcea8c0992e7f194a1a3bbdf354ca3ec4a17

Found an bmp and carving it to 3162112031699062.bmp
SHA256: e03847846808d152d5ecbc9e4477eee28d92e4930a5c0db4bffda4d9b7a27dfc

Found DOCX starting offset 47820800 End offset 47957409
carving it to 47820800_47957409.docx
SHA256: 8ea570f638b4c727cdb905dd1f6554e9a948662a8e4a01cb1b695af1c0d739d9

Found GIF starting offset 34922496 End offset 37575139
carving it to 34922496_37575139.gif
SHA256: c3c82461c8d7cd3974a82967d5c6cf18449e1b373c8123b01508be277df725e4

Found GIF starting offset 37576704 End offset 37904876
carving it to 37576704_37904876.gif
SHA256: 8869dd5fcb077005be3195028db6fe58938c4ec2786a5ff7e818d2f5411ded52

Found JPG starting offset 229376 End offset 241747
carving it to 229376_241747.jpg
SHA256: 59e0ec78f30c50db44d24a413ca1cccbd7ef5910cad4d3cf0e4753095725ec94

Found JPG starting offset 34897920 End offset 34920237
carving it to 34897920_34920237.jpg
SHA256: bde9e54f4e1ec3b6ab8d439aa64eef33216880685f8a4621100533397d114bf9

Found MPG starting offset 37914214 End offset 50002088
carving it to 37914214_50002088.mpg
SHA256: 3429f283b3a24f7256e2a767a6d6ad454fe37ba61db0424ed49d122b83bd1d29

Found PDF starting offset 29233152 End offset 31294609
carving it to 2923315231294609.pdf
SHA256: b52d27f414edf27872139ce52729c139530a27803b69ba01eec3ea07c55d7366

Found PDF starting offset 31703040 End offset 34897020
carving it to 3170304034897020.pdf
SHA256: 9ef248560dc49384c0ec666db6a7b4320bfec74e62baed1c610a765f056fd3b7

Found PNG starting offset 31297536 End offset 31525491
carving it to 31297536_31525491.png
SHA256: c9ac5048fb37dc0a95f844e190507f7d145d869a0ccbe9d222eb7f5d1365efc2

Found PNG starting offset 47824425 End offset 47948420
carving it to 47824425_47948420.png
SHA256: 36d2109322f9da9cd0f56d2d56987f778692fad9b91a13617a141a65ce32550f


Process finished with exit code 0