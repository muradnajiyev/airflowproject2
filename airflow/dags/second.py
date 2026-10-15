from datetime import datetime
from airflow.sdk import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook


@dag(
    dag_id="Postgres_Hook",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False
)
def postgres():

    @task
    def select_data():
        hook = PostgresHook(
            postgres_conn_id="pg_conn_id"
        )

        result = hook.get_records("SELECT 1")
        print(result)

    select_data()


postgres()
