#!/bin/bash

git pull && git mv job_state.completed/job.*/job.*.json job_state.queued/ && git rm -r job_state.completed/job.*/ && git commit -m 'requeue completed jobs for testing' && git push

git pull && git mv job_state.failed/job.*/job.*.json job_state.queued/ && git rm -r job_state.failed/job.*/ && git commit -m 'requeue failed jobs for testing' && git push
