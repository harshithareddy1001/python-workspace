from abc import ABC,abstractmethod
class electronics(ABC):
    @abstractmethod
    def play_video(self):
        pass
class laptop(electronics):
    def play_video(self):
        print("press play button frrom keyboard")
class mobile(electronics):
    def play_video(self):
        print("press play button frrom keyboard")
laptop=laptop()
laptop.play_video()
mob=mobile()
mob.play_video()