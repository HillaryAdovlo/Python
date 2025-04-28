class Television:
    """
    A class to mimic the action of a TV with basic controls like power, volume, channel, and mute.
    """

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        starts a new Television object with power off, volume and channel set to minimum values, and not muted.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__previous_volume = Television.MIN_VOLUME  # for mute functionality

    def power(self) -> None:
        """
        changes the power status of the television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mute or unmutes the television.
        If muted, it sets the  volume to MIN_VOLUME and saves the current volume.
        If unmuted, it restores the volume to its previous level.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume  # Restore volume
            else:
                self.__muted = True
                self.__previous_volume = self.__volume  # Save volume
                self.__volume = Television.MIN_VOLUME

    def channel_up(self) -> None:
        """
        Increase the television channel by one.
        If at the maximum channel, goes back to the minimum channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrease the television channel by one.
        If at the minimum channel, goes back around to the maximum channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increase the television volume by one.
        Volume can only be changed if the TV is not muted and the volume is below MAX_VOLUME.
        """
        if self.__status and not self.__muted:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the television volume by one.
        Volume can only be changed if the TV is not muted and the volume is above MIN_VOLUME.
        """
        if self.__status and not self.__muted:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return a string representation of the television's current state,
        showing power status, channel, and either volume or muted status.
        """
        power_status = "True" if self.__status else "False"
        if self.__muted:
            return f'Power = {power_status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {power_status}, Channel = {self.__channel}, Volume = {self.__volume}'
