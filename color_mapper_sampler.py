#!/usr/bin/python3

from color_mapper import ColorMapper

mapper = ColorMapper()

print("<html>")
print("<style>"
    "table td { border:1px solid black; text-align:center; height: 90px; width: 100px; }"
    "div { color: #ffffff; }"
    "</style>")
print("<table>")

values = [0, 64, 128, 191, 255]

for r in values:
    for g in values:
        print("<tr>")
        for b in values:
            print("<td style='background-color: rgb(" + str(r) + "," + str(g) + "," + str(b) + ")'>" 
                    + mapper.map([r,g,b]) + "<br>" + str(r) + "-" + str(g) + "-" + str(b)
                    + "<div>" + mapper.map([r,g,b]) + "<br>" + str(r) + "-" + str(g) + "-" + str(b) + "</div>"
                    + "</td>")
        print("</tr>")

print("</table>")
print("</html>")
