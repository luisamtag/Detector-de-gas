import RPi.GPIO as GPIO
import time

# Configuración de pines
buzzer_pin = 5
mq4_pin = 37

# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(mq4_pin, GPIO.IN)

# Función para detectar gas
def detectar_gas():
    gas_detected = GPIO.input(mq4_pin)
    return gas_detected

# Función para activar el buzzer
def activar_buzzer():
    GPIO.output(buzzer_pin, GPIO.HIGH)

# Función para desactivar el buzzer
def desactivar_buzzer():
    GPIO.output(buzzer_pin, GPIO.LOW)

# Loop principal
try:
    while True:
        gas = detectar_gas()
        
        if gas == GPIO.HIGH:
            print("¡Gas detectado!")
            activar_buzzer()
        else:
            desactivar_buzzer()
        
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()