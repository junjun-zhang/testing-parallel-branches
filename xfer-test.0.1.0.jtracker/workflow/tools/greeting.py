#!/usr/bin/env python

import os
import sys
import json
import time
import subprocess
from random import randint
from utils import get_task_dict, save_output_json

task_dict = get_task_dict(sys.argv[1])
cwd = os.getcwd()

task_start = int(time.time())

# do the real work here

cmd = 'hello_world'
arg = task_dict.get('input').get('who_are_you')

try:
    r = subprocess.check_output("%s %s" % (cmd, arg), shell=True)
except Exception, e:
    sys.exit(1)  # task failed

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if f.startswith('hello_'):
        greeting_file_name = f
        break

# complete the task

task_stop = int(time.time())

output_json = {
    'greeting_file': os.path.join(cwd, greeting_file_name),
    'runtime': {
        'task_start': task_start,
        'task_stop': task_stop
    }
}

save_output_json(output_json)
