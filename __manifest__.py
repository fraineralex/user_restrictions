{
    'name': 'User Restrictions',
    'version': '1.0',
    'summary': 'Restricciones de usuario: Evita que los usuarios modifiquen otros usuarios si no pertenecen al grupo de Recursos Humanos.',
    'description': 'Este módulo implementa restricciones para evitar que los usuarios modifiquen los datos de otros usuarios en Odoo, a menos que pertenezcan al grupo de Recursos Humanos. Si un usuario no pertenece a ese grupo, no podrá realizar cambios en los registros de usuarios.',
    'author': 'Lifter',
    'depends': ['base'],
    'category': 'Human Resources',
    'installable': True,
    'application': False,
    'auto_install': False,
}
