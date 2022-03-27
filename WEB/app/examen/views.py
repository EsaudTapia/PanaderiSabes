
from imp import is_frozen
import re
from flask import render_template,redirect,flash,url_for,request
from app.forms import Exform,consultas
from . import examen

class exam:
    def __init__(self,archivo):
        self.archivo = archivo
    def captura(self,matricula,grupo,resultado):
         a = open(self.archivo,"a")
         line = "{},{},{}\n".format(matricula,grupo,resultado)
         a.write(line)
         a.close()
         return True
    def consulta(self):    
        animal = ["rata","buey","tigre","conejo","dragon","serpiente","caballo","cabra","mono","gallo","perro","cerdo"]    
        ayuda = []
        ayu=[]
        res=[]
        nomc=""
        a = open(self.archivo)        
        for lin in a:
            ayu=lin.split(",")
            f = open('alumnos.txt')
            for linea  in f:
                resulta=[]
                ayuda= linea.split(",")
                if ayu[0] == ayuda[0]:               
                    nomc=ayuda[1]+" "+ayuda[2]+" "+ayuda[3]
                    año =int(ayuda[7])
                    t = ((int(año-999)/12))
                    ubica=int(año-999 - int(t) * 12 -1)
                    resulta.append(ayuda[0]) #matricula
                    resulta.append(nomc)#nombre
                    resulta.append(ayuda[4])#grupo
                    resulta.append((2022-int(ayuda[7])))#edad
                    resulta.append(animal[ubica])
                    resulta.append(ayu[2])#calificacion
                    res.append(resulta)
                    print(resulta)
            f.close()
        a.close 
        return res
    def fil1(self,formv):
        animal = ["rata","buey","tigre","conejo","dragon","serpiente","caballo","cabra","mono","gallo","perro","cerdo"]
        ayuda = []
        ayu=[]
        res=[]
        nomc=""
        a = open(self.archivo)        
        for lin in a:
            ayu=lin.split(",")
            f = open('alumnos.txt')
            if ayu[0] == formv.matricula.data:  
                for linea  in f:
                    resulta=[]
                    ayuda= linea.split(",")
                    print(formv.matricula.data)
                    if ayu[0] == ayuda[0]:               
                        nomc=ayuda[1]+" "+ayuda[2]+" "+ayuda[3]
                        año =int(ayuda[7])
                        t = ((int(año-999)/12))
                        ubica=int(año-999 - int(t) * 12 -1)
                        resulta.append(ayuda[0]) #matricula
                        resulta.append(nomc)#nombre
                        resulta.append(ayuda[4])#grupo
                        resulta.append((2022-int(ayuda[7])))#edad
                        resulta.append(animal[ubica])
                        resulta.append(ayu[2])#calificacion
                        res.append(resulta)
                        print(resulta)
            f.close()
        a.close 
        return res
    def fil2(self,form):
        animal = ["rata","buey","tigre","conejo","dragon","serpiente","caballo","cabra","mono","gallo","perro","cerdo"]
        ayuda = []
        ayu=[]
        res=[]
        nomc=""
        a = open(self.archivo)        
        for lin in a:
            ayu=lin.split(",")
            f = open('alumnos.txt')
            if ayu[1] == form.grupo.data:  
                for linea  in f:
                    resulta=[]
                    ayuda= linea.split(",")
                    if ayu[0] == ayuda[0]:               
                        nomc=ayuda[1]+" "+ayuda[2]+" "+ayuda[3]
                        año =int(ayuda[7])
                        t = ((int(año-999)/12))
                        ubica=int(año-999 - int(t) * 12 -1)
                        resulta.append(ayuda[0]) #matricula
                        resulta.append(nomc)#nombre
                        resulta.append(ayuda[4])#grupo
                        resulta.append((2022-int(ayuda[7])))#edad
                        resulta.append(animal[ubica])
                        resulta.append(ayu[2])#calificacion
                        res.append(resulta)
                        print(resulta)
            f.close()
        a.close 
        return res
@examen.route("/calificaciones",methods=['GET','POST'])
def resultados():
    filtro_form =consultas()
    obje = exam('examenes.txt')
    if filtro_form.validate_on_submit():
        if request.method == 'POST' and request.form.get('tipo')== 'Matricula':
            resulta= obje.fil1(filtro_form)
        else:
            if request.method == 'POST' and request.form.get('tipo')== 'Grupo':
                resulta= obje.fil2(filtro_form)
            else:
                resulta=obje.consulta()  
    else:
        resulta=obje.consulta()         
    context={
        'resulta':resulta,
        'filtro_form':filtro_form
    }
    
    return render_template('pagina3.html',**context)

@examen.route("/examen",methods=['GET','POST'])
def prueba():
    exam_form = Exform()
    
    context ={
        'exam_form':exam_form
    }
    if exam_form.validate_on_submit():
        calular = int (exam_form.pre1.data)+int(exam_form.pre2.data)+int(exam_form.pre3.data)+int(exam_form.pre4.data)+int(exam_form.pre5.data)
        obje = exam('examenes.txt')
        res = obje.captura(exam_form.matricula.data,exam_form.grupo.data,calular)
        msg = 'Laprueba no pudo ser registrada correctamente'
        
        if res:
            msg ='Examen completado exitosamente'
        flash(msg)
        return redirect(url_for('examen.resultados'))
    return render_template('pagina4.html',**context)