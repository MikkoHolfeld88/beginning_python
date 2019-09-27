from urllib.request import urlopen

with urlopen('https://www.google.de') as fh:
    for line in fh:
        line = line.decode('utf-8').rstrip()
        print(line)
