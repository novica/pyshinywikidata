from shiny import module, ui, render


@module.ui
def modUI():
    return ui.div(
        ui.h2("Every column needs a title"),
        ui.strong("Awesome stuff"),
        ui.output_ui(id="ya")
    )


@module.server
def modServer(input, output, session):
    @output
    @render.ui
    def ya():
        dv = ui.div("This is some server-generated UI")
        return dv
