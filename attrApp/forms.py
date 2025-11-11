from django import forms
from .models import *


class attrForm(forms.ModelForm):
    class Meta():
        model=attrModel
        fields=['Age', 'DailyRate', 'DistanceFromHome', 'Education', 'EnvironmentSatisfaction',
            'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobSatisfaction', 'MonthlyIncome',
            'MonthlyRate', 'NumCompaniesWorked', 'PercentSalaryHike', 'PerformanceRating',
            'RelationshipSatisfaction', 'StockOptionLevel', 'TotalWorkingYears',
            'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
            'YearsSinceLastPromotion', 'YearsWithCurrManager', 'BusinessTravel_Travel_Frequently',
            'BusinessTravel_Travel_Rarely', 'Department_Research_and_Development',
            'Department_Sales', 'EducationField_Life_Sciences', 'EducationField_Marketing',
            'EducationField_Medical', 'EducationField_Other', 'EducationField_Technical_Degree',
            'Gender_Male', 'JobRole_Human_Resources', 'JobRole_Laboratory_Technician',
            'JobRole_Manager', 'JobRole_Manufacturing_Director', 'JobRole_Research_Director',
            'JobRole_Research_Scientist', 'JobRole_Sales_Executive',
            'JobRole_Sales_Representative', 'MaritalStatus_Married', 'MaritalStatus_Single',
            'OverTime_Yes']
