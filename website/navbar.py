from flask_nav.elements import View, Navbar, Subgroup

navbar = Navbar(
    'IoT',
    View('Home', '.index'),
    Subgroup('Account',
             View('Settings', '.account_settings'),
             View('Log out', '.logout')
             ),
    View('Home Actions', '.home_actions'),
    View('Devices', '.devices'),
    View('Room View', '.room_view')
)
