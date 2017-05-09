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
cmd = 'md5sum'
input_file = task_dict.get('input').get('file')

try:
    r = subprocess.check_output("%s %s |awk '{print $1}' > %s.md5sum" % (cmd, input_file, input_file), shell=True)
except Exception, e:
    print e
    sys.exit(1)  # task failed

with open("%s.md5sum" % input_file, "r") as f:
    md5sum = f.read().strip()

file_size = os.path.getsize(input_file)

# complete the task

task_stop = int(time.time())

output_json = {
    'file_md5sum': md5sum,
    'file_size': file_size,
    'runtime': {
        'task_start': task_start,
        'task_stop': task_stop
    }
}

save_output_json(output_json)
