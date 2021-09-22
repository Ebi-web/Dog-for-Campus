import streamlit as st
import boto3
from boto3.dynamodb.conditions import Key

class UserTable:
    def __init__(self, table_index=1):
        dynamoDB_config = st.secrets["dynamoDB_config"]
        
        session = boto3.session.Session(
            region_name = dynamoDB_config["region_name"],
            aws_access_key_id = dynamoDB_config["aws_access_key_id"],
            aws_secret_access_key = dynamoDB_config["aws_secret_access_key"]
        )
        dynamodb = session.resource('dynamodb')

        tables = ["ScrapingResults", "User"]
        self.table_name = tables[table_index]
        self.table = dynamodb.Table(self.table_name)
    def get(self):
        response = self.table.get_item(Key={"Mail": st.session_state["email"]})
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            print(response)
            st.error("登録情報の取得に失敗しました")
        return response["Item"]

    def put(self, item):
        response = self.table.put_item(
            Item = item
        )
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            print(response)
            st.error("登録に失敗しました")
        else:
            st.success("登録が完了しました")
        return

    def update(self, item):
        response = self.table.update_item(
            Key={"Mail": item["Mail"]},
            UpdateExpression="set RegisteredBinaryNum=:b",
            ExpressionAttributeValues={":b": item["RegisteredBinaryNum"]}
            )
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            print(response)
            st.error("登録に失敗しました")
        else:
            st.success("登録が完了しました")
        return

    def query(self, req_name):
        response = self.table.query(
            KeyConditionExpression = Key("scraping_function_name").eq(req_name)
        )
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            print(response)
            st.error("結果の取得に失敗しました")
        return response["Items"][0]["result"]