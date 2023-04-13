from daq.models import Tnh

def save_db(msg):
    db_tab1 = Tnh()
    db_tab1.temperature = float(msg.topic)
    db_tab1.humidity = float(msg.payload)

    print(db_tab1.temperature, db_tab1.humidity)



