import datetime as t
import os

text = input("DIgite um texto para ser salvo : ")

file_path = os.path.abspath("novo_arquivo.txt")
timeNow = str(t.datetime.now())

with open(file_path, "a") as file:
    file.write("Alguem digitou : '"+text+"' na data e hora :"+timeNow+"\n")
