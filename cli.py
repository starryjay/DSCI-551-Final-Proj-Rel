import cmd
import pandas as pd
import os
from queryparse import parse_query

class CLI(cmd.Cmd):
    intro = 'Welcome to Roma Jay Data Base (RJDB) :D\n'
    prompt = 'RJDB > '
    
    def __init__(self, current_db=None):
        super(CLI, self).__init__()
        self.current_db = current_db

    def do_makedb(self, user_input_query):
        '''
        Use this keyword at the beginning of a query to
        create a new database.

        Syntax: MAKEDB REL/NOSQL dbname
        ''' 
        user_input_query = user_input_query.strip().split(" ")
        if self.current_db is not None:
            if user_input_query[0].upper() == "REL":
                os.chdir("..")
                os.chdir("../DSCI-551-Final-Proj-Rel")
            elif user_input_query[0].upper() == "NOSQL":
                os.chdir("..")
                os.chdir("../DSCI-551-Final-Proj-NoSQL")
        else:
            if user_input_query[0].upper() == "REL":
                os.chdir("../DSCI-551-Final-Proj-Rel")
            elif user_input_query[0].upper() == "NOSQL":
                os.chdir("../DSCI-551-Final-Proj-NoSQL")
        if os.path.exists(user_input_query[1]):
            print("DB name already exists! Please use the existing DB or make a DB with a different name.")
        else:
            os.mkdir("./" + user_input_query[1])
            if user_input_query[0].upper() == "REL":
                print("Created relational DB ", user_input_query[1])
            elif user_input_query[0].upper() == "NOSQL":
                print("Created non-relational DB ", user_input_query[1])
        
    def do_usedb(self, user_input_query):
        """
        Use this keyword at the beginning of a query to
        use an existing database.

        Syntax: USEDB REL/NOSQL dbname
        """
        user_input_query = user_input_query.strip().split(" ")
        if user_input_query[0].upper() == "REL":
            os.chdir("../DSCI-551-Final-Proj-Rel")
        elif user_input_query[0].upper() == "NOSQL":
            os.chdir("../DSCI-551-Final-Proj-NoSQL")
        if not os.path.exists(user_input_query[1]):
            print("DB does not exist!")
        else:
            os.chdir("./" + user_input_query[1])
            self.current_db = user_input_query[1]
            print("Using DB " + user_input_query[1])

    def do_dropdb(self, user_input_query):
        """
        Use this keyword at the beginning of a query to
        drop an existing database.

        Syntax: DROPDB REL/NOSQL dbname
        """
        user_input_query = user_input_query.strip().split(" ")
        if user_input_query[1] == self.current_db:
            self.current_db = None
            if user_input_query[0].upper() == "REL":
                os.chdir("..")
                os.chdir("../DSCI-551-Final-Proj-Rel")
            elif user_input_query[0].upper() == "NOSQL":
                os.chdir("..")
                os.chdir("../DSCI-551-Final-Proj-NoSQL")
        elif self.current_db is not None:
            if user_input_query[0].upper() == "REL":
                os.chdir("..")
                os.chdir("../DSCI-551-Final-Proj-Rel")
            elif user_input_query[0].upper() == "NOSQL":
                os.chdir("..")
                os.chdir("../DSCI-551-Final-Proj-NoSQL")
        else:
            if user_input_query[0].upper() == "REL":
                os.chdir("../DSCI-551-Final-Proj-Rel")
            elif user_input_query[0].upper() == "NOSQL":
                os.chdir("../DSCI-551-Final-Proj-NoSQL")
        if user_input_query[1] not in os.listdir('.'):
            print("DB does not exist!")
            return
        else:
            os.rmdir("./" + user_input_query[1])
            if user_input_query[0].upper() == "REL":
                print("Dropped relational DB", user_input_query[1])
            elif user_input_query[0].upper() == "NOSQL":
                print("Dropped non-relational DB", user_input_query[1])

    def do_make(self, user_input_query):
        """
        Use this keyword at the beginning of a query
        to make a new table within the current database.

        Syntax: MAKE (COPY) tablename (tablename2) COLUMNS col1=dtype1, col2=dtype2, col3=dtype3...
        """
        user_input_query = "MAKE " + user_input_query
        return parse_query(user_input_query, self.current_db)
        
    def do_edit(self, user_input_query):
        """
        Use this keyword at the beginning of a query
        to edit an existing table within the current database,
        including insert, update, and delete operations.

        General syntax: EDIT tablename INSERT/UPDATE/DELETE record
        Syntax for INSERT (one record at a time): EDIT tablename INSERT col1=x, col2=y, col3=z...
        Syntax for INSERT (whole file): EDIT tablename INSERT FILE filename
        Syntax for UPDATE: EDIT tablename UPDATE id=rownum, col3=abc, col5=xyz... 
        Syntax for DELETE: EDIT tablename DELETE id=rownum...
        """
        user_input_query = "EDIT " + user_input_query
        return parse_query(user_input_query, self.current_db)
        
    
    def do_fetch(self, user_input_query): 
        """
        Use this keyword at the beginning of a query to 
        fetch existing table and perform aggregation, bunching, 
        filtering, sorting, or merging operations on specified columns.

        Syntax: FETCH tablename [COLUMNS] [column(s)] [AGGREGATION FUNCTION] [column] [BUNCH/SORT/MERGE] [column] [HAS] [column(s)]

        * Keywords should specifically be in the order of 
          COLUMNS --> TOTALNUM/SUM/MEAN/MIN/MAX --> BUNCH --> SORT --> MERGE --> HAS

        """
        user_input_query = "FETCH " + user_input_query
        return parse_query(user_input_query, self.current_db)
        
    def do_drop(self, user_input_query): 
        """
        Use this keyword at the beginning of a query to
        drop a table from the current database.

        Syntax: DROP tablename
        """
        user_input_query = "DROP " + user_input_query
        return parse_query(user_input_query, self.current_db)
    
    def do_exit(self, *args):
        print("Bye")
        return True

if __name__ == "__main__": 
    CLI().cmdloop()