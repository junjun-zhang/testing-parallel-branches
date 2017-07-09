#!/usr/bin/env python

import sys
import json
import time
from random import randint
from utils import get_task_dict, save_output_json

task_dict = get_task_dict(sys.argv[1])

task_start = int(time.time())

# do the real work here
time.sleep(randint(1,10))


# complete the task

task_stop = int(time.time())

output_json = {
    'file': '/path/to/downloaded/file.bam',
    'ega_file_id': 'EGAFxxxx',
    'file_name': 'file.bam',
    'object_id': 'xxxxx',
    'file_size': 32322,
    'file_md5sum': 'yyyyy',
    'runtime': {
        'task_start': task_start,
        'task_stop': task_stop
    }
}

save_output_json(output_json)
