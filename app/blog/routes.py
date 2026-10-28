from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__, url_prefix="/blog", template_folder="templates")


#2.	Crea un módulo "blog" con una ruta /entrada/<id> que muestre el título de una entrada
@blog_bp.route('/')
def lista_entradas():
    return render_template('base.html')

@blog_bp.route('/entrada/<id>')
def mostrar_entrada(id):
    return f"<h3>Entrada: {id}</h3>"