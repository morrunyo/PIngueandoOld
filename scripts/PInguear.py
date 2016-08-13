import logging
import time
import RPi.GPIO as GPIO
logging.basicConfig(filename='/home/pi/PIngueando/logs/'+time.strftime("%Y%m%d")+'_pinguear.txt',format='%(asctime)s %(message)s',level=logging.DEBUG)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, False)
logging.info('Iniciando PIngueo...')
GPIO.output(18, True)
time.sleep(10)
GPIO.output(18, False)
logging.info('PIngueo finalizado...')
exit(0)
