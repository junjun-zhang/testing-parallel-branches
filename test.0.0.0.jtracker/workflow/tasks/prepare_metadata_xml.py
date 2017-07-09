#!/usr/bin/env python

import sys
import json
import time
from utils import get_task_dict, save_output_json

task_dict = get_task_dict(sys.argv[1])

task_start = int(time.time())

# do the real work here



# complete the task

task_stop = int(time.time())

output_json = {
    'task_start': task_start,
    'task_stop': task_stop
}

save_output_json(output_json)

