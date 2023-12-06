--[[
http://14.99.184.178:8080/birt/frameset?__report=mydsi/exam/Exam_Result_Sheet_f1.rptdesign&__format=pdf&USN=eng20cy0024
]]
--HEAD
local http = require "http"

local ip_addr ="14.99.184.178"
--RULE
portrule = function(host, port)
    return port.number == 8080 and port.state == "open" and port.protocol == "tcp"
end

-- ACTION
action = function(host)
    print("------------------")
    print("Port 8080 is open on host:", host.ip)
    print("------------------")

    -- Replace this with your HTTP request logic using 'http' library if needed
    -- Example: http.request("http://" .. host.ip .. ":8080/your_path")
end
