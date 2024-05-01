from django.contrib import admin
from myapp.models import Imeage
from myapp.models import contactEnquiry
from myapp.models import Member
# Register your models here.

@admin.register(Imeage)
class ImeageAdmin(admin.ModelAdmin):
    list_display=('id','photo','date')

class contactenq(admin.ModelAdmin):
    list_display=('name','email','phone','websitelink','message')

admin.site.register(contactEnquiry,contactenq)

class Membersdetail(admin.ModelAdmin):
    
 
    list_display=('Fname','Lname','Fathername','City','State','mobileno','Country','Education','Bank_ac','himalay','man','h','m')

admin.site.register(Member,Membersdetail)