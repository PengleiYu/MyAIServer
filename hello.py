import getpass
import os

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage
from langchain_core.runnables import RunnableLambda

if not os.environ.get("DEEPSEEK_API_KEY"):
    os.environ["DEEPSEEK_API_KEY"] = getpass.getpass("请输入openAI的apiKey:")

model = init_chat_model("deepseek-chat", model_provider="deepseek")


def create_messages(text: str) -> [BaseMessage]:
    return [
        SystemMessage("请把下述内容翻译为英文"),
        HumanMessage(text),
    ]


def extra_messages_content(msg: BaseMessage) -> str:
    return msg.content


translation_chain = (
        RunnableLambda(create_messages)  # RunnableLambda其实无需显式声明，会被强制转型
        | model
        | extra_messages_content
)

result = translation_chain.invoke("我的征途是星辰大海")
print(result)
