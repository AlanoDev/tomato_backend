import os
import sys
from pathlib import Path

from dynaconf import Dynaconf

_BASE_DIR = Path(__file__).parent.parent

settings_files = [
    Path(__file__).parent / 'settings.yml',
]

settings = Dynaconf(
    envvar_prefix="TOMATO",  
    settings_files=settings_files,
    environments=False,  # 启用多层次日志，支持 dev, pro
    load_dotenv=True,  # 加载 .env
    env_switcher="TOMATO_ENV",  
    lowercase_read=False,  # 禁用小写访问， settings.name 是不允许的
    # 自定义配置覆盖默认配置
    includes=[os.path.join(sys.prefix, 'etc', 'tomato', 'settings.yml')],
    base_dir=_BASE_DIR,  # 编码传入配置
)
