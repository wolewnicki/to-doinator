import re

def parse_csv(csv):
    return re.sub(r',\s*', ',', csv).split(',')