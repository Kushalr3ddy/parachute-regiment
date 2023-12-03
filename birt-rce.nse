
--HEAD--
local _G = require "_G"
local http = require "http"
local nmap = require "nmap"
local shortport = require "shortport"
local stdnse = require "stdnse"
local string = require "string"
local table = require "table"

description =[[a poc exploit for the BIRT vulnerability CVE-2021-34427
DISCLAIMER: THIS SCRIPT IS MEANT ONLY FOR EDUCATIONAL PURPOSES. ANY ILLEGAL USE IS PROHIBITED]]

author="kushalr3ddy"

categories ={"exploit","intrusive","vuln"}


--FUNCTIONS--
local function http_get_request(host)
    -- Use the http library to send an HTTP GET request
    local response = http.get(host)
    
    -- Check if the request was successful
    if response and response.status == 200 then
        -- Print the HTTP response body
        print("HTTP GET request to " .. host .. " successful. Response:")
        print(response.body)
    else
        print("HTTP GET request to " .. host .. " failed")
    end
end

--RULE--
portrule = function(host, port)
    port.number=8080
    return port.state == "open" and port.protocol == "tcp"
end

--ACTION--

action = function(host)
    -- Perform the http_get_request function with the target host
    print("script loaded successfully")
    print("sent get request to:"..host)--.hostname)
    http_get_request(host)--.hostname)
    return "Test if this is working or not"
end