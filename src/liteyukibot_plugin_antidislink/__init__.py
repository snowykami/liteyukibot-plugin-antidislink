import random
from liteyuki.plugin import PluginMetadata, PluginType

from liteyuki.message.on import on_keywords

__plugin_meta__ = PluginMetadata(
    name="防断联插件",
    type=PluginType.APPLICATION
)


@on_keywords(["看看你的", "看看j", "给我看看", "看看J", "我要小正太"]).handle()
async def _(event):
    event.reply(random.choice(["No dislink", "严禁断联化"]))