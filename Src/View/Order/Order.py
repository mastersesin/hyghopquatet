import gspread
from oauth2client.service_account import ServiceAccountCredentials


def view(params):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('turing-striker-162110-4f7d7dd61c3b.json', scope)

    gc = gspread.authorize(credentials)

    sh = gc.open_by_url(
        'https://docs.google.com/spreadsheets/d/1k_k59oXUVaAai2auEcQ884fnemmhXdaSjPjNeMolfzE/edit?ts=5dea0f98#gid=0')
    my_list = [param for param in params]
    return sh.sheet1.append_row(my_list)
