import gspread
from oauth2client.service_account import ServiceAccountCredentials


def view(params):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    a = {
        "type": "service_account",
        "project_id": "turing-striker-162110",
        "private_key_id": "4f7d7dd61c3b5f779955c9208c2a8fc013679e16",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCp8xh0U2ME+jDV\nvcO5Oh5120fsL8bLhOiBTWIL77fUcie0izQY9R+iHK5QEXUpobacK7grfS4rLmYt\nD47WLycaw/J+QED17N0xXpvyy7APpO6YWRselP0iMKSYho1z+giyzXnCgUDM9OGZ\n8SVySLwNQIv49TF8h97j3Mo3A3oei8Ka4sNNnhEn4M1ay5frpT7oVlDner78A8Fj\nqIkOR3nrY4YmNsjPheinIfu//FuZZXB6iLWDywWNeDlG/j/Ib/Q9WTaVbECqC5lH\nf1J8zX2R1ViEbP3Y2rPQld5jHxFtk2qGKAgwmSzU2P9HtajQgkoUhNqHFCxwdGTs\nSuxwx6gjAgMBAAECggEAGC2tfdCRPAI2Pr/OioR8v0AREEakeIxHodcMYG4HOsfP\njfg8qLeoUPbV9oPipdIhJJXJurzb+9O660/qfolbKGEr7OSfo/1CDjCLbPRSmjSD\np2lh74IQg16P7uKRrv1/DaUoXKY+kwox1dDA3EIB0xGATc01xaWfmHkZzHrc/bRM\nD0XCcUlel3fF8ngR5eZNfeGADhLVsArbIJBT5tx+gowm50K6ZsIoIB3b5ecCOVOx\noqW9eWmosuhXjTjcKZO9RfewBcTOskBB1cZiJxkOa22ZLuliYmxjdHuZf83YT3b/\nAh8Gbuczw5VzlBQe5YrdnLWOwcZ2fiQLwrZPaecQIQKBgQDeZ4MZ8mNvFTp/+ocg\n+E3cDpp3F8nAsOtaKy8A3MruTez1NEHuRXyc0WTFcFlGQFc1UQfA874nN686hBf+\nq/02gwdEge/MPFWm+duiARIXOGgqDXUvI6HceZyZYZlYhRQ8qhdf3/bBCOdSa0Of\n1RbAGVmhzasmeL1qokmXg9qOQwKBgQDDnyG6O1Dk/30Z/Al1rLaNrE6k7+olY+WC\nBTbzbb9M3wi1nZ/uR+Mr5T5KF0V4tCwcAgZRQ/NsIejVBWWfrFBcSuztxEKtl2ec\nVgalCNNJV4k8A6TppLjqWjLHGPqkimnHC6RH0QIdvl/mSRzlzkrrxSE28IlyWXH2\nv89d19AQoQKBgFRZvgdhPwUqb/2J7yY6Bo2nnD3+7639a8XPCwywsOag93YoU7ki\n8ZgocqfPbIyQaoL2MJKl30DQhc0TvGYCpQ6/s0nwXhp/55xkt0BCV7Im2prYb9Fp\nGkKcfSBPO/Gux3YarLLYJqYf0lwYApXkI7TH6I7NilQVBwIievbUM1gxAoGAUy4o\nLkMom6cTr+fesd3V5hn9et7VJj77CTVkb1AcRviTgH5c0fpZW4Hn4aNRlAiwtNwb\niZSmPjWRBnt8AdBIf2YQpu2MGLpHgU+HFcfR597D6PP3vK2hP21JKCWz9iEw50VI\n/oyeJL2dk5NFKWZ1rxksjWrsVuY3sl9PMq0guOECgYA/2kBFXCLcTeu4+qSGTzuv\nNwhZpyG3Y6YwTp49O3c8ofarZ38mYozL7efQUivxhoBKE+WIQhxN7bdIAlSEX/rx\nmpWIp/VOabt0vyrZBqcXBOKjRtIp9Oz+OCSBB7n5HGkwRYYSGOxPXWV04/iVLBZe\nZ0HAGFeFWKUky7y88szXqg==\n-----END PRIVATE KEY-----\n",
        "client_email": "starting-account-xawhri1413s4@turing-striker-162110.iam.gserviceaccount.com",
        "client_id": "102083397472594304607",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/starting-account-xawhri1413s4%40turing-striker-162110.iam.gserviceaccount.com"
    }

    credentials = ServiceAccountCredentials._from_parsed_json_keyfile(a, scope)

    gc = gspread.authorize(credentials)

    sh = gc.open_by_url(
        'https://docs.google.com/spreadsheets/d/1k_k59oXUVaAai2auEcQ884fnemmhXdaSjPjNeMolfzE/edit?ts=5dea0f98#gid=0')
    my_list = [param for param in params]

    return sh.sheet1.append_row(my_list)
