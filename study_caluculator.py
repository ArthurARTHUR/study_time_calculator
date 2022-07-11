import os
from datetime import datetime
import time
import re
import numpy as np


def main():
    key = input('''======STUDY RECORD APPLICATION ======

1.Record your study
2.Show how many minutes you have studied today
Please indicate your choice(default is 1):''')
    print('\n')
    if key != "2":
        study_logging()
    else:
        aggregate_study_time()

# change the directory to where we save the study logs.
def change_directory():
    destination = r'E:\study_logging'
    if os.getcwd() != destination:
        if not os.path.exists(destination):
            os.mkdir(destination)
        else:
            os.chdir(destination)
        
        
# create the study logging file
def study_logging():
    change_directory()
    
    date_prefix = datetime.now().strftime('%Y-%m-%d')
    study_logging_file = date_prefix+'_study_logging.txt'
    
    if not os.path.exists(study_logging_file): 
        study_count = 0 # study count variable would count the number of times we have runned the script in a day.
    else:
        with open(study_logging_file, 'r') as f:
            records = f.readlines()[-5]
        reg = r"your (\d+)"
        study_count = re.findall(reg, records)[0]
        study_count = int(study_count)
            
    count_logging = f'This is your {study_count+1} time(s) study, it should last 90 minutes!'
    start_time = datetime.now()
    start_logging = f'Start Time: {start_time}'
    print(count_logging)
    print(start_logging)

    try:
        interval = 5
        for i in range(1, 13):# alarm for every 5 minutes
            time.sleep(450)
            print(f'{interval} minutes!')
            interval = interval + 5
        print('Session completed!')
        # demenstrate the end time of your study and the total study time of this session.
        end_time = datetime.now()
        end_logging = f'End time: {end_time}'
        time_diff = (end_time - start_time).seconds
        total_study_time_logging = f'Total study minutes: {int(time_diff/60)}'
        
        print(end_logging)
        print(total_study_time_logging)
        
        logging = '\n'.join([count_logging, start_logging, end_logging, total_study_time_logging])
        with open(study_logging_file, 'a') as f:
            f.write(logging)
            f.write("\n\n")
    except KeyboardInterrupt:
        end_time = datetime.now()
        end_logging = f'End time: {end_time}'
        time_diff = (end_time - start_time).seconds
        total_study_time_logging = f'Total study minutes: {round(time_diff/60,0)}'
        logging = '\n'.join([count_logging, start_logging, end_logging, total_study_time_logging])
        with open(study_logging_file, 'a') as f:
            f.write(logging)
            f.write("\n\n")


def aggregate_study_time():
    change_directory()
    date_prefix = datetime.now().strftime('%Y-%m-%d')
    study_logging_file = date_prefix+'_study_logging.txt'
    
    if not os.path.exists(study_logging_file):
        print("Could not find the records!")
        exit()
    else:
        reg = r'minutes: (\d+)'
        with open(study_logging_file, 'r') as f:
            lines = f.readlines()
        lines = ','.join(lines)
        study_in_minutes = re.findall(reg, lines)
        study_in_minutes = [ int(i) for i in study_in_minutes]
        result = np.sum(study_in_minutes)
        print(f'You have study {result} minutes today') 
                    
if __name__ == "__main__":
    main()
    