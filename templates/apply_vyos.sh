#!/bin/bash
# Standardized batch-apply of VyOS set/delete commands.
# Usage: apply_vyos.sh <host-fqdn> <commands-file>
# File: one "set ..." / "delete ..." per line. vbash is the VyOS CLI shell;
# "save" inside a piped vbash -i session errors, so persistence is done
# with an explicit `save` op via the same session afterwards.
set -e
HOST=$1
FILE=$2
{ echo "configure"; cat "$FILE"; echo "commit"; echo "save"; echo "exit"; } \
  | ssh "vyos@$HOST" 'vbash -i' 2>&1 | grep -vE 'no job control|^\s*$|^vyos@'
