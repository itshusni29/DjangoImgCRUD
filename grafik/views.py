# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import ChartData
from .forms import ChartDataForm

import json

def chart_data_list(request):
    chart_data = ChartData.objects.all()

    months = []
    actual_values = []
    target_values = []

    for data in chart_data:
        months.append(data.month)
        actual_values.append(data.actual_value)
        target_values.append(data.target_value)

    chart_data_json = {
        'months': months,
        'actual_values': actual_values,
        'target_values': target_values,
    }

    return render(request, 'grafik_list.html', {'chart_data': chart_data, 'chart_data_json': json.dumps(chart_data_json)})




def create_chart_data(request):
    if request.method == 'POST':
        form = ChartDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chart_data_list')
    else:
        form = ChartDataForm()
    return render(request, 'grafik_upload.html', {'form': form})

def update_chart_data(request, id):
    chart_data = get_object_or_404(ChartData, id=id)
    if request.method == 'POST':
        form = ChartDataForm(request.POST, instance=chart_data)
        if form.is_valid():
            form.save()
            return redirect('chart_data_list')
    else:
        form = ChartDataForm(instance=chart_data)
    return render(request, 'grafik_edit.html', {'form': form})

def delete_chart_data(request, id):
    chart_data = get_object_or_404(ChartData, id=id)
    if request.method == 'POST':
        chart_data.delete()
        return redirect('chart_data_list')
    return render(request, 'grafik_delete.html', {'chart_data': chart_data})
