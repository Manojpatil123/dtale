
from flask import redirect
import pandas as pd
from dtale.app import build_app, initialize_process_props
from dtale.views import startup
from dtale.utils import build_url


HOST = "0.0.0.0"
PORT = 8080

initialize_process_props(HOST, PORT)
app_url = build_url(HOST, str(PORT))
app = build_app(app_url, reaper_on=False)


@app.route("/create-df")
def create_df():
    df = pd.DataFrame(dict(a=[1, 2, 3], b=[4, 5, 6]))
    instance = startup("", data=df, ignore_duplicate=True)

    return redirect(f"/dtale/main/{instance._data_id}", code=302)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)