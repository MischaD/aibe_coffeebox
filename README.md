# kitty
A GUI app in python to manage the kitty for coffee with a Raspberry Pi.

# Table of Contents
1. [Flow Chart](#flow-chart)
2. [Class Diagram](#class-diagram)
3. [Third Example](#third-example)

## Flow Chart

## Class Diagram

```mermaid
classDiagram
    class Tk
    class CafeApp{
        String database
        __init__(self)
        create_tree(self, parent) tree
        user_selected(self, event)
        popup_window(self)
    }
    class PopupWindow{
        __init__(self,parent)
        get_selected_item_price(self, item)
        get_price(self)
    }

    Tk <|-- CafeApp
```