import getpass
import os

if not os.environ.get("DEEPSEEK_API_KEY"):
    os.environ["DEEPSEEK_API_KEY"] = getpass.getpass("请输入openAI的apiKey:")

from langchain.chat_models import init_chat_model

model = init_chat_model("deepseek-chat", model_provider="deepseek")

result = model.invoke("你好，deepseek")
print(result.content)
