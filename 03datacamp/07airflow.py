#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Tue Feb 25 16:34:57 2025 @author: yurii"""

# Simple DAG:
etl_dag = DAG(
    dag_id='etl_pipeline',
    default_args={"start_date": "2024-01-08"}
    )


# Running a simple Airflow task
$ airflow tasks test <dag_id> <task_id> [execution_date]
# Using a DAG named example-etl, a task named download-file on 2024-01-10:
$ airflow tasks test example-etl download-file 2024-01-10


# ###################################
# ###################################
# ###################################

from airflow import DAG
from datetime import datetime

default_arguments = {
    'owner': 'jdoe',
    'email': 'jdoe@datacamp.com',
    'start_date': datetime(2020, 1, 20)
    }
    'retries': 2

with DAG('etl_workflow', default_args=default_arguments) as etl_dag:
    # code
    
$ airflow -h        # help

# ###################################
from airflow.operators.bash import BashOperator

example_task = BashOperator(task_id='bash_ex',
                            bash_command='echo 1',
                            )

bash_task = BashOperator(task_id='clean_addresses',
                bash_command='cat addresses.txt | awk "NF==10" > cleaned.txt')

# ###################################
from airflow.operators.bash import BashOperator

with DAG(dag_id="test_dag", 
         default_args={"start_date": "2024-01-01"}) as analytics_dag:
    cleanup = BashOperator(task_id='cleanup_task',
                           bash_command='cleanup.sh')
    consolidate = BashOperator(task_id='consolidate_task',
                               bash_command='consolidate_data.sh')
    push_data = BashOperator(task_id='pushdata_task',
                             bash_command='push_data.sh')

pull_data >> cleanup
consolidate << cleanup
consolidate >> push_data


# ###################################                   PythonOperator
from airflow.operators.python import PythonOperator

def printme():
    print("This goes in the logs!")
    
python_task = PythonOperator(
    task_id='simple_print',
    python_callable=printme)


# ###
def sleep(length_of_time):
    time.sleep(length_of_time)

sleep_task = PythonOperator(task_id='sleep',
                            python_callable=sleep,
                            op_kwargs={'length_of_time': 5})

# ###
def pull_file(URL, savepath):
    r = requests.get(URL)
    with open(savepath, 'wb') as f:
        f.write(r.content)   
    print(f"File pulled from {URL} and saved to {savepath}") # Use the print method for logging

from airflow.operators.python import PythonOperator

pull_file_task = PythonOperator(
    task_id='pull_file',
    python_callable=pull_file,
    op_kwargs={'URL':'http://dataserver/sales.json', 
               'savepath': 'latestsales.json'}
    )


# ###################################
from airflow.operators.email import EmailOperator

email_task = EmailOperator(
    task_id='email_sales_report',
    to='sales_manager@example.com',
    subject='Automated Sales Report',
    html_content='Attached is the latest sales report',
    files='latest_sales.xlsx'
    )
    dag=process_sales_dag

# ###################################
default_args = {
  'owner': 'Engineering',
  'start_date': datetime(2023, 11, 1),
  'email': ['airflowresults@datacamp.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 3,
  'retry_delay': timedelta(minutes=20)
}

dag = DAG('update_dataflows', 
          default_args=default_args, 
          schedule_interval='30 12 * * 3')

# ###################################                   Sensor
from airflow.sensors.filesystem import FileSensor

file_sensor_task = FileSensor(task_id='file_sense',
                              filepath='salesdata.csv',
                              dag=sales_report_dag)

init_sales_cleanup >> file_sensor_task >> generate_report

mode=
    mode='poke'
    mode='reschedule'
poke_interval
timeout

#
ExternalTaskSensor
HttpSensor
SqlSensor

airflow.sensors
airflow.providers.*.sensors

# ###################################  


airflow.cfg
| grep "executor ="
| grep dags_folder


# ###################################           SLA

from datetime import timedelta

task1 = BashOperator(task_id='sla_task',
                     bash_command='runcode.sh',
                     sla=timedelta(seconds=30),
                     dag=dag)

default_args = {'sla': timedata(minutes=20),
                'start_date': datetime(2023, 2, 20)}

dag = DAG('sla_dag', default_args=default_args)

default_args = {'email': ['airflowalerts@datacamp.com'],
                'email_on_failure': True,
                'email_on_retry': False,
                'email_on_success': True}

timedelta(weeks=2)
timedelta(days=4, hours=10, minutes=20, seconds=30)


# ###################################               Templates

templated_command = """
  bash cleandata.sh {{ ds_nodash }} {{ params.filename }}
"""

# Modify clean_task to pass the new argument
clean_task = BashOperator(task_id='cleandata_task',
                          bash_command=templated_command,
                          params={'filename': 'salesdata.txt'},
                          dag=cleandata_dag)

# ###

templated_command="""
{% for filename in params.filenames %}
  echo "Reading {{ filename }}"
{% endfor %}"""

t1 = BashOperator(task_id='template_task',
                  bash_command=templated_command,
                  params={'filenames': ['file1.txt', 'file2.txt']},
                  dag=example_dag)
# >> Reading file1.txt
# >> Reading file2.txt

# ###
Execution Date: {{ ds }}                        # YYYY-MM-DD
Execution Date, no dashes: {{ ds_nodash }}      # YYYYMMDD
Previous Execution date: {{ prev_ds }}          # YYYY-MM-DD
Prev Execution date, no dashes: {{ prev_ds_nodash }}  # YYYYMMDD
DAG object: {{ dag }}
Airflow config object: {{ conf }} 

# https://airflow.apache.org/docs/stable/macros-ref.html1


# ###
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

filelist = [f'file{x}.txt' for x in range(30)]

default_args = {'start_date': datetime(2020, 4, 15)}

cleandata_dag = DAG('cleandata',
                    default_args=default_args,
                    schedule_interval='@daily')

templated_command = """
{% for filename in params.filenames %}
  bash cleandata.sh {{ ds_nodash }} {{ filename }};
{% endfor %}
"""

clean_task = BashOperator(task_id='cleandata_task',
                          bash_command=templated_command,
                          params={'filenames': filelist},
                          dag=cleandata_dag)


# ###################################               Branching
from airflow.operators.python import BranchPythonOperator

def branch_test(**kwargs):
    if int(kwargs['ds_nodash']) % 2 == 0:
        return'even_day_task'
    else:
        return'odd_day_task'
        
branch_task = BranchPythonOperator(task_id='branch_task',
                                   dag=dag,       
                                   provide_context=True,
                                   python_callable=branch_test)

start_task >> branch_task >> even_day_task >> even_day_task2
branch_task >> odd_day_task >> odd_day_task2

# ###
from airflow import DAG
from airflow.operators.python import BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

dag = DAG('BranchingTest',
          default_args={'start_date': datetime(2023, 4, 15)},
          schedule_interval='@daily')

def branch_test(**kwargs):
  if int(kwargs['ds_nodash']) % 2 == 0:
    return 'even_day_task'
  else:
    return 'odd_day_task'
 
start_task = EmptyOperator(task_id='start_task', dag=dag)

branch_task = BranchPythonOperator(
       task_id='branch_task',
       provide_context=True,
       python_callable=branch_test,
       dag=dag)

even_day_task = EmptyOperator(task_id='even_day_task', dag=dag)
even_day_task2 = EmptyOperator(task_id='even_day_task2', dag=dag)

odd_day_task = EmptyOperator(task_id='odd_day_task', dag=dag)
odd_day_task2 = EmptyOperator(task_id='odd_day_task2', dag=dag)

start_task >> branch_task 
even_day_task >> even_day_task2
odd_day_task >> odd_day_task2




# ###################################  
# ###################################  
# ###################################  

from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.email import EmailOperator
from dags.process import process_data
from datetime import datetime, timedelta

# Update the default arguments and apply them to the DAG.

default_args = {'start_date': datetime(2023,1,1),
                'sla': timedelta(minutes=90)}
    
dag = DAG(dag_id='etl_update', default_args=default_args)

sensor = FileSensor(task_id='sense_file', 
                    filepath='/home/repl/workspace/startprocess.txt',
                    poke_interval=45,
                    dag=dag)

bash_task = BashOperator(task_id='cleanup_tempfiles', 
                         bash_command='rm -f /home/repl/*.tmp',
                         dag=dag)

python_task = PythonOperator(task_id='run_processing', 
                             python_callable=process_data,
                             provide_context=True,
                             dag=dag)

email_subject="""
  Email report for {{ params.department }} on {{ ds_nodash }}
"""

email_report_task = EmailOperator(task_id='email_report_task',
                                  to='sales@mycompany.com',
                                  subject=email_subject,
                                  html_content='',
                                  params={'department': 'Data subscription services'},
                                  dag=dag)

no_email_task = EmptyOperator(task_id='no_email_task', dag=dag)

def check_weekend(**kwargs):
    dt = datetime.strptime(kwargs['execution_date'],"%Y-%m-%d")
    # If dt.weekday() is 0-4, it's Monday - Friday. If 5 or 6, it's Sat / Sun.
    if (dt.weekday() < 5):
        return 'email_report_task'
    else:
        return 'no_email_task'
    
branch_task = BranchPythonOperator(task_id='check_if_weekend',
                                   python_callable=check_weekend,
                                   provide_context=True,                                
                                   dag=dag)

sensor >> bash_task >> python_task
python_task >> branch_task >> [email_report_task, no_email_task]
# ###################################  
# ###################################  
# ###################################  

















