# Postmortem Report

## Apache 500 Internal Server Error

<p align="center">
<img src="https://i0.wp.com/faildesk.net/wp-content/uploads/2019/01/prolific_pen_down_server.jpg?resize=696%2C723&ssl=1" width=100% height=100% />
</p>

### Incident report for [500 Internal Server Error / Site Outage](https://github.com/Sohilahamdy/alx-system_engineering-devops/tree/master/0x17-web_stack_debugging_3)

#### Summary

We experienced a huge problem on August 18, 2024 that basically took down our whole Wordpress site went down and I got the 500 Internal Server Error This error where LAMP (Linux, Apache, MySQL and PHP) stack was hit we locked users out plunging them into the abyss of logins or even signup which meant total shutdown. A total of 127 complaints from infurated users were poured on us. The site was down from 09:55 - 11:20 GMT+1, which is a nice reminder how important uptime of our services are and subsequently user experience.

#### Timeline

- **9:55 AM GMT+1** - The 1st complain from a user who could not log in / register on the site.
- **10:15 AM GMT+1** - Time to investigate on what happened, so we began reading this code logs and server configuration.
- **10:25 AM GMT+1** - The apache logs seemed to suggest that this was PHP related, and all signs pointed towards a configuration or code issue.
- **10:30 AM GMT+1** - We started looking more closely to what exactly Apache was doing with strace to rewrite the error better understood.
- **10:40 AM GMT+1** - We found that it was due to misconfigurations in the Apache virtual host.
- **11:00 AM GMT+1** - We raised the matter with our backend development squad.
- **11:20 AM GMT+1** - Apache configuration was fixed, we verified that the site load and running smoothly.

#### Root Cause and Resolution

The 500 Internal Server Error was simply just a misconfiguration inside the Apache virtual host settings. Some common issues will be that the DocumentRoot directive was set to /var/www instead of /var/www/html and the directory permissions. The Apache had been configured to not be allowed the files, and so it fell.

#### Resolution Steps

- Modified the DocumentRoot Directive: Changed the document root in.conf file of Apache to correct path.
- Permissoins Adjusted: Correcting the permissions to access apache at required files.
After changed configuration,
- Restarted apache service: Server restarted and checked everything working fine with Apache.

#### Corrective and Preventative Action

##### What we will do to prevent this in the future:

- Configuration Management: Enforce preflight checks to automate validation of configurations - but do it before deployment Track Changes to Configuration Files and Roll Them Back If Necessary via version control
- Monitoring & Alerts: Enhance how errors from Apache/PHP are being monitored and Enable alerts for signals that are related to consensus algorithm so they get addressed immediately
- Record Keeping & Review: Detailed config change records review the configurations periodically to see if they are according to best practices.
- Automated Tests: Automation tests for the core functionalities to prevent issues before it reaches out user add these tests to our continuous integration process so we can catch issues sooner.
