import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "11973721"))
    API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5622965116:AAHGo5ZLTRZ0TiXaNkhT49G5txIHGhSMkZ0")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1391556668")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQBEfsiIKyiEL0vZYfgCzXKVjmv8xhHtu6PUJpold8o6f5veO-XAKoCLXN3bVHvUGkCv9NgwTrWrnc3lZRwNdREsinh9wOZnc9wQOsllTUpvE2Hzbax8rhkji4Roqsaziw-sDdDfGft42t0DbGVlSe7lf_WOxbrFPlfyJ94AMiGpEYBIwT_VKT_QYrDl8IEwlYAuqgKoQVkhNeB0WFIKBYFAt42jVDfeZAZpNMnyQO9F5LVQCsUemf42czKfovAujA6xiIRr9c39y-nsWxxvO6arsCPatQ3uiRXqgvq6rwIcaNqnPBizNRyAAEPnAoLST82Jg3EC5Awet7oH800X8_5dUvF4PAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001342411240"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "UK_Auto_Forward_Bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
