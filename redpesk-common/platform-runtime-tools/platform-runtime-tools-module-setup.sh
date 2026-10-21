#!/bin/bash

# called by dracut
check() {
    return 0
}

# called by dracut
depends() {
    return 0
}

# called by dracut
install() {

    inst_multiple \
	/etc/platform-info \
	/usr/bin/getconf \
	/usr/sbin/dmidecode \
	/usr/bin/pr-detect \
	/libexec/pr-tools/detect/* \
	/libexec/pr-tools/detect/*/* \
	$systemdsystemunitdir/platform-*-detection.service

	systemctl --root "$initdir" --system enable platform-os-detection.service
	systemctl --root "$initdir" --system enable platform-core-detection.service
	systemctl --root "$initdir" --system enable platform-devices-detection.service
}
