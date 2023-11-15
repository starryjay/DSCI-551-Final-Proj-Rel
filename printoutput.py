import pandas as pd
import os

def return_table(user_query_list, tablename, chunkno=None, rownum=None):
    user_query_list = list(map(str.upper, user_query_list))
    # parse whole user_query_list 
    chunk_path = "./" + tablename + "_chunks"
    col_agg = "/col_agg"                          # directly under chunks
    agg = "/agg"                                  # directly under chunks
    bunch_agg_chunks = "/bunch_agg_chunks"        # directly under chunks
    bunched_chunks = "/bunched_chunks"            # directly under chunks
    merged_tables = "/merged_tables"              # directly under chunks
    sorted_tables = "/chunk_subsets"              # directly under chunks
    has_chunks = "/has_chunks"                    # could be under any of above
    if "FETCH" in user_query_list:
        filepath = chunk_path
        agglist = ["TOTALNUM", "SUM", "MEAN", "MIN", "MAX"]
        if "BUNCH" in user_query_list:
            if not set(agglist).isdisjoint(set(list(map(str.upper, user_query_list)))):
                if "MERGE" in user_query_list:
                    if "SORT" in user_query_list:
                        filepath += sorted_tables
                    else:
                        filepath += merged_tables
                else:
                    filepath += bunch_agg_chunks
            else:
                filepath += bunched_chunks
        else:
            if not set(agglist).isdisjoint(set(list(map(str.upper, user_query_list)))):
                if "MERGE" in user_query_list:
                    if "SORT" in user_query_list:
                        filepath += sorted_tables
                    else:
                        filepath += merged_tables
                else:
                    if "COLUMNS" in user_query_list:
                        filepath += col_agg
                    else:
                        filepath += agg
            if "MERGE" in user_query_list:
                if "SORT" in user_query_list:
                    filepath += sorted_tables
                else:
                    filepath += merged_tables
            else:
                if "SORT" in user_query_list:
                    filepath += sorted_tables
        if "HAS" in user_query_list:
            filepath += has_chunks
        df = pd.DataFrame()
        print(filepath)
        for chunk in os.listdir(filepath):
            print(filepath + "/" + chunk)
            s = pd.read_pickle(filepath + "/" + chunk)
            df = pd.concat([df, s])
        return df