import usuarios.conexion as conexion
import hashlib

connect = conexion.connect()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre_usuario, apellido_usuario, correo, contrasena, id_tipo_documento, numero_documento, direccion, telefono, edad, altura, peso, id_rol=1, estado='activo'):
        self.nombre_usuario = nombre_usuario
        self.apellido_usuario = apellido_usuario
        self.correo = correo
        self.contrasena = contrasena
        self.id_tipo_documento = id_tipo_documento
        self.numero_documento = numero_documento
        self.direccion = direccion
        self.telefono = telefono
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.id_rol = id_rol
        self.estado = estado

    def registrar(self):
        sql = """
            INSERT INTO usuarios (
                nombre_usuario, apellido_usuario, correo, contrasena, 
                id_tipo_documento, numero_documento, estado, direccion, 
                telefono, edad, altura, peso, id_rol
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        usuario = (
            self.nombre_usuario,
            self.apellido_usuario,
            self.correo,
            self.contrasena,
            self.id_tipo_documento,
            self.numero_documento,
            self.estado,
            self.direccion,
            self.telefono,
            self.edad,
            self.altura,
            self.peso,
            self.id_rol
        )

        try:
            cursor.execute(sql, usuario)
            database.commit()
            return [cursor.rowcount, self]
        except Exception as e:
            print(f"\n[Error de Base de Datos]: {e}")
            return [0, None]

    def identificar(self):
        database, cursor = connect()

        cifrado = hashlib.sha256()
        cifrado.update(self.contrasena.encode('utf8'))

        sql = "SELECT * FROM usuarios WHERE numero_documento = %s AND contrasena = %s"
        datos = (self.numero_documento, cifrado.hexdigest())

        cursor.execute(sql, datos)
        result = cursor.fetchone()

        return result