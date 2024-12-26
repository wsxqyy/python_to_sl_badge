<a href="https://github.com/wsxqyy/python_to_sl_badge/blob/main/en_README.md">Read through English documents</a>
# 🌟 python_to_sl_badge 🌟

## 简介
🚀 **python_to_sl_badge** 是一个基于 Flask 框架和 MySQL 数据库的玩家称号管理系统。它允许用户上传、搜索和删除玩家称号信息，适用于游戏社区和开发者。

## 安装和配置环境

### 🐍 安装 Python 环境
1. **下载和安装 Python**：
   - 访问 [Python 官网](https://www.python.org/downloads/) 下载适合您操作系统的 Python 安装包。
   - 安装 Python，并确保将 Python 添加到系统环境变量中。

2. **安装 Flask**：
   - 打开终端或命令提示符，输入以下命令安装 Flask：
     ```
     pip install Flask
     ```

### 💾 安装 MySQL 数据库
1. **下载和安装 MySQL**：
   - 访问 [MySQL 官网](https://dev.mysql.com/downloads/) 下载适合您操作系统的 MySQL 社区版安装包。
   - 安装 MySQL，并在安装过程中记下您的数据库用户名和密码。

2. **创建数据库和表**：
   - 打开 MySQL 命令行工具或使用 MySQL 客户端连接到 MySQL 服务器。
   - 创建一个新的数据库：
     ```sql
     CREATE DATABASE game_player_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
     ```
   - 使用新创建的数据库，并创建 `game_player` 表：
     ```sql
     USE game_player_db;

     CREATE TABLE game_player (
       id INT AUTO_INCREMENT PRIMARY KEY,
       user_id BIGINT NOT NULL,
       badge VARCHAR(255) NOT NULL,
       badge_color VARCHAR(50) NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
     ```

## 使用方法

### 🛠️ 配置数据库连接
- 在 `python_to_sl_badge.py` 文件中，找到 `db_config` 字典，并替换其中的占位符为您的 MySQL 数据库配置信息：
  ```python
  db_config = {
      'host': 'your_host',
      'database': 'game_player_db',
      'user': 'your_username',
      'password': 'your_password',
      'charset': 'utf8mb4'
  }
  ```
![image](https://github.com/user-attachments/assets/40283e19-e0b6-4aa2-9f31-a934d839d606)

### 🌐 运行 Flask 应用
- 在终端或命令提示符中，导航到包含 `python_to_sl_badge.py` 文件的目录。
- 运行以下命令启动 Flask 应用：
  ```
  python python_to_sl_badge.py
  ```
- 访问 `http://127.0.0.1:5000/` 在浏览器中查看应用界面。
- 打开之后您的界面就是这样的：
![image](https://github.com/user-attachments/assets/4ddf3288-ed2f-414d-a10c-08ebfc654ba0)



### 📝 操作说明
- **上传称号**：在表单中填写用户ID、称号和称号颜色，点击“上传”按钮提交信息。
- **搜索称号**：在搜索表单中输入用户ID、称号或称号颜色，点击“搜索”按钮查询信息。
- **删除称号**：在结果表格中勾选要删除的条目，点击“删除选中”按钮删除信息。

## 修改脚本

### 🛠️ 自定义数据库操作
- 根据需要修改 SQL 查询语句，以适应您的数据库结构和业务逻辑。

### 🖌️ 前端样式调整
- 直接编辑 `HTML_TEMPLATE` 中的 CSS 样式代码，以自定义界面的外观。比如：
- 我们先修改这里的文字
![image](https://github.com/user-attachments/assets/a72481f4-37f5-477b-85b9-30cff07728ac)

- 我们就可以来到代码的第95和第92行：
![image](https://github.com/user-attachments/assets/b20710e0-93c2-4290-9464-41279602318a)

- 修改这一段：
  ```python
    <div class="form-tips">繁星雪球技术出品，如果有疑问或想要加盟，请联系雪球。</div>
    <div class="form-tips"> 盗用或恶意攻击服务器将负法律责任，我们将记录您的IP。</div>
  
- 其中的：
  ```python
  繁星雪球技术出品，如果有疑问或想要加盟，请联系雪球。
  盗用或恶意攻击服务器将负法律责任，我们将记录您的IP。

### 🔧 后端逻辑调整
- 在 Flask 路由中添加或修改逻辑，以实现额外的功能或优化现有功能。

## 数据库表结构

### 📌 `game_player` 表结构
- **id**：主键，自动增长，唯一标识每条记录。
- **user_id**：用户ID，存储 Steam 的64位数字ID，类型为 BIGINT。
- **badge**：称号，存储玩家的称号，类型为 VARCHAR(255)。
- **badge_color**：称号颜色，存储称号的颜色，类型为 VARCHAR(50)。
- **created_at**：创建时间，记录称号创建的时间，类型为 TIMESTAMP，默认值为当前时间。

## 结语

🌈 **Python to SL Badge System** 提供了一个简洁、直观的界面和实用的功能，帮助用户管理玩家称号。无论是游戏开发者还是社区管理员，都能通过这个系统轻松管理称号数据。欢迎体验并贡献代码，让我们共同打造更好的玩家称号系统！🚀🎉
### 求求了，给孩子点个star吧！帮助一个只有16岁的小朋友吧！
---

*请记得在部署前替换数据库配置中的占位符，并确保数据库服务正常运行。* 🛠️💻
