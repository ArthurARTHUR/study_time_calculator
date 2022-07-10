import os
from datetime import datetime
import time
import re


def main():
    study_logging()


# change the directory to where we save the study logs.
def change_directory():
    destination = 'F:/video/study_record'
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
            
    count_logging = f'This is your {study_count+1} time(s) study, it should last 60 minutes!'
    start_time = datetime.now()
    start_logging = f'Start Time: {start_time}'
    print(count_logging)
    print(start_logging)

    try:
        for i in range(1, 13):# alarm for every 5 minutes
            time.sleep(300)
            print(f'This is the {i} five-minute!')
         
        # demenstrate the end time of your study and the total study time of this session.
        end_time = datetime.now()
        end_logging = f'End time: {end_time}'
        time_diff = (end_time - start_time).seconds
        total_study_time_logging = f'Total study minutes:{round(time_diff/60,0)}'
        
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
    
                    
if __name__ == "__main__":
    main()
    