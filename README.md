# Тестовое задание для RocketData

### Выполненные задачи:
### Часть 1:                             
* Пункт номер 1;
* Пункт номер 2;
* Пунтк номер 3;
* Пункт номер 4;
* Пункт номер 5.
### Часть 2:
* Пункт номер1;
* Пункт номер 2 - задача 1;
* Пункт номер 3;
* Пункт номер 4;
* Пунтк номер 5.

##

### Подробнее о выполненных задачах:
### Часть 1:
#### Пункт номер 1:
    Модели сети:
    test_rocket\factory          - Завод;
    test_rocket\distributor      - Дистрибьютор;
    test_rocket\dealership       - Дилерский центр;
    test_rocket\retailnetwork    - Крупная розничная сеть;
    test_rocket\indentrepreneur  - Индивидуальный предприниматель.
#### Пункт номер 2:
    Схема моделей cети:
    test_rocket\factory\model.py          - Завод;
    test_rocket\distributor\model.py      - Дистрибьютор;
    test_rocket\dealership\model.py       - Дилерский центр;
    test_rocket\retailnetwork\model.py    - Крупная розничная сеть;
    test_rocket\indentrepreneur\model.py  - Индивидуальный предприниматель.
 #### Пункт номер 3:
    Админ-панели:
    test_rocket\factory\admin.py          - Завод;
    test_rocket\distributor\admin.py      - Дистрибьютор;
    test_rocket\dealership\admin.py       - Дилерский центр;
    test_rocket\retailnetwork\admin.py    - Крупная розничная сеть;
    test_rocket\indentrepreneur\admin.py  - Индивидуальный предприниматель.
 #### Пункт номер 4(4.1, 4.2, 4.3, 4.4, 4.5 , 4.6):
    Набор представлений и сериализаторы:
    test_rocket\factory\views.py                 - Завод;
    test_rocket\factory\serializers.py          - Завод;
    test_rocket\distributor\views.py             - Дистрибьютор;
    test_rocket\distributor\serializers.py      - Дистрибьютор;
    test_rocket\dealership\views.py              - Дилерский центр;
    test_rocket\dealership\serializers.py       - Дилерский центр;
    test_rocket\retailnetwork\views.py           - Крупная розничная сеть;
    test_rocket\retailnetwork\serializers.py    - Крупная розничная сеть;
    test_rocket\indentrepreneur\views.py         - Индивидуальный предприниматель.
    test_rocket\indentrepreneur\serializers.py  - Индивидуальный предприниматель.
 #### Пункт номер 5:
    Права доступа:
 ```python
 # test_rocket\test_rocket\setting.py
 REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],}
 ###################################################
 permission_classes = [permissions.IsAuthenticated] # in views
 ```
 ### Часть 2:
 #### Пункт номер 1:
    Заполнние базы данных тестовыми данными:
    test_rocket\SQL_INSERT - INSERT QUERY SQL
  #### Пункт номер 2(выполнена задача 1):  
     Сelery задачи:
     test_rocket\factory\task.py
     test_rocket\test_rocket\celery.py
```python
# test_rocket\test_rocket\celery.py
app.conf.beat_schedule = {
    'every': {
        'task': 'factory.tasks.update_debt',
        'schedule': crontab(minute=30), 
    },
}
# test_rocket\factory\task.py
@app.task
def update_debt():
    random_count = random.randint(5, 500)
    distributor = Distributor.objects.get(id=5)
    distributor.debt += random_count
    distributor.save()
```
#### Пункт номер 3:
    Сгенерировать qr:
    test_rocket\factory\views.py
    test_rocket\factory\task.py
    
```python
# test_rocket\factory\views.py
class GeneratedQRCodeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, *args):
        factory = Factory.objects.filter(id=pk)
        serializer = DetailFactorySerializer(factory, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk, *args):
        user_email = request.data['email']
        factory = Factory.objects.get(id=pk)
        img = qrcode.make(factory.idContacts.email)
        img.save(f"media/qr/{factory.name + user_email}.png")
        send_mail_task.delay(f"media/qr/{factory.name + user_email}.png", user_email)
        return Response({"Message": "QR Create. And send!"}, status=status.HTTP_200_OK)
# test_rocket\factory\task.py
@app.task
def send_mail_task(path, email):
    msg = EmailMessage('QRCODE CREATE', 'QR', EMAIL_HOST_USER, [email])
    msg.attach_file(path=path)
    try:
        msg.send()
    except BadHeaderError:
        return Response({"Message": "Send Email error!"}, status=status.HTTP_400_BAD_REQUEST)
```
#### Пункт номер 4:
    Валидация входящих данных:
    
```python    

# test_rocket\factory\serializers.py Factory

class DetailFactorySerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        if len(value) > 50:
            raise serializers.ValidationError("This field must be limited to 50 characters.")
        return value
       
    class Meta:
        model = Factory
        fields = '__all__'
        
# Product      
class DetailProductsFactorySerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        if len(value) > 25:
            raise serializers.ValidationError("This field must be limited to 25 characters.")
        return value

    def validate_date(self, value):
        if datetime(value.year, value.month, value.day, value.hour, value.minute, value.second) > datetime.now():
            raise serializers.ValidationError(
                "Incorrectness of the entered date of release of the product on the market.")
        return value
        
    class Meta:
        model = Products
        fields = '__all__'
```
#### Пункт номер 5:    
    Доступ Token:
```python 
# test_rocket\test_rocket\urls.py
urlpatterns = [
    (...)
    # Part №2
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),
]
# test_rocket\test_rocket\setting.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}
```  
    
##  
    
<img  src="https://user-images.githubusercontent.com/67423989/189544762-75f9cda9-b386-4f87-bb76-7c49d4423e7e.jpg" align="left" width="160">
  
# Ilya Chernik

### Personal info:
   • Country: Belarus, Minsk)<br/>
   • Discord: Mounted.rk (@MountedRPC)<br/>
   • Email: Mounted.rk@gmail.com<br/>
   • Linkedln:  [ILya Chernik](https://www.linkedin.com/in/ilya-chernik-390177222/)

##

### Education:
    Minsk College of Business  Sep 2018 - May 2023

    I study at the specialty POIT (Information Technology Software).
    I am getting a secondary education.

##
    
    
    
    
    
    
