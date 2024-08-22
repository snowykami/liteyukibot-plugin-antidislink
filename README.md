# liteyukibot-plugin-antidislink

<div align="center">
  <img src="https://cdn.liteyuki.icu/static/img/liteyuki_icon_640.png" width="180" height="180" alt="NoneBotPluginLogo">

</div>

<div align="center">

# liteyukibot-plugin-antidislink

_✨ 防止群友断联化 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/LiteyukiStudio/nonebot-plugin-acgnshow.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/liteyukibot-plugin-antidislink">
    <img src="https://img.shields.io/pypi/v/liteyukibot-plugin-antidislink.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">

</div>

## 📖 介绍

个别群友断联化(dislinklize)，其他群友苦不堪言，怎么办? 一个简单的 liteyukibot 示例插件，使用轻雪会话控制器。

## 💿 安装

<details open>
<summary>使用 pip 安装</summary>
在 轻雪 项目的根目录下打开命令行, 输入以下指令即可安装

    pip install liteyukibot-plugin-antidislink

</details>

<details>
<summary>使用包管理器安装</summary>
在 轻雪 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install liteyukibot-plugin-antidislink

</details>
<details>
<summary>pdm</summary>

    pdm add liteyukibot-plugin-antidislink

</details>
<details>
<summary>poetry</summary>

    poetry add liteyukibot-plugin-antidislink

</details>
<details>
<summary>conda</summary>

    conda install liteyukibot-plugin-antidislink

</details>
</details>

## 🎉 使用

### 测试运行

- 使用`pdm`
    
```shell
pdm run dev
```

- 或运行入口文件

```shell
python main.py
```

- 或自行通过开发工具运行

```python
from liteyuki.dev.plugin import run_plugins

if __name__ == "__main__":
    run_plugins("liteyukibot_plugin_antidislink")
```

### 装载到机器人程式运行(生产环境)

在轻雪配置文件中添加如下结构配置其一，使轻雪知晓应加载此插件

- 扁平化配置(推荐在少量配置时使用)

```yaml
liteyuki.plugins: [ ..., "liteyukibot_plugin_antidislink" ]

```

- 或普通配置(在主要配置文件中使用)

```yaml
liteyuki:
  plugins:
    ...
    - liteyukibot_plugin_antidislink
```

## ⚙️ 配置

参考LiteyukiBot的[配置文档](https://bot.liteyuki.icu/deploy/config.html)，在config下新建配置文件
使用如下配置项

```yaml
antidislink:
  keywords: [ "看看你的", "给我看看", "看看j" ]
  replies: [ "不看", "禁止断联化" ]
```

## ℹ️ 其他

- 无