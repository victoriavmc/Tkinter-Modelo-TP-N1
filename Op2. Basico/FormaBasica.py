from tkinter import *
import os
ventana = Tk()
##############################################################################################
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "logo")
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))
############################# Base#################################################################
ticksError = "Comic Sans MS", 10, "bold"
tiposub = "Comic Sans MS", 10, "italic", "underline"
tipotexto = "Comic Sans MS", 10, "italic"
ventana.config(bg="blanched almond")
ventana.title("Tasa de Compromiso")
ventana.geometry("580x365")
################################ RADIOBUTTON############################################################


def segunAlcance():
    op = alcance.get()
    if op == 1:
        ################################ Entry0############################################################
        Label(ventana, text="Ingrese la cantidad de vistos:",
              background="thistle2", font=tiposub).place(x=120, y=110)
        visto = IntVar()
        qvisto = Entry(ventana, textvariable=visto, font=tipotexto, width=17)
        qvisto.place(x=120, y=140)
        # NO VER LA PARTE DE SEGUIDORES
        Label(ventana, bg="blanched almond",
              width=17, height=7).place(x=425, y=80)
    else:
        ################################ CHECKBUTTON############################################################
        red1 = IntVar()
        red2 = IntVar()
        red3 = IntVar()

        Checkbutton(ventana, text="Instagram", variable=red1,
                    background="thistle2", font=tipotexto).place(x=430, y=85)
        Checkbutton(ventana, text="Facebook", variable=red2,
                    background="thistle2", font=tipotexto).place(x=430, y=118)
        Checkbutton(ventana, text="Twitter", variable=red3,
                    background="thistle2", font=tipotexto).place(x=430, y=150)
        a = ("+ Cantidad de Seguidores:\n  * Instagram : 6500 \n  * Facebook : 3670 \n  * Twitter : 7880")
        print(a + "\n")

        # NO VER LA PARTE DE VISTOS
        Label(ventana, bg="blanched almond",
              width=30, height=5).place(x=110, y=100)

    def tasa():
        if alcance.get() == 1:
            n0Aux = visto.get()
            # NO VER LA PARTE DEL CUADRADO ANTERIOR
            Label(ventana, background="blanched almond",
                  width=3, height=2).place(x=247, y=134)
            if n0Aux <= 0:
                Label(ventana, text="X", bg="red", font=ticksError,
                      padx=3, pady=2, borderwidth=3, relief="groove").place(x=250, y=138)
                a = "La cantidad de vistos deben ser mayor a 0."
            else:
                Label(ventana, text="✔", bg="#0cfb6d", font=ticksError,
                      padx=2, pady=2, borderwidth=2, relief="groove").place(x=250, y=138)
                a = "La cantidad de vistos fue cargado correctamente."
            print("\n", a, "\n")
        else:
            n0Aux = 0
        if alcance.get() == 2:
            mensaje = " "
            seguidores = 0
            if red1.get() == 1:
                print(" Instagram : 6500 seguidores")
                mensaje += " Instagram - "
                seguidores += 6500
            if red2.get() == 1:
                print(" Facebook : 3670 seguidores")
                mensaje = mensaje+" Facebook - "
                seguidores += 3670
            if red3.get() == 1:
                print(" Twitter : 7880 seguidores")
                mensaje = mensaje+" Twitter - "
                seguidores += 7880
            if seguidores == 0:
                print("\n    DEBE SELECCIONAR UNA RED SOCIAL COMO MINIMO.\n")
                Message(ventana, font=tipotexto, text="ERROR",
                        width=2, bg="gold").place(x=524, y=84)
            else:
                print(
                    f"\n * Haz seleccionado combinar el número de seguidores de: \n {mensaje} \n ¬ Presenta un total de: {seguidores} seguidores.  \n")

        else:
            seguidores = 0

        n1Aux = n1.get()
        n2Aux = n2.get()
        n3Aux = n3.get()

        if alcance.get() == 1 or alcance.get() == 0:
            Label(ventana, background="blanched almond",
                  width=3, height=6).place(x=250, y=205)
            if n1Aux < 0:
                Label(ventana, text="X ", bg="red", font=ticksError, padx=3, pady=2,
                      borderwidth=2, relief="groove").place(x=250, y=210)
            else:
                Label(ventana, text="✔", bg="#0cfb6d", font=ticksError, padx=2, pady=2,
                      borderwidth=3, relief="groove").place(x=250, y=210)
            if n2Aux < 0:
                Label(ventana, text="X ", bg="red", font=ticksError, padx=3, pady=2,
                      borderwidth=2, relief="groove").place(x=250, y=240)
            else:
                Label(ventana, text="✔", bg="#0cfb6d", font=ticksError, padx=2, pady=2,
                      borderwidth=3, relief="groove").place(x=250, y=240)
            if n3Aux < 0:
                Label(ventana, text="X ", bg="red", font=ticksError, padx=3, pady=2,
                      borderwidth=2, relief="groove").place(x=250, y=270)
            else:
                Label(ventana, text="✔", bg="#0cfb6d", font=ticksError, padx=2, pady=2,
                      borderwidth=3, relief="groove").place(x=250, y=270)
        if (n1Aux > -1) and (n2Aux > -1) and (n3Aux > -1):
            texto = "Las Interraciones fueron cargados correctamente!"
        else:
            texto = "Las Interraciones deben ser números positivos o 0."
        print(texto+"\n ")
##                                             TASA                                        ##
        if (n1Aux >= 0) and (n2Aux >= 0) and (n3Aux >= 0):
            sumar = (n1Aux+n2Aux+n3Aux)*100
            parte2 = True
            if (n0Aux > 0):
                ejercicio = (sumar)/n0Aux
            elif (seguidores > 0):
                ejercicio = (sumar)/seguidores
            else:
                parte2 = False
        if parte2:
            Label(ventana, bg="thistle2", width=40, height=8,
                  borderwidth=2, relief="groove").place(x=280, y=210)
            resultado = (
                f"  La Tasa de Compromiso es: {round(ejercicio,2)}%  ")
            print(resultado, "\n")
            Label(ventana, text=resultado, font=tipotexto,
                  bg="thistle2").place(x=300, y=230)
            if ejercicio < 1:
                tipoTasa = "Muy Baja."
            elif ejercicio >= 1 and ejercicio <= 3.5:
                tipoTasa = "Bueno."
            else:
                tipoTasa = "Excelente."
            a = (" La Tasa de Compromiso que presenta es: \n"+tipoTasa)
        else:
            Label(ventana, bg="thistle2", width=40, height=8,
                  borderwidth=2, relief="groove").place(x=280, y=210)
            Label(ventana, bg="thistle2", text="Error, verificar datos ingresados!",
                  font=tipotexto).place(x=300, y=230)

            a = "Complete los datos correctamente para \n Calcular la Tasa de Compromiso"
        print(a, "\n ")
        Label(ventana, text=a, font=tipotexto,
              bg="thistle2").place(x=300, y=270)
##                                 Ingreso de Interacciones                                 ##
    Label(ventana, text="# Me Gusta:", background="salmon1",
          font=tipotexto).place(x=20, y=210)
    Label(ventana, text="# Comentarios:", background="salmon1",
          font=tipotexto).place(x=20, y=240)
    Label(ventana, text="# Compartidos:", background="salmon1",
          font=tipotexto).place(x=20, y=270)

    n1 = IntVar()
    n2 = IntVar()
    n3 = IntVar()

    interaccion1 = Entry(ventana, width=15, font=tipotexto, textvariable=n1)
    interaccion1.place(x=123, y=210)
    interaccion2 = Entry(ventana, width=15, font=tipotexto, textvariable=n2)
    interaccion2.place(x=123, y=240)
    interaccion3 = Entry(ventana, width=15, font=tipotexto, textvariable=n3)
    interaccion3.place(x=123, y=270)

    Button(ventana, text="Tasa", font=tipotexto,
           command=tasa).place(x=140, y=300)


##                                       Seleccion Base                                     ##
Label(ventana, text="Tipo de alcance según la cantidad de:",
      background="Brown1", font=tiposub).pack(anchor=N)
alcance = IntVar()
Radiobutton(ventana, text="Personas", variable=alcance, font=tipotexto, background="IndianRed1",
            value=1, command=segunAlcance).place(x=20, y=50)
Radiobutton(ventana, text="Seguidores", variable=alcance, font=tipotexto, background="IndianRed1",
            value=2, command=segunAlcance).place(x=450, y=50)

Label(ventana, background="Brown1", text="~ VictoriaVMC", font=tipotexto,
      justify=CENTER).pack(side=BOTTOM, fill=BOTH, expand=False)
ventana.mainloop()
