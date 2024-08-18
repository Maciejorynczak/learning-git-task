import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
    except Error as e:
        print(e)
    return conn

if __name__ == '__main__':
    conn = create_connection(r"my_database.db")
    if conn:
        conn.close()

def create_table(conn):
    """ create tables in the SQLite database """
    try:
        sql_create_projects_table = """CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        start_date text,
                                        end_date text
                                    );"""

        sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    project_id integer NOT NULL,
                                    name text NOT NULL,
                                    description text,
                                    status text,
                                    start_date text,
                                    end_date text,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

        conn.execute(sql_create_projects_table)
        conn.execute(sql_create_tasks_table)
    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    conn = create_connection(r"my_database.db")
    if conn:
        create_table(conn)
        conn.close()

def add_project(conn, project):
    """Add a new project to the projects table"""
    sql = '''INSERT INTO projects(name, start_date, end_date)
             VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def add_task(conn, task):
    """Add a new task to the tasks table"""
    sql = '''INSERT INTO tasks(project_id, name, description, status, start_date, end_date)
             VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

if __name__ == '__main__':
    conn = create_connection(r"my_database.db")
    if conn:
        project = ("Project 1", "2024-08-01", "2024-08-15")
        project_id = add_project(conn, project)

        task_1 = (project_id, "Task 1", "Description for Task 1", "started", "2024-08-01 12:00:00", "2024-08-01 15:00:00")
        task_2 = (project_id, "Task 2", "Description for Task 2", "not started", "2024-08-02 12:00:00", "2024-08-02 15:00:00")

        add_task(conn, task_1)
        add_task(conn, task_2)

        conn.close()
def select_all(conn, table):
    """Query all rows in the specified table"""
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    return rows

def select_where(conn, table, **query):
    """Query rows in the specified table based on the query"""
    cur = conn.cursor()
    qs = []
    values = ()
    for k, v in query.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)
    cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
    rows = cur.fetchall()
    return rows

if __name__ == '__main__':
    conn = create_connection(r"my_database.db")
    if conn:
        print("All projects:")
        print(select_all(conn, "projects"))

        print("All tasks:")
        print(select_all(conn, "tasks"))

        print("Tasks for project with id 1:")
        print(select_where(conn, "tasks", project_id=1))

        conn.close()

def update_task_status(conn, id, status):
    """Update the status of a task"""
    sql = ''' UPDATE tasks
              SET status = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (status, id))
    conn.commit()

if __name__ == '__main__':
    conn = create_connection(r"my_database.db")
    if conn:
        update_task_status(conn, 1, "completed")
        conn.close()
def delete_task(conn, id):
    """Delete a task by task id"""
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

if __name__ == '__main__':
    conn = create_connection(r"my_database.db")
    if conn:
        delete_task(conn, 1)
        conn.close()

