import random

from liteyuki import logger
from liteyuki.plugin import PluginMetadata, PluginType
from liteyuki.bot import get_config
from liteyuki.message.on import on_keywords

__plugin_meta__ = PluginMetadata(
    name="防断联插件",
    type=PluginType.APPLICATION
)

# 获取配置文件示例代码
keywords = get_config("antidislink.keywords", ["看看你的", "看看j", "给我看看", "看看J", "我要小正太"])
replies = get_config("antidislink.replies", ["No dislink", "严禁断联化"])


@on_keywords(keywords).handle()
async def _(event):
    event.reply(random.choice(replies))  # reply是无状态的，同步的，不需要await


logger.success(f"防断联插件已加载，关键词：{keywords}，回复：{replies}")
