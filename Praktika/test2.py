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
            #создал таблицу
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS `team1`(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            qa INT(10))
            '''
            cursor.execute(create_table_query)

            insert_qu = '''INSERT INTO `team` (name,qa)
            VALUES
            ('Erik',10),
            ('BMV',9),
            ('NNN',8),
            ('jona',5),
            ('jjjd',8),
            ('kkkk',7),
            ('RYHNBGV',10),
            ('dte',7),
            ('gsdjks',4),
            ('ASD',10)'''
            
            cursor.execute(insert_qu)
            connection.commit()
            print('data inserted')   
            print('table team created')


    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)
