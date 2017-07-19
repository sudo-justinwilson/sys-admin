# start ssh-agent on login:

# start ssh-agent:
/bin/ssh-agent &> /dev/null

# add key to agent:
for key in $SSHKEYS; do
	/usr/bin/ssh-add $key &> /dev/null;
done
