from abc import ABC, abstractmethod
from typing import Optional

from langchain_core.embeddings import Embeddings
from langchain_community.chat_models.tongyi import  BaseChatModel
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.chat_models.tongyi import ChatTongyi
from utils.config_handler import rag_conf


class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self) -> Optional[Embeddings | BaseChatModel] :
        pass

class ChatModelFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel] :
        return ChatTongyi(model = rag_conf["chat_model_name"])

class EmbeddingsFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel] :
        return DashScopeEmbeddings(model = rag_conf["embedding_model_name"])

chat_model = ChatModelFactory().generator()
embed_model = EmbeddingsFactory().generator()


""""
为什么要写 BaseModelFactory？

为了统一模型创建接口。

项目后续可能接入：
- DeepSeek
- GPT
- Qwen
- Claude

通过抽象工厂约束所有模型工厂实现同样的generator方法。

业务代码依赖抽象而不是具体实现，
符合开闭原则和依赖倒置原则。
"""

"""
ABC和abstractmethod作用是什么？
ABC用于定义抽象基类。

@abstractmethod用于声明抽象方法。

子类必须实现这些方法，否则无法实例化。

作用类似Java中的
abstract class + abstract method
或者interface。


"""