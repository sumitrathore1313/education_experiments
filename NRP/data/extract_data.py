from bs4 import BeautifulSoup
import re
import pandas as pd
from tqdm import tqdm

file = "/home/sumit/PycharmProjects/education_experiments/NRP/output.html"

# l = " 1  2001000002 KISHOR BHATT                             9              2   2     1   1       60.00"
pattern = re.compile("^[0-9 ]+ *[0-9a-zA-Z .]*$")

# print(pattern.match(l))

def cleanhtml(raw_html):
  cleanr = re.compile('[0-9]*')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

f = open(file, "r")
lines = f.readlines()
f.close()

dataset = []

for line in tqdm(lines):
    line = BeautifulSoup(line, "lxml").text
    words = line.split()
    if pattern.match(line) and len(words) > 5:
        temp = []
        temp.append(words[0])
        temp.append(words[1])
        temp.append(cleanhtml(" ".join(words)).strip())
        temp.append(words[-5])
        temp.append(words[-4])
        temp.append(words[-3])
        temp.append(words[-2])
        temp.append(words[-1])
        dataset.append(temp)

dataset = pd.DataFrame(dataset, columns=["id", "roll_no", "name", "jso", "eqjso", "aao", "eqaao", "marks"])

import sqlite3

conn = sqlite3.connect('/home/sumit/PycharmProjects/education_experiments/NRP/data/ssc')

dataset.to_csv("data.csv")

dataset.to_sql("question",conn, if_exists="replace")