# Below code is part of Lecture,

# Create snowconnction component part 1
#https://www.udemy.com/course/snowpark-data-engineering-with-snowflake/learn/lecture/35877124#overview

# Create snowconnection component part 2
# https://www.udemy.com/course/snowpark-data-engineering-with-snowflake/learn/lecture/35877126#overview

# Copy to snowflake table.
#https://www.udemy.com/course/snowpark-data-engineering-with-snowflake/learn/lecture/36039456?instructorPreviewMode=instructor_v4#overview


import sys
sys.path.append('/workspaces/Snowpark_pipeline/')
from generic_code import code_library
from schema import source_schema
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.types import IntegerType, StringType, StructField, StructType, DateType


connection_parameters = {"account":"CERVELLOPARTNER", \
"user":"bkuder", \
"password": "B4psadagger@1", \
"role":"CERVELLO_INTERNAL", \
"warehouse":"CERVELLO_XSMALL_1", \
"database":"DEMODB", \
"schema":"PUBLIC" \
}

config_file = {"Database_name":"DEMODB",\
"Schema_name":"PUBLIC",\
"Target_table":"EMPLOYEE",
"Reject_table":"EMPLOYEE_REJECTS",\
"target_columns":["FIRST_NAME","LAST_NAME","EMAIL","ADDRESS","CITY","DOJ"],\
"on_error":"CONTINUE",\
"Source_location":"@my_s3_stage/employee/",\
"Source_file_type":"csv"\
}
    
# Declare schema for csv file and read data
schema = StructType([StructField("FIRST_NAME", StringType()),
StructField("LAST_NAME", StringType()),
StructField("EMAIL", StringType()),
StructField("ADDRESS", StringType()),
StructField("CITY", StringType()),
StructField("DOJ",DateType())])

session = code_library.snowconnection(connection_parameters)
copied_into_result, qid = code_library.copy_to_table(session,config_file,schema)

print(copied_into_result)
print(qid)

copied_into_result_df = session.create_dataframe(copied_into_result)
copied_into_result_df.show()