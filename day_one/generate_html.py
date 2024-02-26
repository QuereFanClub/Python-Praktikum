# Bearbeitet mit Enno Pieper & Sandro Schusters

import html


def createHtmlElement(type: str, classname=None, id=None, style=None, content=None, text: str = ""):
    attributes: list[str] = []
    attributes.append(f" class=\"{str(classname)}\"") if classname is not None else ""
    attributes.append(f" id=\"{str(id)}\"") if id is not None else ""
    attributes.append(f" style=\"{str(style)}\"") if style is not None else ""

    starting_tag: str = f"<{type}{''.join(attributes)}>"
    closing_tag: str = f"</{type}>"

    if content is not None:
        return f"{starting_tag}{str(content)}{closing_tag}"
    elif text is not None:
        html_text = html.escape(text)
        return f"{starting_tag}{html_text}{closing_tag}"
    else:
        return f"{starting_tag}{closing_tag}"


span = createHtmlElement("span", text="Werbung <:)")
div = createHtmlElement("div", classname="ad", id="teaser", style="width: 100%;", content=span)
print(span)
print(div)
# <div class="ad" id="teaser" style="width: 100%;">WERBUNG &lt;:)</div>
