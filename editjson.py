#! python3

import json
import re

with open('strudel.json', mode='r+') as f:
    d = json.load(f)
    things = []
    for key in d:
        for val in d[key]:
            # print(val)
            if val.endswith('A#0.wav'):
                things.append(key)
    for key in things:
      # print(key)
      construct = {}

      for x in d[key]:
         construct[x[x.rfind('/')+1:x.rfind('.')]] = x

      d[key] = construct

    f.seek(0)
    json.dump(d, f)
    f.truncate()
