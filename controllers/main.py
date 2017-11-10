from weppy import response

from base_n_treble import app, auth


@app.route("/")
def welcome():
    response.meta.title = "Base N Treble"
    return dict()


@app.route('/account(/<str:f>)?(/<str:k>)?')
def account(f, k):
    response.meta.title = "Base N Treble | Account"
    form = auth(f, k)
    return dict(req=f, form=form)
