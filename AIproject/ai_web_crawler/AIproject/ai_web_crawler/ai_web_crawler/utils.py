#工具函数(如加载配置文件)
import yaml

def load_config(config_path):
    """
    加载配置文件。
    :param config_path: 配置文件的路径
    :return: 配置字典
    """
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)
