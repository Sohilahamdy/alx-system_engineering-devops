# 0x17. Web Stack Debugging #3

## Project Overview

In this project, you'll be debugging a Wordpress website running on a LAMP stack. The primary focus is to identify and fix a 500 Internal Server Error using \`strace\`, and then automate the fix using Puppet.

## Background Context

Debugging can sometimes require more than just logs, especially if the software fails in unexpected ways or the logs don’t provide sufficient information. This project involves diagnosing issues in a Wordpress site, which is commonly powered by a LAMP stack (Linux, Apache, MySQL, and PHP).

## Requirements

- **Operating System**: Ubuntu 14.04 LTS
- **Files**: All files should end with a new line.
- **Puppet**: Ensure Puppet manifests pass \`puppet-lint\` version 2.1.1 without errors and run without issues.
- **File Extensions**: Puppet manifest files must end with the \`.pp\` extension.

## Tasks

### 0. Strace is Your Friend

**Mandatory**  
**Score**: 0.0%

**Objective**:  
Use \`strace\` to find out why Apache is returning a 500 error. Once identified, fix the issue and automate the solution using Puppet.

**Requirements**:
- Your Puppet manifest file must be named \`0-strace_is_your_friend.pp\`.
- Use Puppet resources to implement the fix.

**Example**:

1. **Using \`strace\`**:
   \`\`\`bash
   strace -p <PID>
   \`\`\`

2. **Verifying Apache Response**:
   \`\`\`bash
   curl -sI 127.0.0.1
   \`\`\`

3. **Applying Puppet Manifest**:
   \`\`\`bash
   puppet apply 0-strace_is_your_friend.pp
   \`\`\`

4. **Confirming Fix**:
   \`\`\`bash
   curl -sI 127.0.0.1:80
   curl -s 127.0.0.1:80 | grep Holberton
   \`\`\`

## Installation

1. **Install Puppet**:
   \`\`\`bash
   sudo apt-get update
   sudo apt-get install -y puppet-agent
   \`\`\`

2. **Run Puppet Manifest**:
   \`\`\`bash
   sudo puppet apply 0-strace_is_your_friend.pp
   \`\`\`

## Repo Information

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Sohilahamdy/alx-system_engineering-devops)
- **Directory**: \`0x17-web_stack_debugging_3\`
- **File**: \`0-strace_is_your_friend.pp\`
EOF


