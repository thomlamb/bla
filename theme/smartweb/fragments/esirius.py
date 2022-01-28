import requests


def message(self):
    if "smartweb.esirius_apikey" not in context.portal_registry:
        return ""
    esirius_apikey = context.portal_registry["smartweb.esirius_apikey"]
    response = requests.get(f"https://passerelle-braine-l-alleud.test.entrouvert.org/esirius-swi/prod/get_all_indicators?apikey={esirius_apikey}")
    data = response.json()
    if data.get("data") is None:
        return ""
    return data.get("data")[0].get("estimatedAvgWaitingTime")