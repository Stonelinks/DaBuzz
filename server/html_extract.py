import urllib2
import htmllib
import formatter
import StringIO
import string

# from tutorial at http://ai-depot.com/articles/the-easy-way-to-extract-useful-text-from-arbitrary-html/

#Remove the garbage so htmllib can read it
def preprocess_page(html):
  start = html.find("<body>")
  end = html.find("</body>")
  return html[start:end+7]

def extract_text(html):
  # Derive from formatter.AbstractWriter to store paragraphs.
  writer = LineWriter()
  # Default formatter sends commands to our writer.
  format = formatter.AbstractFormatter(writer)
  # Derive from htmllib.HTMLParser to track parsed bytes.
  parser = TrackingParser(writer, format)
  # Give the parser the raw HTML data.
  parser.feed(html)
  parser.close()
  # Filter the paragraphs stored and output them.
  return writer.output()
  
class TrackingParser(htmllib.HTMLParser):
  """Try to keep accurate pointer of parsing location."""
  def __init__(self, writer, *args):
    htmllib.HTMLParser.__init__(self, *args)
    self.writer = writer
  def parse_starttag(self, i):
    index = htmllib.HTMLParser.parse_starttag(self, i)
    self.writer.index = index
    return index
  def parse_endtag(self, i):
    self.writer.index = i
    return htmllib.HTMLParser.parse_endtag(self, i)

class Paragraph:
  def __init__(self):
    self.text = ''
    self.bytes = 0
    self.density = 0.0
 
class LineWriter(formatter.AbstractWriter):
  def __init__(self, *args):
    #Was crashing. Added line. Crashing stopped.
    #Possibly broken in subtle way now, maybe not.
    self.index = 0
    self.last_index = 0
    self.lines = [Paragraph()]
    formatter.AbstractWriter.__init__(self)
 
  def send_flowing_data(self, data):
    # Work out the length of this text chunk.
    t = len(data)
    # We've parsed more text, so increment index.
    self.index += t
    # Calculate the number of bytes since last time.
    b = self.index - self.last_index
    self.last_index = self.index
    # Accumulate this information in current line.
    l = self.lines[-1]
    l.text += data
    l.bytes += b
 
  def send_paragraph(self, blankline):
    """Create a new paragraph if necessary."""
    if self.lines[-1].text == '':
      return
    self.lines[-1].text += '\n' * (blankline + 1)
    self.lines[-1].bytes += 2 * (blankline + 1)
    self.lines.append(Paragraph())
 
  def send_literal_data(self, data):
    self.send_flowing_data(data)
 
  def send_line_break(self):
    self.send_paragraph(0)
    
  def compute_density(self):
    """Calculate the density for each line, and the average."""
    total = 0.0
    for l in self.lines:
      l.density = len(l.text) / (float(l.bytes) + .000001)
      total += l.density
    # Store for optional use by the neural network.
    self.average = total / float(len(self.lines))
 
  def output(self):
    """Return a string with the useless lines filtered out."""
    self.compute_density()
    output = ''
    for l in self.lines:
      #print l.text,l.density
      
      # Check density against threshold.
      # Custom filter extensions go here.
      try:
        # its HTML, we don't care about it
        if l.text[0] == '>':
          continue
          
        # it doesn't end with a period, so its not a sentence, so we don't care about it
        if l.text[-2] != '.':
          continue
        
      except:
        pass
        
      if l.density > 0.5:
        output += l.text

      """
      if l.density > 0.5:
        # "bag of words"
        t = l.text.replace('\n', ' ').replace('-', ' ')
        exclude = set(string.punctuation)
        t = ''.join(ch for ch in t if ch not in exclude)
        include = set(str(string.ascii_letters + ' ' + string.digits))
        t = ''.join(ch for ch in t if ch in include)
        s = ''
        for w in t.split(' '):
          if w == '':
            continue
          else:
            s += w.lower() + ' '
        output += s
      """
    return output

def text_from_url(url):
  response = urllib2.urlopen(str(url))
  html = response.read()
  html = preprocess_page(html)
  return extract_text(html)

if __name__ == "__main__":
  response = urllib2.urlopen("http://www.google.com/racing")
  html = response.read()
  html = preprocess_page(html)
  # Derive from formatter.AbstractWriter to store paragraphs.
  writer = LineWriter()
  # Default formatter sends commands to our writer.
  format = formatter.AbstractFormatter(writer)
  # Derive from htmllib.HTMLParser to track parsed bytes.
  parser = TrackingParser(writer, format)
  # Give the parser the raw HTML data.
  parser.feed(html)
  parser.close()
  # Filter the paragraphs stored and output them.
  print repr(writer.output())