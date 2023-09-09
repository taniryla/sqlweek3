import psycopg2

# connect to your postgres db
conn = psycopg2.connect(
    """
    dbname=week 3 user=postgres host=localhost port=5432
    """
)