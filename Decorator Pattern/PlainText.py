from Text import Text

class PlainText(Text):

    def __init__(self, text: str) -> None:
        self._text = text

    def display(self) -> str:
        return self._text
