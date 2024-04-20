from time import perf_counter
from tabulate import tabulate
from utils import average, hours
from hashing import hash
import charts

# global variables
LIMIT = 5  # number of tests
plain_text_password = "Hello World"  # plain text to be used
table_size = 1000000  # get the statistics for a force-brute attack with a table


def run():
  times = {'bcrypt': [], 'hashlib': []}  # times
  for _ in range(LIMIT):
    # measure the performance of Bcrypt
    start = perf_counter()
    hash['bcrypt'](plain_text_password)
    end = perf_counter()
    times['bcrypt'].append(end - start)

    # measure the performance of Hashlib
    start = perf_counter()
    hash['hashlib'](plain_text_password)
    end = perf_counter()
    times['hashlib'].append(end - start)

  # labels for graphs
  labels = [i for i in range(LIMIT)]
  # creates the graphs
  charts.generate_line_chart('bcrypt-hashlib.line', labels, times['bcrypt'], times['hashlib'])
  charts.generate_line_chart('bcrypt.line', labels, times['bcrypt'])
  charts.generate_line_chart('hashlib.line', labels, times['hashlib'])

  sums = {  # sums of bcrypt and hashlib
      'bcrypt': sum(times['bcrypt']),
      'hashlib': sum(times['hashlib'])
  }

  averages = {  # averages of bcrypt and hashlib
      'bcrypt': average(times['bcrypt']),
      'hashlib': average(times['hashlib'])
  }

  table = [
      ["Average (S)", averages['bcrypt'], averages['hashlib']],  # averages
      ["Total Time (S)", sums['bcrypt'], sums['hashlib']],  # total times
      ["Ratios", sums['bcrypt'] / sums['hashlib'], sums['hashlib'] / sums['bcrypt']],  # ratios
      [f"{table_size} Table (H)", hours(averages['bcrypt'] * table_size),
       hours(averages['hashlib'] * table_size)]
  ]
  headers = ["Names", "Bcrypt", "Hashlib"]  # headers of the table
  print(tabulate(table, headers=headers, tablefmt="grid"))  # prints the table with grid layout


if __name__ == '__main__':
  run()
