local http = require("http")


portrule = function(host,port)
    return port.number == 8080 and port.state == "open" and port.protocol =="tcp"
end
action = function(host)
    local url = "http://" .. host.ip .. "/"
    
    local response = http.get(host.ip,host.port,path)

    if response and response.status == 200 then
        print("HTTP GET request to " .. url .. " successful.")
        print("Response code:", response.status)
        print("Response body:")
        print(response.body)
    else
        print("HTTP GET request to " .. url .. " failed.")
    end
end