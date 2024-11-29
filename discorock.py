from flask import Flask,render_template,url_for, request, redirect, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user
from flask_mail import Mail, Message
from config import config
from werkzeug.security import generate_password_hash
import datetime
from models.ModelUser import ModelUser
from models.entities.User import User

discorockApp = Flask(__name__)  
db           = MySQL(discorockApp)
discorockApp.config.from_object(config['development'])
discorockApp.config.from_object(config['mail'])
db           = MySQL(discorockApp)
mail         = Mail(discorockApp)

#pythonanywhere
adminsesion  = LoginManager(discorockApp)

@adminsesion.user_loader
def agregarUsuario(id):
    return ModelUser.get_by_id(db,id)

@discorockApp.route('/')
def home():
    return render_template('usuarios.html')

@discorockApp.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave  = generate_password_hash(request.form['clave'])
        fechareg = datetime.datetime.now()
        regUsuario = db.connection.cursor()
        regUsuario.execute("INSERT INTO usuario (nombre,correo,clave,fechareg)VALUES (%s,%s,%s,%s)",(nombre,correo,clave,fechareg)) 
        db.connection.commit()
        msg = Message("Bienvenido a SoundWave", recipients=[correo])
        msg.html = render_template('mail.html', nombre  =   nombre)
        mail.send(msg)
        return render_template('home.html')
    else:
        return render_template('signup.html')
    
@discorockApp.route('/signin',methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        usuario = User(None,None,request.form['correo'],request.form['clave'],None,None)
        usuarioAutenticado = ModelUser.sigin(db, usuario)
        if usuarioAutenticado is not None:
            login_user(usuarioAutenticado)
            if usuarioAutenticado.clave:
                if usuarioAutenticado.perfil == 'A':
                    return render_template('admin.html')
                else:
                    return render_template('user.html')
            else:
                flash('Contraseña incorrecta')
                return redirect(request.url)
        else:
                flash('Usuario inexistente')
                return redirect(request.url)
    else:
        return render_template('signin.html')

@discorockApp.route('/signout',methods = ['GET','POST'])
def signout():
    logout_user()
    return redirect(url_for('home'))

@discorockApp.route('/sUsuario',methods = ['GET','POST'])
def sUsuario():
    selUsuario = db.connection.cursor()
    selUsuario.execute("SELECT * FROM usuario")
    u = selUsuario.fetchall()
    selUsuario.close()
    return render_template('usuarios.html',usuarios=u)

@discorockApp.route('/iUsuario',methods=['GET','POST'])
def iUsuario():
    nombre = request.form['nombre']
    correo = request.form['correo']
    clave  = generate_password_hash(request.form['clave'])
    fechareg = datetime.datetime.now()
    perfil = request.form['perfil']
    regUsuario = db.connection.cursor()
    regUsuario.execute("INSERT INTO usuario (nombre,correo,clave,fechareg,perfil)VALUES (%s,%s,%s,%s,%s)",(nombre,correo,clave,fechareg,perfil))
    db.connection.commit()
    regUsuario.close()
    flash('Usuario Registrado Correctamente')
    return redirect(url_for('sUsuario'))

@discorockApp.route('/uUsuario/<int:id>',methods=['GET','POST'])
def uUsuario(id):
    nombre = request.form['nombre']
    correo = request.form['correo']
    clave  = generate_password_hash(request.form['clave'])
    fechareg = datetime.datetime.now()
    perfil = request.form['perfil']
    actUsuario = db.connection.cursor()
    actUsuario.execute("UPDATE usuario SET nombre =%s, correo =%s, clave =%s, fechareg =%s, perfil =%s WHERE id = %s",(nombre,correo,clave,fechareg,perfil,id))
    db.connection.commit()
    actUsuario.close()
    flash('usuario actualizado')
    return redirect(url_for('sUsuario'))

@discorockApp.route('/dUsuario/<int:id>',methods=['GET','POST'])
def dUsuario(id):
    delUsuario = db.connection.cursor()
    delUsuario.execute("DELETE FROM usuario WHERE id = %s",(id,))
    db.connection.commit()
    delUsuario.close()
    flash('usuario eliminado')
    return redirect(url_for('sUsuario'))

@discorockApp.route('/sProducto',methods = ['GET','POST'])
def sProducto():
    selProducto = db.connection.cursor()
    selProducto.execute("SELECT * FROM producto")
    p = selProducto.fetchall()
    selProducto.close()
    return render_template('productos.html',productos=p)


if __name__ == '__main__':
    discorockApp.config.from_object(config['development'])
    discorockApp.run(port=3300)
