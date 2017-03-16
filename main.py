from __future__ import with_statement
import contextlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import sys

def make_tiny(url):
    request_url = ( 'http://tinyurl.com/api-create.php?' + urlencode({'url': url}) )
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

def main():
    print("-------------URLShortener.py-------------\n")

    if len(sys.argv) < 2:
        while True:
            url = input("Enter URL: ")
            if (url == "") or (url == "q") or (url == "quit") or (url == "exit"):
                break
            else:
                print("\nResult: "),
                print(make_tiny(url))
    else:
        num = 1
        for tinyurl in map(make_tiny, sys.argv[1:]):
            print(num, tinyurl)
            num += 1

    print("\n-----------------------------------------")

if __name__ == '__main__':
    main()
