from abc import ABC

class Text(ABC): 
    
    def display(self) -> str:
        """returns the string stored with modifiers or in a plain form"""

if __name__ == "__main__":
    class T(Text):
        def display(self) -> str:
            return "working"
    t = T("some text")
    print(t.display())
