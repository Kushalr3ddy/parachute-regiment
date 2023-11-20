# BIRT RCE vulnerability found on the DSU result server

## following is the complete overview of the RCE exploit found on the BIRT server used to generate results

> the exploit is based on the vulnerability based on [CVE-2021-34427](https://bugs.eclipse.org/bugs/show_bug.cgi?id=538142)

the above exploit makes use of a birt vulnerability that can be used to access and write files to the directory where the BIRT software is installed

```
http://localhost:8080/birt-viewer/output?__report=test.rptdesign&__format=pdf&__overwrite=true&__document=./filename.jsp&sample=<url-encoded-payload-here>
```
as we can see above using the `_document=` and `sample=` url arguments we can write to file in a directory that we have permission to with own desired content.

NOTE: here the `_overwrite=true` argument is used so that the birt viewer creates or overwrites a file if not present.

using this we can url encode code and save it with a .jsp extension for executing it.

NOTE: here we are using .jsp extension as the BIRT server uses the apache tomcat server under the hood to server the generated content


