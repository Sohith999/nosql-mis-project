// MongoDB Database Setup Script
// Run this with: mongosh < database_setup.js

db = db.getSiblingDB('nosql_mis_db');

// Drop existing collections
db.employees.drop();
db.projects.drop();
db.tasks.drop();
db.users.drop();

print("Creating collections...");

// Create Employees collection
db.createCollection("employees");
print("✅ Employees collection created");

// Create Projects collection
db.createCollection("projects");
print("✅ Projects collection created");

// Create Tasks collection
db.createCollection("tasks");
print("✅ Tasks collection created");

// Create Users collection
db.createCollection("users");
print("✅ Users collection created");

// Create indexes
db.employees.createIndex({ email: 1 }, { unique: true });
db.employees.createIndex({ department: 1 });
db.projects.createIndex({ status: 1 });
db.tasks.createIndex({ status: 1 });
db.users.createIndex({ username: 1 }, { unique: true });
print("✅ Indexes created");

// Insert sample employees
db.employees.insertMany([
  {
    name: "John Doe",
    email: "john@company.com",
    department: "Engineering",
    position: "Senior Developer",
    salary: 95000,
    createdAt: new Date()
  },
  {
    name: "Jane Smith",
    email: "jane@company.com",
    department: "Marketing",
    position: "Marketing Manager",
    salary: 85000,
    createdAt: new Date()
  },
  {
    name: "Mike Johnson",
    email: "mike@company.com",
    department: "Sales",
    position: "Sales Lead",
    salary: 90000,
    createdAt: new Date()
  }
]);
print("✅ Sample employees inserted");

// Insert sample projects
db.projects.insertMany([
  {
    name: "Website Redesign",
    client: "Acme Corp",
    budget: 50000,
    status: "In Progress",
    startDate: "2024-01-15",
    endDate: "2024-06-30",
    createdAt: new Date()
  },
  {
    name: "Mobile App Development",
    client: "TechStart Inc",
    budget: 120000,
    status: "Planning",
    startDate: "2024-03-01",
    endDate: "2024-12-31",
    createdAt: new Date()
  }
]);
print("✅ Sample projects inserted");

// Insert sample tasks
var project1 = db.projects.findOne({name: "Website Redesign"});
var project2 = db.projects.findOne({name: "Mobile App Development"});

db.tasks.insertMany([
  {
    title: "Design Homepage",
    projectId: project1._id,
    assignee: "John Doe",
    priority: "High",
    status: "In Progress",
    dueDate: "2024-02-15",
    createdAt: new Date()
  },
  {
    title: "Setup CI/CD Pipeline",
    projectId: project2._id,
    assignee: "Jane Smith",
    priority: "Medium",
    status: "Not Started",
    dueDate: "2024-03-10",
    createdAt: new Date()
  }
]);
print("✅ Sample tasks inserted");

// Insert users (password: admin123 and manager123)
db.users.insertMany([
  {
    username: "admin",
    password: "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9",
    role: "admin",
    createdAt: new Date()
  },
  {
    username: "manager",
    password: "6ee4a469cd4e91053847f5d3fcb61dbcc91e8f0ef10be7748da4c4a1ba382d17",
    role: "manager",
    createdAt: new Date()
  }
]);
print("✅ Users inserted");

print("\n" + "=".repeat(50));
print("✅ Database setup completed successfully!");
print("=".repeat(50));
print("Database: nosql_mis_db");
print("Collections: employees, projects, tasks, users");
print("Sample data inserted");
print("\nLogin Credentials:");
print("  Username: admin  | Password: admin123");
print("  Username: manager | Password: manager123");
print("=".repeat(50) + "\n");