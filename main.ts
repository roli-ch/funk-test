radio.onReceivedNumber(function (receivedNumber) {
    basic.showNumber(receivedNumber)
    basic.showNumber(radio.receivedPacket(RadioPacketProperty.SignalStrength))
    serial.writeNumber(receivedNumber)
    serial.writeNumber(radio.receivedPacket(RadioPacketProperty.SignalStrength))
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(4)
    music.ringTone(262)
    pause(1000)
music.stopAllSounds()
    radio.sendString("test")
    radio.sendValue("name", 0)
})
radio.onReceivedString(function (receivedString) {
    music.play(music.tonePlayable(349, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(2)
})
radio.onReceivedValue(function (name, value) {
    serial.writeValue(name, value)
    basic.showString(name)
    basic.showNumber(value)
})
radio.setGroup(1)
basic.forever(function () {
	
})
