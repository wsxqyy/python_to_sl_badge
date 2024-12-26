<a href="https://github.com/wsxqyy/python_to_sl_badge/blob/main/README.md">通过中文阅读</a>       
# 🌟 python_to_sl_badge 🌟

## Introduction
🚀 **python_to_sl_badge** is a player title management system based on the Flask framework and MySQL database. It allows users to upload, search, and delete player title information, suitable for gaming communities and developers.

## Environment Setup and Configuration

### 🐍 Installing Python Environment
1. **Download and Install Python**:
   - Visit [Python's Official Website](https://www.python.org/downloads/) to download the Python installer suitable for your operating system.
   - Install Python, ensuring that Python is added to your system's environment variables.

2. **Install Flask**:
   - Open a terminal or command prompt and enter the following command to install Flask:
     ```
     pip install Flask
     ```

### 💾 Installing MySQL Database
1. **Download and Install MySQL**:
   - Visit [MySQL's Official Website](https://dev.mysql.com/downloads/) to download the MySQL Community Edition installer suitable for your operating system.
   - Install MySQL, and remember your database username and password during the installation process.

2. **Create Database and Table**:
   - Open MySQL command-line tools or use a MySQL client to connect to the MySQL server.
   - Create a new database:
     ```sql
     CREATE DATABASE game_player_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
     ```
   - Use the newly created database and create the `game_player` table:
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

## Usage

### 🛠️ Configure Database Connection
- In the `python_to_sl_badge.py` file, find the `db_config` dictionary and replace the placeholders with your MySQL database configuration information:
  ```python
  db_config = {
      'host': 'your_host',
      'database': 'game_player_db',
      'user': 'your_username',
      'password': 'your_password',
      'charset': 'utf8mb4'
  }
  ```

### 🌐 Running the Flask Application
- In the terminal or command prompt, navigate to the directory containing the `python_to_sl_badge.py` file.
- Run the following command to start the Flask application:
  ```
  python python_to_sl_badge.py
  ```
- Visit `http://127.0.0.1:5000/` in your browser to view the application interface.

### 📝 Operation Instructions
- **Upload Title**: Fill in the user ID, title, and title color in the form and click the "Upload" button to submit the information.
- **Search Title**: Enter the user ID, title, or title color in the search form and click the "Search" button to query the information.
- **Delete Title**: Check the entries you want to delete in the result table and click the "Delete Selected" button to delete the information.

## Modifying the Script

### 🛠️ Customize Database Operations
- Modify SQL query statements as needed to adapt to your database structure and business logic.

### 🖌️ Frontend Style Adjustments
- Directly edit the CSS style code in `HTML_TEMPLATE` to customize the appearance of the interface. For example:
- We first modify the text here:
  ![image](https://github.com/user-attachments/assets/a72481f4-37f5-477b-85b9-30cff07728ac) 

- We can then go to lines 95 and 92 of the code:
  ![image](https://github.com/user-attachments/assets/b20710e0-93c2-4290-9464-41279602318a) 

- Modify this section:
  ```python
  <div class="form-tips">Fanxing Snowball Technology production, if you have any questions or want to join, please contact Snowball.</div>
  <div class="form-tips"> Unauthorized use or malicious attacks on the server will bear legal responsibility, and we will record your IP.</div>
  ```

### 🔧 Backend Logic Adjustments
- Add or modify logic in Flask routes to implement additional features or optimize existing features.

## Database Table Structure

### 📌 `game_player` Table Structure
- **id**: Primary key, auto-incrementing, uniquely identifying each record.
- **user_id**: User ID, stores Steam's 64-bit numerical ID, type BIGINT.
- **badge**: Title, stores the player's title, type VARCHAR(255).
- **badge_color**: Title color, stores the color of the title, type VARCHAR(50).
- **created_at**: Creation time, records the time the title was created, type TIMESTAMP, default value is the current time.

## Conclusion

🌈 **Python to SL Badge System** provides a clean, intuitive interface and practical features to help users manage player titles. Whether you are a game developer or community administrator, you can easily manage title data through this system. We welcome you to experience and contribute code, let's build a better player title system together! 🚀🎉

### Please, give this project a star! Help a 16-year-old kid out!
---

*Please remember to replace the placeholders in the database configuration before deployment and ensure that the database service is running properly.* 🛠️💻

---

Regarding the images and links provided, it appears there was an issue with parsing them due to network reasons. If you need the content of these web pages, please check the legality of the web page links and try again. If the problem persists, it might be related to the links themselves or network issues. You can also try accessing the pages directly in your browser to see if they load correctly. If you have any specific questions about the content or need further assistance, feel free to ask!
