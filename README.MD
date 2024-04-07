 Made this for my dear wife. We shoot a lot of photos, and we often have to look at our photos on our computer and delete the ones that are not good for anything.
 
 Here's the problem: when we shoot photos, we shoot JPG+RAW; when we look, we only look at JPGs. So after deleting a bunch of JPG files. We're still left with a bunch of useless RAW files in the same folder. We often have to sort by filename and look for RAW files without a pairing JPG file.
 
 
 As we take more photos, this task is becoming increasingly tedious. I thought of a simple solution of writing a Python script to do this for us. It scans a folder, look for raw files without corresponding and delete them 
 
 For example:
 
 You have a folder with 6 files. The folder contains sets of files such as:
 
-  A0001.JPG
-  A0001.ARW
-  A0002.JPG
-  A0002.ARW
-  A0003.ARW
-  A0004.ARW
 
 This program will scan for JPG and supported raw files(current ARW and CR2) and move the raw/jpg files without an accompanying raw/jpg to another folder. In the example above, A0003.ARW and A0004.ARW will be moved to a subfolder for user to review.
