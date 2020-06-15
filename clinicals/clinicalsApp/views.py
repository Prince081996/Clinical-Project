from django.shortcuts import render,redirect
from .models import Patient,ClinicalData
from django.views.generic import ListView,CreateView,UpdateView,DeleteView 
from django.urls import reverse_lazy
from .forms import ClinicalDataForm


# Create your views here.
class PatientListView(ListView):
    model = Patient
    


class PatientCreateView(CreateView):
    model = Patient   
    success_url = reverse_lazy('index')
    fields = ('first_name','last_name','age')

class PatientUpdateView(UpdateView):
    model = Patient    
    success_url = reverse_lazy('index')
    fields = ('first_name','last_name','age')

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')


def add_data(request,**kwargs):
     form = ClinicalDataForm ()
     patient = Patient.objects.get(id = kwargs['pk'])
     if request.method =="POST":
         form =ClinicalDataForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/')    
     return render(request,'clinicalsApp/clinical_data_form.html',{'form':form,'patient':patient})  

def analyze(request,**kwargs):
    data = ClinicalData.objects.filter(patient_id = kwargs['pk'])
    responseData = []
    for eachEntry in data:
            if eachEntry.component_name == 'hw':
                heightAndweight = eachEntry.component_Value.split('/')
                if len(heightAndweight) >1:
                    height_in_meters = float(heightAndweight[0]) * 0.4536
                    BMI = (float(heightAndweight[1]))/(height_in_meters*height_in_meters)
                    bmi_entry = ClinicalData()
                    bmi_entry.component_name = "BMI"
                    bmi_entry.component_Value = BMI
                    responseData.append(bmi_entry)
                   
            responseData.append(eachEntry)    


    return render(request,'clinicalsApp/generate_report.html',{'data':responseData})     