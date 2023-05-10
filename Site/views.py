import dataclasses
from flask import Blueprint,render_template,request,flash,json,jsonify,redirect,url_for
from flask_login import current_user,login_required
from .models import Notes,db


#Linking the Blueprint
views = Blueprint('views',__name__)


#Home Route
@views.route('/',methods=['POST','GET'])
@login_required
def home():
    if request.method=='POST':
        note = request.form.get('note')
         
        if note == '':
            flash("Note cannot be Empty",category='error')
        elif len(note)<5:
            flash("Your Note is too short!!",category='error')
        else:
            add_note=Notes(content=note,user_id=current_user.id) 
            db.session.add(add_note)   
            db.session.commit()
            flash("Note Added Successfully",category='success')
    return render_template('home.html',user=current_user)

#Deleting a particular Note
@views.route('/delete-note',methods=['POST'])
def Delete_note():
    note = json.loads(request.data)
    note_id = note['note_id']
    note =Notes.query.get(note_id)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})


#Admin Route In Progress
@views.route('/Admin',methods=['POST','GET'])
def Admin():
  if request.method=='POST':
      username= request.form.get('admin-username')
      pwd =request.form.get('pwd')
      if username =='':
        flash("Sorry Username cannot be Empty!!",category='error')
      elif username<3:
        flash("Username cannot be less than three characters!!",category='error')
      elif pwd=='':
          flash("Password cannot be  Empty!!",category='error')          
      admin= Admin(username=username,pwd=pwd)
      db.session.add(admin)
      db.session.commit()
      flash("Admin Login Successful!!",category='success')
      return redirect(url_for('views.dashboard'))
  

@views.route('/Dashboard',methods=['POST','GET'])
def Dashboard():
  return "<h1>Building the dashboard page</h1>"
       





      




