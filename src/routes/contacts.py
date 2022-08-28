from flask import Blueprint, render_template, request, redirect, url_for
from models.contact import Contact
from utils.db import db 

contacts = Blueprint('contacts', __name__)

#################### INDEX ####################
@contacts.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

#**********************************************

#################### NEW ####################
@contacts.route('/new', methods=['POST'])
def add_contact():
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]

    new_contact = Contact(fullname, email, phone)

    db.session.add(new_contact)
    db.session.commit()

    return redirect(url_for('contacts.index'))
    #return redirect('/')

#**********************************************

#################### UPDATE ####################
@contacts.route('/update/<id>')
def update(id):

    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]
    print(fullname, email, phone)

    return 'update a contact'
#**********************************************

#################### DELETE ####################
@contacts.route('/delete/<id>')
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    return redirect(url_for('contacts.index'))

#**********************************************