from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from .forms import attrForm
import numpy as np
import pickle

class dataUploadView(View):
    form_class = attrForm
    template_name = 'create.html'
    success_url = reverse_lazy('success')
    failure_url = reverse_lazy('fail')

    def get(self, request, *args, **kwargs):
        """Display form to collect employee details."""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """Handle form submission and predict attrition."""
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Collect numeric and categorical inputs from the POST request
            input_features = [
                request.POST.get('Age'),
                request.POST.get('DailyRate'),
                request.POST.get('DistanceFromHome'),
                request.POST.get('Education'),
                request.POST.get('EnvironmentSatisfaction'),
                request.POST.get('HourlyRate'),
                request.POST.get('JobInvolvement'),
                request.POST.get('JobLevel'),
                request.POST.get('JobSatisfaction'),
                request.POST.get('MonthlyIncome'),
                request.POST.get('MonthlyRate'),
                request.POST.get('NumCompaniesWorked'),
                request.POST.get('PercentSalaryHike'),
                request.POST.get('PerformanceRating'),
                request.POST.get('RelationshipSatisfaction'),
                request.POST.get('StockOptionLevel'),
                request.POST.get('TotalWorkingYears'),
                request.POST.get('TrainingTimesLastYear'),
                request.POST.get('WorkLifeBalance'),
                request.POST.get('YearsAtCompany'),
                request.POST.get('YearsInCurrentRole'),
                request.POST.get('YearsSinceLastPromotion'),
                request.POST.get('YearsWithCurrManager'),
                request.POST.get('BusinessTravel_Travel_Frequently'),
                request.POST.get('BusinessTravel_Travel_Rarely'),
                request.POST.get('Department_Research & Development'),
                request.POST.get('Department_Sales'),
                request.POST.get('EducationField_Life Sciences'),
                request.POST.get('EducationField_Marketing'),
                request.POST.get('EducationField_Medical'),
                request.POST.get('EducationField_Other'),
                request.POST.get('EducationField_Technical Degree'),
                request.POST.get('Gender_Male'),
                request.POST.get('JobRole_Human Resources'),
                request.POST.get('JobRole_Laboratory Technician'),
                request.POST.get('JobRole_Manager'),
                request.POST.get('JobRole_Manufacturing Director'),
                request.POST.get('JobRole_Research Director'),
                request.POST.get('JobRole_Research Scientist'),
                request.POST.get('JobRole_Sales Executive'),
                request.POST.get('JobRole_Sales Representative'),
                request.POST.get('MaritalStatus_Married'),
                request.POST.get('MaritalStatus_Single'),
                request.POST.get('OverTime_Yes'),
            ]

            # Convert to numpy array and reshape for model input
            try:
                data = np.array(input_features, dtype=float).reshape(1, -1)
            except ValueError:
                # Handle invalid inputs gracefully
                return render(request, "fail.html", {
                    'error_message': 'Invalid input type detected. Please enter valid numeric values.'
                })

            # Load trained model and scaler
            try:
                model = pickle.load(open('Final_model_Attrition.sav', 'rb'))
                scaler = pickle.load(open('scaler.pkl', 'rb'))
            except Exception as e:
                return render(request, "fail.html", {
                    'error_message': f'Error loading model files: {e}'
                })

            # Scale input and predict
            try:
                data_scaled = scaler.transform(data)
                prediction = model.predict(data_scaled)
                result = 'Yes' if prediction[0] == 1 else 'No'
            except Exception as e:
                return render(request, "fail.html", {
                    'error_message': f'Prediction failed: {e}'
                })

            # Return result page
            return render(request, "succ_msg.html", {
                'out': result,
                'inputs': input_features
            })

        else:
            return redirect(self.failure_url)
