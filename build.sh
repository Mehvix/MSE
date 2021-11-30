#!/bin/sh

log() {
    now=$(date +"%T.%3N")
    echo "$now :: $1"
}

TMP="img-min-tmp.py"
MIN="img-min.py"
GEN="img-to-scm.py"

log "Removing contest.scm..."
command rm contest.scm
log "Minifying $GEN..."
command pyminifier -o $TMP --lzma $GEN # todo pipe to log
MIN="img-min.py"
command head -n -1 $TMP >$MIN
log "Evaluating Python code to get scheme..."
command python $GEN >/dev/null
log "Generating QR of min and reg Python..."
command python gen-py-qr.py $MIN >/dev/null
command python gen-py-qr.py $GEN >/dev/null
log "Evaluating scheme code..."
command python3 scheme.py contest.scm --pillow-turtle --turtle-save-path output >/dev/null
log "Removing tmp files..."
command rm $TMP
command rm $MIN
