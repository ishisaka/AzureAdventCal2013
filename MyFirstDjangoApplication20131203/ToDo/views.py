from django.http import HttpResponse
from django.template.loader import render_to_string
from azure.storage import *

account_name = 'advent2014'
account_key = 'Jdvs+jCR0RV1sedMjg930HncLIOjn047oYvbyy2XGNVo+vCTW7L0S3R1b9WokX34fzPpWoUZ8sX9owSUd9sh+g=='
table_service = TableService(account_name=account_name, account_key=account_key);
table_service.create_table('mytasks')

def list_tasks(request):      
    entities = table_service.query_entities('mytasks', '', 'name,category,date,complete')         
    html = render_to_string('index.html', {'entities':entities})     
    return HttpResponse(html)


def add_task(request):     
    name = request.GET['name']     
    category = request.GET['category']     
    date = request.GET['date']     
    table_service.insert_entity('mytasks', {'PartitionKey':name+category, 'RowKey':date, 'name':name, 'category':category, 'date':date, 'complete':'No'})     
    entities = table_service.query_entities('mytasks', '', 'name,category,date,complete')     
    html = render_to_string('index.html', {'entities':entities})     
    return HttpResponse(html)

def update_task(request):     
    name = request.GET['name']     
    category = request.GET['category']     
    date = request.GET['date']     
    partition_key = name + category     
    row_key = date     
    table_service.update_entity('mytasks', partition_key, row_key, {'PartitionKey':partition_key, 'RowKey':row_key, 'name': name, 'category':category, 'date':date, 'complete':'Yes'})     
    entities = table_service.query_entities('mytasks', '', 'name,category,date,complete')         
    html = render_to_string('index.html', {'entities':entities})     
    return HttpResponse(html)