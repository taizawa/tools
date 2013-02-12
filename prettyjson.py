# coding: utf-8
import sys
import json

s = ''
f = None

argvs = sys.argv
argc = len(argvs)

if (argc < 2):
	print 'Not enough arguements (useage: $python prettyjson.py [example.json|\'{"example": "example"}\'])'
	quit()

try:
	f = open(argvs[1])
	s = f.read()
	f.close()
except Exception as e:
	s = argvs[1]
try:
	s = json.loads(s.replace('\r\n', '\\r\\n'))
	print(json.dumps(s, sort_keys = False, indent = 4))
except Exception as e:
	print e
