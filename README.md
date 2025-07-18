# 🕒 Telegram 昵称自动更新时间机器人

这是一个基于 Python + Telethon 的 Telegram 客户端自动化脚本，用于**每隔 30 秒更新 Telegram 昵称为当前时间**，适合用作“心跳昵称”展示你在线活跃状态。

---

## ✨ 功能特色

- 每 30 秒自动更新昵称（格式：`昵称 2025-07-18 21:00`）
- 程序中断会自动恢复原昵称
- 支持 emoji 昵称
- 支持 Ubuntu、CentOS、Debian 等主流系统
- 支持后台常驻运行（nohup / screen / tmux）
- 支持开机自启（配合 systemd 可选）

---

## 🚀 快速部署

### 1. 一键安装依赖（自动创建虚拟环境）

```bash
chmod +x an.sh
./an.sh
```

---

## 🔐 获取 Telegram API 授权

访问官方接口平台，申请 API ID 和 Hash：

1. 打开链接：  
   👉 https://my.telegram.org/

2. 登录 Telegram 手机号（含区号，如：`+8613812345678`）

3. 点击 `API Development Tools`

4. 填写以下信息：

   - **App title**：任意名称（如：`AutoNickBot`）
   - **Short name**：任意短名（如：`autonick`）

5. 创建后你会获得：

   - `api_id`
   - `api_hash`

---

## ⚙️ 配置参数

编辑 `tg_username_update.py` 文件，找到以下位置并填入你的凭证：

```python
api_id = 你的api_id
api_hash = '你的api_hash'
```

---

## ▶️ 首次运行主程序

```bash
# 激活虚拟环境
source venv/bin/activate

# 启动主程序
python3 tg_username_update.py
```

**首次运行流程如下：**

- 输入你的手机号（如：`+8613812345678`）
- Telegram 会发送验证码 → 输入验证码
- 如果开启了两步验证 → 输入密码

**成功后显示：**  
```
It works!
```
**完成后会生成两个文件然后进入虚拟环境杀掉当前进程然后下一步操作**  

## ♻️ 后台运行（终端断开后仍继续运行）

推荐方式：`nohup`

```bash
# 杀掉旧进程（如已运行）
ps aux | grep tg_username_update.py
kill 进程号

# 激活虚拟环境
source venv/bin/activate

# 启动后台进程
nohup python3 tg_username_update.py > run.log 2>&1 &
```

查看运行日志：

```bash
tail -f run.log
```

---

## 🛠 二次开发说明

本项目由原帖进行二次开发扩展而来，原始灵感和基础结构参考自：

🔗 [https://hostloc.com/thread-516863-1-1.html](https://hostloc.com/thread-516863-1-1.html)

特别致谢原帖作者提供的思路参考。

---

## 📦 requirements.txt 内容

如需手动安装依赖：

```bash
pip install setuptools emoji telethon
```

---



## 📜 LICENSE

本项目使用 **MIT 开源许可证**。可自由使用、分发与修改。

---

## ⭐️ Star 鼓励创作

如果这个脚本对你有帮助，请帮忙点个 Star ⭐️ 支持一下！

---
