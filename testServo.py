from Adafruit_MotorHAT.Adafruit_PWM_Servo_Driver import PWM
import atexit

pwm=PWM(0x60)

pwm_frequency=60
pwm.setPWMFrequency(pwm_frequency)

period_in_ms=1000/pwm_frequency
pulse_steps=4096
servo_midPoint_ms=1.5
deflect_90_in_ms=0.5
flect_90_in_ms=2
steps_per_ms=pulse_steps/period_in_ms
steps_per_degree=(deflect_90_in_ms*steps_per_ms)/90
sero_mid_point_steps=servo_midPoint_ms*steps_per_ms

def convert_degrees_to_pwm(position):
    return int(sero_mid_point_steps+(position*steps_per_degree))

def stop():
    #set pin off flag
    pwm.setPWM(0,0,4096)

atexit.register(stop)

while 1:
    position=int(input("请输入角度（-90 ~ 90 0是中间）:"))
    end_step=convert_degrees_to_pwm(position)
    PWM.setPWM(0,0,end_step)