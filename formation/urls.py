
from django.urls import path
from formation import views 
from django.contrib import admin
urlpatterns = [
path('formation',views.index,name='formation'),
path('login/',views.connect,name="login"),
path('loginaction/', views.signIn, name='loginaction'),
path('ajoutdip/',views.add,name='ajoutdip'),
path('modif/<int:id>',views.modif,name='modif'),
path('modif/modif_action/<int:id>',views.modif_dip,name='modif_action'),
path('ajoutdip/add_dip/',views.add_dip,name='add_dip'),
path('delDip/<int:id>',views.del_dip,name="delDip"),
path('logout/',views.signOut,name="logout"),
path('type/logout/',views.signOut,name="logout"),
path('type/',views.type,name="type"),
path('type/addtyp/',views.addtyp,name="addtyp"),
path('type/modiftp/<int:id>',views.modiftp,name="modiftyp"),
path('type/modiftp/modif_action/<int:id>',views.modif_typ,name="modif_action"),
path('type/addtyp/add_typ/',views.add_typ,name="add_typ"),
path('type/deltyp/<int:id>',views.del_typ,name="deltyp"),
path('admin/',admin.site.urls,name="admin"),

]