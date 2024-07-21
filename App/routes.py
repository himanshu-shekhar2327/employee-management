from flask import Blueprint, request, jsonify, abort
from .schemas import EmployeeSchema
from .models import Employee
from .db_instance import db

# Create a Blueprint
employees_bp = Blueprint('employees', __name__)

employee_schema = EmployeeSchema()
# employee_schema = EmployeeSchema(many=True)

# Homepage route
@employees_bp.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the Employee Management System!"})

# Create a new employee
@employees_bp.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    print(data,"Received data")#debugging statement
    errors = employee_schema.validate(data)
    if errors:
        print(errors,"Validation errors")
        return jsonify(errors), 400
    new_employee = Employee(name=data['name'], department=data['department'], age=data['age'])
    db.session.add(new_employee)
    db.session.commit()
    return "Employee created successfully", 201

# Get all employees
@employees_bp.route('/employees', methods=['GET'])
def get_all_employees():
    employees = Employee.query.all()
    data = [emp.to_dict() for emp in employees]
    return jsonify(data)

# Get employee by ID
@employees_bp.route('/employee/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        abort(404, description=f"Employee with id {id} not found!")
    result = employee_schema.dump(employee)
    return jsonify(result)

# Update employee details
@employees_bp.route('/employee/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    errors = employee_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    employee = Employee.query.get_or_404(id)
    employee.name = data['name']
    employee.department = data['department']
    employee.age = data['age']
    db.session.commit()
    result = employee_schema.dump(employee)
    return jsonify(result)

# Delete an employee
@employees_bp.route('/employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted successfully'})