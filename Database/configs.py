import operators

class database_configs():
    def __init__(self) -> None:
        self.dbName = './Database/db_main.db'
        self.make_conn()
        self.sql_create_table_users = """ CREATE TABLE IF NOT EXISTS users (
                                        snsID text NOT NULL,
                                        name text NOT NULL,
                                        email text NOT NULL,
                                        lunchs inter,
                                        snacks integer,
                                        id integer primary key
                                    ); """
        operators.create_table(self.conn, self.sql_create_table_users)

    def make_conn(self):
        self.conn = operators.create_connection(self.dbName)