# Module Imports
import mariadb
import sys
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="127.0.0.1",
        port=3306,
        database="tfg_database"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.execute("delete from locations")
cur.execute("delete from materials")
cur.execute("delete from material_locations")


for i in range(1, 100):

    material_id = i
    location_id = i
    name = "n"
    description = "d"
    importance = 100 % i
    date_creation = '2021-12-31'
    city = "c1"
    country = "c2"

    query_m = f"INSERT INTO materials (material_id, name" \
              f",description, importance, date_creation) " \
              f"VALUES ('{material_id}', '{name}'," \
              f" '{description}', '{importance}', '{date_creation}') "
    cur.execute(query_m)

    query_l = f"INSERT INTO locations (location_id, name," \
              f"description, importance,country, city, date_creation) " \
              f"VALUES ('{location_id}', '{name}', " \
              f"'{description}','{importance}'," \
              f" '{country}','{city}', '{date_creation}')"
    cur.execute(query_l)

    query_ml = f"INSERT INTO material_locations (location_id, material_id) VALUES ('{location_id}', '{material_id}')"
    cur.execute(query_ml)

conn.commit()

cur.execute("SHOW columns from locations")
print(cur)
cur.execute("SELECT * FROM materials")

for a in cur:
    print(a)

print("d")
