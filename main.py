def on_received_number(receivedNumber):
    basic.show_number(receivedNumber)
    basic.show_number(radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH))
    serial.write_number(receivedNumber)
    serial.write_number(radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH))
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    basic.show_number(4)
    music.ring_tone(262)
    pause(1000)
    music.stop_all_sounds()
    radio.send_string("test")
    radio.send_value("name", 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    serial.write_value(name, value)
    basic.show_string(name)
    basic.show_number(value)
radio.on_received_value(on_received_value)

radio.set_group(1)

def on_forever():
    pass
basic.forever(on_forever)
