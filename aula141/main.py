# from log import LogPrintMixin, LogFileMixin

# lp = LogPrintMixin()
# lp.log_error('Qualquer coisa')
# lp.log_success('Que legal')

# lf = LogFileMixin()
# lf.log_error('Qualquer coisa')
# lf.log_success('Que legal')

from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy_s.ligar()
galaxy_s.desligar()
iphone.ligar()
iphone.desligar()
