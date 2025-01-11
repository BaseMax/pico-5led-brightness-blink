from machine import Pin, PWM, ADC
from time import sleep

LED1 = PWM(Pin(6))
LED2 = PWM(Pin(7))
LED3 = PWM(Pin(8))
LED4 = PWM(Pin(9))
LED5 = PWM(Pin(10))

BTN_ON = Pin(3, Pin.IN, Pin.PULL_UP)
BTN_OFF = Pin(4, Pin.IN, Pin.PULL_UP)

potentiometer = ADC(Pin(26))

LED1.freq(1000)
LED2.freq(1000)
LED3.freq(1000)
LED4.freq(1000)
LED5.freq(1000)

is_odd = True
led_state = False

while True:
    maxvalue = potentiometer.read_u16()
    minvalue = 0
    btn_on_pressed = not BTN_ON.value()
    btn_off_pressed = not BTN_OFF.value()

    if btn_off_pressed:
        print("second button")
        LED1.duty_u16(minvalue)
        LED2.duty_u16(minvalue)
        LED3.duty_u16(minvalue)
        LED4.duty_u16(minvalue)
        LED5.duty_u16(minvalue)
        led_state = False

    if btn_on_pressed and btn_off_pressed: 
        print("both")
        LED1.duty_u16(maxvalue)
        LED2.duty_u16(maxvalue)
        LED3.duty_u16(maxvalue)
        LED4.duty_u16(maxvalue)
        LED5.duty_u16(maxvalue)
    elif btn_on_pressed:
        print("first button")
        led_state = True
    
    if led_state and not btn_off_pressed:
        if is_odd:
            LED1.duty_u16(maxvalue)
            LED3.duty_u16(maxvalue)
            LED5.duty_u16(maxvalue)
            LED2.duty_u16(minvalue)
            LED4.duty_u16(minvalue)
        else:
            LED2.duty_u16(maxvalue)
            LED4.duty_u16(maxvalue)
            LED1.duty_u16(minvalue)
            LED3.duty_u16(minvalue)
            LED5.duty_u16(minvalue)
        is_odd = not is_odd
        sleep(0.3)

    sleep(0.05)
