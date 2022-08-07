```mermaid
classDiagram

    Text <|-- PlainText
    Text <|-- TextDecorator
    TextDecorator <-- Text
    class Text{
        +display() str
    }

    class PlainText{
    }

    class TextDecorator{
    }
```
