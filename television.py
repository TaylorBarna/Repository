class Television:
    """
    A class representing details for a television object.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        A method to set default values of a television object.
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        A method to toggle whether a television object is powered on.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        A method to toggle whether a television object is muted.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        A method to increase the channel value of a television object.
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        A method to decrease the channel value of a television object.
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        A method to increase the volume value of a television object.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        A method to decrease the volume value of a television object.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to access television object information.
        :return: Object's information.
        """
        return (f"Power = {self.__status}, Channel = {self.__channel}, Volume = {0 if self.__muted == True else self.__volume}")