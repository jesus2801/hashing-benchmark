from time import perf_counter
from tabulate import tabulate
from utils import average, hours
from hashing import hash
import charts

LIMIT = 5
plain_text_password = "Hello World"
table_size = 1000000


def run():
  times = {'bcrypt': [], 'hashlib': []}
  for _ in range(LIMIT):
    start = perf_counter()
    hash['bcrypt'](plain_text_password)
    end = perf_counter()
    times['bcrypt'].append(end - start)

    start = perf_counter()
    hash['hashlib'](plain_text_password)
    end = perf_counter()
    times['hashlib'].append(end - start)

  labels = [i for i in range(LIMIT)]
  charts.generate_line_chart('bcrypt-hashlib.line', labels, times['bcrypt'], times['hashlib'])
  charts.generate_line_chart('bcrypt.line', labels, times['bcrypt'])
  charts.generate_line_chart('hashlib.line', labels, times['hashlib'])

  sums = {
      'bcrypt': sum(times['bcrypt']),
      'hashlib': sum(times['hashlib'])
  }

  averages = {
      'bcrypt': average(times['bcrypt']),
      'hashlib': average(times['hashlib'])
  }

  table = [
      ["Average (S)", averages['bcrypt'], averages['hashlib']],
      ["Total Time (S)", sums['bcrypt'], sums['hashlib']],
      ["Ratios", sums['bcrypt'] / sums['hashlib'], sums['hashlib'] / sums['bcrypt']],
      [f"{table_size} Table (H)", hours(averages['bcrypt'] * table_size),
       hours(averages['hashlib'] * table_size)]
  ]
  headers = ["Names", "Bcrypt", "Hashlib"]

  print(tabulate(table, headers=headers, tablefmt="grid"))


if __name__ == '__main__':
  run()
