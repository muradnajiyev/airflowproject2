from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="mc-alias-dag",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    configure_minio = BashOperator(
        task_id="configure_minio",
        bash_command="mc alias set local http://minio:9000 minioadmin minioadmin123",
    )

    create_and_upload = BashOperator(
        task_id="create_and_upload",
        bash_command="""
        mkdir -p /tmp/matrix
        touch /tmp/matrix/bronze.py
        mc cp /tmp/matrix/bronze.py local/matrix/test_bash/bronze.py
        """,
    )

    list_files = BashOperator(
        task_id="list_minio_files",
        bash_command="mc ls local/matrix/test_bash/",
    )

    verify_upload = BashOperator(
        task_id="verify_upload",
        bash_command="""
        mc stat local/matrix/test_bash/bronze.py
        echo "Ugurlu"
        """,
    )

    configure_minio >> create_and_upload >> list_files >> verify_upload