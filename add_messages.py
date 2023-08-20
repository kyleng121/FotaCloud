import psycopg2
import datetime
# Update connection string information

host = "fotadbstoreserver.postgres.database.azure.com"
dbname = "otadb2"
user = "cong@fotadbstoreserver"
password = "C123456789."
sslmode = "require"

# Construct connection string

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

cursor.execute('INSERT INTO "interfacesApi_messages" (time, message_type, message_content) VALUES (%s, %s, %s);', (datetime.datetime.now(),"fw_status", '0x533'))

conn.commit()
cursor.close()
conn.close()