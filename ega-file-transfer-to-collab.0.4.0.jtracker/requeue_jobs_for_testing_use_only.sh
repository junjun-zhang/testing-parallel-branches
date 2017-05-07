#!/bin/bash

git pull && git mv job_state.*/job.*/job.*.json job_state.queued/ && git rm -r job_state.*/job.*/ && git commit -m 'requeue' && git push
