import psycopg2
conn = psycopg2.connect(
    dbname="newsdb",
    user="postgres",
    password="My_Password",
    host="127.0.0.1",
    port=5432
)
print("✅ Connected via psycopg2")
conn.close()
