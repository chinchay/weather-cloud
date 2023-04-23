#%%
import json
import boto3
from boto3.dynamodb.conditions import Key

client = boto3.resource("dynamodb", region_name="us-east-2")
table = client.Table("x_sample_table")


# %%
db = boto3.resource("dynamodb", region_name="us-east-2")
# %%
__TableName__ = "x_sample_table"
table = db.Table(__TableName__)
# %%
# Primary_Column_Name = "x_partition_key"
# Primary_Key = 1

response = table.get_item(
    Key = {
        "x_partition_key":"1",
        "x_sort_key":"a"
    }
)

print(response)
# %%

import boto3

# %%
dynamodb = boto3.client("dynamodb", region_name="us-east-2")
# %%
response = dynamodb.scan(TableName="x_sample_table")
# %%
