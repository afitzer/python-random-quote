import random

def primary():
  p = open("quotes.txt")
  quotes = p.readlines()
  p.close()
  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
