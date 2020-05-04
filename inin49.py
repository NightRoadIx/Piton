from firebase import firebase

firebase = firebase.FirebaseApplication('https://beispiel-35600.firebaseio.com/',None)

data = {'RollNo': 2,
        'Nombre': 'Juan Nepomuceno 2',
        'Calificacion': 6.85
        }

'''
    CRUD
    Create
    Read
    Update
    Delete
'''

# Create
result = firebase.put('Estudiantes/','2',data)
print(result)

#%%
# Read
todo = firebase.get('Estudiantes/', '')
print(todo)
resultado = firebase.get('Estudiantes/', '5')
print(resultado)

#%%
# Update
result = firebase.put('Estudiantes/2', 'Calificacion', 7.50)

#%%
# Delete
print(firebase.delete('Estudiantes/', '1'))
