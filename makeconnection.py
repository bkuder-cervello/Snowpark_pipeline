import sys
from snowflake.snowpark import Session

# If you are running this code in Github code spaces you don't need to execute below command,
sys.path.append('/workspaces/Snowpark_pipeline/')

from generic_code import code_library

# Make connection and create Snowpark session.
# Please mention your snowflake account credentials below,
connection_parameters = {"account":"CERVELLOPARTNER", \
"user":"bkuder", \
"password": "B4psadagger@1", \
"role":"CERVELLO_INTERNAL", \
"warehouse":"CERVELLO_XSMALL_1", \
"database":"DEMODB", \
"schema":"PUBLIC" \
}

# Create connection with snowflake and return the session
session = code_library.snowconnection(connection_parameters)