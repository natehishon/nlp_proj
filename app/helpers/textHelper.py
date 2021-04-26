import re
import csv
import os

def getTextOutput(input):

    result = re.sub(r'[^\sa-zA-Z0-9]', '', input).lower().strip()
    array = result.split()
    document_path = os.getcwd() + "/app/data/test.csv"
    reader = csv.reader(open(document_path))

    words = {}

    max = 0
    min = 1
    for row in reader:
        key = row[0]
        if float(row[1]) > max:
            max = float(row[1])
        if float(row[1]) < min:
            min = float(row[1])
        if key in words:
            # implement your duplicate row handling here
            pass
        words[key] = row[1:]

    max = 0.018432689633471715
    min = .000005665758205534548

    ab = abs(max - min) / 10

    ranges = []
    for i in range(1, 11):
        ranges.append(min + ab * i)


    colors = dict()
    colors[0] = "#ffffff"
    colors[1] = "#CCE5FF"
    colors[2] = "#99CCFF"
    colors[3] = "#66B2FF"
    colors[4] = "#3399FF"
    colors[5] = "#0080FF"
    colors[6] = "#0066CC"
    colors[7] = "#004C99"
    colors[8] = "#003366"
    colors[9] = "#001933"
    colors[10] = "#000000"

    output = []
    #
    for word in array:
        try:
            if float(words[word][0]) < ranges[0]:
                output.append("<span style=\"background-color:" + colors[0] + "\">" + word + "</span>")
            elif float(words[word][0]) < ranges[1]:
                output.append("<span style=\"background-color:" + colors[1] + "\">" + word + "</span>")
            elif float(words[word][0]) < ranges[2]:
                output.append("<span style=\"background-color:" + colors[2] + "\">" + word + "</span>")
            elif float(words[word][0]) < ranges[3]:
                output.append("<span style=\"background-color:" + colors[3] + "\">" + word + "</span>")
            elif float(words[word][0]) < ranges[4]:
                output.append("<span style=\"background-color:" + colors[4] + "\">" + word + "</span>")
            elif float(words[word][0]) < ranges[5]:
                output.append("<span style=\"background-color:" + colors[5] + "\">" + word + "</span>")
            elif float(words[word][0]) < ranges[6]:
                output.append("<span style=\"background-color:" + colors[6] + "\">" + word + "</span>")
            elif float(words[word][0]) < ranges[7]:
                output.append("<span style=\"background-color:" + colors[7] + "\">" + word + "</span>")
            elif float(words[word][0]) < ranges[8]:
                output.append("<span style=\"background-color:" + colors[8] + "\">" + word + "</span>")
            elif float(words[word][0]) < ranges[9]:
                output.append("<span style=\"background-color:" + colors[9] + "\">" + word + "</span>")
            else:
                output.append("<span style=\"background-color:" + colors[10] + "\">" + word + "</span>")
        except:
            print("Not Found")



    return " ".join(output)


