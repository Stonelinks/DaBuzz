import string

nyse_file = "../data/NYSE.txt"
nasdaq_file = "../data/NASDAQ.txt"
amex_file = "../data/AMEX.txt"

class company_finder():
  def __init__(self):
    self.build_data()
  
  def build_data(self):
    
    # empty list of tickers
    self.tickers = []
    self.tickers_no_punct = []
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
          this_ticker_no_punct = ''.join(ch for ch in this_ticker if ch not in set(string.punctuation))
          this_name = l[1].lower()
          
          # some lines in the files are not complete
          assert this_name != ''
          assert this_ticker != ''
        except:
          #print "problem with line", i ,"in file", file, ':', l
          continue
          
        # add it to data
        self.tickers.append(this_ticker)
        self.tickers_no_punct.append(this_ticker_no_punct)
        self.names.append(this_name)
        self.lookup_table[this_name] = i
        self.lookup_table[this_ticker] = i
        self.lookup_table[this_ticker_no_punct] = i
        i += 1
      f.close()

  def ticker2name(self, ticker):
    return self.names[self.lookup_table[ticker]]

  def is_ticker(self, ticker):
    if len(ticker) >= 5:
      return False
    elif ticker in self.lookup_table.keys():
      return True
    else:
      return False
  
  def is_name(self, name):
    if name in self.lookup_table.keys():
      return True
    else:
      return False
  
  def name2ticker(self, name):
    # the naive approach
    if name in self.lookup_table:
      return self.tickers[self.lookup_table[name]]
    
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
      #print "ticker", name, "not found"
      return False
    else:
      return self.tickers[hits[max(hits.keys())]]

def tickers_from_text(text):
  wordlist = text.split(' ')
  search_list = []
  depth = 3
  for i in range(1, depth + 1):
    for j in range(len(wordlist)):
      tmp = []
      for k in range(j, j + i):
        if k < len(wordlist):
          tmp.append(wordlist[k])
      search_string = ' '.join(tmp).replace('\n', ' ').strip()
      search_list.append(search_string)

  hits = {}
  c = company_finder()

  for term in search_list:
    # treat the term as a ticker first
    ticker1 = string.upper(term)
    if c.is_ticker(ticker1):
      try:
        hits[ticker1] += 1
      except:
        hits[ticker1] = 1
    
    # treat the term as a company name second
    ticker2 = c.name2ticker(term)
    if ticker2:
      try:
        hits[ticker2] += 1
      except:
        hits[ticker2] = 1

  output = []
  for ticker, hit in reversed(sorted(hits.items(), key=lambda x: x[1])):
    output.append((hit, ticker))

  return output[0]

