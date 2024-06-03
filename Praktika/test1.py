import pymysql
import pymysql.cursors
from main_config_base import host,user,password,db_name

try:
    connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
    )
    print('succsess')
    print('#' * 30)

    try:
        with connection.cursor() as cursor:
            #тут пишем запросы
             
            check_table = 'SHOW TABLES LIKE "good"'
            cursor.execute(check_table)
            result = cursor.fetchone()
            if result:
               print('good')
            else:
               print('not good')
    except Exception as e:
        print('An error ')
        print(e)        
except Exception as ex:
        print('An error ')
        print(ex)        

