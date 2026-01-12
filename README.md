# 🚀 NoSQL Management Information System (MIS)

A full-stack web application demonstrating CRUD operations using two NoSQL databases: **MongoDB** and **Redis**.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![MongoDB](https://img.shields.io/badge/mongodb-7.0-green.svg)
![Redis](https://img.shields.io/badge/redis-5.0+-red.svg)

---

## 📋 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [API Documentation](#-api-documentation)
- [Screenshots](#-screenshots)
- [Database Schema](#-database-schema)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### Core Functionality
- ✅ **User Authentication** - Login/Logout with session management
- ✅ **Employee Management** - Complete CRUD operations
- ✅ **Project Tracking** - Manage projects with budgets and timelines
- ✅ **Task Assignment** - Track tasks with priorities and status
- ✅ **Real-time Caching** - Redis-powered data caching for performance
- ✅ **Responsive UI** - Modern, mobile-friendly interface

### Technical Features
- 🗄️ **MongoDB** - Document-based data storage
- 🔴 **Redis** - Session management and caching
- 🔐 **Secure Authentication** - SHA256 password hashing
- 🌐 **RESTful API** - Clean API architecture
- 📊 **Data Validation** - Input sanitization and validation
- ⚡ **Performance Optimization** - Query optimization and indexing

---

## 🛠️ Tech Stack

### Backend
- **Python 3.8+**
- **Flask** - Web framework
- **PyMongo** - MongoDB driver
- **Redis-py** - Redis client
- **Flask-CORS** - Cross-origin resource sharing

### Frontend
- **HTML5**
- **CSS3** - Custom styling
- **Vanilla JavaScript** - No framework dependencies

### Databases
- **MongoDB 7.0** - Primary data storage
- **Redis 5.0+** - Session management & caching

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **MongoDB 7.0 or higher** - [Download MongoDB](https://www.mongodb.com/try/download/community)
- **Redis 5.0 or higher** - [Download Redis](https://redis.io/download)
- **Git** - [Download Git](https://git-scm.com/downloads)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/nosql-mis-project.git
cd nosql-mis-project
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start MongoDB

**Windows:**
```cmd
net start MongoDB
```

**Mac:**
```bash
brew services start mongodb-community
```

**Linux:**
```bash
sudo systemctl start mongod
```

### 5. Initialize Database

```bash
mongosh < database_setup.js
```

Expected output:
```
✅ Employees collection created
✅ Projects collection created
✅ Tasks collection created
✅ Users collection created
✅ Database setup completed successfully!
```

### 6. Start Redis

**Windows (WSL):**
```bash
wsl
sudo service redis-server start
```

**Mac:**
```bash
brew services start redis
```

**Linux:**
```bash
sudo systemctl start redis
```

Verify Redis is running:
```bash
redis-cli ping
# Should return: PONG
```

### 7. Run the Application

```bash
python app.py
```

The application will start on **http://localhost:5000**

---

## 🎯 Usage

### Default Login Credentials

| Username | Password | Role |
|----------|----------|------|
| admin | admin123 | Administrator |
| manager | manager123 | Manager |

### Accessing the Application

1. Open your web browser
2. Navigate to `http://localhost:5000`
3. Login with the credentials above
4. Start managing employees, projects, and tasks!

### Basic Operations

#### Employee Management
- **Create**: Click "+ Add Employee" button
- **Read**: View all employees in the table
- **Update**: Click "Edit" button on any employee
- **Delete**: Click "Delete" button (with confirmation)

#### Project Management
- **Create**: Add new projects with client and budget details
- **Update**: Modify project status, dates, and budget
- **Track**: Monitor project progress (Planning → In Progress → Completed)

#### Task Management
- **Assign**: Link tasks to projects and assign team members
- **Prioritize**: Set priority levels (Low, Medium, High)
- **Monitor**: Track task status and due dates

---

## 📁 Project Structure

```
nosql-mis-project/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── database_setup.js           # MongoDB initialization script
├── index.html                  # Frontend interface
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
│
├── screenshots/                # Application screenshots
│   ├── login.png
│   ├── employees.png
│   ├── projects.png
│   └── tasks.png
│
└── redis_data/                 # Redis persistence (not in repo)
    └── dump_mis.rdb
```

---

## 🔌 API Documentation

### Authentication Endpoints

#### Login
```http
POST /api/login
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}

Response:
{
  "success": true,
  "session_id": "abc123...",
  "username": "admin"
}
```

#### Logout
```http
POST /api/logout
Session-ID: {session_id}

Response:
{
  "success": true
}
```

### Employee Endpoints

```http
GET    /api/employees           # Get all employees
POST   /api/employees           # Create employee
PUT    /api/employees/:id       # Update employee
DELETE /api/employees/:id       # Delete employee
```

### Project Endpoints

```http
GET    /api/projects            # Get all projects
POST   /api/projects            # Create project
PUT    /api/projects/:id        # Update project
DELETE /api/projects/:id        # Delete project
```

### Task Endpoints

```http
GET    /api/tasks               # Get all tasks
POST   /api/tasks               # Create task
PUT    /api/tasks/:id           # Update task
DELETE /api/tasks/:id           # Delete task
```

**Note:** All endpoints (except login) require `Session-ID` header.

---

## 📸 Screenshots

### Login Page
![Login Page](screenshots/login.png)

### Employee Management
![Employees](screenshots/employees.png)

### Project Dashboard
![Projects](screenshots/projects.png)

### Task Tracking
![Tasks](screenshots/tasks.png)

---

## 🗄️ Database Schema

### MongoDB Collections

#### Employees Collection
```json
{
  "_id": ObjectId("..."),
  "name": "John Doe",
  "email": "john@company.com",
  "department": "Engineering",
  "position": "Senior Developer",
  "salary": 95000,
  "createdAt": ISODate("2024-01-01")
}
```

#### Projects Collection
```json
{
  "_id": ObjectId("..."),
  "name": "Website Redesign",
  "client": "Acme Corp",
  "budget": 50000,
  "status": "In Progress",
  "startDate": "2024-01-15",
  "endDate": "2024-06-30",
  "createdAt": ISODate("2024-01-01")
}
```

#### Tasks Collection
```json
{
  "_id": ObjectId("..."),
  "title": "Design Homepage",
  "projectId": ObjectId("..."),
  "assignee": "John Doe",
  "priority": "High",
  "status": "In Progress",
  "dueDate": "2024-02-15",
  "createdAt": ISODate("2024-01-01")
}
```

### Redis Keys

```
session:{session_id}           # User sessions (TTL: 24 hours)
employees_cache                # Cached employee data (TTL: 5 minutes)
projects_cache                 # Cached project data (TTL: 5 minutes)
tasks_cache                    # Cached task data (TTL: 5 minutes)
```

---

## 🧪 Testing

### Manual Testing

1. **Test Authentication:**
   - Try invalid credentials (should fail)
   - Login with valid credentials (should succeed)
   - Logout and verify session is cleared

2. **Test CRUD Operations:**
   - Create new employee/project/task
   - Read and verify data appears
   - Update existing records
   - Delete records with confirmation

3. **Test Caching:**
   - Make first request (cache miss)
   - Make second request within 5 minutes (cache hit)
   - Check Redis: `GET employees_cache`

### Database Verification

**MongoDB:**
```bash
mongosh nosql_mis_db

# View all employees
db.employees.find().pretty()

# Count documents
db.employees.countDocuments()

# Find by department
db.employees.find({department: "Engineering"})
```

**Redis:**
```bash
redis-cli

# View all keys
KEYS *

# Get session
GET session:your_session_id

# Check TTL
TTL employees_cache
```

---

## 🔒 Security Considerations

- ✅ Passwords are hashed using SHA256
- ✅ Sessions auto-expire after 24 hours
- ✅ CORS enabled for specific origins
- ✅ Input validation on all forms
- ✅ Parameterized MongoDB queries
- ⚠️ **For Production:** Use environment variables for secrets
- ⚠️ **For Production:** Implement JWT tokens
- ⚠️ **For Production:** Add rate limiting

---

## 🚀 Deployment

### Production Checklist

- [ ] Use environment variables for sensitive data
- [ ] Enable MongoDB authentication
- [ ] Configure Redis password
- [ ] Use HTTPS
- [ ] Set up database backups
- [ ] Implement logging
- [ ] Add monitoring
- [ ] Configure firewall rules
- [ ] Use production WSGI server (Gunicorn/uWSGI)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- Sohith Sai Doddapaneni- [GitHub Profile](https://github.com/sohith999)

---

## 🙏 Acknowledgments

- Flask documentation
- MongoDB documentation
- Redis documentation
- Python community

---

## 📧 Contact

For questions or support, please contact:
- Email: doddapanenisai9@gmail.com
- GitHub: [@YOUR_USERNAME](https://github.com/Sohith9999)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/doddapanenisai9)

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/nosql-mis-project)
![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/nosql-mis-project)
![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/nosql-mis-project)

---

**Made with ❤️ using Python, MongoDB, and Redis**
