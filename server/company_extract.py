nyse_file = "../data/NYSE.txt"
nasdaq_file = "../data/NASDAQ.txt"
amex_file = "../data/AMEX.txt"

class company_finder():
  def __init__(self):
    self.build_data()
  
  def build_data(self):
    # empty list of tickers
    self.tickers = []
    self.names = []
    
    # keys = tickers and company names
    # value = index in the two lists
    
    self.lookup_table = {}
    i = 0
    
    files = [nyse_file, nasdaq_file, amex_file]
    for file in files:
      f = open(file, 'r')
      s = f.read()
      for line in s.split('\n'):
        l = line.split('\t')
        try:
          this_ticker = l[0]
          this_name = l[1].lower()
          
          # some lines in the files are not complete
          assert this_name != ''
          assert this_ticker != ''
        except:
          #print "problem with line", i ,"in file", file, ':', l
          continue
          
        # add it to data
        self.tickers.append(this_ticker)
        self.names.append(this_name)
        self.lookup_table[this_name] = i
        self.lookup_table[this_ticker] = i
        i += 1
      f.close()

  def ticker2name(self, ticker):
    return self.names[self.lookup_table[ticker]]

  def name2ticker(self, name):
    
    # the naive approach
    try:
      return self.tickers[self.lookup_table[name]]
    except:
      pass
    
    desired_name = name.split(' ')
    
    i = 0
    hits = {}
    for _name in self.names:
      this_company = _name.split(' ')
      this_hit_count = 0
      for word in desired_name:
        if word in this_company:
          this_hit_count += 1
      hits[this_hit_count] = i
      i += 1
    if max(hits.keys()) == 0:
      print "ticker", name, "not found"
      raise
    else:
      return self.tickers[hits[max(hits.keys())]]


c = company_finder()

print c.name2ticker('apple')
print c.name2ticker('google')
print c.name2ticker('toyota motor')
print c.name2ticker('honda')
print c.name2ticker('motorola')

print c.name2ticker('bread')
print c.name2ticker('panera')
print c.name2ticker('panera bread')
