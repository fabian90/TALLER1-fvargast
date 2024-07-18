
# from models.guarderia import Guarderia
from flask import Flask, render_template,make_response,request
from flask_restful import Resource
from flask_login import login_required, current_user
from models.perros import  Perros
from models.cuidadores import Cuidadores
from db import db


class CuidadorPerroController(Resource):
    @login_required
    def get(self):
        try:
            print(current_user.is_admin)
            nombre = request.args.get('nombre')
            tabla = request.args.get('tabla')
            print(nombre)
            print(tabla)
            if tabla=='Cuidador':                
                mensaje= self.Update_Asignar_Perro(nombre)   
                return make_response(render_template('perros_mario.html', mensaje=mensaje))
            elif tabla=='Perro':
                 if current_user.is_admin:
                    perros = Perros.query.filter_by(nombre=nombre).all()
                    return make_response(render_template('consulta_lassie.html', perros=perros, mensaje=f"Hay {len(perros)} perros llamados {nombre}"))
                 else:
                     return (f"el usuario {current_user.username} no tiene permiso de administrador ingresa login http://127.0.0.1:5000/login")               
            else:
                error_message = (f"{str(e)} Por favor, ingresa los parámetros correctos en el siguiente enlace: "
                         "http://127.0.0.1:5000/consulta_nombre?tabla=Cuidador&&nombre=Mario")
                return make_response(render_template('error.html', mensaje=error_message), 500)
        except Exception as e:
            return make_response(render_template('error.html', mensaje=str(e)))
   
    @staticmethod
    def obtener_perros_por_peso_y_cuidador(peso_maximo, cuidador_id):
        cuidador = Cuidadores.query.get(cuidador_id)
        if cuidador:
            perros = Perros.query.filter(Perros.peso < peso_maximo, Perros.cuidador_id == cuidador.id).all()
            return make_response(render_template('perros_mario.html', perros=perros, mensaje=f"Mario tiene {len(perros)} perros con menos de {peso_maximo} kg"))
        return make_response(render_template('perros_mario.html', mensaje=f"No se encontró al cuidador con ID {cuidador_id}"))
   
    @staticmethod
    def Update_Asignar_Perro(nombre)->str:
        try:
            # Buscar al cuidador Mario
            mario = Cuidadores.query.filter_by(nombre=nombre).first()
            if not mario:
                raise ValueError(f"No se encontró un cuidador llamado '{nombre}'")

            # Actualizar la tabla perros para asignar los perros con peso < 3 a Mario
            Perros.query.filter(Perros.peso < 3).update({Perros.cuidador_id: mario.id})

            # Confirmar los cambios en la base de datos
            db.session.commit()

            # Devolver respuesta con plantilla renderizada
            return (f"Todos los perros con menos de 3 kg han sido asignados a Mario (ID: {mario.id})")
        except Exception as e:
            # En caso de error, hacer rollback de la transacción
            db.session.rollback()
            return str(e)