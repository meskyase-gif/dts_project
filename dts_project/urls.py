from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # ተጠቃሚው ገና ዌብሳይቱን ሲከፍት ቀጥታ ወደ letters አፕሊኬሽን እንዲሄድ እናደርጋለን
    path('', include('letters.urls')),
]