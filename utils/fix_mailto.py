import os

from bs4 import BeautifulSoup
PARSER = 'html.parser'

def fix_mailto(filename):
    with open(filename, "r+") as html_file:
        soup = BeautifulSoup(html_file, PARSER)
        try:
            soup.find(id='footer').find('a').attrs['href'] = 'mailto:webadmin@pistrang.com'
        except AttributeError:
            print(filename)
            html = soup.prettify(soup.original_encoding)
        else:
            html = soup.prettify(soup.original_encoding)

    with open(filename, "wb") as html_file:
        html_file.write(html)


rootDir = '/Users/michaelpistrang/Desktop/pistrang.com/www.pistrang.com'
for dirname, subdirlist, filelist in os.walk(rootDir):
    for filename in filelist:
        if filename.endswith('.html'):
            full_path = os.path.join(dirname, filename)
            fix_mailto(full_path)

