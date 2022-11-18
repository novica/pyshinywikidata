from shiny import App, render, ui, reactive, req
from .functions import endpoint_url, get_results, wrangle_results
from .testmodule import modUI, modServer

app_ui = ui.page_fluid(
    ui.row(
        ui.column(6,
                  ui.h2("Wikidata demo"),
                  ui.input_text(id='country_code',
                                label="Wikidata Country Code"),
                  ui.input_action_button(id='enter_code', label="Enter Code"),
                  ui.output_text_verbatim("txt"),
                  ui.output_text_verbatim("res")),
        ui.column(3,
                  modUI(id = "testmodule1")
                  )
    )
)


def server(input, output, session):

    @reactive.Calc
    def paste_query():
        req(input.country_code)
        query = """SELECT ?personLabel ?personGenderLabel ?dateOfBirth ?politicalPartyLabel ?spouseLabel ?childLabel WHERE {{
                    ?person wdt:P106 wd:Q82955;
                    wdt:P27 {country_code};
                    wdt:P21 ?personGender;
                    wdt:P569 ?dateOfBirth;
                    OPTIONAL {{?person wdt:P102 ?politicalParty. }}
                    OPTIONAL {{?person wdt:P26 ?spouse. }}
                    OPTIONAL {{?person wdt:P40 ?child. }}
                    SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
                    }}
                    LIMIT 500""".format(country_code=input.country_code())
        return query

    @reactive.Calc()
    def query_results():
        req(input.country_code)
        results = get_results(endpoint_url=endpoint_url(), query=paste_query())
        names = wrangle_results(results=results)
        return names

    @output
    @render.text
    @reactive.event(input.enter_code)
    def txt():
        return paste_query()

    @output
    @render.text
    @reactive.event(input.enter_code)
    def res():
        res = query_results()
        return res

    modServer(id = "testmodule1")


app = App(app_ui, server)
