import streamlit as st
import boto3


class UserTable:
    def __init__(self):
        dynamoDB_config = st.secrets["dynamoDB_config"]
        
        session = boto3.session.Session(
            region_name = dynamoDB_config["region_name"],
            aws_access_key_id = dynamoDB_config["aws_access_key_id"],
            aws_secret_access_key = dynamoDB_config["aws_secret_access_key"]
        )
        dynamodb = session.resource('dynamodb')

        self.table_name = "User"
        self.table = dynamodb.Table(self.table_name)
    def get(self):
        response = self.table.get_item(Key={"Mail": st.session_state["email"]})
        if response['ResponseMetadata']['HTTPStatusCode'] is not 200:
            print(response)
            st.error("登録情報の取得に失敗しました")
        return response["Item"]

    def put(self, item):
        response = self.table.put_item(
            Item = item
        )
        if response['ResponseMetadata']['HTTPStatusCode'] is not 200:
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
        if response['ResponseMetadata']['HTTPStatusCode'] is not 200:
            print(response)
            st.error("登録に失敗しました")
        else:
            st.success("登録が完了しました")
        return