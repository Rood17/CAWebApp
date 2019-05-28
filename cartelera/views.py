from django.shortcuts import render, HttpResponse, get_object_or_404
from datetime import datetime, date, time, timedelta
from .models import Presentaciones, Obra
# Create your views here.



def cartelera(request):

    # Cartelera
    all_presentaciones = list(Presentaciones.objects.filter(status__icontains='01'))
    funciones = list(Presentaciones.objects.filter(status__icontains='01', presentacion__icontains='01'))
    # Query Program Espe - '02'
    program_espe = list(Presentaciones.objects.filter(status__icontains='01', presentacion__icontains='02'))

    # Fecha actual
    ahora = datetime.now()
    mes = {1:"Enero ", 2:"Febrero ", 3:"Marzo ", 4:"Abril ", 5:"Mayo ", 6:"Junio ", 7:"Julio ", 8:"Agosto ", 9:"Septiembre ", 10:"Octubre ", 11:"Noviembre ", 12:"Diciembre "}
    mes_actual = mes[ahora.month]
    mes_cal = ahora.month - 1
    mes_cal_2 = ahora.month
    dia = ahora.day
    # Próxima función
    hoy = False
    search_day = dia
    diferencia = []
    casicompleta = []
    cool = []
    dd = 0
    # Prósimo Evento
    hoyE = False
    espe_day = dia
    diferenciaE = []
    casicompletaE = []
    coolE = []
    ddE = 0
    dst = False
    # Calendario día de la semana
    diaCal_1 = 0
    diaCal_2 = 0
    diaCal_3 = 0
    diaCal_4 = 0
    diaCal_5 = 0
    diaCal_6 = 0
    diaCal_7 = 0
    diaCal_8 = 0
    diaCal_9 = 0
    dci_1 = 0
    dci_2 = 0
    dci_3 = 0
    dci_4 = 0
    dci_5 = 0
    dci_6 = 0
    dci_7 = 0
    dci_8 = 0
    dci_9 = 0

    # Próxima Función
    # Crear Lista de los Días
    a = []  # var prueba 1
    r = []  # var prueba 2
    dayss = []
    for obra_dia in funciones:
        d = obra_dia.fechaCal.all()
        for i in d:
            a = int(i.fechaCa)
            r.append(a)
        # Día Sem
        diaSemTest = obra_dia.diaSem.all()
        if len(diaSemTest) > 1:
            dst = True


    print('holaaaaaaaaaa')

    # Próxima Evento
    # Crear Lista de los Días
    aE = []  # var prueba 1
    rE = []  # var prueba 2
    dayssE = []
    for obra_dia in program_espe:
        dE = obra_dia.fechaCal.all()
        for i in dE:
            aE = int(i.fechaCa)
            rE.append(aE)
        
    # Próxima Función
    # Ordenar los días
    dayss = sorted(r)
    print(dayss)
    if len(dayss) > 0:
        # El más pequeño
        menor = dayss[0]
        # El mayor
        n = int(len(dayss))
        mayor = dayss[n-1]
        
        
        # Operación Número más cercano
        for i in range(len(dayss)):
            dd = dayss[i] - dia
            diferencia.append(dd)
            diferenciar = sorted(diferencia)

        
        for o in range(len(diferenciar)):
            sd = dia + diferenciar[o]
            casicompleta.append(sd)

            if dia < casicompleta[o]:
                de = casicompleta[o]
                cool.append(de)

            
        # Condiciones finales
        if dia in dayss:
            search_day = dia
            hoy = True
        elif dia <= menor or dia > mayor:
            search_day = menor
        elif dia == mayor:
            search_day = mayor
           
        else:
            search_day = cool[0]
    
    print(dia)
    print(hoy)
    print('holaaaaaaaaaa')
    # Próximo Evento
    # Ordenar los días
    dayssE = sorted(rE)
    print(dayssE)
    if len(dayssE) > 0:
        # El más pequeño
        menorE = dayssE[0]
        # El mayor
        nE = int(len(dayssE))
        mayorE = dayssE[nE-1]
        
        
        # Operación Número más cercano
        for i in range(len(dayssE)):
            ddE = dayssE[i] - dia
            diferenciaE.append(ddE)
            diferenciarE = sorted(diferenciaE)

        
        for o in range(len(diferenciarE)):
            sdE = dia + diferenciarE[o]
            casicompletaE.append(sdE)

            if dia < casicompletaE[o]:
                deE = casicompletaE[o]
                coolE.append(deE)

            
        # Condiciones finales
        if dia in dayssE:
            espe_day = dia
            hoyE = True
        elif dia <= menorE or dia > mayorE:
            espe_day = menorE
        elif dia == mayorE:
            espe_day = mayorE
        else:
            espe_day = coolE[0]
    
        # Calendario Días de la Semana

    print(hoyE)
    # Calendario Días de la Semana
    # si el tamaño de cool es mayor a 0
    if len(cool) == 1: 
        diaCal_1 = cool[0]
        diaCal_1_q = Presentaciones.objects.filter(diaSem__diaSem=cool[0])
        for i in diaCal_1_q:
            diaCal_id = i.id

    elif len(cool) ==2:
        diaCal_1 = cool[0]
        diaCal_2 = cool[1]
        diaCal_1_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_1))
        diaCal_2_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_2))

        for i in diaCal_1_q:
            dci_1 = i.titulo.id
        for i in diaCal_2_q:
            dci_2 = i.titulo.id
       
    elif len(cool) ==3:
        diaCal_1 = cool[0]
        diaCal_2 = cool[1]
        diaCal_3 = cool[2]
        diaCal_1_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_1))
        diaCal_2_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_2))
        diaCal_3_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_3))

        for i in diaCal_1_q:
            dci_1 = i.titulo.id
        for i in diaCal_2_q:
            dci_2 = i.titulo.id
        for i in diaCal_3_q:
            dci_3 = i.titulo.id

    elif len(cool) ==4:
        diaCal_1 = cool[0]
        diaCal_2 = cool[1]
        diaCal_3 = cool[2]
        diaCal_4 = cool[3]
        diaCal_1_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_1))
        diaCal_2_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_2))
        diaCal_3_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_3))
        diaCal_4_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_4))

        for i in diaCal_1_q:
            dci_1 = i.titulo.id
        for i in diaCal_2_q:
            dci_2 = i.titulo.id
        for i in diaCal_3_q:
            dci_3 = i.titulo.id
        for i in diaCal_4_q:
            dci_4 = i.titulo.id

    elif len(cool) ==5:
        diaCal_1 = cool[0]
        diaCal_2 = cool[1]
        diaCal_3 = cool[2]
        diaCal_4 = cool[3]
        diaCal_5 = cool[4]
        diaCal_1_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_1))
        diaCal_2_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_2))
        diaCal_3_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_3))
        diaCal_4_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_4))
        diaCal_5_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_5))


        for i in diaCal_1_q:
            dci_1 = i.titulo.id
        for i in diaCal_2_q:
            dci_2 = i.titulo.id
        for i in diaCal_3_q:
            dci_3 = i.titulo.id
        for i in diaCal_4_q:
            dci_4 = i.titulo.id
        for i in diaCal_5_q:
            dci_5 = i.titulo.id

    elif len(cool) ==6:
        diaCal_1 = cool[0]
        diaCal_2 = cool[1]
        diaCal_3 = cool[2]
        diaCal_4 = cool[3]
        diaCal_5 = cool[4]
        diaCal_6 = cool[5]
        diaCal_1_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_1))
        diaCal_2_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_2))
        diaCal_3_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_3))
        diaCal_4_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_4))
        diaCal_5_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_5))
        diaCal_6_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_6))


        for i in diaCal_1_q:
            dci_1 = i.titulo.id
        for i in diaCal_2_q:
            dci_2 = i.titulo.id
        for i in diaCal_3_q:
            dci_3 = i.titulo.id
        for i in diaCal_4_q:
            dci_4 = i.titulo.id
        for i in diaCal_5_q:
            dci_5 = i.titulo.id
        for i in diaCal_6_q:
            dci_6 = i.titulo.id

    elif len(cool) ==7:
        diaCal_1 = cool[0]
        diaCal_2 = cool[1]
        diaCal_3 = cool[2]
        diaCal_4 = cool[3]
        diaCal_5 = cool[4]
        diaCal_6 = cool[5]
        diaCal_7 = cool[6]
        diaCal_1_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_1))
        diaCal_2_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_2))
        diaCal_3_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_3))
        diaCal_4_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_4))
        diaCal_5_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_5))
        diaCal_6_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_6))
        diaCal_7_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_7))


        for i in diaCal_1_q:
            dci_1 = i.titulo.id
        for i in diaCal_2_q:
            dci_2 = i.titulo.id
        for i in diaCal_3_q:
            dci_3 = i.titulo.id
        for i in diaCal_4_q:
            dci_4 = i.titulo.id
        for i in diaCal_5_q:
            dci_5 = i.titulo.id
        for i in diaCal_6_q:
            dci_6 = i.titulo.id
        for i in diaCal_7_q:
            dci_7 = i.titulo.id

    elif len(cool) ==8:
        diaCal_1 = cool[0]
        diaCal_2 = cool[1]
        diaCal_3 = cool[2]
        diaCal_4 = cool[3]
        diaCal_5 = cool[4]
        diaCal_6 = cool[5]
        diaCal_7 = cool[6]
        diaCal_8 = cool[7]
        diaCal_1_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_1))
        diaCal_2_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_2))
        diaCal_3_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_3))
        diaCal_4_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_4))
        diaCal_5_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_5))
        diaCal_6_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_6))
        diaCal_7_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_7))
        diaCal_8_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_8))


        for i in diaCal_1_q:
            dci_1 = i.titulo.id
        for i in diaCal_2_q:
            dci_2 = i.titulo.id
        for i in diaCal_3_q:
            dci_3 = i.titulo.id
        for i in diaCal_4_q:
            dci_4 = i.titulo.id
        for i in diaCal_5_q:
            dci_5 = i.titulo.id
        for i in diaCal_6_q:
            dci_6 = i.titulo.id
        for i in diaCal_7_q:
            dci_7 = i.titulo.id
        for i in diaCal_8_q:
            dci_8 = i.titulo.id

    elif len(cool) ==9:
        diaCal_1 = cool[0]
        diaCal_2 = cool[1]
        diaCal_3 = cool[2]
        diaCal_4 = cool[3]
        diaCal_5 = cool[4]
        diaCal_6 = cool[5]
        diaCal_7 = cool[6]
        diaCal_8 = cool[7]
        diaCal_9 = cool[8]
        diaCal_1_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_1))
        diaCal_2_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_2))
        diaCal_3_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_3))
        diaCal_4_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_4))
        diaCal_5_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_5))
        diaCal_6_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_6))
        diaCal_7_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_7))
        diaCal_8_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_8))
        diaCal_9_q = list(Presentaciones.objects.filter(fechaCal__fechaCa=diaCal_9))


        for i in diaCal_1_q:
            dci_1 = i.titulo.id
        for i in diaCal_2_q:
            dci_2 = i.titulo.id
        for i in diaCal_3_q:
            dci_3 = i.titulo.id
        for i in diaCal_4_q:
            dci_4 = i.titulo.id
        for i in diaCal_5_q:
            dci_5 = i.titulo.id
        for i in diaCal_6_q:
            dci_6 = i.titulo.id
        for i in diaCal_7_q:
            dci_7 = i.titulo.id
        for i in diaCal_8_q:
            dci_8 = i.titulo.id
        for i in diaCal_9_q:
            dci_9 = i.titulo.id

    print('soy dios s')
    print(dci_2)
    print(dci_3)
    print(diaCal_2)
    print(diaCal_3)

    # Query para Hero-One
    hero_func = list(Presentaciones.objects.filter(fechaCal__fechaCa=search_day,status__icontains='01', presentacion__icontains='01'))
    # Query para Prox Evento
    prox_ev = list(Presentaciones.objects.filter(fechaCal__fechaCa=espe_day, status__icontains='01', presentacion__icontains='02'))



    context = {'mes_cal_2':mes_cal_2,'mes_cal':mes_cal,'año':ahora.year,'espe_day':espe_day,'mes':mes_actual,'search_day':search_day,'cartelera':cartelera, 'hero_func':hero_func, 'hoyE':hoyE  , 'hoy':hoy,'funciones':funciones, 'program_espe':program_espe,'dst':dst, 'prox_ev':prox_ev, 'diaCal_1':diaCal_1,'diaCal_2':diaCal_2,'diaCal_3':diaCal_3,'diaCal_4':diaCal_4,'diaCal_5':diaCal_5,'diaCal_6':diaCal_6,'diaCal_7':diaCal_7,'diaCal_8':diaCal_8,'diaCal_9':diaCal_9,'dci_1':dci_1, 'dci_2':dci_2, 'dci_3':dci_3 , 'dci_4':dci_4 , 'dci_5':dci_5 , 'dci_6':dci_6 , 'dci_7':dci_7 , 'dci_8':dci_8 , 'dci_9':dci_9}
    return render(request, 'cartelera/cartelera.html', context )

def CarteleraBio(request, obra_id):
    lala = get_object_or_404(Obra, id=obra_id)
    a = Obra.objects.get(id=obra_id)
    obra = Presentaciones.objects.filter(titulo=lala)
    context = {'obra':obra}

    

    return render(request, 'cartelera/cartelera_bio.html', context)

