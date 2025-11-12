from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.conf import settings # <--- NEW: Required to access BASE_DIR
from .forms import attrForm
import numpy as np
import pickle
import os

# Define absolute paths globally for reliability in deployment.
# We assume the model files are in the project root (the directory above attrApp).
MODEL_FILE_PATH = os.path.join(settings.BASE_DIR.parent, 'Final_model_Attrition.sav')
SCALER_FILE_PATH = os.path.join(settings.BASE_DIR.parent, 'scaler.pkl')


class dataUploadView(View):
    form_class = attrForm
    template_name = 'create.html'
    success_url = reverse_lazy('success')
    failure_url = reverse_lazy('fail')

    def get(self, request, *args, **kwargs):
        """Display the form to collect employee details."""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """Handle form submission and predict attrition."""
        form = self.form_class(request.POST)

        # NOTE: Even if form is valid, the data collection keys below must match
        # the model/form field names exactly (using underscores, not spaces).
        if form.is_valid():
            form.save()

            # Collect all input values from the POST request.
            # Keys corrected to use underscores to match model field names.
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

                # Corrected keys below: using underscores instead of spaces to match Django field names
                request.POST.get('Department_Research_and_Development'), # <-- FIXED
                request.POST.get('Department_Sales'),
                request.POST.get('EducationField_Life_Sciences'),        # <-- FIXED
                request.POST.get('EducationField_Marketing'),
                request.POST.get('EducationField_Medical'),
                request.POST.get('EducationField_Other'),
                request.POST.get('EducationField_Technical_Degree'),     # <-- FIXED
                request.POST.get('Gender_Male'),
                request.POST.get('JobRole_Human_Resources'),             # <-- FIXED
                request.POST.get('JobRole_Laboratory_Technician'),       # <-- FIXED
                request.POST.get('JobRole_Manager'),
                request.POST.get('JobRole_Manufacturing_Director'),      # <-- FIXED
                request.POST.get('JobRole_Research_Director'),          # <-- FIXED
                request.POST.get('JobRole_Research_Scientist'),         # <-- FIXED
                request.POST.get('JobRole_Sales_Executive'),            # <-- FIXED
                request.POST.get('JobRole_Sales_Representative'),        # <-- FIXED
                request.POST.get('MaritalStatus_Married'),
                request.POST.get('MaritalStatus_Single'),
                request.POST.get('OverTime_Yes'),
            ]

            # Convert inputs to a NumPy array
            try:
                # Filter out any None values if form fields are not mandatory or not present
                # (though ModelForms usually ensure all fields are present).
                data = np.array(input_features, dtype=float).reshape(1, -1)
            except ValueError:
                # Log the error for debugging
                print("ValueError: Input features could not be converted to float array.")
                return render(request, "fail.html", {
                    'error_message': 'Invalid input detected. Please check your inputs.'
                })

            # Load the model and scaler using the stable global paths
            try:
                with open(MODEL_FILE_PATH, 'rb') as f:
                    model = pickle.load(f)
                with open(SCALER_FILE_PATH, 'rb') as f:
                    scaler = pickle.load(f)
            except Exception as e:
                # This exception handles the FileNotFoundError in deployment.
                print(f"FATAL FILE ERROR: Error loading model/scaler. Check if files are uploaded correctly. Error: {e}")
                return render(request, "fail.html", {
                    'error_message': f"Internal Server Error: Could not load ML assets. Error details: {e}"
                })

            # Predict using the model
            try:
                data_scaled = scaler.transform(data)
                prediction = model.predict(data_scaled)
                result = 'Yes' if prediction[0] == 1 else 'No'
            except Exception as e:
                print(f"Prediction failed during transform or predict: {e}")
                return render(request, "fail.html", {
                    'error_message': f"Prediction failed: {e}"
                })

            # Render success page
            return render(request, "succ_msg.html", {
                'out': result,
                'inputs': input_features
            })

        # If form invalid, redirect to fail
        return redirect(self.failure_url)
