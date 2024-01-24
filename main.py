
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rent_tracker.db'
app.config['SECRET_KEY'] = 'supersecretkey'
db = SQLAlchemy(app)

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

class Rent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    month = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

class ElectricityMeterReading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    month = db.Column(db.String(20), nullable=False)
    reading = db.Column(db.Integer, nullable=False)

class CommonAreaMaintenance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    month = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    shops = Shop.query.all()
    return render_template('dashboard.html', shops=shops)

@app.route('/shop_details/<shop_id>')
def shop_details(shop_id):
    shop = Shop.query.get(shop_id)
    rents = Rent.query.filter_by(shop_id=shop_id).all()
    electricity_meter_readings = ElectricityMeterReading.query.filter_by(shop_id=shop_id).all()
    common_area_maintenance_expenses = CommonAreaMaintenance.query.filter_by(shop_id=shop_id).all()
    return render_template('shop_details.html', shop=shop, rents=rents, electricity_meter_readings=electricity_meter_readings, common_area_maintenance_expenses=common_area_maintenance_expenses)

@app.route('/mark_rent_paid/<rent_id>')
def mark_rent_paid(rent_id):
    rent = Rent.query.get(rent_id)
    rent.status = 'Paid'
    db.session.commit()
    return redirect(url_for('shop_details', shop_id=rent.shop_id))

@app.route('/mark_rent_unpaid/<rent_id>')
def mark_rent_unpaid(rent_id):
    rent = Rent.query.get(rent_id)
    rent.status = 'Unpaid'
    db.session.commit()
    return redirect(url_for('shop_details', shop_id=rent.shop_id))

@app.route('/enter_meter_reading/<shop_id>')
def enter_meter_reading(shop_id):
    return render_template('enter_meter_reading.html', shop_id=shop_id)

@app.route('/common_area_maintenance/<shop_id>')
def common_area_maintenance(shop_id):
    return render_template('common_area_maintenance.html', shop_id=shop_id)

@app.route('/generate_report/<report_type>')
def generate_report(report_type):
    if report_type == 'pdf':
        return 'PDF report generated successfully'
    elif report_type == 'csv':
        return 'CSV report generated successfully'
    elif report_type == 'json':
        return 'JSON report generated successfully'
    else:
        return 'Invalid report type'

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
