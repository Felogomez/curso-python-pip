import matplotlib.pyplot as ptl

def generate_bar_chart(name, labels, values):
  fig, ax = ptl.subplots()
  ax.bar(labels, values)
  ptl.savefig(f'./imgs/{name}.png')
  ptl.close()

def generate_pie_chart(labels, values):
  fig, ax = ptl.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  ptl.savefig('pie.png')
  ptl.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)