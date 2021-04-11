import csv
import re
import pandas as pd
import time
import tracemalloc
list3=[[],[],[]]
#To write the performance into performance.txt file
def writePerfomance(start):
    p=open("Performance.txt","w")
    p.write("Time to process:" + str(time.time() - start) + " " + "seconds")
    p.write("Memory used: "+'{:,.0f}'.format(tracemalloc.get_tracemalloc_memory() / float(1 << 20)) + " MB"+"\n")
#The english words are replaced with french words
def change():
    reader = csv.reader(open('french_dictionary.csv', 'r'))
    d = {}
    for row in reader:
        i, j = row
        d[i] = j
    fin = open("t8.shakespeare.translated.txt", "wt")
    with open("t8.shakespeare.txt") as p:
        start_time = time.time()
        tracemalloc.start()
        for line in p:
            list2=[]
            for words in line.split():
                if str("".join(re.findall("[a-zA-Z]+", words))) in d.keys():
                    list2.append(d[str("".join(re.findall("[a-zA-Z]+", words)))])
                    list3[0].append(str("".join(re.findall("[a-zA-Z]+", words))))
                    list3[1].append(d[str("".join(re.findall("[a-zA-Z]+", words)))])
                    list3[2].append(0)
                else:
                    list2.append(words)
            fin.write(" ".join(list2))
    print(sorted(list(set(list3[0]))))
    print("Memory used: ", '{:,.0f}'.format(tracemalloc.get_tracemalloc_memory() / float(1 << 20)) + " MB")
    print("Time to process:", time.time() - start_time, "seconds")
    print("Translation done!")
    writePerfomance(start_time)
change()
df = pd.DataFrame({'English word': list3[0], 'French word': list3[1],'Frequency count':list3[2]})
df=(df.groupby(['English word','French word'])['Frequency count'].count()).drop_duplicates()
df.to_csv('Frequency.csv') #Writing to Frequency.csv file







