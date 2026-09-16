#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)

from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/infinix/X6739',
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
    'hardware/mediatek/libaedv',
    'hardware/transsion',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    ('vendor/bin/hw/android.hardware.gnss-service.mediatek', 'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),
    ('vendor/bin/hw/vendor.mediatek.hardware.pq@2.2-service', 'vendor/lib64/hw/vendor.mediatek.hardware.pq@2.15-impl.so'): blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so')
        .replace_needed('libutils.so', 'libutils-v31.so'),
    'vendor/etc/init/android.hardware.media.c2@1.2-mediatek.rc': blob_fixup()
        .add_line_if_missing('    interface android.hardware.media.c2@1.0::IComponentStore default')
        .add_line_if_missing('    interface android.hardware.media.c2@1.1::IComponentStore default')
        .add_line_if_missing('    interface android.hardware.media.c2@1.2::IComponentStore default')
        .regex_replace('@1.2-mediatek', '@1.2-mediatek-64b'),
    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so')
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so'),
    ('vendor/bin/mnld', 'vendor/lib64/libaalservice.so', 'vendor/lib64/libcam.utils.sensorprovider.so', 'vendor/lib64/hw/android.hardware.sensors@2.X-subhal-mediatek.so'): blob_fixup()
        .add_needed('android.hardware.sensors@1.0-convert-shared.so'),
    'vendor/lib64/hw/audio.primary.mt6893.so': blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so')
        .replace_needed('libutils.so', 'libutils-v31.so')
        .replace_needed('libalsautils.so', 'libalsautils-v31.so'),
    ('system_ext/etc/init/init.vtservice.rc', 'vendor/etc/init/android.hardware.neuralnetworks@1.3-service-mtk-neuron.rc'): blob_fixup()
        .regex_replace('start', 'enable'),
    'vendor/etc/vintf/manifest/manifest_media_c2_V1_2_default.xml': blob_fixup()
        .regex_replace('1.1', '1.2'),
    ('vendor/bin/hw/android.hardware.usb@1.2-service-mediatekv2', 'vendor/bin/hw/android.hardware.neuralnetworks@1.3-service-mtk-neuron', 'vendor/bin/nfcstackp-vendor', 'vendor/lib64/libnvram.so', 'vendor/lib64/libsysenv.so', 'vendor/lib64/libtflite_mtk.so'): blob_fixup()
        .add_needed('libbase_shim.so'),
    'vendor/lib64/hw/hwcomposer.mt6893.so': blob_fixup()
        .add_needed('libprocessgroup_shim.so'),
    ('vendor/lib64/libtranssion_bodybeauty.so', 'vendor/lib64/mt6789/libeffect_hal.so', 'vendor/lib64/libsegmentionPre.so', 'vendor/lib64/libMegviiHum.so'): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_createFromHandle')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_getNativeHandle')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_lockPlanes')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    'vendor/bin/hw/mtkfusionrild': blob_fixup()
        .add_needed('libutils-v31.so'),
    'vendor/lib64/hw/mt6789/vendor.mediatek.hardware.camera.isphal@1.0-impl.so': blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v31.so')
        .replace_needed('libbinder.so', 'libbinder-v31.so')
        .replace_needed('libutils.so', 'libutils-v31.so'),
    'vendor/bin/hw/camerahalserver': blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v31.so')
        .replace_needed('libbinder.so', 'libbinder-v31.so')
        .replace_needed('libutils.so', 'libutils-v31.so')
        .add_needed('libhidlbase_shim.so')
        .add_needed('libprocessgroup_shim.so'),
    'vendor/lib64/hw/android.hardware.camera.provider@2.6-impl-mediatek.so': blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v31.so')
        .replace_needed('libutils.so', 'libutils-v31.so')
        .add_needed('libcamera_metadata_shim.so'),
    ('vendor/lib64/lib3a.ae.stat.so', 'vendor/lib64/lib3a.flash.so', 'vendor/lib64/lib3a.sensors.color.so', 'vendor/lib64/lib3a.sensors.flicker.so', 'vendor/lib64/libaaa_ltm.so', 'vendor/lib64/libSQLiteModule_VER_ALL.so'): blob_fixup()
        .add_needed('liblog.so'),
    'vendor/lib64/mt6893/libmnl_mtk.so': blob_fixup()
        .add_needed('libcutils.so'),
    'vendor/etc/libnfc-hal-st.conf': blob_fixup()
        .regex_replace('STNFC_FW_DEBUG_ENABLED=1', 'STNFC_FW_DEBUG_ENABLED=0'),
    'vendor/lib64/librt_extamp_intf.so': blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
     ('vendor/lib64/libcodec2_mtk_venc.so', 'vendor/lib64/libcodec2_mtk_vdec.so'): blob_fixup()
        .replace_needed('libformatter.so', 'libformatter_mtk.so'),
     ('vendor/bin/mnld', 'vendor/lib64/libwpfa.so'): blob_fixup()
        .replace_needed('libmnl.so', 'libmnl_mtk.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'X6739',
    'infinix',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
