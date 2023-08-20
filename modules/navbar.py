from reactpy import component, html


BRAND = 'ECCPMA'


@component
def NavItemDropDownFabrication(label: str, is_active: bool = False):
    attribute = {'href': '#', 'role': 'button', 'data-bs-toggle': 'dropdown',
                 'aria-expanded': 'false'}
    if is_active:
        attribute.update({'class': 'nav-link active dropdown-toggle'})
    else:
        attribute.update({'class': 'nav-link dropdown-toggle'})

    return html.div(
        html.li(
            {'class': 'nav-item dropdown'},
            html.a(attribute, label),
            html.ul(
                {'class': 'dropdown-menu'},
                html.li(
                    html.a(
                        {
                            'class': 'dropdown-item',
                            'href': '/fabrication-status',
                            'type': 'button'
                        },
                        'Add Status'
                    )
                )
            )
        )
    )


@component
def NavItemDropDownConstruction(label: str, is_active: bool = False):
    attribute = {'href': '#', 'role': 'button', 'data-bs-toggle': 'dropdown',
                 'aria-expanded': 'false'}
    if is_active:
        attribute.update({'class': 'nav-link active dropdown-toggle'})
    else:
        attribute.update({'class': 'nav-link dropdown-toggle'})

    return html.div(
        html.li(
            {'class': 'nav-item dropdown'},
            html.a(attribute, label),
            html.ul(
                {'class': 'dropdown-menu'},
                html.li(
                    html.a(
                        {
                            'class': 'dropdown-item',
                            'href': '/construction-status',
                            'type': 'button'
                        },
                        'Add Status'
                    )
                )
            )
        )
    )


@component
def NavItemDropDownTask(label: str, is_active: bool = False):
    attribute = {'href': '#', 'role': 'button', 'data-bs-toggle': 'dropdown',
                 'aria-expanded': 'false'}
    if is_active:
        attribute.update({'class': 'nav-link active dropdown-toggle'})
    else:
        attribute.update({'class': 'nav-link dropdown-toggle'})

    return html.div(
        html.li(
            {'class': 'nav-item dropdown'},
            html.a(attribute, label),
            html.ul(
                {'class': 'dropdown-menu'},
                html.li(
                    html.a(
                        {
                            'class': 'dropdown-item',
                            'href': '/search-task',
                            'type': 'button'
                        },
                        'Search Task'
                    )
                ),
                html.li(
                    html.a(
                        {
                            'class': 'dropdown-item',
                            'href': '/input-task',
                            'type': 'button'
                        },
                        'Input Task'
                    )
                )
            )
        )
    )


@component
def NavItem(label: str, path: str, is_active: bool = False):
    attribute = {'href': path}
    if is_active:
        attribute.update(
            {'class': 'nav-link active', 'aria-current': 'page'},
        ),
    else:
        attribute.update(
            {'class': 'nav-link'},
        ),

    return html.div(
        html.li(
            {'class': 'nav-item'},
            html.a(attribute, label),
        ),
    )


@component
def NavBar(nav_attr: dict):
    return html.nav(
        {'class': 'navbar navbar-dark navbar-expand-sm bg-dark fixed-top'},
        html.div(
            {'class': 'container-fluid'},
            html.a(
                {'class': 'navbar-brand text-primary', 'href': '#'},
                f'{BRAND}'
            ),
            html.button(
                {
                    'class': 'navbar-toggler',
                    'type': 'button',
                    'data-bs-toggle': 'collapse',
                    'data-bs-target': '#navbarSupportedContent',
                    'aria-controls': 'navbarSupportedContent',
                    'aria-expanded': 'false',
                    'aria-label': 'Toggle navigation',
                },
                html.span({'class': 'navbar-toggler-icon'}),
            ),
            html.div(
                {'class': 'collapse navbar-collapse',
                 'id': 'navbarSupportedContent'},
                html.ul(
                    {'class': 'navbar-nav me-auto mb-2 mb-lg-0'},
                    NavItem('Home', '/', nav_attr.get('Home', False)),
                    NavItem('Blog', '/blog', nav_attr.get('Blog', False)),
                    NavItemDropDownTask('Task', nav_attr.get('Task', False)),
                    NavItemDropDownFabrication(
                        'Fabrication',
                        nav_attr.get('Fabrication', False)
                    ),
                    NavItemDropDownConstruction(
                        'Construction',
                        nav_attr.get('Construction', False)
                    ),
                    NavItem(
                        'Dashboard',
                        '/dashboard',
                        nav_attr.get('Dashboard', False)
                    )
                )
            )
        )
    )
