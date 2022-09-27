#!/bin/bash
/etc/init.d/ssh start
cat /tmp/delta_hosts >> /etc/hosts
/bin/bash
