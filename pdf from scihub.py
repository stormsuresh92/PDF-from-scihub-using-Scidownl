from scidownl.scihub import *
from time import sleep

input = open("input.txt", "r")
read = input.readlines()
output = 'PDFs'
for r in read:

    try:
        SciHub(r.strip(), output).download(choose_scihub_url_index=1)
        time.sleep(3)

    except:
        pass
