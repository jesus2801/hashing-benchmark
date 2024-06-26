import matplotlib.pyplot as plt
from os.path import exists
from os import mkdir


def generate_line_chart(name, labels, values1, *args):  # generates line chart
  if (not exists("./docs")):
    mkdir("./docs")

  fig, ax = plt.subplots()
  ax.plot(labels, values1, marker='o', linestyle='-')
  if (len(args) > 0):
    ax.plot(labels, args[0], marker='s',
            linestyle='--', label='Conjunto 2')
  plt.savefig(f'./docs/{name}.png')
  plt.close()
