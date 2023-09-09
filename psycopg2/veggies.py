import psycopg2

# connect to your postgres db
conn = psycopg2.connect(
    """
    dbname=week3 user=postgres host=localhost port=5432
    """
)

conn.set_session(autocommit=True)

# open a cursor to perform database operations
cur = conn.cursor()

cur.execute(
    """
    DROP TABLE IF EXISTS veggies
    """
)

cur.execute(
    """
    CREATE TABLE veggies(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        color TEXT NOT NULL
    )
    """
)

cur.execute(
    """
    INSERT INTO veggies VALUES 
    (1, 'carrot', 'orange'),
    (2, 'onion', 'yellow'),
    (3, 'zucchini', 'green'),
    (4, 'squash', 'yellow'),
    (5, 'pepper', 'red'),
    (6, 'onion', 'red')
    """
)

# execute a query
cur.execute(
    """
    SELECT * FROM veggies
    """
)


# retrieve query results
records = cur.fetchall()

# print(records)

cur.execute(
    """
    SELECT color, name FROM veggies
    """
)

veggie_records = cur. fetchall()
for v in veggie_records:
    print(v[0], v[1])