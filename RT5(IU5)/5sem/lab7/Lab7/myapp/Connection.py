import MySQLdb

class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.host= host
        self.user= user
        self.password=password
        self.db=db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__ (self):
        self.connect()

    def __exit__ (self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        #открытие соединения
        if not self._connection:
            self._connection= MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db
            )

    def disconnect(self):
        #закрытие соединения
        if self._connection:
            self._connection.close()


class User:
    def __init__(self, db_connection, id, name, idconcert):
        self.db_connection = db_connection.connection
        self.id = id
        self.name = name
        self.idconcert = idconcert

    def save(self):
        c = self.db_connection.cursor()
        #c.execute("insert into user (id, name, idconcert) values (%s, %s, %s);",
         #         (self.id, self.name, self.idconcert))
        c.execute("update user set name = %s, idconcert = %s Where id = %s;",
                  (self.name, self.idconcert, self.id))
        self.db_connection.commit()
        c.close()

class SelAll:
    def __init__(self, db_connection):
        self.db_connection = db_connection.connection

    def save(self):
        c = self.db_connection.cursor()
        c.execute("Select * from USER ")
        entries = c.fetchall()
        c.close()
        #for e in entries:
        #    print(e)
        return('<br>'.join(map(str, entries)))

con = Connection("root", "1111", "userbronkoncert")
with con:
    user = User(con, '10', 's3rpyn', '3')
    user.save()


con = Connection("root", "1111", "userbronkoncert")
with con:
    user = SelAll(con)
    user.save()







