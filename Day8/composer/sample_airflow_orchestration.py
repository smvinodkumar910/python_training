from airflow import models
from airflow.operators import python
from airflow.utils import dates
import datetime
from airflow.contrib.operators import gcs_to_bq
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
import pendulum

args = {
        'owner': 'Airflow',
        'start_date':pendulum.today('UTC').add(days=-1),
    }

dag = models.DAG(
        dag_id='sample_airflow_orchestration', default_args=args,
        schedule_interval=None)

load_csv = gcs_to_bq.GoogleCloudStorageToBigQueryOperator(
    task_id='gcs_to_bq_task',
    bucket='mynewdevenv-bucket',
    source_objects=['sample/us-states.csv'],
    skip_leading_rows=1,
    destination_project_dataset_table='mynewdevenv.python_learning_demo.us_states_composer',
    autodetect = True, 
    create_disposition = 'CREATE_IF_NEEDED', 
    write_disposition='WRITE_TRUNCATE',
    dag=dag)

t1_procedure = BigQueryExecuteQueryOperator(
    task_id="dag1_procedure",
    sql="CALL `bamboo-bulwark-319114.CST_I090.ad_pro`();",
    use_legacy_sql=False,
    dag=dag
)

[load_csv, tas2 ] >> t1_procedure