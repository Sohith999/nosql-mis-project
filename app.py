from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
import redis
from bson.objectid import ObjectId
import hashlib
import os

app = Flask(__name__, static_folder='.')
app.secret_key = 'your-secret-key-change-in-production'
CORS(app)

# MongoDB Connection
try:
    mongo_client = MongoClient('mongodb://localhost:27017/')
    db = mongo_client['nosql_mis_db']
    employees_collection = db['employees']
    projects_collection = db['projects']
    tasks_collection = db['tasks']
    users_collection = db['users']
    print("✅ Connected to MongoDB successfully")
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")

# Redis Connection
try:
    redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    redis_client.ping()
    print("✅ Connected to Redis successfully")
except Exception as e:
    print(f"❌ Redis connection failed: {e}")

def serialize_doc(doc):
    if doc and '_id' in doc:
        doc['_id'] = str(doc['_id'])
    return doc

# Serve frontend
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Authentication
@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        user = users_collection.find_one({'username': username, 'password': password_hash})
        
        if user:
            session_id = str(ObjectId())
            redis_client.setex(f'session:{session_id}', 86400, username)
            return jsonify({'success': True, 'session_id': session_id, 'username': username})
        else:
            return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/logout', methods=['POST'])
def logout():
    session_id = request.headers.get('Session-ID')
    if session_id:
        redis_client.delete(f'session:{session_id}')
    return jsonify({'success': True})

def require_auth(f):
    def wrapper(*args, **kwargs):
        session_id = request.headers.get('Session-ID')
        if not session_id or not redis_client.exists(f'session:{session_id}'):
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

# EMPLOYEES
@app.route('/api/employees', methods=['GET'])
@require_auth
def get_employees():
    cached = redis_client.get('employees_cache')
    if cached:
        import json
        return jsonify({'data': json.loads(cached), 'from_cache': True})
    
    employees = list(employees_collection.find())
    employees = [serialize_doc(emp) for emp in employees]
    
    import json
    redis_client.setex('employees_cache', 300, json.dumps(employees))
    return jsonify({'data': employees, 'from_cache': False})

@app.route('/api/employees', methods=['POST'])
@require_auth
def create_employee():
    data = request.json
    result = employees_collection.insert_one(data)
    redis_client.delete('employees_cache')
    return jsonify({'success': True, 'id': str(result.inserted_id)}), 201

@app.route('/api/employees/<employee_id>', methods=['PUT'])
@require_auth
def update_employee(employee_id):
    data = request.json
    result = employees_collection.update_one({'_id': ObjectId(employee_id)}, {'$set': data})
    redis_client.delete('employees_cache')
    return jsonify({'success': True, 'modified_count': result.modified_count})

@app.route('/api/employees/<employee_id>', methods=['DELETE'])
@require_auth
def delete_employee(employee_id):
    result = employees_collection.delete_one({'_id': ObjectId(employee_id)})
    redis_client.delete('employees_cache')
    return jsonify({'success': True, 'deleted_count': result.deleted_count})

# PROJECTS
@app.route('/api/projects', methods=['GET'])
@require_auth
def get_projects():
    cached = redis_client.get('projects_cache')
    if cached:
        import json
        return jsonify({'data': json.loads(cached), 'from_cache': True})
    
    projects = list(projects_collection.find())
    projects = [serialize_doc(proj) for proj in projects]
    
    import json
    redis_client.setex('projects_cache', 300, json.dumps(projects))
    return jsonify({'data': projects, 'from_cache': False})

@app.route('/api/projects', methods=['POST'])
@require_auth
def create_project():
    data = request.json
    result = projects_collection.insert_one(data)
    redis_client.delete('projects_cache')
    return jsonify({'success': True, 'id': str(result.inserted_id)}), 201

@app.route('/api/projects/<project_id>', methods=['PUT'])
@require_auth
def update_project(project_id):
    data = request.json
    result = projects_collection.update_one({'_id': ObjectId(project_id)}, {'$set': data})
    redis_client.delete('projects_cache')
    return jsonify({'success': True, 'modified_count': result.modified_count})

@app.route('/api/projects/<project_id>', methods=['DELETE'])
@require_auth
def delete_project(project_id):
    result = projects_collection.delete_one({'_id': ObjectId(project_id)})
    redis_client.delete('projects_cache')
    return jsonify({'success': True, 'deleted_count': result.deleted_count})

# TASKS
@app.route('/api/tasks', methods=['GET'])
@require_auth
def get_tasks():
    cached = redis_client.get('tasks_cache')
    if cached:
        import json
        return jsonify({'data': json.loads(cached), 'from_cache': True})
    
    tasks = list(tasks_collection.find())
    tasks = [serialize_doc(task) for task in tasks]
    
    import json
    redis_client.setex('tasks_cache', 300, json.dumps(tasks))
    return jsonify({'data': tasks, 'from_cache': False})

@app.route('/api/tasks', methods=['POST'])
@require_auth
def create_task():
    data = request.json
    result = tasks_collection.insert_one(data)
    redis_client.delete('tasks_cache')
    return jsonify({'success': True, 'id': str(result.inserted_id)}), 201

@app.route('/api/tasks/<task_id>', methods=['PUT'])
@require_auth
def update_task(task_id):
    data = request.json
    result = tasks_collection.update_one({'_id': ObjectId(task_id)}, {'$set': data})
    redis_client.delete('tasks_cache')
    return jsonify({'success': True, 'modified_count': result.modified_count})

@app.route('/api/tasks/<task_id>', methods=['DELETE'])
@require_auth
def delete_task(task_id):
    result = tasks_collection.delete_one({'_id': ObjectId(task_id)})
    redis_client.delete('tasks_cache')
    return jsonify({'success': True, 'deleted_count': result.deleted_count})

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 NoSQL MIS Server Starting...")
    print("="*50)
    print("📍 Server running at: http://localhost:5000")
    print("🌐 Open your browser and go to: http://localhost:5000")
    print("👤 Login: admin / admin123")
    print("="*50 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)