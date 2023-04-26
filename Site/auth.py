from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import Users,db
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import login_required,login_user,logout_user,current_user


#Linking the blueprint
auth = Blueprint('auth',__name__)


#Login Route
@auth.route('/login',methods=['POST','GET'])
def Login():
    if request.method == 'POST':
        email = request.form.get('email')
        pwd1 = request.form.get('pwd1')

        user = Users.query.filter_by(email=email).first()
        if user:
             if check_password_hash(user.password,pwd1):
                  flash("Logged In Successfully!",category='success')
                  login_user(user,remember=True)
                  return redirect(url_for('views.home')) 
             else:
                   flash("Sorry,Incorrect password ",category='error')   
        elif pwd1 =='' and email=='':
             flash('Input fields cannot be empty',category='error')             
        else:
              flash("Email does not Exist",category='error') 

    return render_template('login.html',user=current_user)


#Sign Up Route
@auth.route('/sign-up',methods=['POST','GET'])
def Sign_Up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        pwd1 = request.form.get('pwd1')
        pwd2 = request.form.get('pwd2')

        user = Users.query.filter_by(email=email).first()
        if user:
             flash("Email already Exists,Use  a different Email Address!",category='error')
             return redirect(url_for('auth.Sign_Up')) 
        elif len(email)<4:
            flash("Email must be greater than 4 characters",category='error')
        elif len(firstname)<2:
            flash("FirstName must be greater than 2 characters",category='error')
        elif pwd1 =='' and pwd2=='':
             flash('Password fields cannot be empty',category='error')
        elif pwd1 != pwd2:
              flash("Sorry ,Passwords don't match, make sure they match before proceeding.",category='error')
        elif len(pwd1) and len(pwd2) <4:
              flash("Passwords must be greater than 4 characters",category='error')
        else:
               new_user = Users(email=email,firstname=firstname,password=generate_password_hash(pwd1,method='sha256'))
               db.session.add(new_user)
               db.session.commit()
               login_user(user.is_active(),remember=True)
               flash("Account created Successfully",category='success') 
               return redirect(url_for('views.home'))            
            
    return render_template("signup.html",user=current_user)


#Log Out Route
@auth.route('/log-out')
@login_required
def Log_Out():
    logout_user()
    return redirect(url_for('auth.Login')) 

























    