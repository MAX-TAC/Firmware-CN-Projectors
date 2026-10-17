# ET32 detailed read-only APK and service analysis
A static decompilation of the modified ET32 firmware; observed references are not proof of execution.

## Overview

| App | Package | Target SDK | Permissions | Exported / total components | Java files |
|---|---|---:|---:|---:|---:|
| AutoFocus3 | com.zhiying.autofocus | 28 | 8 | 3/13 | 1748 |
| ZYSetting | com.zhiying.settings | 22 | 27 | 14/43 | 1390 |
| TvSettingsPlus | com.android.tv.settings | 28 | 37 | 31/67 | 1701 |
| NLHotkeyService | com.newlink.hotkeysservices | 23 | 10 | 2/3 | 1 |
| ZYCustomUI | com.zhiying.sourceui | 26 | 6 | 1/7 | 1235 |
| ZYYTBLauncher | com.zhiying.ytb.zy.tv | 28 | 15 | 0/4 | 1 |
| NLTvTestingTools | com.newlink.tvtestingtools | 28 | 28 | 6/12 | 0 |
| NLAutoTest | com.newlink.autotest | 32 | 31 | 6/6 | 0 |
| Arbitratorservice | com.mediatek.tvinputservice.arbitratorservice | 28 | 0 | 0/1 | 5 |
| NewLinkService | com.newlink.service | 29 | 34 | 10/27 | 2723 |
| ZYHBStore | com.zhiying.appstore | 28 | 9 | 0/11 | 1608 |
| HBCastNew | com.newlink.cast | 26 | 13 | 0/28 | 1 |
| MtkNetworkMonitorService | com.mediatek.network | 28 | 4 | 0/2 | 1 |
| PowerService | com.zhiying.powerservice | 19 | 6 | 1/5 | 1 |
| WTProvision | com.newlink.wtprovision | 23 | 35 | 7/17 | 0 |
| AutoPair | com.newlink.service | 29 | 29 | 4/12 | 0 |
| BootAppSplashScreen | com.google.android.boot.appsplashscreen | 28 | 0 | 0/1 | 0 |

## Per-app detail

### AutoFocus3
Package: com.zhiying.autofocus
Android flags: {'allowBackup': 'true'}
Shared user: android.uid.system
Permissions: android.permission.INTERNET, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.READ_EXTERNAL_STORAGE, android.permission.RECEIVE_BOOT_COMPLETED, android.permission.CAMERA, android.permission.FOREGROUND_SERVICE, android.permission.SYSTEM_ALERT_WINDOW, android.permission.KILL_BACKGROUND_PROCESSES
service: com.zhiying.autofocus.AutoFocusService, com.zhiying.autofocus.AutoCorrectKeyStoneService, com.zhiying.autofocus.OneACKSService
provider: com.lzf.easyfloat.EasyFloatInitializer
Exported with no component permission (verify intent validation): service:com.zhiying.autofocus.AutoFocusService, service:com.zhiying.autofocus.AutoCorrectKeyStoneService, service:com.zhiying.autofocus.OneACKSService
JADX status 1; classes/files 1748
Matched patterns {"focus": 4552, "remote": 369, "device": 477, "privileged": 685, "jni": 232, "network": 15, "weak_security": 0, "catch": 1299}
URL hostnames schemas.android.com
focus com/mediatek/twoworlds/factory/MtkTvFApiCustom.java:6 private static final int CMD_ID_EX_CUS_CALIBRATEAUTOKEYSTONE = 61725;
focus com/mediatek/twoworlds/factory/MtkTvFApiCustom.java:8 private static final int CMD_ID_EX_CUS_GETAUTOKEYSTONE = 61723;
focus com/mediatek/twoworlds/factory/MtkTvFApiCustom.java:9 private static final int CMD_ID_EX_CUS_GETAUTOKEYSTONEUNCALIB = 61726;
focus com/mediatek/twoworlds/factory/MtkTvFApiCustom.java:12 private static final int CMD_ID_EX_CUS_GETFOCUSCAMERAENABLE = 61721;
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:4 public class MtkTvKeyEventBase {
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:5 public static final java.lang.String TAG = "MtkTvKeyEvent";
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:8 public MtkTvKeyEventBase() {
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:73 public int androidKeyToDFBkey(int i, android.view.KeyEvent keyEvent) {
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:9 private static java.util.Hashtable<java.lang.Integer, java.lang.Integer> gpioHashTable = new java.util.Hashtable<>();
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:13 loadGpioTable();
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:21 private void loadGpioTable() throws java.lang.NumberFormatException {
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:23 int i = java.lang.Integer.parseInt(mtkFApiInformationImp.getIniParameter(path, "BOARD_GPIO_SETTING:BOARD_GPIO_NUM"));
privileged com/mediatek/twoworlds/tv/SystemProperties.java:4 public final class SystemProperties {
privileged com/mediatek/twoworlds/tv/SystemProperties.java:5 private static final java.lang.String TAG = "SystemProperties";
privileged com/mediatek/twoworlds/tv/SystemProperties.java:14 str3 = (java.lang.String) java.lang.Class.forName("android.os.SystemProperties").getDeclaredMethod("get", java.lang.String.class).invoke(null, str);
privileged com/mediatek/twoworlds/tv/SystemProperties.java:24 int iIntValue = ((java.lang.Integer) java.lang.Class.forName("android.os.SystemProperties").getDeclaredMethod("getInt", java.lang.String.class, java.lang.Integer.TYPE).invoke(null, str, java.lang.Integer.valueOf(i))).int
jni com/mediatek/twoworlds/tv/TVNativeCustom.java:14 com.mediatek.twoworlds.tv.TvDebugLog.i(TAG, "Load libcom_mediatek_twoworlds_tv_jni.so start !");
jni com/mediatek/twoworlds/tv/TVNativeCustom.java:15 java.lang.System.loadLibrary("com_mediatek_twoworlds_tv_jni");
jni com/mediatek/twoworlds/tv/TVNativeCustom.java:16 com.mediatek.twoworlds.tv.TvDebugLog.i(TAG, "Load libcom_mediatek_twoworlds_tv_jni.so OK !");
jni com/mediatek/twoworlds/tv/MtkTvAppTVBase.java:5 private static final int JNI_APPTV_SYS_STATUS_AFTER_ASPECT_RATIO_CHG = 9;

### ZYSetting
Package: com.zhiying.settings
Android flags: {'allowBackup': 'true'}
Shared user: android.uid.system
Permissions: android.permission.RECEIVE_BOOT_COMPLETED, android.permission.RECOVERY, com.mstar.android.permissionn.ACCESS_TV_DATA, android.permission.ACCESS_WIFI_STATE, android.permission.CHANGE_WIFI_STATE, android.permission.OVERRIDE_WIFI_CONFIG, android.permission.ACCESS_NETWORK_STATE, android.permission.INTERNET, android.permission.WRITE_SETTINGS, android.permission.WRITE_SECURE_SETTINGS, android.permission.SHUTDOWN, android.permission.INTERACT_ACROSS_USERS, android.permission.CHANGE_NETWORK_STATE, android.permission.CONNECTIVITY_INTERNAL, android.permission.BLUETOOTH, android.permission.BLUETOOTH_ADMIN, android.permission.GET_PACKAGE_SIZE, android.permission.GET_TASKS, android.permission.READ_EXTERNAL_STORAGE, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.SET_WALLPAPER, android.permission.SET_WALLPAPER_HINTS, android.permission.ACCESS_FINE_LOCATION, android.permission.ACCESS_COARSE_LOCATION, android.permission.PACKAGE_USAGE_STATS, android.permission.CHANGE_CONFIGURATION, android.permission.SYSTEM_ALERT_WINDOW
service: com.zhiying.settings.projection.ProjectionService, com.zhiying.settings.shutdown.ShutDownService, com.zhiying.settings.MyService, com.zhiying.settings.update.UpdateService, com.zhiying.settings.update.AutoSystemUpdateService
receiver: com.zhiying.settings.update.NetChangeReceiver
provider: android.support.v4.content.FileProvider
Exported with no component permission (verify intent validation): activity:com.zhiying.settings.projection.ProjectionCra6DSenActivity, activity:com.zhiying.settings.dlpsetting.MotorFocusingActivity, activity:com.zhiying.settings.projection.Projection3DSensorActivity, activity:com.zhiying.settings.projection.Projection3DNewSensorActivity, activity:com.zhiying.settings.projection.ProjectionActivity, activity:com.zhiying.settings.shutdown.ShutDownActivity, activity:com.zhiying.settings.update.AutoSystemUpdateGuideActivity, activity:com.zhiying.settings.dlpsetting.CorrectSettingsActivity, activity:com.zhiying.settings.projection.KeystoneSettingsActivity, activity:com.zhiying.settings.projection.FocusSettingActivity, activity:com.zhiying.settings.projection.ProjectionDirectionActivity, service:com.zhiying.settings.projection.ProjectionService, service:com.zhiying.settings.shutdown.ShutDownService, service:com.zhiying.settings.MyService
JADX status 1; classes/files 1390
Matched patterns {"focus": 820, "remote": 478, "device": 482, "privileged": 391, "jni": 32, "network": 24, "weak_security": 0, "catch": 1187}
URL hostnames 121.40.159.114, schemas.android.com
focus com/mediatek/twoworlds/factory/MtkTvFApiCustom.java:6 private static final int CMD_ID_EX_CUS_CALIBRATEAUTOKEYSTONE = 61725;
focus com/mediatek/twoworlds/factory/MtkTvFApiCustom.java:8 private static final int CMD_ID_EX_CUS_GETAUTOKEYSTONE = 61723;
focus com/mediatek/twoworlds/factory/MtkTvFApiCustom.java:9 private static final int CMD_ID_EX_CUS_GETAUTOKEYSTONEUNCALIB = 61726;
focus com/mediatek/twoworlds/factory/MtkTvFApiCustom.java:12 private static final int CMD_ID_EX_CUS_GETFOCUSCAMERAENABLE = 61721;
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:4 public class MtkTvKeyEventBase {
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:5 public static final java.lang.String TAG = "MtkTvKeyEvent";
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:8 public MtkTvKeyEventBase() {
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:72 public int androidKeyToDFBkey(int i, android.view.KeyEvent keyEvent) {
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:9 private static java.util.Hashtable<java.lang.Integer, java.lang.Integer> gpioHashTable = new java.util.Hashtable<>();
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:13 loadGpioTable();
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:21 private void loadGpioTable() throws java.lang.NumberFormatException {
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:23 int i = java.lang.Integer.parseInt(mtkFApiInformationImp.getIniParameter(path, "BOARD_GPIO_SETTING:BOARD_GPIO_NUM"));
privileged com/mediatek/twoworlds/tv/SystemProperties.java:4 public final class SystemProperties {
privileged com/mediatek/twoworlds/tv/SystemProperties.java:5 private static final java.lang.String TAG = "SystemProperties";
privileged com/mediatek/twoworlds/tv/SystemProperties.java:14 str3 = (java.lang.String) java.lang.Class.forName("android.os.SystemProperties").getDeclaredMethod("get", java.lang.String.class).invoke(null, str);
privileged com/mediatek/twoworlds/tv/SystemProperties.java:24 int iIntValue = ((java.lang.Integer) java.lang.Class.forName("android.os.SystemProperties").getDeclaredMethod("getInt", java.lang.String.class, java.lang.Integer.TYPE).invoke(null, str, java.lang.Integer.valueOf(i))).int
jni com/mediatek/twoworlds/tv/TVNativeCustom.java:14 com.mediatek.twoworlds.tv.TvDebugLog.i(TAG, "Load libcom_mediatek_twoworlds_tv_jni.so start !");
jni com/mediatek/twoworlds/tv/TVNativeCustom.java:15 java.lang.System.loadLibrary("com_mediatek_twoworlds_tv_jni");
jni com/mediatek/twoworlds/tv/TVNativeCustom.java:16 com.mediatek.twoworlds.tv.TvDebugLog.i(TAG, "Load libcom_mediatek_twoworlds_tv_jni.so OK !");
jni com/mediatek/twoworlds/tv/MtkTvAppTVBase.java:5 private static final int JNI_APPTV_SYS_STATUS_AFTER_ASPECT_RATIO_CHG = 9;

### TvSettingsPlus
Package: com.android.tv.settings
Android flags: {'usesCleartextTraffic': 'true'}
Shared user: android.uid.system
Permissions: android.permission.ACCESS_WIFI_STATE, android.permission.ACCESS_NETWORK_STATE, android.permission.BACKUP, android.permission.BLUETOOTH, android.permission.BLUETOOTH_ADMIN, android.permission.CHANGE_WIFI_STATE, android.permission.CLEAR_APP_USER_DATA, android.permission.DELETE_CACHE_FILES, android.permission.DUMP, android.permission.FORCE_STOP_PACKAGES, android.permission.GET_ACCOUNTS_PRIVILEGED, android.permission.GET_PACKAGE_SIZE, android.permission.INJECT_EVENTS, android.permission.INTERNET, android.permission.MANAGE_ACCOUNTS, android.permission.MANAGE_SCOPED_ACCESS_DIRECTORY_PERMISSIONS, android.permission.MANAGE_USERS, android.permission.NETWORK_SETTINGS, android.permission.OVERRIDE_WIFI_CONFIG, android.permission.PEERS_MAC_ADDRESS, android.permission.READ_CONTACTS, android.permission.REBOOT, android.permission.READ_EXTERNAL_STORAGE, android.permission.RECEIVE_BOOT_COMPLETED, android.permission.SET_PREFERRED_APPLICATIONS, android.permission.SET_TIME, android.permission.SET_TIME_ZONE, android.permission.USE_RESERVED_DISK, android.permission.WRITE_MEDIA_STORAGE, android.permission.WRITE_SETTINGS, android.permission.WRITE_SECURE_SETTINGS, android.permission.REQUEST_DELETE_PACKAGES, com.google.android.assistant.READ_HOTWORD_STATE, com.google.android.assistant.WRITE_HOTWORD_STATE, 
service: .users.UserSwitchListenerService, .device.storage.SettingsStorageService$Impl, com.android.tv.settings.partnercustomizer.tvsettingservice.TVMenuSettingsService, .partnercustomizer.retailmode.RetailModeService, .partnercustomizer.switchofftimer.SwitchOffTimerService, .update.UpdateService
receiver: .accessories.BluetoothPairingRequest, .users.UserSwitchListenerService$BootReceiver, .device.storage.DiskReceiver
provider: android.support.v4.content.FileProvider, .name.SuggestionContentProvider
Exported with no component permission (verify intent validation): activity:.connectivity.WifiConnectionActivity, activity:.connectivity.AddWifiNetworkActivity, activity:.accounts.AccountSyncActivity, activity:.accounts.AddAccountWithTypeActivity, activity:.device.apps.AppsActivity, activity:.device.apps.AllAppsActivity, activity:.device.apps.specialaccess.DirectoryAccessActivity, activity:.device.apps.AppManagementActivity, activity:.device.StorageResetActivity, activity:.connectivity.NetworkActivity, activity:.system.SecurityActivity, activity:.device.sound.SoundActivity, activity:.device.display.daydream.DaydreamActivity, activity:.device.display.daydream.DaydreamVoiceAction, activity:.device.privacy.PrivacyActivity, activity:.system.CaptionSetupActivity, activity:.system.DateTimeActivity, activity:com.android.tv.settings.partnercustomizer.timer.TimerActivity, activity:.system.LocationActivity, activity:.system.development.DevelopmentActivity, activity:.inputmethod.KeyboardActivity, activity:.system.LanguageActivity, activity:.system.InputsActivity
JADX status 1; classes/files 1701
Matched patterns {"focus": 20, "remote": 453, "device": 43, "privileged": 393, "jni": 34, "network": 173, "weak_security": 0, "catch": 1206}
URL hostnames 172.21.29.243, schemas.android.com
focus com/mediatek/twoworlds/tv/model/MtkTvDvbsConfigInfoBase.java:17 protected int motorPosition;
focus com/mediatek/twoworlds/tv/model/MtkTvDvbsConfigInfoBase.java:18 protected int motorType;
focus com/mediatek/twoworlds/tv/model/MtkTvDvbsConfigInfoBase.java:280 public int getMotorType() {
focus com/mediatek/twoworlds/tv/model/MtkTvDvbsConfigInfoBase.java:281 return this.motorType;
remote com/mediatek/wwtv/tvcenter/util/Constants.java:6 public static final java.util.HashSet<java.lang.Integer> BLACKLIST_KEYCODE_TO_TIS = new java.util.HashSet<>();
remote com/mediatek/wwtv/tvcenter/util/Constants.java:23 BLACKLIST_KEYCODE_TO_TIS.add(java.lang.Integer.valueOf(com.mediatek.wwtv.tvcenter.util.KeyMap.KEYCODE_MTKIR_CHUP));
remote com/mediatek/wwtv/tvcenter/util/Constants.java:24 BLACKLIST_KEYCODE_TO_TIS.add(java.lang.Integer.valueOf(com.mediatek.wwtv.tvcenter.util.KeyMap.KEYCODE_MTKIR_CHDN));
remote com/mediatek/wwtv/tvcenter/util/Constants.java:25 BLACKLIST_KEYCODE_TO_TIS.add(84);
device com/mediatek/twoworlds/tv/MtkTvGpio.java:4 public class MtkTvGpio extends com.mediatek.twoworlds.tv.MtkTvGpioBase {
device com/mediatek/twoworlds/tv/MtkTvGpio.java:5 private static final int GPIO_ID_COMPONENT = 3;
device com/mediatek/twoworlds/tv/MtkTvGpio.java:6 public static final int GPIO_ID_CVBS = 1;
device com/mediatek/twoworlds/tv/MtkTvGpio.java:7 private static final int GPIO_ID_HEADPHONE = 4;
privileged com/mediatek/wwtv/tvcenter/util/MarketRegionInfo.java:80 platfrom = com.mediatek.twoworlds.tv.SystemProperties.get("ro.board.platform");
privileged com/mediatek/wwtv/tvcenter/util/MarketRegionInfo.java:81 java.lang.String marketregion = com.mediatek.twoworlds.tv.SystemProperties.get("ro.vendor.mtk.system.marketregion");
privileged com/mediatek/wwtv/tvcenter/util/MarketRegionInfo.java:89 sba.append(4, 1 == com.mediatek.twoworlds.tv.SystemProperties.getInt("ro.vendor.mtk.system.dvbs.existed", 0));
privileged com/mediatek/wwtv/tvcenter/util/MarketRegionInfo.java:90 sba.append(5, 1 == com.mediatek.twoworlds.tv.SystemProperties.getInt("ro.vendor.mtk.system.hbbtv.existed", 0));
jni com/mediatek/net/MtkNetworkNative.java:21 android.util.Log.d(TAG, "MtkNetworkNative begin load  libcom_mediatek_net_jni.so !");
jni com/mediatek/net/MtkNetworkNative.java:23 java.lang.System.loadLibrary("com_mediatek_net_jni");
jni com/mediatek/twoworlds/tv/TVNativeCustom.java:14 com.mediatek.twoworlds.tv.TvDebugLog.i(TAG, "Load libcom_mediatek_twoworlds_tv_jni.so start !");
jni com/mediatek/twoworlds/tv/TVNativeCustom.java:15 java.lang.System.loadLibrary("com_mediatek_twoworlds_tv_jni");

### NLHotkeyService
Package: com.newlink.hotkeysservices
Android flags: {'allowBackup': 'false'}
Shared user: android.uid.system
Permissions: android.permission.INTERACT_ACROSS_USERS, android.permission.MASTER_CLEAR, android.permission.SHUTDOWN, android.permission.INJECT_EVENTS, android.permission.WRITE_SECURE_SETTINGS, android.permission.RECOVERY, android.permission.CHANGE_OVERLAY_PACKAGES, android.permission.ACCESS_NETWORK_STATE, android.permission.BLUETOOTH, com.hisilicon.permission.COMMON_PERMISSION
service: com.newlink.hotkeyservices.main.NLSettingHotKeyService, com.newlink.hotkeyservices.main.NLHotkeyServices
Exported with no component permission (verify intent validation): service:com.newlink.hotkeyservices.main.NLSettingHotKeyService
JADX status 0; classes/files 1
Matched patterns {"focus": 0, "remote": 0, "device": 0, "privileged": 0, "jni": 0, "network": 0, "weak_security": 0, "catch": 0}
URL hostnames 

### ZYCustomUI
Package: com.zhiying.sourceui
Android flags: {'allowBackup': 'true'}
Shared user: system.uid.system
Permissions: android.permission.RECOVERY, android.permission.SYSTEM_ALERT_WINDOW, android.permission.RECEIVE_BOOT_COMPLETED, android.permission.WRITE_SETTINGS, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.READ_EXTERNAL_STORAGE
receiver: com.zhiying.sourceui.BootBroadcastReceiver
Exported with no component permission (verify intent validation): receiver:com.zhiying.sourceui.BootBroadcastReceiver
JADX status 1; classes/files 1235
Matched patterns {"focus": 449, "remote": 347, "device": 488, "privileged": 116, "jni": 34, "network": 24, "weak_security": 0, "catch": 1258}
URL hostnames schemas.android.com
focus com/mediatek/twoworlds/factory/MtkTvFApiCustom.java:6 private static final int CMD_ID_EX_CUS_CALIBRATEAUTOKEYSTONE = 61725;
focus com/mediatek/twoworlds/factory/MtkTvFApiCustom.java:8 private static final int CMD_ID_EX_CUS_GETAUTOKEYSTONE = 61723;
focus com/mediatek/twoworlds/factory/MtkTvFApiCustom.java:9 private static final int CMD_ID_EX_CUS_GETAUTOKEYSTONEUNCALIB = 61726;
focus com/mediatek/twoworlds/factory/MtkTvFApiCustom.java:12 private static final int CMD_ID_EX_CUS_GETFOCUSCAMERAENABLE = 61721;
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:4 public class MtkTvKeyEventBase {
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:5 public static final java.lang.String TAG = "MtkTvKeyEvent";
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:8 public MtkTvKeyEventBase() {
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:73 public int androidKeyToDFBkey(int i, android.view.KeyEvent keyEvent) {
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:9 private static java.util.Hashtable<java.lang.Integer, java.lang.Integer> gpioHashTable = new java.util.Hashtable<>();
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:13 loadGpioTable();
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:21 private void loadGpioTable() throws java.lang.NumberFormatException {
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:23 int i = java.lang.Integer.parseInt(mtkFApiInformationImp.getIniParameter(path, "BOARD_GPIO_SETTING:BOARD_GPIO_NUM"));
privileged com/mediatek/twoworlds/tv/SystemProperties.java:4 public final class SystemProperties {
privileged com/mediatek/twoworlds/tv/SystemProperties.java:5 private static final java.lang.String TAG = "SystemProperties";
privileged com/mediatek/twoworlds/tv/SystemProperties.java:14 str3 = (java.lang.String) java.lang.Class.forName("android.os.SystemProperties").getDeclaredMethod("get", java.lang.String.class).invoke(null, str);
privileged com/mediatek/twoworlds/tv/SystemProperties.java:24 int iIntValue = ((java.lang.Integer) java.lang.Class.forName("android.os.SystemProperties").getDeclaredMethod("getInt", java.lang.String.class, java.lang.Integer.TYPE).invoke(null, str, java.lang.Integer.valueOf(i))).int
jni com/mediatek/twoworlds/tv/TVNativeCustom.java:14 com.mediatek.twoworlds.tv.TvDebugLog.i(TAG, "Load libcom_mediatek_twoworlds_tv_jni.so start !");
jni com/mediatek/twoworlds/tv/TVNativeCustom.java:15 java.lang.System.loadLibrary("com_mediatek_twoworlds_tv_jni");
jni com/mediatek/twoworlds/tv/TVNativeCustom.java:16 com.mediatek.twoworlds.tv.TvDebugLog.i(TAG, "Load libcom_mediatek_twoworlds_tv_jni.so OK !");
jni com/mediatek/twoworlds/tv/MtkTvAppTVBase.java:5 private static final int JNI_APPTV_SYS_STATUS_AFTER_ASPECT_RATIO_CHG = 9;

### ZYYTBLauncher
Package: com.zhiying.ytb.zy.tv
Android flags: {'allowBackup': 'true', 'usesCleartextTraffic': 'true'}
Shared user: android.uid.system
Permissions: android.permission.INTERNET, android.permission.ACCESS_WIFI_STATE, android.permission.CHANGE_WIFI_MULTICAST_STATE, android.permission.CHANGE_WIFI_STATE, android.permission.ACCESS_NETWORK_STATE, android.permission.BLUETOOTH, android.permission.BLUETOOTH_ADMIN, android.permission.ACCESS_COARSE_LOCATION, android.permission.ACCESS_FINE_LOCATION, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.READ_EXTERNAL_STORAGE, android.permission.REQUEST_INSTALL_PACKAGES, android.permission.KILL_BACKGROUND_PROCESSES, android.permission.FORCE_STOP_PACKAGES, android.permission.SYSTEM_ALERT_WINDOW
service: com.zhiying.ytb.zy.tv.service.MyMuteListenerService, com.zhiying.ytb.zy.tv.download.UpdateService
JADX status 0; classes/files 1
Matched patterns {"focus": 0, "remote": 0, "device": 0, "privileged": 0, "jni": 0, "network": 0, "weak_security": 0, "catch": 0}
URL hostnames 

### NLTvTestingTools
Package: com.newlink.tvtestingtools
Android flags: {'allowBackup': 'false', 'networkSecurityConfig': '@xml/network_security_config'}
Shared user: android.uid.system
Permissions: android.permission.WRITE_SECURE_SETTINGS, android.permission.ACCESS_COARSE_LOCATION, android.permission.ACCESS_FINE_LOCATION, android.permission.BLUETOOTH_ADMIN, android.permission.ACCESS_WIFI_STATE, android.permission.BLUETOOTH, android.permission.CHANGE_WIFI_STATE, android.permission.ACCESS_NETWORK_STATE, android.permission.INTERNET, android.permission.READ_EXTERNAL_STORAGE, android.permission.WRITE_MEDIA_STORAGE, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.MOUNT_UNMOUNT_FILESYSTEMS, android.permission.GET_PACKAGE_SIZE, android.permission.GET_TASKS, com.mstar.android.permissionn.ACCESS_TV_DATA, android.permission.CHANGE_NETWORK_STATE, android.permission.SYSTEM_ALERT_WINDOW, android.permission.RECEIVE_BOOT_COMPLETED, android.permission.RECOVERY, android.permission.WRITE_SETTINGS, android.permission.SHUTDOWN, android.permission.INTERACT_ACROSS_USERS, android.permission.CONNECTIVITY_INTERNAL, android.permission.MASTER_CLEAR, android.permission.SET_WALLPAPER, android.permission.SET_WALLPAPER_HINTS, android.permission.CAMERA
service: com.newlink.tvtestingtools.service.MyMusicService, com.newlink.tvtestingtools.service.RySerialportService, com.newlink.tvtestingtools.service.TestService
Exported with no component permission (verify intent validation): activity:com.newlink.tvtestingtools.acticity.MainActivity_RG, activity:com.newlink.tvtestingtools.acticity.MainActivity_NL, activity:com.newlink.tvtestingtools.acticity.PCBAActivity_MTK, activity:com.newlink.tvtestingtools.acticity.PCBAActivity, service:com.newlink.tvtestingtools.service.RySerialportService

### NLAutoTest
Package: com.newlink.autotest
Android flags: {'allowBackup': 'true'}
Shared user: android.uid.system
Permissions: android.permission.BLUETOOTH_CONNECT, android.permission.BLUETOOTH_SCAN, android.permission.KILL_BACKGROUND_PROCESSES, android.permission.LOCAL_MAC_ADDRESS, android.permission.MODIFY_PHONE_STATE, android.permission.WRITE_SECURE_SETTINGS, android.permission.ACCESS_COARSE_LOCATION, android.permission.ACCESS_FINE_LOCATION, android.permission.BLUETOOTH_ADMIN, android.permission.ACCESS_WIFI_STATE, android.permission.BLUETOOTH, android.permission.CHANGE_WIFI_STATE, android.permission.ACCESS_NETWORK_STATE, android.permission.INTERNET, android.permission.READ_EXTERNAL_STORAGE, android.permission.WRITE_MEDIA_STORAGE, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.MOUNT_UNMOUNT_FILESYSTEMS, android.permission.GET_PACKAGE_SIZE, android.permission.GET_TASKS, com.mstar.android.permissionn.ACCESS_TV_DATA, android.permission.CHANGE_NETWORK_STATE, android.permission.SYSTEM_ALERT_WINDOW, android.permission.RECOVERY, android.permission.WRITE_SETTINGS, android.permission.SHUTDOWN, android.permission.INTERACT_ACROSS_USERS, android.permission.CONNECTIVITY_INTERNAL, android.permission.MASTER_CLEAR, android.permission.SET_WALLPAPER, android.permission.SET_WALLPAPER_HINTS
service: com.newlink.autotest.TestService
Exported with no component permission (verify intent validation): activity:com.newlink.autotest.activity.PCBAActivity_SigmaStar, activity:com.newlink.autotest.activity.PCBAActivity, activity:com.newlink.autotest.activity.PCBAActivity_Hisi, activity:com.newlink.autotest.activity.PCBAActivity_Mtk, activity:com.newlink.autotest.activity.PCBAActivity_QuanZhi

### Arbitratorservice
Package: com.mediatek.tvinputservice.arbitratorservice
Android flags: {}
Shared user: None
Permissions: 
service: com.mediatek.tvinputservice.arbitratorservice.HardwareManagerService
JADX status 0; classes/files 5
Matched patterns {"focus": 0, "remote": 0, "device": 0, "privileged": 0, "jni": 0, "network": 0, "weak_security": 0, "catch": 14}
URL hostnames 

### NewLinkService
Package: com.newlink.service
Android flags: {'allowBackup': 'true', 'networkSecurityConfig': '@xml/network_security_config'}
Shared user: android.uid.system
Permissions: android.permission.ACCESS_COARSE_LOCATION, android.permission.ACCESS_FINE_LOCATION, android.permission.ACCESS_NETWORK_STATE, android.permission.ACCESS_WIFI_STATE, android.permission.CHANGE_WIFI_STATE, android.permission.INTERNET, android.permission.RECEIVE_BOOT_COMPLETED, android.permission.SYSTEM_ALERT_WINDOW, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.READ_EXTERNAL_STORAGE, android.permission.RECOVERY, com.mstar.android.permissionn.ACCESS_TV_DATA, android.permission.ACCESS_WIFI_STATE, android.permission.CHANGE_WIFI_STATE, android.permission.WRITE_SETTINGS, android.permission.WRITE_SECURE_SETTINGS, android.permission.SHUTDOWN, android.permission.INTERACT_ACROSS_USERS, android.permission.CHANGE_NETWORK_STATE, android.permission.CONNECTIVITY_INTERNAL, android.permission.BLUETOOTH, android.permission.BLUETOOTH_ADMIN, android.permission.GET_PACKAGE_SIZE, android.permission.GET_TASKS, android.permission.REQUEST_INSTALL_PACKAGES, android.permission.MASTER_CLEAR, android.permission.SET_WALLPAPER, android.permission.SET_WALLPAPER_HINTS, android.Manifest.permission.INTERACT_ACROSS_USERS, android.permission.RESTART_PACKAGES, android.permission.MOUNT_UNMOUNT_FILESYSTEMS, android.permission.FORCE_STOP_PACKAGES, android.permission.INTERACT_ACROSS_USERS_FULL, android.permis
service: com.newlink.service.service.UsbIntentService, com.newlink.service.service.BootService, com.newlink.service.service.SimpleFactoryRecoveryService, com.newlink.service.service.MyServices, com.newlink.service.service.RegisterService, com.newlink.service.service.BTSpeakerService
receiver: com.newlink.service.receiver.ClearNotificationReceiver, com.newlink.service.receiver.BootCompleteReceiver, com.newlink.service.receiver.WifiBroadcastReceiver, com.newlink.service.receiver.UsbReceiver, com.newlink.service.receiver.NetWorkChangeReceiver, com.newlink.service.receiver.ForceStopPackageReceiver
Exported with no component permission (verify intent validation): activity:com.newlink.service.activity.MacQRCodeActivity, activity:com.newlink.service.activity.USBActivity, activity:com.newlink.service.activity.VideoActivity, service:com.newlink.service.service.BootService, service:com.newlink.service.service.SimpleFactoryRecoveryService, service:com.newlink.service.service.BTSpeakerService, receiver:com.newlink.service.receiver.ClearNotificationReceiver, receiver:com.newlink.service.receiver.BootCompleteReceiver, receiver:com.newlink.service.receiver.WifiBroadcastReceiver, receiver:com.newlink.service.receiver.UsbReceiver
JADX status 1; classes/files 2723
Matched patterns {"focus": 1060, "remote": 366, "device": 484, "privileged": 182, "jni": 34, "network": 4386, "weak_security": 0, "catch": 2039}
URL hostnames schemas.android.com, whois.pconline.com.cn, www.baidu.com, www.newlinksz.com
focus com/mediatek/twoworlds/factory/MtkTvFApiCustom.java:137 public int setFocusMotor(int i, boolean z) {
focus com/mediatek/twoworlds/factory/MtkTvFApiCustom.java:141 public int setFocusMotor(int i, int i2, int i3) {
focus com/mediatek/twoworlds/factory/util/AdvancedPictureSetting.java:8 public static final int FOCUS_MOTOR = 66;
focus com/mediatek/twoworlds/factory/util/AdvancedPictureSetting.java:9 public static final int KEYSTONE_3D_FOV = 48;
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:4 public class MtkTvKeyEventBase {
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:5 public static final java.lang.String TAG = "MtkTvKeyEvent";
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:8 public MtkTvKeyEventBase() {
remote com/mediatek/twoworlds/tv/MtkTvKeyEventBase.java:73 public int androidKeyToDFBkey(int i, android.view.KeyEvent keyEvent) {
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:9 private static java.util.Hashtable<java.lang.Integer, java.lang.Integer> gpioHashTable = new java.util.Hashtable<>();
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:13 loadGpioTable();
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:21 private void loadGpioTable() throws java.lang.NumberFormatException {
device com/mediatek/twoworlds/factory/MtkTvFApiPeripheralBase.java:23 int i = java.lang.Integer.parseInt(mtkFApiInformationImp.getIniParameter(path, "BOARD_GPIO_SETTING:BOARD_GPIO_NUM"));
privileged com/mediatek/twoworlds/tv/SystemProperties.java:4 public final class SystemProperties {
privileged com/mediatek/twoworlds/tv/SystemProperties.java:5 private static final java.lang.String TAG = "SystemProperties";
privileged com/mediatek/twoworlds/tv/SystemProperties.java:14 str3 = (java.lang.String) java.lang.Class.forName("android.os.SystemProperties").getDeclaredMethod("get", java.lang.String.class).invoke(null, str);
privileged com/mediatek/twoworlds/tv/SystemProperties.java:24 int iIntValue = ((java.lang.Integer) java.lang.Class.forName("android.os.SystemProperties").getDeclaredMethod("getInt", java.lang.String.class, java.lang.Integer.TYPE).invoke(null, str, java.lang.Integer.valueOf(i))).int
jni com/mediatek/twoworlds/tv/TVNativeCustom.java:14 com.mediatek.twoworlds.tv.TvDebugLog.i(TAG, "Load libcom_mediatek_twoworlds_tv_jni.so start !");
jni com/mediatek/twoworlds/tv/TVNativeCustom.java:15 java.lang.System.loadLibrary("com_mediatek_twoworlds_tv_jni");
jni com/mediatek/twoworlds/tv/TVNativeCustom.java:16 com.mediatek.twoworlds.tv.TvDebugLog.i(TAG, "Load libcom_mediatek_twoworlds_tv_jni.so OK !");
jni com/mediatek/twoworlds/tv/MtkTvAppTVBase.java:5 private static final int JNI_APPTV_SYS_STATUS_AFTER_ASPECT_RATIO_CHG = 9;

### ZYHBStore
Package: com.zhiying.appstore
Android flags: {'allowBackup': 'true', 'usesCleartextTraffic': 'true'}
Shared user: None
Permissions: android.permission.INTERNET, android.permission.REQUEST_INSTALL_PACKAGES, android.permission.REQUEST_DELETE_PACKAGES, android.permission.READ_EXTERNAL_STORAGE, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.ACCESS_WIFI_STATE, android.permission.CHANGE_WIFI_STATE, android.permission.ACCESS_NETWORK_STATE, android.permission.CHANGE_WIFI_MULTICAST_STATE
provider: androidx.core.content.FileProvider
JADX status 1; classes/files 1608
Matched patterns {"focus": 9, "remote": 294, "device": 19, "privileged": 21, "jni": 0, "network": 75, "weak_security": 0, "catch": 712}
URL hostnames schemas.android.com, www.newlinksz.com
focus com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:10 private static final int MOTOROLA_TIFF_MAGIC_NUMBER = 19789;
focus com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:46 return (i & EXIF_MAGIC_NUMBER) == EXIF_MAGIC_NUMBER || i == MOTOROLA_TIFF_MAGIC_NUMBER || i == INTEL_TIFF_MAGIC_NUMBER;
focus com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:208 if (int16 != MOTOROLA_TIFF_MAGIC_NUMBER && android.util.Log.isLoggable(TAG, 3)) {
focus androidx/core/util/PatternsCompat.java:16 static final java.lang.String IANA_TOP_LEVEL_DOMAINS = "(?:(?:aaa|aarp|abb|abbott|abogado|academy|accenture|accountant|accountants|aco|active|actor|ads|adult|aeg|aero|afl|agency|aig|airforce|airtel|allfinanz|alsace|amica
remote com/zhiying/appstore/view/MyScrollView.java:4 @kotlin.Metadata(bv = {1, 0, 3}, d1 = {"\u0000B\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\n\u0002\u0010\t\n\u0
remote com/zhiying/appstore/view/MyScrollView.java:63 public boolean dispatchKeyEvent(@org.jetbrains.annotations.Nullable android.view.KeyEvent event) {
remote com/zhiying/appstore/view/MyScrollView.java:69 return super.dispatchKeyEvent(event);
remote com/zhiying/appstore/view/MyScrollView.java:74 return super.dispatchKeyEvent(event);
device com/bumptech/glide/load/resource/bitmap/HardwareConfigState.java:5 private static final java.io.File FD_SIZE_LIST = new java.io.File("/proc/self/fd");
device com/bumptech/glide/load/engine/executor/RuntimeCompat.java:5 private static final java.lang.String CPU_LOCATION = "/sys/devices/system/cpu/";
device com/zhiying/appstore/utils/QUtils.java:392 java.lang.String r3 = "cat /sys/class/net/wlan0/address"
device com/zhiying/appstore/utils/QUtils.java:456 java.lang.String r0 = "/sys/class/net/eth0/address"
privileged com/bumptech/glide/load/engine/executor/RuntimeCompat.java:13 int iAvailableProcessors = java.lang.Runtime.getRuntime().availableProcessors();
privileged com/zhiying/appstore/utils/QUtils.java:391 java.lang.Runtime r2 = java.lang.Runtime.getRuntime()     // Catch: java.lang.Exception -> L5c
privileged com/zhiying/appstore/activity/LoadingActivity.java:230 java.lang.reflect.Method method = java.lang.Class.forName("android.os.SystemProperties").getMethod("get", java.lang.String.class, java.lang.String.class);
privileged com/zhiying/appstore/activity/StartActivity.java:147 java.lang.reflect.Method method = java.lang.Class.forName("android.os.SystemProperties").getMethod("get", java.lang.String.class, java.lang.String.class);

### HBCastNew
Package: com.newlink.cast
Android flags: {'allowBackup': 'true'}
Shared user: android.uid.system
Permissions: android.permission.ACCESS_NETWORK_STATE, android.permission.ACCESS_WIFI_STATE, android.permission.BLUETOOTH_ADMIN, android.permission.CHANGE_WIFI_STATE, android.permission.DISABLE_KEYGUARD, android.permission.SYSTEM_ALERT_WINDOW, android.permission.SYSTEM_OVERLAY_WINDOW, android.permission.BROADCAST_STICKY, android.permission.RECEIVE_BOOT_COMPLETED, android.permission.INTERNET, android.permission.READ_EXTERNAL_STORAGE, android.permission.WAKE_LOCK, android.permission.WRITE_EXTERNAL_STORAGE
service: com.newlink.cast.service.AirplayService, com.newlink.cast.service.IOSCableService, com.hzy.platinum.media.service.DLNAService, tv.danmaku.ijk.media.example.services.MediaPlayerService
receiver: com.newlink.cast.receiver.GlobalBroadcastReceiver
provider: com.blankj.utilcode.util.Utils$FileProvider4UtilCode
JADX status 0; classes/files 1
Matched patterns {"focus": 0, "remote": 0, "device": 0, "privileged": 0, "jni": 0, "network": 0, "weak_security": 0, "catch": 0}
URL hostnames 

### MtkNetworkMonitorService
Package: com.mediatek.network
Android flags: {}
Shared user: android.uid.system
Permissions: android.permission.SYSTEM_ALERT_WINDOW, android.permission.ACCESS_NETWORK_STATE, android.permission.DEVICE_POWER, android.permission.RECEIVE_BOOT_COMPLETED
service: .MtkNetworkMonitorService
receiver: .MtkNetworkMonitorReceiver
JADX status 0; classes/files 1
Matched patterns {"focus": 0, "remote": 0, "device": 0, "privileged": 0, "jni": 0, "network": 0, "weak_security": 0, "catch": 0}
URL hostnames 

### PowerService
Package: com.zhiying.powerservice
Android flags: {'allowBackup': 'true'}
Shared user: android.uid.system
Permissions: android.permission.INTERACT_ACROSS_USERS, android.permission.RECEIVE_BOOT_COMPLETED, android.permission.BATTERY_STATS, android.permission.SYSTEM_ALERT_WINDOW, android.permission.SHUTDOWN, android.permission.INTERNET
receiver: com.zhiying.powerservice.ShutdownBroadcastReceiver
Exported with no component permission (verify intent validation): activity:com.zhiying.powerservice.ShutDownActivity
JADX status 0; classes/files 1
Matched patterns {"focus": 0, "remote": 0, "device": 0, "privileged": 0, "jni": 0, "network": 0, "weak_security": 0, "catch": 0}
URL hostnames 

### WTProvision
Package: com.newlink.wtprovision
Android flags: {'allowBackup': 'true', 'networkSecurityConfig': '@xml/network_security_config'}
Shared user: android.uid.system
Permissions: android.permission.KILL_BACKGROUND_PROCESSES, android.permission.SYSTEM_ALERT_WINDOW, android.permission.RECEIVE_BOOT_COMPLETED, android.permission.RECOVERY, android.permission.PACKAGE_USAGE_STATS, com.mstar.android.permissionn.ACCESS_TV_DATA, android.permission.ACCESS_WIFI_STATE, android.permission.CHANGE_WIFI_STATE, android.permission.ACCESS_NETWORK_STATE, android.permission.INTERACT_ACROSS_USERS, android.permission.CHANGE_NETWORK_STATE, android.permission.GET_PACKAGE_SIZE, android.permission.SET_WALLPAPER, android.permission.SET_WALLPAPER_HINTS, android.permission.SET_PREFERRED_APPLICATIONS, android.permission.INTERNET, android.permission.ACCESS_FINE_LOCATION, android.permission.ACCESS_COARSE_LOCATION, android.permission.BLUETOOTH, android.permission.WRITE_SETTINGS, android.permission.INSTALL_LOCATION_PROVIDER, android.permission.INSTALL_PACKAGES, android.permission.BLUETOOTH_ADMIN, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.READ_EXTERNAL_STORAGE, android.permission.REQUEST_INSTALL_PACKAGES, android.permission.BLUETOOTH_PRIVILEGED, android.permission.ACCESS_WIFI_STATE, android.permission.CHANGE_WIFI_STATE, android.permission.OVERRIDE_WIFI_CONFIG, android.permission.WRITE_SECURE_SETTINGS, android.permission.CHANGE_CONFIGURATION, android.permission.FOREGROUND_
service: com.newlink.wtprovision.service.TempService, com.newlink.wtprovision.dlpsetting.MyUtilsService, com.newlink.wtprovision.service.TVService
provider: androidx.core.content.FileProvider
Exported with no component permission (verify intent validation): activity:com.newlink.wtprovision.BluetoothActivity, activity:com.newlink.wtprovision.dlpsetting.DLPEntryActivity, activity:com.newlink.wtprovision.dlpsetting.KeyStoneActivity, activity:com.newlink.wtprovision.InstallLiveApkActivity, service:com.newlink.wtprovision.service.TempService, service:com.newlink.wtprovision.dlpsetting.MyUtilsService, service:com.newlink.wtprovision.service.TVService

### AutoPair
Package: com.newlink.service
Android flags: {'allowBackup': 'true', 'networkSecurityConfig': '@xml/network_security_config'}
Shared user: android.uid.system
Permissions: android.permission.ACCESS_COARSE_LOCATION, android.permission.ACCESS_FINE_LOCATION, android.permission.ACCESS_NETWORK_STATE, android.permission.ACCESS_WIFI_STATE, android.permission.CHANGE_WIFI_STATE, android.permission.INTERNET, android.permission.RECEIVE_BOOT_COMPLETED, android.permission.SYSTEM_ALERT_WINDOW, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.READ_EXTERNAL_STORAGE, android.permission.RECOVERY, com.mstar.android.permissionn.ACCESS_TV_DATA, android.permission.ACCESS_WIFI_STATE, android.permission.CHANGE_WIFI_STATE, android.permission.ACCESS_NETWORK_STATE, android.permission.INTERNET, android.permission.WRITE_SETTINGS, android.permission.WRITE_SECURE_SETTINGS, android.permission.SHUTDOWN, android.permission.INTERACT_ACROSS_USERS, android.permission.CHANGE_NETWORK_STATE, android.permission.CONNECTIVITY_INTERNAL, android.permission.BLUETOOTH, android.permission.BLUETOOTH_ADMIN, android.permission.GET_PACKAGE_SIZE, android.permission.GET_TASKS, android.permission.READ_EXTERNAL_STORAGE, android.permission.SET_WALLPAPER, android.permission.SET_WALLPAPER_HINTS
service: com.newlink.service.service.UsbIntentService, com.newlink.service.service.UsbServer, com.newlink.service.service.BootService, com.newlink.service.service.MyServices
receiver: com.newlink.service.receiver.BootCompleteReceiver, com.newlink.service.receiver.UsbReceiver, com.newlink.service.receiver.NetWorkChangeReceiver
Exported with no component permission (verify intent validation): service:com.newlink.service.service.UsbServer, service:com.newlink.service.service.BootService, receiver:com.newlink.service.receiver.BootCompleteReceiver, receiver:com.newlink.service.receiver.UsbReceiver

### BootAppSplashScreen
Package: com.google.android.boot.appsplashscreen
Android flags: {'allowBackup': 'false'}
Shared user: android.uid.system
Permissions: 

## Native service binaries

### trapezoidServer
Type: /tmp/et32-research/native_trapezoidServer: ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /system/bin/linker, BuildID[md5/uuid]=c56a2965c55d5cbdec4c74f62ca0c646, stripped
Linked: libcutils.so, liblog.so, libutils.so, libbinder.so, libui.so, libEGL.so, libGLESv2.so, libmutils.so, libmi3.so, libiniparser.so, libtrapezoidService.so, libtrapezoidVertexGenerator.so, libutopia.so, libteec.so, libkeystoneCA.so, libc++.so, libc.so, libm.so, libdl.so
- _ZN7android11BnInterfaceINS_24ITrapezoidCorrectServiceEE10onAsBinderEv
- _ZN7android14sp_report_raceEv
- _ZN7android24ITrapezoidCorrectService10descriptorE
- _ZN7android24ITrapezoidCorrectServiceC2Ev
- _ZN7android24ITrapezoidCorrectServiceD0Ev
- _ZN7android24ITrapezoidCorrectServiceD1Ev
- _ZN7android24ITrapezoidCorrectServiceD2Ev
- _ZN7android25BnTrapezoidCorrectService10onTransactEjRKNS_6ParcelEPS1_j
- _ZN7android7BBinder10onTransactEjRKNS_6ParcelEPS1_j
- _ZN7android7BBinder10pingBinderEv
- _ZN7android7BBinder11linkToDeathERKNS_2spINS_7IBinder14DeathRecipientEEEPvj
- _ZN7android7BBinder11localBinderEv
- _ZN7android7BBinder12attachObjectEPKvPvS3_PFvS2_S3_S3_E
- _ZN7android7BBinder12detachObjectEPKv
- _ZN7android7BBinder13unlinkToDeathERKNS_2wpINS_7IBinder14DeathRecipientEEEPvjPS4_
- _ZN7android7BBinder4dumpEiRKNS_6VectorINS_8String16EEE
- _ZN7android7BBinder8transactEjRKNS_6ParcelEPS1_j
- _ZN7android7BBinderC2Ev
- _ZN7android7BBinderD0Ev
- _ZN7android7BBinderD1Ev
- _ZN7android7BBinderD2Ev
- _ZN7android7IBinder11localBinderEv
- _ZN7android7IBinder12remoteBinderEv
- _ZN7android7IBinder19queryLocalInterfaceERKNS_8String16E
- _ZN7android7IBinderD0Ev
- _ZN7android7IBinderD1Ev
- _ZNK7android24ITrapezoidCorrectService22getInterfaceDescriptorEv
- _ZNK7android7BBinder10findObjectEPKv
- _ZNK7android7BBinder13isBinderAliveEv
- _ZNK7android7BBinder22getInterfaceDescriptorEv

### trapezoidTest
Type: /tmp/et32-research/native_trapezoidTest: ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /system/bin/linker, BuildID[md5/uuid]=e414ead4db49a96cc9007dfb60a827d9, stripped
Linked: libtrapezoidClient.so, libcutils.so, libbinder.so, liblog.so, libui.so, libutils.so, libc++.so, libc.so, libm.so, libdl.so
- _ZN7android15TrapezoidClient11setLBoffsetEii
- _ZN7android15TrapezoidClient11setLMoffsetEii
- _ZN7android15TrapezoidClient11setLToffsetEii
- _ZN7android15TrapezoidClient11setMBoffsetEii
- _ZN7android15TrapezoidClient11setMToffsetEii
- _ZN7android15TrapezoidClient11setRBoffsetEii
- _ZN7android15TrapezoidClient11setRMoffsetEii
- _ZN7android15TrapezoidClient11setRToffsetEii
- _ZN7android15TrapezoidClient14setDisplayModeE19E_TRAPEZOID_3D_MODE
- _ZN7android15TrapezoidClient17setVerticalDegreeEf
- _ZN7android15TrapezoidClient19getTrapezoidServiceEv
- _ZN7android15TrapezoidClient19setHorizontalDegreeEf
- _ZN7android15TrapezoidClient19setVideoAspectRatioEf
- _ZN7android15TrapezoidClient20setVideoRotateDegreeEf
- _ZN7android15TrapezoidClient21getTrapezoidAllPointsER18TrapezoidPoint_hal
- _ZN7android15TrapezoidClient21setTrapezoidAllPointsE18TrapezoidPoint_hal
- _ZN7android15TrapezoidClient21setVideoTrapezoidStopEi
- _ZN7android15TrapezoidClient22saveTrapezoidAllPointsEv
- _ZN7android15TrapezoidClient22setVideoTrapezoidStartEi
- _ZN7android15TrapezoidClient23setTrapezoidCorrectTypeE24E_TRAPEZOID_CORRECT_TYPE
- _ZN7android15TrapezoidClient8dumpInfoEv
- libtrapezoidClient.so
- libbinder.so
- Trapezoid test begin..........
- vendor.mstar.trapezoid.enable.vndbinder
- /dev/vndbinder
- Trapezoid without vndbinder.If you want with vndbinder,before start trapezoid,please set prop of %s with 1
- Trapezoid:: getTrapezoidService fail!
- vendor.mstar.trapezoid.allpointsset
- %s error!!! Trapezoid Points offset get value not equal with set value!!!!!!

### trapezoid_save.sh
Type: /tmp/et32-research/native_trapezoid_save.sh: a /vendor/bin/sh script, ASCII text executable
Linked: 
- /vendor/bin/echo %%%%%%%%/data/trapezoid/ not trapezoidcorrect_points_offset.ini
- if [ ! -s /data/trapezoid/trapezoidcorrect_points_offset.ini ] ; then
-     /vendor/bin/echo %%%%%%%%/data/trapezoid/ not p2p_supplicant.conf
-     /vendor/bin/cp -a /vendor/etc/trapezoidcorrect_points_offset.ini /data/trapezoid/trapezoidcorrect_points_offset.ini
-     /vendor/bin/chmod 777 /data/trapezoid/trapezoidcorrect_points_offset.ini

### boa
Type: /tmp/et32-research/native_boa: ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /system/bin/linker, BuildID[md5/uuid]=da851f9a49a8d2f7e9ce846e5309aadf, stripped
Linked: libcutils.so, libc++.so, libc.so, libm.so, libdl.so
- application/x-httpd-cgi
- /dev/null
- can't open /dev/null
- can't dup2 /dev/null to STDIN_FILENO
- can't dup2 /dev/null to STDOUT_FILENO
- unable to bind
- unable to listen
- SERVER_PORT
- REMOTE_ADDR
- REMOTE_PORT
- server does not support internal redirection: "%s"
- HTTP/1.0 200 OK-GUNZIP
- http://%s:%d%s/
- http://%s%s/
- HTTP/1.0 200 OK
- mime_hashtable has %d total entries
- HTTP/0.9
- HTTP/%u.%u
- bogus HTTP version: "%s"
- HTTP/1.0 301 Moved Permanently
- HTTP/1.0 302 Moved Temporarily
- HTTP/1.0 304 Not Modified
- HTTP/1.0 400 Bad Request
- HTTP/1.0 401 Unauthorized
- HTTP/1.0 403 Forbidden
- HTTP/1.0 404 Not Found
- HTTP/1.0 500 Server Error
- HTTP/1.0 501 Not Implemented
- POST to non-script is not supported in Boa.
- HTTP/1.0 502 Bad Gateway

### cmdsrv
Type: /tmp/et32-research/native_cmdsrv: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), statically linked, for GNU/Linux 2.6.16, stripped
Linked: 
- [1;33;40m cannot bind server socket.
- [1;33;40m cannot listen the client connect request
- ############Create binderThreadId is fail############
- [1;33;40m#########Server.ZM_StopBinder########
- /dev/full
- /dev/null
- /dev/tty
- /proc/self/maps
- (size from="%zu" to="%zu" total="%zu" count="%zu"/>
- (unsorted from="%zu" to="%zu" total="%zu" count="%zu"/>
- (total type="fast" count="%zu" size="%zu"/>
- (total type="rest" count="%zu" size="%zu"/>
- (aspace type="total" size="%zu"/>
- Total (incl. mmap):
- (total type="fast" count="%zu" size="%zu"/>
- (total type="rest" count="%zu" size="%zu"/>
- (aspace type="total" size="%zu"/>
- /proc/sys/kernel/rtsig-max
- /proc/sys/kernel/ngroups_max
- /dev/log
- /dev/console
- /proc/meminfo
- /sys/devices/system/cpu/online
- /proc/stat
- /proc/cpuinfo
- /sys/devices/system/cpu
- MemTotal: %ld kB
- LD_BIND_NOW
- LD_BIND_NOT
- /proc/sys/kernel/osrelease

### MtkRmServer
Type: /tmp/et32-research/native_MtkRmServer: ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /system/bin/linker, BuildID[md5/uuid]=0988086c1856966cf8833f194d7499b4, stripped
Linked: liblog.so, libutils.so, libcutils.so, libmtal.so, libc++.so, libc.so, libm.so, libdl.so
- (%s, %s, #%d) BIND ERRRRR, SOCK [%d] errno:%d
- mtkrm_ipc_listen_thd
- not support right now.
- (%s)Resource(%s) is Need(%d) more than Total Count (%d)!
- The Amount Type Resource don't support partial release!

### gpio_spi_read
Type: /tmp/et32-research/native_gpio_spi_read: ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /system/bin/linker, BuildID[md5/uuid]=d27e15a68d7642fddb6f7725e60ba026, stripped
Linked: libbinder.so, libbase.so, liblog.so, libutils.so, libcutils.so, vendor.mediatek.tv.Mm.Mm.mtktvfapicustom@1.0.so, libmi3.so, libc++.so, libc.so, libm.so, libdl.so
- libbinder.so
- cs_gpio_pad  scl_gpio_pad  sda_gpio_pad 
- SPI_CS: GPIO_PAD_%u
- SPI_CLK: GPIO_PAD_%u
- SPI_SDA: GPIO_PAD_%u
- gpiospi init failed!
- gpio_pad_%u is opened
- /sys/class/gpio/gpio%u/%s
- unsupported register class
- unsupported arm register
- gpiospi read failed!
- write to gpio direction failed
- write to gpio value failed
- read from gpio value failed
- rewind gpio value failed

### gpio_spi_write
Type: /tmp/et32-research/native_gpio_spi_write: ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /system/bin/linker, BuildID[md5/uuid]=41b5b6de1621260ffff8f29edc81687d, stripped
Linked: libbinder.so, libbase.so, liblog.so, libutils.so, libcutils.so, vendor.mediatek.tv.Mm.Mm.mtktvfapicustom@1.0.so, libmi3.so, libc++.so, libc.so, libm.so, libdl.so
- libbinder.so
- cs_gpio_pad  scl_gpio_pad  sda_gpio_pad 
- SPI_CS: GPIO_PAD_%u
- SPI_CLK: GPIO_PAD_%u
- SPI_SDA: GPIO_PAD_%u
- gpiospi init failed!
- gpio_pad_%u is opened
- /sys/class/gpio/gpio%u/%s
- unsupported register class
- unsupported arm register
- gpiospi write success!
- gpiospi write failed!
- write to gpio direction failed
- write to gpio value failed
