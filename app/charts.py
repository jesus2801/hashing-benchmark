import matplotlib.pyplot as plt


def generate_line_chart(name, labels, values1, *args):
  fig, ax = plt.subplots()
  ax.plot(labels, values1, marker='o', linestyle='-')
  if (len(args) > 0):
    ax.plot(labels, args[0], marker='s',
            linestyle='--', label='Conjunto 2')
  plt.savefig(f'./docs/{name}.png')
  plt.close()


def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('./docs/pie.png')
  plt.close()
