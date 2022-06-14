from django.conf import settings
from django.conf.urls.static import static

from django.urls import path 
from .views import index, quienessomos, galeria, formulario, apiferiados,mensaje,mostrar,mostrar2,forms_clientes,form_mod_cliente,form_del_cliente,forms_productos,form_mod_producto,form_del_producto

urlpatterns=[
    path('',index, name="index"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    path('apiferiados/', apiferiados, name="apiferiados"),
    path('mensaje/', mensaje, name="mensaje"),
    path('mostrar/', mostrar, name="mostrar"),
    path('mostrar2/', mostrar2, name="mostrar2"),
    path('forms_clientes/', forms_clientes, name="forms_clientes"),
    path('form_mod_cliente/<id>', form_mod_cliente, name="form_mod_cliente"),
    path('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),
    path('forms_productos/', forms_productos, name="forms_productos"),
    path('form_mod_producto/<id>', form_mod_producto, name="form_mod_producto"),
    path('form_del_producto/<id>', form_del_producto, name="form_del_producto"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)