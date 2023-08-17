from reactpy import component, html


@component
def MissingLink():
    return html.div(
        html.div(
            {'class': 'container mt-3'},
            html.h1(html.h1("Missing Link 🔗‍💥"))
        ),
    )
