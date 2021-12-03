from tkinter import*
from tkinter import font
from tkinter import messagebox
from random import randint
import os

window = Tk()
window.title('Cadastro de Usuários')
window.minsize(width=400,height=400)
window.geometry('400x400+100+100')

#random number generated
numId = int()
numId = randint(10000, 99999)

def registration():
    numId = int()
    numId = randint(10000, 99999)
    # grabing the value of each input at the screen
    idFile = identificationInput.get()
    userFile = UserInput.get()
    birthFile = BirthInput.get()
    adressFile = AdressInput.get()
    professionFile = professionInput.get()

    # checking if already exists the id
    if os.path.isfile('./files/' + str(numId) + '.txt'):
        registrationAlreadyExists = messagebox.showinfo('Aviso!', 'Usuário já cadastrado!!')
    else:
        custumerRegistration = open('./files/' + str(numId) + '.txt', 'w')
        custumerRegistration.write('%d\n' % numId)
        custumerRegistration.write('%s\n' % userFile)
        custumerRegistration.write('%s\n' % birthFile)
        custumerRegistration.write('%s\n' % adressFile)
        custumerRegistration.write('%s\n' % professionFile)

    # message that the user were registered
    resCad = messagebox.showinfo('Aviso!', 'Usuário cadastrado com sucesso!\nSeu usuário: %d'%numId)
    # random number generated
    identificationInput.delete(0, END)
    identificationInput.insert(0,str(numId))
    return


# input stuff
identification = Label(window, text='Número ID gerado:', font=('Arial Bold', 14))
identification.place(relx=0.25, rely=0.1, anchor=CENTER)
identificationInput = Entry(window, width=15, font=('Arial', 14))
identificationInput.insert(0,numId)
identificationInput.place(relx=0.45, rely=0.1,anchor=W)
# name stuff
UserName = Label(window, text='Nome de Usuário:', font=('Arial Bold', 14))
UserName.place(relx=0.25, rely=0.2, anchor=CENTER)
UserInput = Entry(window, width=15, font=('Arial', 14))
UserInput.place(relx=0.45, rely=0.2,anchor=W)
# Birth date stuff
Birth = Label(window, text='Data de nascimento:', font=('Arial Bold', 14))
Birth.place(relx=0.23, rely=0.3, anchor=CENTER)
BirthInput = Entry(window, width=15, font=('Arial', 14))
BirthInput.place(relx=0.45, rely=0.3,anchor=W)
# Adress stuff
Adress = Label(window, text='Endereço:', font=('Arial Bold', 14))
Adress.place(relx=0.25, rely=0.4, anchor=CENTER)
AdressInput = Entry(window, width=15, font=('Arial', 14))
AdressInput.place(relx=0.45, rely=0.4,anchor=W)
# profession stuff
profession = Label(window, text='Profissão:', font=('Arial Bold', 14))
profession.place(relx=0.25, rely=0.5, anchor=CENTER)
professionInput = Entry(window, width=15, font=('Arial', 14))
professionInput.place(relx=0.45, rely=0.5,anchor=W)
#registration button:
regButton = Button(window, text='Cadastrar!', command=registration)
regButton.place(relx=0.5, rely=0.6,anchor=CENTER)
# mainloop to keep the application opened.
window.mainloop()