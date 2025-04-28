from television import Television

# ----------------- init -----------------
def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

# ----------------- power -----------------
def test_power_toggle_on():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_power_toggle_off():
    tv = Television()
    tv.power()
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

# ----------------- mute -----------------
def test_mute_while_on():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_unmute_while_on():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_mute_while_off():
    tv = Television()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_unmute_while_off():
    tv = Television()
    tv.mute()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

# ----------------- channel up -----------------
def test_channel_up_while_off():
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_up_while_on():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

def test_channel_up_wrap_around():
    tv = Television()
    tv.power()
    for _ in range(5):  # MAX_CHANNEL = 3, so this loops back to 1
        tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

# ----------------- channel down -----------------
def test_channel_down_while_off():
    tv = Television()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_down_wrap_around():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

# ----------------- volume up -----------------
def test_volume_up_while_off():
    tv = Television()
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_volume_up_while_on():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_volume_up_while_muted():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_up_over_max():
    tv = Television()
    tv.power()
    for _ in range(5):  # Should max out at 2
        tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

# ----------------- volume down -----------------
def test_volume_down_while_off():
    tv = Television()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_volume_down_while_on():
    tv = Television()
    tv.power()
    for _ in range(3):  # Increase to max
        tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_volume_down_while_muted():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_volume_down_below_min():
    tv = Television()
    tv.power()
    tv.volume_down()  # Already at min
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
