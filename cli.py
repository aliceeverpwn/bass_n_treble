"""
Usage:   weppy --app=base_n_treble <command>
Example: weppy --app=base_n_treble shell
"""
from base_n_treble import app


@app.cli.command('routes')
def print_routing():
    print(app.route.routes_out)


@app.cli.command('get_users')
def print_users():
    from base_n_treble import db
    from base_n_treble.models.user import User
    rows = db(User.email).select()
    for row in rows:
        print(row)
