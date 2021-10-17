### mitmproxy

For this project we will analyze the flow of data and write our own script to intercept downloaded files and make a trojan out of the file that the target client is downloading.

Here, we are not replacing the file but we are actually giving the target client the file that they requested. However, the requested file will be modified slightly so that when it is executed it will show the target client the file that they expected, while also running our evil file (trojan) in the background. We will write a MITMproxy script to accomplish this file modification. [Click here to read more on MITMproxy.](https://docs.mitmproxy.org/stable/)

For further documentation on "How to Write MITM Scripts Using Python and Executing it With MITMproxy" go to: https://aaronjohn2.github.io/2019/02/10/mitm-script/
