import sqlite3
import shutil
import os
import threading
import time

class DB:
    def __init__(self, db_name="scratch_db.sql", auto_backup=None):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._stop_backup = threading.Event()
        self._backup_thread = None

        if auto_backup:
            try:
                interval = int(auto_backup)
                if interval > 0:
                    self._start_auto_backup(interval)
            except ValueError:
                print(f"Invalid auto_backup interval: {auto_backup}")

    def query(self, sql):
        try:
            self.cursor.execute(sql)
            if sql.strip().upper().startswith("SELECT"):
                results = self.cursor.fetchall()
                for row in results:
                    print(row)
                return results
            else:
                self.conn.commit()
                return "Query executed"
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")

    def close(self):
        self._stop_backup.set()
        if self._backup_thread:
            self._backup_thread.join()
        self.conn.close()

    def _start_auto_backup(self, interval):
        def backup_loop():
            while not self._stop_backup.is_set():
                time.sleep(interval)
                self._backup_file()

        self._backup_thread = threading.Thread(target=backup_loop, daemon=True)
        self._backup_thread.start()

    def _backup_file(self):
        try:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            backup_filename = f"{self.db_name}_backup_{timestamp}.sql"
            shutil.copy2(self.db_name, backup_filename)
        except Exception as e:
            print(f"Backup error: {e}")

def connect_db(db_name="scratch_db.sql", auto_backup=60):
    return DB(db_name=db_name, auto_backup=auto_backup)
