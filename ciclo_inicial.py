import pretools
import configuracion

#CICLO INICIAL: OBTENCIÓN DE IMAGENES 

#Nombra la sesión para tener un nuevo directorio por cada sesión.
sesion = configuracion.sesion
filename = configuracion.filename

pretools.creaDirectorioInicial(sesion)

dataframe = pretools.creaDataframe(filename)

pretools.procesaImagenes(sesion, dataframe)

pretools.df2Excel(dataframe, filename)