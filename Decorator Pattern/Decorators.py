from Text import Text 
from PlainText import PlainText
from colorama import Fore, Style, init, Back 

# init(autoreset=True)

class RedColoredText(Text):
    def __init__(self, text_obj: Text):
        self._text_obj = text_obj
    
    def display(self) -> str:
        return Fore.RED + self._text_obj.display()


class BlueColoredText(Text):
    def __init__(self, text_obj: Text):
        self._text_obj = text_obj
    
    def display(self) -> str:
        return Fore.BLUE + self._text_obj.display()



class BlueBackgroundText(Text):
    def __init__(self, text_obj: Text):
        self._text_obj = text_obj
    
    def display(self) -> str:
        return Back.BLUE + self._text_obj.display()

class GreenBackgroundText(Text):
    def __init__(self, text_obj: Text):
        self._text_obj = text_obj
    
    def display(self) -> str:
        return Back.GREEN + self._text_obj.display()


def main() -> None:
    obj: Text = RedColoredText(PlainText("Seom Text"))
    obj: Text = BlueBackgroundText(obj)
    print(obj.display()) 
if __name__ == "__main__":
    main()
