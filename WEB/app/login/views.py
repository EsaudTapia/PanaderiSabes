from flask import render_template,request,session,redirect,flash,url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security import login_required,roles_required ,current_user
from flask_security.utils import login_user, logout_user, hash_password, encrypt_password
from . import login
from .forms import Registro
from ..models import User
@login.route('/profile')
@login_required
@roles_required('ADMINISTRADOR')# autorizacion para el rol admn¿in
def profile():
    return render_template('inicio.html')


@login.route('/profileCli')
@login_required
@roles_required('CLIENTE')# autorizacion para el rol admn¿in
def profileCli():
    return render_template('inicio.html')


@login.route('/profileEmp')
@login_required
@roles_required('EMPLEADO')# autorizacion para el rol admn¿in
def profileEmp():
    return render_template('inicio.html')


@login.route("/iniciar")
def iniciar():
    form_login = Registro()
    context={
        'form_login':form_login
    }
    return render_template("login.html",**context)


@login.route("/iniciar",methods=['POST'])
def loginPost():
    email = request.form.get('emailLogin')
    password= request.form.get('passwordLogin')
    remember = True if request.form.get('remember') else False
   
   
    user= User.query.filter_by( email=email).first()
    
   
    if not user or not check_password_hash(user.password, password):
        flash('El usuario y/o la contraseña son incorrectos',category="error")
        return redirect(url_for('login.iniciar'))
   
   
   
    login_user(user,remember=remember)
    
    if not user.active:
            flash('El usuario esta inactivo en el sistema',category="error")
            logout_user()
            return redirect(url_for('login.iniciar'))
    if current_user.roles[0].name=="ADMINISTRADOR": 
        return redirect(url_for('login.profile'))
   
    if current_user.roles[0].name=="CLIENTE":
        return redirect(url_for('login.profileCli'))
    
    if current_user.roles[0].name=="EMPLEADO":
        return redirect(url_for('login.profileEmp'))
    form_login = Registro()
    context={
        'form_login':form_login
    }
   
    render_template("login.html",**context)
   
       
@login.route('/logout')
@login_required
def logout():
    #Cerramos la sessión
    logout_user()
    return redirect(url_for('login.iniciar'))