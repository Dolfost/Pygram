import matplotlib.pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import sys

version = "1.1"

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", "--file", type = str, help = "Input datafile", required = True)
# parser.add_argument("-h", "--help", type = bool, help = "Print this message")
parser.add_argument("-v", "--version", action = "version", version = version, help = "Print version")
parser.add_argument("-x", "--xname", default = "X-axis", type = str, help = "Name of the x axis")
parser.add_argument("-y", "--yname", default = "Y-axis", type = str, help = "Name of the y axis")
parser.add_argument("-w", "--width", default = 0.6, type = float, help = "Width of diagram bars")
parser.add_argument("-r", "--rotation", default = "horizontal", type = str, choices = ["vertical", "horizontal"], help = "Diagram bars names rotation")
parser.add_argument("-t", "--title", default = "Pygram diagram", type = str, help = "Diagram title")
parser.add_argument("-c", "--color", default = "#0772f5", type = str, help = "Diagram bars color")
parser.add_argument("-o", "--outline", default = "black", type = str, help = "Diagram bars outline color")

args = parser.parse_args()

data = {}
with open(args.file) as file:
    data = dict(line.strip().split(" ") for line in file)

for idx, var in data.items():
    data[idx] = float(var)

print("Data, extracted from", args.file, ":\n", data)


plt.figure(num = 'Pygram ' + version)
plt.ylabel(args.yname)
plt.xlabel(args.xname)

plt.xticks(rotation = args.rotation)

plt.bar(range(len(data)), list(data.values()) , tick_label = list(data.keys()), color = args.color, edgecolor = args.outline, width = args.width)
plt.title(args.title, color = "#f09f0a", loc = "left", fontstyle = "italic")
plt.show()
