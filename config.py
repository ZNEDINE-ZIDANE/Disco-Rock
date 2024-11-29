class Config:
    SECRET_KEY = 'qqqqqq'
    DEBUG      = True

class ConfigDeveloment(Config):
    MYSQL_HOST      = 'localhost'
    MYSQL_USER      = 'root'
    MYSQL_PASSWORD  = 'mysql'
    MYSQL_DB        = 'rock'
    
'''
    #pythonanywhere
    MYSQL_HOST      = ''
    MYSQL_USER      = 'rock'
    MYSQL_PASSWORD  = ''
    MYSQL_DB        = ''
      
'''

class MailConfig(Config):
    MAIL_SERVER     = 'smtp.gmail.com'
    MAIL_PORT       = 587
    MAIL_USE_TLS    = True
    MAIL_SSL        = False
    MAIL_USERNAME   = 'pedro.mayorga1800@alumnos.udg.mx'
    MAIL_PASSWORD   = 'rosp vvzz tywu abmi'
    MAIL_DEFAULT_SENDER = 'pedro.mayorga1800@alumnos.udg'
    MAIL_ASCII_ATTACHMENTS = True

config = {
    'development': ConfigDeveloment,
    'mail'       : MailConfig   
}