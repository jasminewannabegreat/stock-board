#!/bin/bash
service redis_6379 start
service mongod start

pip install -r requirements.txt

nohup npm start >/dev/null 2>&1 

cd stocks_pipeline
python stocks_monitor.py

echo "=================================================="
read -p "PRESS [ANY KEY] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)