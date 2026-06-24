"""
yaml
k:v
"""

import yaml

from utils.path_tool import get_abs_path

# def load_rag_config(config_path: str=get_abs_path('config/rag.yml'), encoding='utf-8'):
#     with open(config_path, 'r', encoding=encoding) as f:
#         return yaml.load(f, Loader=yaml.FullLoader)
#
# def load_chroma_config(config_path: str=get_abs_path('config/chroma.yml'), encoding='utf-8'):
#     with open(config_path, 'r', encoding=encoding) as f:
#         return yaml.load(f, Loader=yaml.FullLoader)
#
# def load_prompts_config(config_path: str=get_abs_path('config/prompts.yml'), encoding='utf-8'):
#     with open(config_path, 'r', encoding=encoding) as f:
#         return yaml.load(f, Loader=yaml.FullLoader)
#
#
# def load_agent_config(config_path: str=get_abs_path('config/agent.yml'), encoding='utf-8'):
#     with open(config_path, 'r', encoding=encoding) as f:
#         return yaml.load(f, Loader=yaml.FullLoader)
#
# def load_weather_config(config_path: str=get_abs_path('config/weather.yml'), encoding='utf-8'):
#     with open(config_path, 'r', encoding=encoding) as f:
#         return yaml.load(f, Loader=yaml.FullLoader)
#
# rag_conf = load_rag_config()
# chroma_conf = load_chroma_config()
# prompts_conf = load_prompts_config()
# agent_conf = load_agent_config()
# weather_conf = load_weather_config()
def load_config(config_name):

    path = get_abs_path(f"config/{config_name}")

    with open(path, "r", encoding="utf-8") as f:
        return yaml.load(
            f,
            Loader=yaml.FullLoader
        )

agent_conf = load_config("agent.yml")
rag_conf = load_config("rag.yml")
weather_conf = load_config("weather.yml")
chroma_conf = load_config("chroma.yml")
prompts_conf = load_config("prompts.yml")
weather_conf = load_config("weather.yml")



if __name__ == '__main__':
    print(rag_conf["chat_model_name"])