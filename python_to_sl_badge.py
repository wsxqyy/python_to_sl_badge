from flask import Flask, request, jsonify, render_template_string
import mysql.connector

app = Flask(__name__)

# 数据库配置
db_config = {
    'host': 'your_host',
    'database': 'game_player_db',
    'user': 'your_username',
    'password': 'your_password',
    'charset': 'utf8mb4'
}
# 连接数据库
cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()

# HTML模板，包括CSS样式
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>繁星--只做最好的服务器</title>
<style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 20px;
    }
    .container {
        max-width: 800px;
        margin: 50px auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    h2 {
        text-align: center;
        color: #333;
    }
    form {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    label {
        margin-top: 10px;
        font-weight: bold;
    }
    input[type="text"], button {
        padding: 10px;
        margin-top: 5px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-size: 16px;
    }
    button {
        background-color: #5cb85c;
        color: white;
        cursor: pointer;
        transition: background-color 0.3s;
        border: none;
    }
    button:hover {
        background-color: #4cae4c;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #f2f2f2;
    }
    .form-tips {
        font-size: 14px;
        color: #666;
        margin-top: 5px;
    }
</style>
</head>
<body>
<div class="container">
    <h2>玩家称号上传系统</h2>
    <div class="form-tips">繁星雪球技术出品，如果有疑问或想要加盟，请联系雪球。</div>
    <div class="form-tips"> 盗用或恶意攻击服务器将负法律责任，我们将记录您的IP。</div>
    <form id="uploadForm" method="post">
        <label for="user_id">用户ID:</label>
        <input type="text" id="user_id" name="user_id" required>
        
        <label for="badge">称号:</label>
        <input type="text" id="badge" name="badge">
        
        <label for="badge_color">称号颜色:</label>
        <input type="text" id="badge_color" name="badge_color">
        
        <div class="form-tips">颜色请用英文填写，用户ID请用Steam的64位ID，只要数字部分。</div>
        <button type="submit">上传</button>
        <div class="form-tips">搜索请填写下面框，上传请填写上面。</div>
    </form>
    <form id="searchForm" onsubmit="fetchData(); return false;">
        <label for="search_user_id">用户ID:</label>
        <input type="text" id="search_user_id" name="user_id">
        
        <label for="search_badge">称号:</label>
        <input type="text" id="search_badge" name="badge">
        
        <label for="search_badge_color">称号颜色:</label>
        <input type="text" id="search_badge_color" name="badge_color">
        
        <button type="submit">搜索</button>
    </form>
    <button class="delete-selected" onclick="deleteSelected()">删除选中</button>
    <table id="dataTable">
        <thead>
            <tr>
                <th><input type="checkbox" id="select-all" onclick="selectAll()"></th>
                <th>编号</th>
                <th>用户ID</th>
                <th>称号</th>
                <th>称号颜色</th>
                <th>创建时间</th>
            </tr>
        </thead>
        <tbody>
            <!-- 数据将通过JavaScript动态插入 -->
        </tbody>
    </table>
</div>
<script>
// JavaScript functions for form submission, data fetching, and delete operations
document.getElementById('uploadForm').onsubmit = function(e) {
    e.preventDefault();
    var formData = new FormData(this);
    fetch('/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if(data.message === "提交成功") {
            alert(data.message);
            document.getElementById('uploadForm').reset();
            fetchData();
        } else {
            alert(data.message);
        }
    })
    .catch(error => alert('糟糕，提交失败'));
};

function fetchData() {
    const searchUser = document.getElementById('search_user_id').value;
    const searchBadge = document.getElementById('search_badge').value;
    const searchBadgeColor = document.getElementById('search_badge_color').value;
    
    const searchParams = new URLSearchParams({
        user_id: searchUser,
        badge: searchBadge,
        badge_color: searchBadgeColor
    });
    
    fetch(`/data?${searchParams}`)
    .then(response => response.json())
    .then(data => {
        const tableBody = document.getElementById('dataTable').getElementsByTagName('tbody')[0];
        tableBody.innerHTML = '';
        data.forEach(row => {
            let rowHtml = `<tr>
                <td><input type="checkbox" class="select-row" value="${row.id}"></td>
                <td>${row.id}</td>
                <td>${row.user_id}</td>
                <td>${row.badge}</td>
                <td>${row.badge_color}</td>
                <td>${row.created_at}</td>
            </tr>`;
            tableBody.innerHTML += rowHtml;
        });
    })
    .catch(error => alert('糟糕，获取数据失败'));
}

function deleteSelected() {
    const selectedIds = Array.from(document.querySelectorAll('.select-row:checked')).map(checkbox => checkbox.value);
    if (selectedIds.length === 0) {
        alert('请选择至少一个条目进行删除。');
        return;
    }
    fetch('/delete', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ids: selectedIds })
    })
    .then(response => response.json())
    .then(data => {
        if(data.message === "删除成功") {
            alert(data.message);
            fetchData();
        } else {
            alert(data.message);
        }
    })
    .catch(error => alert('糟糕，删除失败'));
}

function selectAll() {
    const checkboxes = document.querySelectorAll('.select-row');
    checkboxes.forEach(checkbox => checkbox.checked = document.getElementById('select-all').checked);
}

window.onload = fetchData;
</script>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/submit', methods=['POST'])
def submit():
    user_id = request.form['user_id']
    badge = request.form['badge']
    badge_color = request.form['badge_color']
    query = ("INSERT INTO game_player (user_id, badge, badge_color, created_at) "
             "VALUES (%s, %s, %s, NOW())")
    try:
        cursor.execute(query, (user_id, badge, badge_color))
        cnx.commit()
        return jsonify({'message': '提交成功'})
    except mysql.connector.Error as err:
        cnx.rollback()
        return jsonify({'message': '数据库错误', 'error': str(err)})

@app.route('/data')
def data():
    user_id = request.args.get('user_id', '')
    badge = request.args.get('badge', '')
    badge_color = request.args.get('badge_color', '')
    query = "SELECT * FROM game_player WHERE 1"
    if user_id:
        query += " AND user_id LIKE %s"
    if badge:
        query += " AND badge LIKE %s"
    if badge_color:
        query += " AND badge_color LIKE %s"
    
    params = []
    if user_id:
        params.append('%' + user_id + '%')
    if badge:
        params.append('%' + badge + '%')
    if badge_color:
        params.append('%' + badge_color + '%')
    
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        data_list = [{'id': row[0], 'user_id': row[1], 'badge': row[2], 'badge_color': row[3], 'created_at': row[4]} for row in rows]
        return jsonify(data_list)
    except mysql.connector.Error as err:
        cnx.rollback()
        return jsonify({'message': '数据库错误', 'error': str(err)})

@app.route('/delete', methods=['POST'])
def delete_selected():
    data = request.json
    selected_ids = data.get('ids', [])
    
    if not selected_ids:
        return jsonify({'message': '没有选择任何条目'})
    
    try:
        cursor.executemany("DELETE FROM game_player WHERE id = %s", [(id,) for id in selected_ids])
        cnx.commit()
        return jsonify({'message': '删除成功'})
    except mysql.connector.Error as err:
        cnx.rollback()
        return jsonify({'message': '删除失败', 'error': str(err)})

if __name__ == '__main__':
    app.run(debug=True)