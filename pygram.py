import matplotlib.pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import sys

version = "1.2"

parser = ArgumentParser(formatter_class = ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", "--file", type = str, help = "Input datafile", required = True)
# parser.add_argument("-h", "--help", type = bool, help = "Print this message")
parser.add_argument("-v", "--version", action = "version", version = version, help = "Print version")
parser.add_argument("-x", "--xname", default = "X-axis", type = str, help = "Name of the x axis")
parser.add_argument("-y", "--yname", default = "Y-axis", type = str, help = "Name of the y axis")
parser.add_argument("-w", "--width", default = 0.6, type = float, help = "Width of diagram bars")
parser.add_argument("-r", "--rotation", default = 0, type = float, help = "Diagram bars names rotation in degreees")
parser.add_argument("-t", "--title", default = "Pygram diagram", type = str, help = "Diagram title")
parser.add_argument("-l", "--label", action = "store_true", help = "Show bar value at its top")
parser.add_argument("-c", "--color", default = "#0772f5", type = str, help = "Diagram bars color")
parser.add_argument("-o", "--outline", default = "black", type = str, help = "Diagram bars outline color")

args = parser.parse_args()

data = {}
with open(args.file) as file:
    data = dict(line.strip().split(" ") for line in file)

for idx, var in data.items():
    data[idx] = float(var)

print("Data, extracted from", args.file, ":\n", data)
fig, ax = plt.subplots(figsize = (16,9), dpi = 96)
# plt.figure(num = 'Pygram ' + version) # TODO make it work


plt.title(args.title, color = "#f09f0a", loc = "left", fontstyle = "italic")

ax.grid(which = "major", axis = 'both', color = '#DAD8D7', alpha = 0.5, zorder = 0)
bar1 = ax.bar(range(len(data)), list(data.values()) , tick_label = list(data.keys()), color = args.color, edgecolor = args.outline, width = args.width, zorder = 3)
# x-axis
ax.set_xlabel(args.xname, fontsize = 12, labelpad = 10)
ax.xaxis.set_label_position("bottom")
ax.xaxis.set_tick_params(pad = 2, labelbottom = True, bottom = True, labelsize = 12, rotation = args.rotation)

# y-axis
ax.set_ylabel(args.yname, fontsize = 12, labelpad = 10)
ax.yaxis.set_label_position("left")
ax.yaxis.set_tick_params(pad = 2, labeltop = False, labelbottom = True, bottom = False, labelsize = 12)

if args.label:
    ax.bar_label(bar1, labels = list(data.values()), padding = 3, color = 'black', fontsize = 8) 


plt.show()
