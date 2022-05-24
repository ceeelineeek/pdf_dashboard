import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.A(
                        html.Img(
                            src=app.get_asset_url(
                                "thermoplan_sustain_logo.png"),
                            className="logo",
                        ),
                        href="https://www.thermoplan.ch/de/thermoplan/nachhaltigkeit",
                    ),
                    # html.A(
                    #     html.Button(
                    #         "Enterprise Demo",
                    #         id="learn-more-button",
                    #         style={"margin-left": "-10px"},
                    #     ),
                    #     href="https://plotly.com/get-demo/",
                    # ),
                    # html.A(
                    #     html.Button("Source Code", id="learn-more-button"),
                    #     href="https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-financial-report",
                    # ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Thermoplan AG, Product Environmental Report")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/dash-financial-report/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/dash-financial-report/overview",
                className="tab first",
            ),
            dcc.Link(
                "Black & White 4",
                href="/dash-financial-report/price-performance",
                className="tab",
            ),
            dcc.Link(
                "Black & White 4c",
                href="/dash-financial-report/portfolio-management",
                className="tab",
            ),
            dcc.Link(
                "Black & White 4neo", href="/dash-financial-report/fees", className="tab"
            ),
            dcc.Link(
                "Thermoplan AG",
                href="/dash-financial-report/distributions",
                className="tab",
            ),
            dcc.Link(
                "News & Reviews",
                href="/dash-financial-report/news-and-reviews",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
