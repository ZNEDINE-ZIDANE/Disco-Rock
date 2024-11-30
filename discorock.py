from flask import Flask,render_template,url_for, request, redirect, flash, session
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, current_user
from flask_mail import Mail, Message
from config import config
from werkzeug.security import generate_password_hash
import datetime
from models.ModelUser import ModelUser
from models.entities.User import User
import os
discorockApp = Flask(__name__)  


discorockApp.config.from_object(config['development'])
discorockApp.config.from_object(config['mail'])
db           = MySQL(discorockApp)
mail         = Mail(discorockApp)

#pythonanywhere
adminsesion  = LoginManager(discorockApp)

@adminsesion.user_loader
def agregarUsuario(id):
    return ModelUser.get_by_id(db,id)

@discorockApp.context_processor
def barrotas():
    if current_user.is_authenticated:
        inu = f'<a class="nav-link active" aria-current="page">{current_user.nombre}</a>'
        re = '<a class="nav-link" href="/signout">Cerrar Sesion</a>'
    else:
        inu = '<a class="nav-link active" aria-current="page" href="/signin">Iniciar Sesion</a>'
        re = '<a class="nav-link" href="/signup">Registrar</a>'

    #asar las variables a layout
    return dict(iniciar=inu, registrar=re)


@discorockApp.route('/')
def home():
    return render_template('home.html')

@discorockApp.route('/user')
def usurs():
    return render_template('user.html')

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

        msg = Message(subject='Bienvenido a Spendy', recipients=[correo])
        msg.html = render_template('mail.html', nombre=nombre)
        with discorockApp.open_resource(os.path.join('static', 'img', 'guta.jpg')) as img:
                msg.attach('guta.jpg', 'image/jpg', img.read(), headers={'Content-ID': '<Img>'})
        
        mail.send(msg)
        return render_template('home.html')
    else:
        return render_template('signup.html')
    
@discorockApp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        usuario = User(0, None, request.form['correo'], request.form['clave'], None, None)

        usuarioAutenticado = ModelUser.sigin(db, usuario)
        if usuarioAutenticado is not None:
            if usuarioAutenticado.clave:  
                login_user(usuarioAutenticado)
                session['NombreU'] = usuarioAutenticado.nombre
                session['PerfilU'] = usuarioAutenticado.perfil
                if usuarioAutenticado.perfil == 'U':
                    return render_template('user.html')  
                else:
                    render_template('admin.html') 
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

@discorockApp.route('/iProducto', methods=['GET', 'POST'])
def agregarProducto():
    if request.method == 'POST':
        
        anio = request.form['nombre']
        producto = request.form['precio']
        cantidad = request.form['cantidad']
        precio = request.form['categoria']
        
        
        cursor = db.connection.cursor()
        cursor.execute("""
            INSERT INTO producto (nombre, precio, cantidad, categoria)
            VALUES (%s, %s, %s, %s)
        """, (anio, producto, cantidad, precio))
        db.connection.commit()
        cursor.close()
        
      
        return redirect(url_for('sProducto'))
    
    return render_template('agregarProducto.html')

@discorockApp.route('/uProducto/<int:idProducto>', methods=['GET', 'POST'])
def modificarProducto(idProducto):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM producto WHERE idProducto = %s", (idProducto,))
    producto = cursor.fetchone()
    
    if request.method == 'POST':
       
        anio = request.form['nombre']
        producto_nombre = request.form['precio']
        cantidad = request.form['cantidad']
        precio = request.form['categoria']
        
        
        cursor.execute("""
            UPDATE producto
            SET nombre = %s, precio = %s, cantidad = %s, categoria = %s
            WHERE idProducto = %s
        """, (anio, producto_nombre, cantidad, precio, idProducto))
        db.connection.commit()
        cursor.close()
        
        
        return redirect(url_for('sProducto'))
    
    return render_template('modificarProducto.html', producto=producto)

@discorockApp.route('/dProducto/<int:idProducto>', methods=['GET', 'POST'])
def eliminarProducto(idProducto):
    if request.method == 'POST':
        
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM producto WHERE idProducto = %s", (idProducto,))
        db.connection.commit()
        cursor.close()
        return redirect(url_for('sProducto'))
    return render_template('eliminarProducto.html', idProducto=idProducto)



if __name__ == '__main__':
    discorockApp.config.from_object(config['development'])
    discorockApp.run(port=3300)
