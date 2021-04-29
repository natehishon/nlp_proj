import re
import csv
import os

def getTextOutput(input):

    result = re.sub(r'[^\sa-zA-Z0-9]', '', input).lower().strip()
    array = result.split()
    document_path = os.getcwd() + "/app/data/test4.csv"
    reader = csv.reader(open(document_path))

    # words = {}
    #
    # max = 0
    # min = 1
    # for row in reader:
    #     key = row[0]
    #     if float(row[1]) > max:
    #         max = float(row[1])
    #     if float(row[1]) < min:
    #         min = float(row[1])
    #     if key in words:
    #         # implement your duplicate row handling here
    #         pass
    #     words[key] = row[1:]
    #
    # max = 0.018432689633471715
    # min = .000005665758205534548
    #
    # ab = abs(max - min) / 10
    #
    # ranges = []
    # for i in range(1, 11):
    #     ranges.append(min + ab * i)


    # sort = sorted(words.items(), key=lambda kv: kv[1], reverse=True)

    words = {}

    for row in reader:
        key = row[0]

        if key in words:
            pass
        x = float((row[1:][0]))
        x = round(x, 6)

        words[key] = "{:.8f}".format(x)

    sort = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))

    keys = list(sort.keys())

    first = (keys[0:1000])
    second = (keys[1000:2000])
    third = (keys[2000:3000])
    fourth = (keys[3000:4000])
    fifth = (keys[4000:5000])
    sixth = (keys[5000:6000])
    seventh = (keys[6000:7000])
    eighth = (keys[7000:8000])
    ninth = (keys[8000:9000])
    tenth = (keys[9000:30350])

    # try percents

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
    colors[10] = "#00000"

    output = []
    #
    for word in array:
        try:
            if word in first:
                output.append("<span style=\"background-color:" + colors[7] + "; " + "color:white" + "\">" + word + "</span>")
            elif word in second:
                output.append("<span style=\"background-color:" + colors[6] + "; " + "color:white" + "\">" + word + "</span>")
            elif word in third:
                output.append("<span style=\"background-color:" + colors[5] + "; " + "color:white" + "\">" + word + "</span>")
            elif word in fourth:
                output.append("<span style=\"background-color:" + colors[4] + "; " + "color:white" + "\">" + word + "</span>")
            elif word in fifth:
                output.append("<span style=\"background-color:" + colors[3] + "; " + "color:white" + "\">" + word + "</span>")
            elif word in sixth:
                output.append("<span style=\"background-color:" + colors[2] + "\">" + word + "</span>")
            elif word in seventh:
                output.append("<span style=\"background-color:" + colors[1] + "\">" + word + "</span>")
            elif word in eighth:
                output.append("<span style=\"background-color:" + colors[1] + "\">" + word + "</span>")
            elif word in ninth:
                output.append("<span style=\"background-color:" + colors[1] + "\">" + word + "</span>")
            elif word in tenth:
                output.append("<span style=\"background-color:" + colors[0] + "\">" + word + "</span>")
            else:
                output.append("<span style=\"background-color:" + colors[0] + "\">" + word + "</span>")
        except:
            print("Not Found")



    return " ".join(output)


