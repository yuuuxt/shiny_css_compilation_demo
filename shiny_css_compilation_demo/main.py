# Core
from shiny import App, render, ui, Inputs, Outputs, Session

custom_theme = ui.Theme(name="test_theme", preset="yeti")

app_ui = ui.page_fixed(
    ui.h1("Title"),
    ui.output_code("greeting"),
    theme=custom_theme, # using this theme causes error
)

"""
sass.CompileError: Error: File to import not found or unreadable: C:Usersmy-user
       ppDataLocalpypoetryಬhevirtualenvsshiny-css-compilation-demo-4s52n7d6-py3.10Libsite-packagesshinywwwsharedsasspresetyeti_01_functions.scss.
        on line 1:1 of stdin
>> @import "C:\Users\my-user\AppData\Local\pypoetry\Cache\virtualenvs\shiny-css-co
"""

def server(input: Inputs, output: Outputs, session: Session):
    @render.code
    def greeting():
        return "Hello, world!"


app = App(app_ui, server)
