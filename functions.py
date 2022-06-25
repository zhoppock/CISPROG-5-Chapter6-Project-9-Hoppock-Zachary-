def average(filename):
  total = 0
  count = 0
  with open(filename, 'r') as f:
    for line in f:
      for num in line.strip().split():
        total += float(num)
        count += 1
  print('\nThe average is ' + str(total / count))

def main():
  filename = input('Enter the input file name: ')
  average(filename)