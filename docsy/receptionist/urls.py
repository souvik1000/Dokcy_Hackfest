from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name="login"),
    path('registrationValidation/',views.registrationValidation,name='registrationValidation'),
    path('loginauth/',views.loginauth,name="loginauth"),
    path('doctorsDashboard/',views.doctorsDashboard,name="doctorsDashboard"),
<<<<<<< HEAD
    path('prescription/',views.doctorprescription,name="doctorprescription"),
    path('prescriptionBackend/',views.prescriptionBackend,name="prescriptionBackend"),
    path('logout/',views.logout,name="logout")

=======
    path('patientSummary/',views.patientsummary,name="patientsummary"),
    path('patientSummary/allergies',views.allergies,name="allergies"),
    path('patientSummary/procedure',views.procedure,name="procedure"),
    path('patientSummary/historyofillness', views.historyofillness, name="historyofillness"),
    path('patientSummary/patientIllnessCreation', views.patientIllnessCreation, name="patientIllnessCreation")
>>>>>>> 0b1e69d824fe2b10dcc90d6c560c700dfc632c85
]