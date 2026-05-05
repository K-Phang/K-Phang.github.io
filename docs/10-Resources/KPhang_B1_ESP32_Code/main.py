# EGR314 Team 201 B1 Propulsion main program
# K Phang
# Final report code artifact
# Notes:
# - Receiver/module ID: D
# - UART2 at 9600 baud
# - Local test commands: F = forward, B = back
# - Legacy throttle handling included
# - Final hardware testing used ESP32 breadboard/devkit support because the PCB 3.3 V rail did not work

from machine import UART, Pin
import asyncio

# UART
uart = UART(2, 9600, tx=17, rx=16)
uart.init(9600, bits=8, parity=None, stop=1, flow=0)

# Motor pins
in1 = Pin(18, Pin.OUT)
in2 = Pin(19, Pin.OUT)

# Buttons
btn_forward = Pin(4,  Pin.IN, Pin.PULL_UP)
btn_reverse = Pin(21, Pin.IN, Pin.PULL_UP)
btn_speed   = Pin(23, Pin.IN, Pin.PULL_UP)

# State
team_ids = ['A','B','C','D','E','F','G','H','I','J','X']
MY_ID = 'D'

# Speed levels: (on_ms, off_ms, label)
speed_levels = [
    (1000,   0, '100%'),
    ( 750, 250,  '75%'),
    ( 250, 250,  '50%'),
    ( 125, 375,  '25%'),
]
speed_index = 0
current_dir = 0  # 0=stop, 1=forward, -1=reverse

# --- Motor ---
def set_forward():
    in2.value(0)
    in1.value(1)

def set_reverse():
    in1.value(0)
    in2.value(1)

def set_stop():
    in1.value(0)
    in2.value(0)

def toggle_forward():
    global current_dir
    current_dir = 0 if current_dir == 1 else 1
    print('FORWARD toggle | dir:', current_dir,
          '| speed:', speed_levels[speed_index][2])

def toggle_reverse():
    global current_dir
    current_dir = 0 if current_dir == -1 else -1
    print('REVERSE toggle | dir:', current_dir,
          '| speed:', speed_levels[speed_index][2])

def toggle_speed():
    global speed_index
    speed_index = (speed_index + 1) % 4
    on_ms, off_ms, label = speed_levels[speed_index]
    print('Speed:', label, '| on:', on_ms, 'ms | off:', off_ms, 'ms')

async def motor_pulse_task():
    while True:
        if current_dir == 0:
            set_stop()
            await asyncio.sleep_ms(20)
            continue

        on_ms, off_ms, label = speed_levels[speed_index]

        if current_dir == 1:
            set_forward()
        else:
            set_reverse()

        if off_ms == 0:
            await asyncio.sleep_ms(20)
            continue

        await asyncio.sleep_ms(on_ms)
        set_stop()
        await asyncio.sleep_ms(off_ms)

# --- UART ---
def build_message(sender, receiver, data):
    return b'AZ' + bytes([ord(sender)]) + bytes([ord(receiver)]) + data + b'YB'

def parse_message(raw):
    if len(raw) < 6:
        return None
    if raw[0] != ord('A') or raw[1] != ord('Z'):
        return None
    if raw[-2] != ord('Y') or raw[-1] != ord('B'):
        return None
    sender   = chr(raw[2])
    receiver = chr(raw[3])
    if sender not in team_ids or receiver not in team_ids:
        return None
    data = raw[4:-2]
    return sender, receiver, data

def handle_message(data):
    """Handle data payload addressed to this node"""
    global speed_index, current_dir

    if len(data) == 0:
        return

    cmd = chr(data[0])

    if cmd == 'F':
        toggle_forward()
        ack = build_message(MY_ID, 'A', b'F_ACK')
        uart.write(ack)
        print('ACK: forward toggle')

    elif cmd == 'B':
        toggle_reverse()
        ack = build_message(MY_ID, 'A', b'B_ACK')
        uart.write(ack)
        print('ACK: reverse toggle')

    elif data[0] == 2 and len(data) >= 2:
        # Legacy throttle message type 2
        throttle_val = data[1]

        if throttle_val > 128:
            pct = ((throttle_val - 128) * 100) // 127
            if   pct >= 75: new_idx = 0
            elif pct >= 50: new_idx = 1
            elif pct >= 25: new_idx = 2
            else:           new_idx = 3
            speed_index = new_idx
            current_dir = 1

        elif throttle_val < 128:
            pct = ((128 - throttle_val) * 100) // 127
            if   pct >= 75: new_idx = 0
            elif pct >= 50: new_idx = 1
            elif pct >= 25: new_idx = 2
            else:           new_idx = 3
            speed_index = new_idx
            current_dir = -1

        else:
            current_dir = 0

        ack = build_message(MY_ID, 'A', bytes([2, throttle_val]))
        uart.write(ack)
        print('Throttle ACK:', throttle_val)

    elif data[0] == 12:
        print('ROLLCALL: PRESENT')

async def uart_receive():
    while True:
        try:
            raw = uart.read()

            if not raw:
                await asyncio.sleep_ms(100)
                continue

            parsed = parse_message(raw)

            if parsed is None:
                await asyncio.sleep_ms(100)
                continue

            sender, receiver, data = parsed

            if sender == MY_ID:
                await asyncio.sleep_ms(100)
                continue

            if receiver == MY_ID:
                print('uart rx: message for me:', data)
                handle_message(data)

            elif receiver == 'X':
                print('ROLLCALL broadcast: PRESENT')

            else:
                uart.write(raw)
                print('uart rx: forwarded', raw)

        except Exception as e:
            print('Error in uart_receive:', e)

        await asyncio.sleep_ms(100)

async def uart_send():
    while True:
        msg = build_message(MY_ID, 'X', b'HiProf')
        uart.write(msg)
        print('uart tx: ping sent')
        await asyncio.sleep(5)

# --- Buttons ---
async def button_task():
    last_f = last_r = last_s = 1

    while True:
        f = btn_forward.value()
        r = btn_reverse.value()
        s = btn_speed.value()

        if f == 0 and last_f == 1:
            toggle_forward()
            await asyncio.sleep_ms(200)

        if r == 0 and last_r == 1:
            toggle_reverse()
            await asyncio.sleep_ms(200)

        if s == 0 and last_s == 1:
            toggle_speed()
            await asyncio.sleep_ms(200)

        last_f = f
        last_r = r
        last_s = s
        await asyncio.sleep_ms(20)

# --- Main ---
async def main():
    t1 = asyncio.create_task(uart_receive())
    t2 = asyncio.create_task(uart_send())
    t3 = asyncio.create_task(motor_pulse_task())
    t4 = asyncio.create_task(button_task())
    await asyncio.gather(t1, t2, t3, t4)

asyncio.run(main())
