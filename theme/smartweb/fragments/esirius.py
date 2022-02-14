import requests


def message(self):
    if "smartweb.esirius_apikey" not in context.portal_registry:
        return ""
    self.request.response.setHeader("Cache-Control", "no-cache")
    esirius_apikey = context.portal_registry["smartweb.esirius_apikey"]
    response = requests.get(
        f"https://passerelle-braine-l-alleud.test.entrouvert.org/esirius-swi/prod/get_all_indicators?apikey={esirius_apikey}")
    data = response.json()
    if data.get("data") is None:
        return

    data = data.get("data")[0]
    if data.get("closed") is True:
        return {"closed": True}

    level = None
    # str au format "HH:MM:SS"
    time = data.get("estimatedAvgWaitingTime")
    hours, minutes, seconds = time.split(":")
    seconds = int(seconds)
    hours = int(hours) * 60
    minutes = int(minutes) + 1 if seconds > 1 else int(minutes)
    time = hours + minutes
    if time < 5:
        level = "level0"
    elif time < 10:
        level = "level1"
    elif time < 20:
        level = "level2"
    elif time < 40:
        level = "level3"
    else:
        level = "level4"
    value = "<span class=\"value\">{}</span>".format(time)
    unit = "<span class=\"unit\">minute{}</span>".format("s" if time > 1 else "")
    return {"closed": False,
            "level": level,
            "time_str": "{} {}".format(value, unit)
            }