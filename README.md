# Bank Details API Based Project

This project is created using [Django REST framework](https://www.django-rest-framework.org/).

#### To run the project
*   install all the dependencies specified in ```requirements.txt``` file.
> For this project, CSV file which is present in [this repository](https://github.com/snarayanank2/indian_banks) is used.
*   run following commands:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runscript populate_db
    ```
> *python manage.py populate_db* command runs the script named [populate_db.py](../blob/master/bank_app/scripts/populate_db.py), which populate the database with the data stored in the csv file.
*   then to run the server run the following:
    ```bash
    python manage.py runserver
    ```
    
    
## Following is the full list of APIs created
| API endpoint        | HTTP Method           | Required Parameters  | Description|
| ------------- |:-------------:| -----:| ---:|
| ```/```      | GET | q (ifsc code of the branch) | This API endpoint will return details of a particular branch of which IFSC code in the q parameter is passed.|
| ```/get-branches/``` | POST      |  bank_name (name of the bank as per DB), city_name (city name as per stored in DB)  | This API will return a list of branches of the bank ```bank_name``` located in the city ```city_name```  |

For more details, refer to docstring of APIs.
