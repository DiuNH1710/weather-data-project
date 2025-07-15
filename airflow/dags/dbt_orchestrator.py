from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
import sys
from docker.types import Mount


default_args = {
      'description': 'A DAG to orchestrator data', 
      'start_date': datetime(2025, 7, 14),
      'catchup': False,
      }

dag = DAG(
    dag_id='weather-dbt-orchestrator',
    default_args=default_args, 
    schedule=None
)

with dag:
      task2 = DockerOperator(
            task_id='transform_data_task',
            image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
            command='run',
            working_dir='/usr/app',
            mounts=[
                  Mount(source='/mnt/e/data-projects/dbtDataPipeline/repos/weather-data-project/dbt/my_project', 
                        target='/usr/app',
                        type='bind'),
                  Mount(source='/mnt/e/data-projects/dbtDataPipeline/repos/weather-data-project/dbt/profiles.yml', 
                        target='/root/.dbt/profiles.yml',
                        type='bind')
                  ],
            network_mode='weather-data-project_my_network',
            docker_url='unix://var/run/docker.sock',
            auto_remove='success')
      
