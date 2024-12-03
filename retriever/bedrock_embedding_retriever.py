from retriever.llama_index_retriever import Retriever
from langchain_aws import BedrockEmbeddings
import boto3
import botocore


class BedrockRetriever(Retriever):
    def __init__(self):
        super()
