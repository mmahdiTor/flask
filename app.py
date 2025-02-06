from flask import Flask, jsonify, request

app = Flask(__name__)

# داده‌های تستی (در دنیای واقعی باید از دیتابیس استفاده شود)
users = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"},
]

# نمایش همه کاربران
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# دریافت اطلاعات یک کاربر با ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"message": "کاربر یافت نشد"}), 404

# اضافه کردن کاربر جدید
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = {"id": len(users) + 1, "name": data["name"]}
    users.append(new_user)
    return jsonify(new_user), 201

# حذف یک کاربر
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "کاربر حذف شد"}), 200

if __name__ == '__main__':
    app.run(debug=True)
