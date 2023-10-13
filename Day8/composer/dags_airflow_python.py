import datetime

from airflow import models
from airflow.providers.google.cloud.operators.dataflow import DataflowCreatePythonJobOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.utils.dates import days_ago


with models.DAG(
    dag_id="Triple_Python_Pipeline",
    start_date=days_ago(1),
    # The interval with which to schedule the DAG
    schedule_interval='@once',  # Override to match your needs
) as dag:
    t1 =DataflowCreatePythonJobOperator(
        task_id="task1_dataflow_runner",
        py_file=f'gs://i090test/address_python.py',
        py_options=[],
        job_name='pipelineone',
        options={
            "output": 'bamboo-bulwark-319114:CST_I090.stg_address'
        },
    )
    t1_procedure = BigQueryExecuteQueryOperator(
        task_id="dag1_procedure",
        sql="CALL `bamboo-bulwark-319114.CST_I090.ad_pro`();",
        use_legacy_sql=False
    )
    t2 =DataflowCreatePythonJobOperator(
        task_id="task2_dataflow_runner",
        py_file=f'gs://i090test/pluralpython_airflow.py',
        py_options=[],
        job_name='pipelinetwo',
        options={
            "output": 'bamboo-bulwark-319114:CST_I090.stg_plural'
        },
    )
    t2_procedure = BigQueryExecuteQueryOperator(
        task_id="dag2_procedure",
        sql="CALL `bamboo-bulwark-319114.CST_I090.merge_pro1`();",
        use_legacy_sql=False
    )
    t3 =DataflowCreatePythonJobOperator(
        task_id="task3_dataflow_runner",
        py_file=f'gs://i090test/test1_python.py',
        py_options=[],
        job_name='pipelinethree',
        options={
            "output": 'bamboo-bulwark-319114:CST_I090.stg_test'
        },
          py_interpreter='python3',
        py_system_site_packages=False,
        location='us-central1',
        wait_until_finished=False,
    )        
    t3_procedure = BigQueryExecuteQueryOperator(
        task_id="dag3_procedure",
        sql="CALL `bamboo-bulwark-319114.CST_I090.test_pro`();",
        use_legacy_sql=False
    )
    
t1 >> t1_procedure 
t2 >> t2_procedure 
t3 >> t3_procedure
