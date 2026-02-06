#! python3

import json
import re

with open('strudel.json', mode='r+') as f:
    d = json.load(f)
    print(d['bsrb2'])
    construct = {}

    for x in d['bsrb2']:
       construct[x[x.rfind('/')+1:x.rfind('.')]] = x
   
    d['bsrb2'] = construct
    f.seek(0)
    json.dump(d, f)
    f.truncate()
