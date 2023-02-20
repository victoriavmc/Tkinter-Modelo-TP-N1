from tkinter import *
import os
##############################################################################################
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "logo")

tiposub = ("Comic Sans MS", 12, "italic", "underline")
tipotexto = ("Comic Sans MS", 12, "italic")
ticksError = ("Comic Sans MS", 12, "bold")
##############################################################################################
ventana = Tk()
ventana.geometry("430x700")
ventana.config(bg="blanched almond")
ventana.title("Tasa de Compromiso")
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))
############################# Funcion Base#################################################################


def segunAlcance():
    divisor = alcance.get()
    Label(ventana, background="thistle2", width=58, borderwidth=4,
          relief="groove", height=12).place(x=10, y=120)
    Label(ventana, background="Brown1", width=58, height=2).place(x=11, y=122)
    if divisor == 1:
        ############################ Entry Vistos##################################################################
        a = "# Ingrese la cantidad de vistos:"
        visto = IntVar()
        qvisto = Entry(ventana, textvariable=visto, font=tipotexto)
        qvisto.place(x=120, y=196)
    else:
        ############################ Checkbutton#################################################################
        red1 = IntVar()
        red2 = IntVar()
        red3 = IntVar()
        a = "# Selecciona la/s redes sociales:"
        b = ("# Cantidad de Seguidores:\n * Instagram : 6500 \n * Facebook : 3670 \n * Twitter : 7880")
        print("\n", b, "\n ", a)

        Checkbutton(ventana, text="Instagram", variable=red1,
                    background="IndianRed1", font=tipotexto).place(x=40, y=170)
        Checkbutton(ventana, text="Facebook", variable=red2,
                    background="IndianRed2", font=tipotexto).place(x=40, y=210)
        Checkbutton(ventana, text="Twitter", variable=red3,
                    background="indian red", font=tipotexto).place(x=40, y=250)

    Label(ventana, width=40, background="Brown1", text=a,
          justify=CENTER, font=tiposub).place(x=11, y=125)
 ############################# Funcion Todo#################################################################

    def tasa():
        divisor = alcance.get()
        if divisor == 1:
            n0Aux = visto.get()
            Label(ventana, background="thistle2",
                  width=4, height=2).place(x=327, y=195)
            if n0Aux <= 0:
                Label(ventana, text="X", bg="red", font=ticksError, padx=3, pady=2,
                      borderwidth=2, relief="groove").place(x=330, y=195)
                a = "Debe ingresar un número positivo."
            else:
                Label(ventana, text="✔", bg="#0cfb6d", font=ticksError, padx=3, pady=2,
                      borderwidth=3, relief="groove").place(x=330, y=195)
                a = "Datos ingresados correctamente!"
            print("\n ", a)
            Label(ventana, font=tipotexto, background="thistle2",
                  text=a).place(x=100, y=250)
        else:
            n0Aux = 0
        if divisor == 2:
            Label(ventana, bg="white", fg="red", borderwidth=4,
                  relief="groove", width=37, height=8).place(x=152, y=167)
            mensaje = "Haz seleccionado:"
            seguidores = 0
            if red1.get() == 1:
                mensaje += " Instagram - "
                seguidores += 6500

            if red2.get() == 1:
                mensaje = mensaje+" Facebook - "
                seguidores += 3670

            if red3.get() == 1:
                mensaje = mensaje+" Twitter - "
                seguidores += 7880

            if seguidores == 0:
                a = (
                    "NO HA SELECCIONADO NADA. \n DEBE SELECCIONAR UNA RED SOCIAL COMO MINIMO.")
            else:
                a = (
                    f"* {mensaje} \n ¬ Presenta un total de: {seguidores} seguidores.")
            print("\n ", a)
            Message(ventana, font=tipotexto, text=a, justify=CENTER,
                    width=237, bg="white").place(x=160, y=172)
        else:
            seguidores = 0

        n1Aux = n1.get()
        n2Aux = n2.get()
        n3Aux = n3.get()
        sumar = suma.get()
        if divisor == 1 or divisor == 2:
            Label(ventana, background="blanched almond",
                  height=6, width=4).place(x=378, y=348)
            if n1Aux < 0:
                Label(ventana, text="X", bg="red", font=ticksError, padx=3, pady=2,
                      borderwidth=2, relief="groove").place(x=380, y=350)
            else:
                Label(ventana, text="✔", bg="#0cfb6d", font=ticksError, padx=2, pady=2,
                      borderwidth=3, relief="groove").place(x=380, y=350)
            if n2Aux < 0:
                Label(ventana, text="X", bg="red", font=ticksError, padx=3, pady=2,
                      borderwidth=2, relief="groove").place(x=380, y=380)
            else:
                Label(ventana, text="✔", bg="#0cfb6d", font=ticksError, padx=2, pady=2,
                      borderwidth=3, relief="groove").place(x=380, y=380)
            if n3Aux < 0:
                Label(ventana, text="X", bg="red", font=ticksError, padx=3, pady=2,
                      borderwidth=2, relief="groove").place(x=380, y=410)
            else:
                Label(ventana, text="✔", bg="#0cfb6d", font=ticksError, padx=2, pady=2,
                      borderwidth=3, relief="groove").place(x=380, y=410)

        if (n1Aux > -1) and (n2Aux > -1) and (n3Aux > -1):
            texto = "Las interracciones fueron cargadas correctamente!"
        else:
            texto = "Las interracciones deben ser Nº Positivos o 0."
        print("\n"+texto+"\n ")

        if (n1Aux >= 0) and (n2Aux >= 0) and (n3Aux >= 0):
            sumar = (n1Aux+n2Aux+n3Aux)*100
            parte2 = True
            Label(ventana, bg="thistle2", width=50, height=10,
                  borderwidth=2, relief="groove").place(x=45, y=500)
            if (n0Aux > 0):
                ejercicio = (sumar)/n0Aux
            if (seguidores > 0):
                ejercicio = (sumar)/seguidores
            else:
                parte2 = False

            if parte2:
                resultado = (
                    f"  La Tasa de Compromiso es: {round(ejercicio,2)}%")
                print(resultado, "\n")
                Label(ventana, text=resultado, font=tipotexto,
                      bg="thistle2").place(x=90, y=530)
                if ejercicio < 1:
                    tipoTasa = "Muy Baja."
                elif ejercicio >= 1 and ejercicio <= 3.5:
                    tipoTasa = "Bueno."
                else:
                    tipoTasa = "Excelente."
                a = ("La Tasa de Compromiso que presenta es: \n"+tipoTasa)
            else:
                a = "Complete los datos correctamente para \n Calcular la Tasa de Compromiso"
                Label(ventana, text="Error, verificar datos ingresados!",
                      font=tipotexto, bg="thistle2").place(x=90, y=530)

            print(a, "\n ")
            Label(ventana, text=a, font=tipotexto, justify=CENTER,
                  bg="thistle2").place(x=70, y=570)

    ################## Entry Datos (mg, comentarios, compartidos)############################################################################
    Label(ventana, text="# Ingrese las interacciones: ",
          bg="Brown1", font=tiposub).place(x=20, y=320)

    Label(ventana, text="# Me Gusta:", background="salmon1",
          font=tipotexto).place(x=40, y=350)
    Label(ventana, text="# Comentarios:", background="IndianRed1",
          font=tipotexto).place(x=40, y=380)
    Label(ventana, text="# Compartidos:", background="IndianRed2",
          font=tipotexto).place(x=40, y=410)

    n1 = IntVar()
    n2 = IntVar()
    n3 = IntVar()
    suma = IntVar()

    interaccion1 = Entry(ventana, textvariable=n1, font=tipotexto)
    interaccion1.place(x=170, y=350)
    interaccion2 = Entry(ventana, textvariable=n2, font=tipotexto)
    interaccion2.place(x=170, y=380)
    interaccion3 = Entry(ventana, textvariable=n3, font=tipotexto)
    interaccion3.place(x=170, y=410)
############ Boton Tasa##################################################################################
    Button(ventana, font=tipotexto, text="Enviar",
           bg="firebrick1", command=tasa).place(x=190, y=450)


#############################################################################################
Label(ventana, text="# Tipo de alcance según la cantidad de:",
      font=tiposub, background="Brown1").place(x=20, y=10)

alcance = IntVar()

Radiobutton(ventana, text="# Personas. (Vistas)", background="indian red",
            variable=alcance, font=tipotexto, value=1, command=segunAlcance).place(x=40, y=40)
Radiobutton(ventana, text="# Seguidores.         ", background="salmon1",
            variable=alcance, font=tipotexto, value=2, command=segunAlcance).place(x=40, y=76)

Label(ventana, background="Brown1", text="~ VictoriaVMC", font=tipotexto,
      justify=CENTER).pack(side=BOTTOM, fill=BOTH, expand=False)
ventana.mainloop()