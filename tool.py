import os, sys
folder = "D:\e-pdf"

for d in os.listdir(folder):
    os.mkdir('D:\e-pdf-another\\'+d)
