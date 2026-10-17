# ET32 Focus, keystone, remote and service audit
Read-only extracted data. APK code is not executed. This is a modified firmware image.

## /vendor/etc/ZYCustom.ini
Bytes: 5485
FOCUS_CONTROLLER     = Y;
AUTO_KEYSTONE_SUPPORT= Y;
[AutoKeystone]
HW_GPIO_NUM           = GPIO_PAD_58;##bootable/bootloader/mboot-mtk/mboot/sboot/inc/MT5862/board/chip/MT5862AYYN-YYA.h
HW_GPIO_ON            = 0;
HW_GPIO_OFF           = 1;
DEFAULT_PWM_MODE      = Y;##Y:PWM N:GPIO 需要对齐slaveboot
HW_GPIO_NUM           = GPIO_PAD_59;##bootable/bootloader/mboot-mtk/mboot/sboot/inc/MT5862/board/chip/MT5862AYYN-YYA.h
HW_GPIO_ON            = 0;
HW_GPIO_OFF           = 1;
DEFAULT_PWM_MODE      = Y;#Y:PWM N:GPIO 需要对齐slaveboot
HW_MOTOR_IN_GPIO_NUM     = GPIO_PAD_47, GPIO_PAD_45, GPIO_PAD_42, GPIO_PAD_46;
HW_MOTOR_EN_GPIO_NUM     = GPIO_PAD_8;
HW_MOTOR_FAULT_GPIO_NUM  = GPIO_PAD_INVALID;
HW_MOTOR_LENS_R_GPIO_NUM = GPIO_PAD_40;
HW_MOTOR_LENS_L_GPIO_NUM = GPIO_PAD_39;
[BoardGpio]
GPIO_NUM = 1;
#   FOCUS_CAMERA = 3,
#BOARD_FOCUS_CAMERA
GPIO_0_TYPE     = 3;
GPIO_0_NAME     = FOCUS_CAMERA;
GPIO_0_GPIONUM  = GPIO_PAD_15;##GPIO8_PM
GPIO_0_ON       = 1;
GPIO_0_OFF      = 0;

## /vendor/etc/trapezoidcorrect_points_offset.ini
Bytes: 289
[trapezoidpointoffset]

## /vendor/etc/customer_keymap.ini
Bytes: 167
TTX_KEYCODE=233
INDEX_KEYCODE=
MIX_KEYCODE=
HOLD_KEYCODE=
REVEAL_KEYCODE=
SUBCODE_KEYCODE=
SIZE_KEYCODE=
CANCEL_KEYCODE=

## /vendor/etc/hot-key-info.ini
Bytes: 703
KeyEvent=266 #KeyEvent.KEYCODE_STEM_2
KeyEvent=267 #KeyEvent.KEYCODE_STEM_3
KeyEvent=250 #KeyEvent.KEYCODE_TV_INPUT_COMPONENT_2
KeyEvent=248 #KeyEvent.KEYCODE_TV_INPUT_COMPOSITE_2

## /vendor/etc/ManualEnterFactory.ini
Bytes: 135
Keys: SerialKeys, PackageName, MainActivity

## /vendor/etc/feature_default.xml
Bytes: 7301
<CompilerFlag name="HDMITX_ENABLE" value="1" />

## /vendor/etc/tv-settings-configs.xml
Bytes: 12576
<pref>tv_picture_video_hdmi_rgb_range</pref>
<pref>tv_input_hdmi_edid_version</pref>
<pref>hdmi2_setting</pref>
<pref>hdmi2_setting</pref>

## /vendor/etc/adb_enable_on.ini
Bytes: 52
Keys: BOOT_ARGS

## /vendor/etc/adb_enable_off.ini
Bytes: 50
Keys: BOOT_ARGS

## /vendor/etc/boot.conf
Bytes: 442
# ADB via USB as default, enable ADB via network by this option

## /vendor/etc/rc.local
Bytes: 7021
Keys: BASIC_MOUNTED, BASIC_MOUNTED

## /vendor/etc/utopia.conf
Bytes: 447
MODULE_HDMIRX = 1

## /vendor/etc/init services
RC files: 35

### factory_svc.rc
service factory_svc /factory/bin/factory_svc

### vendor.mediatek.tv.mtkmtalservice@1.0-service.rc
service tv-mtkmtalservice-hal-1-0 /vendor/bin/hw/vendor.mediatek.tv.mtkmtalservice@1.0-service
group system media mediadrm camera

### android.hardware.drm@1.1-service.widevine.rc
on property:init.svc.mediadrm=running
service vendor.move_data_sh /system/bin/move_widevine_data.sh
service vendor.drm-widevine-hal-1-1 /vendor/bin/hw/android.hardware.drm@1.1-service.widevine

### boa-service.rc
on post-fs-data
service boa /vendor/bin/boa -c /vendor/etc/boa/ -d

### android.hardware.configstore@1.1-service.rc
service vendor.configstore-hal /vendor/bin/hw/android.hardware.configstore@1.1-service

### android.hardware.wifi@1.0-service.rc
on post-fs-data
service vendor.wifi_hal_legacy /vendor/bin/hw/android.hardware.wifi@1.0-service

### vendor.mediatek.tv.mtkdmservice@1.0-service.rc
service tv-mtkdmservice-hal-1-0 /vendor/bin/hw/vendor.mediatek.tv.mtkdmservice@1.0-service

### android.hardware.camera.provider@2.4-service.rc
service vendor.camera-provider-2-4 /vendor/bin/hw/android.hardware.camera.provider@2.4-service
user cameraserver
group audio camera input drmrpc
writepid /dev/cpuset/camera-daemon/tasks /dev/stune/top-app/tasks

### mstar.hardware.power@1.1-service.rc
service mstarpower /vendor/bin/hw/mstar.hardware.power@1.1-service

### android.hardware.keymaster@3.0-service.rc
service vendor.keymaster-3-0 /vendor/bin/hw/android.hardware.keymaster@3.0-service

### mstarhwc-service.rc
service vendor.hwcomposer-2-3 /vendor/bin/hw/mstar.hardware.hwcomposer.composer@2.3-service

### android.hardware.media.omx@1.0-service.rc
service vendor.media.omx /vendor/bin/hw/android.hardware.media.omx@1.0-service
group camera drmrpc mediadrm

### android.hardware.tv.cec@1.0-service.rc
service vendor.cec-hal-1-0 /vendor/bin/hw/android.hardware.tv.cec@1.0-service

### vndservicemanager.rc
service vndservicemanager /vendor/bin/vndservicemanager /dev/vndbinder

### android.hardware.cas@1.0-service.rc
service vendor.cas-hal-1-0 /vendor/bin/hw/android.hardware.cas@1.0-service

### init.fusion.rc
import /vendor/etc/init/hw/init.boottime_trace.rc
on fs
on post-fs
on pre-bspko
on misystem
on early-boot
export LINUX_PERSIST_PATH /vendor/persist
mkdir /data/vendor/tmp/camera
chmod 0771 /data/vendor/tmp/camera
chown root camera /data/vendor/tmp/camera
chown root camera /dev/video*
on property:sys.boot_completed=1
on property:ro.vendor.mtk.oem.lock=1
on property:sys.mtk.bootvideo.exit=1
service midaemon /mnt/vendor/tvservice/bin/midaemon
service mtk_rm /vendor/bin/sh /vendor/bin/mtk_rm.sh
service k2logcat /vendor/bin/k2logcat
service dtv-svc /vendor/bin/sh /vendor/bin/dtv_svc.sh
service aiaq-audio /vendor/bin/aiaq_audio
service zram-svc /vendor/bin/sh /vendor/bin/setup_zram.sh
service cpu-audio /vendor/bin/sh /vendor/bin/cpu_audio.sh
service browserserver /system/bin/browserserver
service limit_android_bg /vendor/bin/sh /vendor/bin/limit_android_bg.sh

### mstarmmdisp_service.rc
service mstarmmdisp /vendor/bin/hw/mstar.hardware.mmdisp@1.0-service

### mstar.hardware.audio@2.0-service.rc
service vendor.audio-hal-2-0 /vendor/bin/hw/mstar.hardware.audio@2.0-service
group audio camera drmrpc inet media mediadrm net_bt net_bt_admin net_bw_acct wakelock

### android.hardware.memtrack@1.0-service.rc
service vendor.memtrack-hal-1-0 /vendor/bin/hw/android.hardware.memtrack@1.0-service

### mstar.hardware.light@2.0-service.rc
service mstar-light-hal-2-0 /vendor/bin/hw/mstar.hardware.light@2.0-service

### android.hardware.tv.input@1.0-service-mediatek.rc
service tv-input-1-0 /vendor/bin/hw/android.hardware.tv.input@1.0-service-mediatek

### vendor.mediatek.hardware.wifidisplay@1.0-service.rc
service wifidisplay-hal-1-0 /vendor/bin/hw/vendor.mediatek.hardware.wifidisplay@1.0-service

### android.hardware.bluetooth@1.0-service.rc
service vendor.bluetooth-1-0 /vendor/bin/hw/android.hardware.bluetooth@1.0-service
on property:vts.native_server.on=1 && property:ro.build.type=userdebug
on property:vts.native_server.on=1 && property:ro.build.type=eng
on property:vts.native_server.on=0 && property:ro.build.type=userdebug
on property:vts.native_server.on=0 && property:ro.build.type=eng

### hostapd.android.rc
on post-fs-data
service hostapd /vendor/bin/hw/hostapd

### android.hardware.graphics.allocator@2.0-service.rc
service vendor.gralloc-2-0 /vendor/bin/hw/android.hardware.graphics.allocator@2.0-service

### vendor.mediatek.tv.mtkloadingequalizer@1.0-service.rc
service tv-mtkloadingequalizer-1-0 /vendor/bin/hw/vendor.mediatek.tv.mtkloadingequalizer@1.0-service

### android.hardware.health@2.0-service.mediatek.rc
service vendor.health-hal-2-0 /vendor/bin/hw/android.hardware.health@2.0-service.mediatek

### android.hardware.drm@1.1-service.clearkey.rc
service vendor.drm-clearkey-hal-1-1 /vendor/bin/hw/android.hardware.drm@1.1-service.clearkey

### vendor.mediatek.tv.mtktvapi@1.0-service.rc
service tv-mtktvapi-1-0 /vendor/bin/hw/vendor.mediatek.tv.mtktvapi@1.0-service

### android.hardware.gatekeeper@1.0-service.rc
service vendor.gatekeeper-1-0 /vendor/bin/hw/android.hardware.gatekeeper@1.0-service

### mstarimgdisp_service.rc
service mstarimgdisp /vendor/bin/hw/mstar.hardware.imgdisp@1.0-service

### vendor.mediatek.tv.mtktvfactory@1.0-service.rc
service tv-mtktvfactory-1-0 /vendor/bin/hw/vendor.mediatek.tv.mtktvfactory@1.0-service

### android.hardware.drm@1.0-service.rc
service vendor.drm-hal-1-0 /vendor/bin/hw/android.hardware.drm@1.0-service

### vendor.mediatek.tv.mtkrm@1.0-service.rc
service tv-mtkrm-hal-1-0 /vendor/bin/hw/vendor.mediatek.tv.mtkrm@1.0-service

### vendor.mediatek.hardware.tv.networkproxy@1.0-service.rc
service networkproxy-hal-1-0 /vendor/bin/hw/vendor.mediatek.hardware.tv.networkproxy@1.0-service

## Relevant Android app packages

### /system/priv-app/AutoFocus3
Files: AutoFocus3.apk, oat
package: name='com.zhiying.autofocus' versionCode='30086' versionName='30.0.86' platformBuildVersionName='9' platformBuildVersionCode='28' compileSdkVersion='28' compileSdkVersionCodename='9'
sdkVersion:'28'
targetSdkVersion:'28'
application-label:'AutoKeyStoneCorrect'

### /system/priv-app/ZYSetting
Files: oat, ZYSetting.apk
package: name='com.zhiying.settings' versionCode='2771' versionName='2771'
sdkVersion:'19'
targetSdkVersion:'22'
application-label:'TVSetting'

### /system/priv-app/TvSettingsPlus
Files: TvSettingsPlus.apk
package: name='com.android.tv.settings' versionCode='2' versionName='1.2' platformBuildVersionCode='2' compileSdkVersion='28' compileSdkVersionCodename='9'
sdkVersion:'23'
targetSdkVersion:'28'
application-label:'Settings'

### /system/app/ZYCustomUI
Files: ZYCustomUI.apk
package: name='com.zhiying.sourceui' versionCode='42' versionName='1.0' platformBuildVersionName='9' platformBuildVersionCode='28' compileSdkVersion='28' compileSdkVersionCodename='9'
sdkVersion:'26'
targetSdkVersion:'26'
application-label:'SOURCE'

### /system/app/NLHotkeyService
Files: oat, NLHotkeyService.apk
package: name='com.newlink.hotkeysservices' versionCode='30' versionName='30' platformBuildVersionName='9' platformBuildVersionCode='28' compileSdkVersion='28' compileSdkVersionCodename='9'
sdkVersion:'16'
targetSdkVersion:'23'
application-label:'NLHotkeysServices'

### /system/app/ZYYTBLauncher
Files: oat, ZYYTBLauncher.apk
package: name='com.zhiying.ytb.zy.tv' versionCode='137' versionName='1.3.7' platformBuildVersionName='9' platformBuildVersionCode='28' compileSdkVersion='28' compileSdkVersionCodename='9'
sdkVersion:'19'
targetSdkVersion:'28'
application-label:'YTB_ZY_TV'
launchable-activity: name='com.zhiying.ytb.zy.tv.activity.MainActivity'  label='' icon=''

### /system/app/NLTvTestingTools
Files: oat, NLTvTestingTools.apk, lib
package: name='com.newlink.tvtestingtools' versionCode='100' versionName='100' platformBuildVersionName='9' platformBuildVersionCode='28' compileSdkVersion='28' compileSdkVersionCodename='9'
sdkVersion:'21'
targetSdkVersion:'28'
application-label:'TVTestingTools'

### /system/app/NLAutoTest
Files: NLAutoTest.apk, oat, lib
package: name='com.newlink.autotest' versionCode='7' versionName='1.7' platformBuildVersionName='12' platformBuildVersionCode='32' compileSdkVersion='32' compileSdkVersionCodename='12'
sdkVersion:'28'
targetSdkVersion:'32'
application-label:'AutoTest'

### /system/app/ZYFileManager
Files: oat, ZYFileManager.apk
package: name='com.newlink.filemanager' versionCode='90' versionName='6.94' platformBuildVersionName='10' platformBuildVersionCode='29' compileSdkVersion='29' compileSdkVersionCodename='10'
sdkVersion:'17'
targetSdkVersion:'23'
application-label:'File Manager'
launchable-activity: name='com.newlink.filemanager.activity.SelectActivity'  label='' icon=''
