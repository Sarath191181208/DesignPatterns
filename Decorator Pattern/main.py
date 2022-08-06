from Text import Text
from PlainText import PlainText
from Decorators import RedColoredText
from Decorators import GreenBackgroundText, BlueBackgroundText
from colorama import init


init(autoreset=True)


def main() -> None:
    txt = PlainText("Seom Text")

    red_txt: Text = RedColoredText(txt)
    txt_blue_bg: Text = BlueBackgroundText(txt)

    print(red_txt.display())
    print(txt_blue_bg.display())

    red_txt_green_bg = GreenBackgroundText(red_txt)
    red_txt_blue_bg = BlueBackgroundText(red_txt)

    print(red_txt_blue_bg.display())
    print(red_txt_green_bg.display())


if __name__ == "__main__":
    main()
