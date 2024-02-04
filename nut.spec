#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: 750e50d
#
# Source0 file verified with key 0x42061031267D11B1 (jimklimov@gmail.com)
#
Name     : nut
Version  : 2.8.1
Release  : 6
URL      : https://networkupstools.org/source/2.8/nut-2.8.1.tar.gz
Source0  : https://networkupstools.org/source/2.8/nut-2.8.1.tar.gz
Source1  : https://networkupstools.org/source/2.8/nut-2.8.1.tar.gz.sig
Summary  : UPS monitoring with Network UPS Tools
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: nut-bin = %{version}-%{release}
Requires: nut-config = %{version}-%{release}
Requires: nut-data = %{version}-%{release}
Requires: nut-lib = %{version}-%{release}
Requires: nut-libexec = %{version}-%{release}
Requires: nut-license = %{version}-%{release}
Requires: nut-man = %{version}-%{release}
Requires: nut-python = %{version}-%{release}
Requires: nut-python3 = %{version}-%{release}
Requires: nut-services = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : aspell-dev
BuildRequires : buildreq-configure
BuildRequires : cppcheck
BuildRequires : i2c-tools-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : openssl-dev
BuildRequires : pkgconfig(avahi-core)
BuildRequires : pkgconfig(cppunit)
BuildRequires : pkgconfig(gdlib)
BuildRequires : pkgconfig(libfreeipmi)
BuildRequires : pkgconfig(libgpiod)
BuildRequires : pkgconfig(libmodbus)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(neon)
BuildRequires : pkgconfig(netsnmp)
BuildRequires : systemd-dev
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Allow-nut-scanner-to-match-versioned-libs.patch

%description


%package bin
Summary: bin components for the nut package.
Group: Binaries
Requires: nut-data = %{version}-%{release}
Requires: nut-libexec = %{version}-%{release}
Requires: nut-config = %{version}-%{release}
Requires: nut-license = %{version}-%{release}
Requires: nut-services = %{version}-%{release}

%description bin
bin components for the nut package.


%package config
Summary: config components for the nut package.
Group: Default

%description config
config components for the nut package.


%package data
Summary: data components for the nut package.
Group: Data

%description data
data components for the nut package.


%package dev
Summary: dev components for the nut package.
Group: Development
Requires: nut-lib = %{version}-%{release}
Requires: nut-bin = %{version}-%{release}
Requires: nut-data = %{version}-%{release}
Provides: nut-devel = %{version}-%{release}
Requires: nut = %{version}-%{release}

%description dev
dev components for the nut package.


%package extras-cgi
Summary: extras-cgi components for the nut package.
Group: Default

%description extras-cgi
extras-cgi components for the nut package.


%package lib
Summary: lib components for the nut package.
Group: Libraries
Requires: nut-data = %{version}-%{release}
Requires: nut-libexec = %{version}-%{release}
Requires: nut-license = %{version}-%{release}

%description lib
lib components for the nut package.


%package libexec
Summary: libexec components for the nut package.
Group: Default
Requires: nut-config = %{version}-%{release}
Requires: nut-license = %{version}-%{release}

%description libexec
libexec components for the nut package.


%package license
Summary: license components for the nut package.
Group: Default

%description license
license components for the nut package.


%package man
Summary: man components for the nut package.
Group: Default

%description man
man components for the nut package.


%package python
Summary: python components for the nut package.
Group: Default
Requires: nut-python3 = %{version}-%{release}

%description python
python components for the nut package.


%package python3
Summary: python3 components for the nut package.
Group: Default
Requires: python3-core

%description python3
python3 components for the nut package.


%package services
Summary: services components for the nut package.
Group: Systemd services
Requires: systemd

%description services
services components for the nut package.


%prep
%setup -q -n nut-2.8.1
cd %{_builddir}/nut-2.8.1
%patch -P 1 -p1
pushd ..
cp -a nut-2.8.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707089381
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static --datadir=/usr/share/nut \
--includedir=/usr/include/nut \
--sysconfdir=/etc/ups \
--with-all \
--with-cgi \
--with-cgipath=/usr/share/nut/cgi-bin \
--with-drvpath=/usr/libexec/nut \
--with-htmlpath=/usr/share/nut/html \
--with-statepath=/var/lib/ups \
--with-systemdshutdowndir=/usr/lib/systemd/system-shutdown \
--with-udev-dir=/usr/lib/udev \
--without-gpio \
--without-powerman \
--without-wrap \
--with-user=_nut \
--with-group=_nut
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --datadir=/usr/share/nut \
--includedir=/usr/include/nut \
--sysconfdir=/etc/ups \
--with-all \
--with-cgi \
--with-cgipath=/usr/share/nut/cgi-bin \
--with-drvpath=/usr/libexec/nut \
--with-htmlpath=/usr/share/nut/html \
--with-statepath=/var/lib/ups \
--with-systemdshutdowndir=/usr/lib/systemd/system-shutdown \
--with-udev-dir=/usr/lib/udev \
--without-gpio \
--without-powerman \
--without-wrap \
--with-user=_nut \
--with-group=_nut
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707089381
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nut
cp %{_builddir}/nut-%{version}/LICENSE-GPL2 %{buildroot}/usr/share/package-licenses/nut/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/nut-%{version}/LICENSE-GPL3 %{buildroot}/usr/share/package-licenses/nut/842745cb706f8f2126506f544492f7a80dbe29b3 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
## install_append content
# This isn't a UPS driver, but keep it in the nut namespace
mv %{buildroot}/usr/libexec/sockdebug %{buildroot}/usr/libexec/nut/sockdebug
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system-shutdown/nutshutdown

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/nut-scanner
/V3/usr/bin/upsc
/V3/usr/bin/upscmd
/V3/usr/bin/upsd
/V3/usr/bin/upsdrvctl
/V3/usr/bin/upslog
/V3/usr/bin/upsmon
/V3/usr/bin/upsrw
/V3/usr/bin/upssched
/usr/bin/nut-scanner
/usr/bin/upsc
/usr/bin/upscmd
/usr/bin/upsd
/usr/bin/upsdrvctl
/usr/bin/upsdrvsvcctl
/usr/bin/upslog
/usr/bin/upsmon
/usr/bin/upsrw
/usr/bin/upssched
/usr/bin/upssched-cmd

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/nut-common-tmpfiles.conf
/usr/lib/udev/rules.d/52-nut-ipmipsu.rules
/usr/lib/udev/rules.d/62-nut-usbups.rules

%files data
%defattr(-,root,root,-)
/usr/share/nut/cmdvartab
/usr/share/nut/driver.list

%files dev
%defattr(-,root,root,-)
/usr/include/nut/nut-scan.h
/usr/include/nut/nutclient.h
/usr/include/nut/nutclientmem.h
/usr/include/nut/nutscan-device.h
/usr/include/nut/nutscan-init.h
/usr/include/nut/nutscan-ip.h
/usr/include/nut/nutscan-serial.h
/usr/include/nut/parseconf.h
/usr/include/nut/upsclient.h
/usr/lib64/libnutclient.so
/usr/lib64/libnutclientstub.so
/usr/lib64/libnutscan.so
/usr/lib64/libupsclient.so
/usr/lib64/pkgconfig/libnutclient.pc
/usr/lib64/pkgconfig/libnutclientstub.pc
/usr/lib64/pkgconfig/libnutscan.pc
/usr/lib64/pkgconfig/libupsclient.pc
/usr/share/man/man3/libnutclient.3
/usr/share/man/man3/libnutclient_commands.3
/usr/share/man/man3/libnutclient_devices.3
/usr/share/man/man3/libnutclient_general.3
/usr/share/man/man3/libnutclient_misc.3
/usr/share/man/man3/libnutclient_tcp.3
/usr/share/man/man3/libnutclient_variables.3
/usr/share/man/man3/nutclient_authenticate.3
/usr/share/man/man3/nutclient_destroy.3
/usr/share/man/man3/nutclient_device_forced_shutdown.3
/usr/share/man/man3/nutclient_device_login.3
/usr/share/man/man3/nutclient_device_master.3
/usr/share/man/man3/nutclient_execute_device_command.3
/usr/share/man/man3/nutclient_get_device_command_description.3
/usr/share/man/man3/nutclient_get_device_commands.3
/usr/share/man/man3/nutclient_get_device_description.3
/usr/share/man/man3/nutclient_get_device_num_logins.3
/usr/share/man/man3/nutclient_get_device_rw_variables.3
/usr/share/man/man3/nutclient_get_device_variable_description.3
/usr/share/man/man3/nutclient_get_device_variable_values.3
/usr/share/man/man3/nutclient_get_device_variables.3
/usr/share/man/man3/nutclient_get_devices.3
/usr/share/man/man3/nutclient_has_device.3
/usr/share/man/man3/nutclient_has_device_command.3
/usr/share/man/man3/nutclient_has_device_variable.3
/usr/share/man/man3/nutclient_logout.3
/usr/share/man/man3/nutclient_set_device_variable_value.3
/usr/share/man/man3/nutclient_set_device_variable_values.3
/usr/share/man/man3/nutclient_tcp_create_client.3
/usr/share/man/man3/nutclient_tcp_disconnect.3
/usr/share/man/man3/nutclient_tcp_get_timeout.3
/usr/share/man/man3/nutclient_tcp_is_connected.3
/usr/share/man/man3/nutclient_tcp_reconnect.3
/usr/share/man/man3/nutclient_tcp_set_timeout.3
/usr/share/man/man3/nutscan.3
/usr/share/man/man3/nutscan_add_device_to_device.3
/usr/share/man/man3/nutscan_add_option_to_device.3
/usr/share/man/man3/nutscan_cidr_to_ip.3
/usr/share/man/man3/nutscan_display_parsable.3
/usr/share/man/man3/nutscan_display_sanity_check.3
/usr/share/man/man3/nutscan_display_sanity_check_serial.3
/usr/share/man/man3/nutscan_display_ups_conf.3
/usr/share/man/man3/nutscan_display_ups_conf_with_sanity_check.3
/usr/share/man/man3/nutscan_free_device.3
/usr/share/man/man3/nutscan_get_serial_ports_list.3
/usr/share/man/man3/nutscan_init.3
/usr/share/man/man3/nutscan_new_device.3
/usr/share/man/man3/nutscan_scan_avahi.3
/usr/share/man/man3/nutscan_scan_eaton_serial.3
/usr/share/man/man3/nutscan_scan_ipmi.3
/usr/share/man/man3/nutscan_scan_nut.3
/usr/share/man/man3/nutscan_scan_snmp.3
/usr/share/man/man3/nutscan_scan_usb.3
/usr/share/man/man3/nutscan_scan_xml_http_range.3
/usr/share/man/man3/upscli_add_host_cert.3
/usr/share/man/man3/upscli_cleanup.3
/usr/share/man/man3/upscli_connect.3
/usr/share/man/man3/upscli_disconnect.3
/usr/share/man/man3/upscli_fd.3
/usr/share/man/man3/upscli_get.3
/usr/share/man/man3/upscli_init.3
/usr/share/man/man3/upscli_list_next.3
/usr/share/man/man3/upscli_list_start.3
/usr/share/man/man3/upscli_readline.3
/usr/share/man/man3/upscli_readline_timeout.3
/usr/share/man/man3/upscli_sendline.3
/usr/share/man/man3/upscli_sendline_timeout.3
/usr/share/man/man3/upscli_splitaddr.3
/usr/share/man/man3/upscli_splitname.3
/usr/share/man/man3/upscli_ssl.3
/usr/share/man/man3/upscli_strerror.3
/usr/share/man/man3/upscli_upserror.3
/usr/share/man/man3/upsclient.3

%files extras-cgi
%defattr(-,root,root,-)
/V3/usr/share/nut/cgi-bin/*
/usr/share/nut/cgi-bin/*
/usr/share/nut/html/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libnutclient.so.2.0.2
/V3/usr/lib64/libnutclientstub.so.1.0.1
/V3/usr/lib64/libnutscan.so.2.0.2
/V3/usr/lib64/libupsclient.so.6.0.1
/usr/lib64/libnutclient.so.2
/usr/lib64/libnutclient.so.2.0.2
/usr/lib64/libnutclientstub.so.1
/usr/lib64/libnutclientstub.so.1.0.1
/usr/lib64/libnutscan.so.2
/usr/lib64/libnutscan.so.2.0.2
/usr/lib64/libupsclient.so.6
/usr/lib64/libupsclient.so.6.0.1

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/nut/adelsystem_cbi
/V3/usr/libexec/nut/al175
/V3/usr/libexec/nut/apc_modbus
/V3/usr/libexec/nut/apcsmart
/V3/usr/libexec/nut/apcsmart-old
/V3/usr/libexec/nut/apcupsd-ups
/V3/usr/libexec/nut/asem
/V3/usr/libexec/nut/bcmxcp
/V3/usr/libexec/nut/bcmxcp_usb
/V3/usr/libexec/nut/belkin
/V3/usr/libexec/nut/belkinunv
/V3/usr/libexec/nut/bestfcom
/V3/usr/libexec/nut/bestfortress
/V3/usr/libexec/nut/bestuferrups
/V3/usr/libexec/nut/bestups
/V3/usr/libexec/nut/blazer_ser
/V3/usr/libexec/nut/blazer_usb
/V3/usr/libexec/nut/clone
/V3/usr/libexec/nut/clone-outlet
/V3/usr/libexec/nut/dummy-ups
/V3/usr/libexec/nut/etapro
/V3/usr/libexec/nut/everups
/V3/usr/libexec/nut/gamatronic
/V3/usr/libexec/nut/generic_modbus
/V3/usr/libexec/nut/genericups
/V3/usr/libexec/nut/huawei-ups2000
/V3/usr/libexec/nut/isbmex
/V3/usr/libexec/nut/ivtscd
/V3/usr/libexec/nut/liebert
/V3/usr/libexec/nut/liebert-esp2
/V3/usr/libexec/nut/masterguard
/V3/usr/libexec/nut/metasys
/V3/usr/libexec/nut/mge-shut
/V3/usr/libexec/nut/mge-utalk
/V3/usr/libexec/nut/microdowell
/V3/usr/libexec/nut/microsol-apc
/V3/usr/libexec/nut/netxml-ups
/V3/usr/libexec/nut/nut-ipmipsu
/V3/usr/libexec/nut/nutdrv_atcl_usb
/V3/usr/libexec/nut/nutdrv_qx
/V3/usr/libexec/nut/nutdrv_siemens-sitop
/V3/usr/libexec/nut/oneac
/V3/usr/libexec/nut/optiups
/V3/usr/libexec/nut/phoenixcontact_modbus
/V3/usr/libexec/nut/pijuice
/V3/usr/libexec/nut/powercom
/V3/usr/libexec/nut/powerpanel
/V3/usr/libexec/nut/rhino
/V3/usr/libexec/nut/richcomm_usb
/V3/usr/libexec/nut/riello_ser
/V3/usr/libexec/nut/riello_usb
/V3/usr/libexec/nut/safenet
/V3/usr/libexec/nut/skel
/V3/usr/libexec/nut/sms_ser
/V3/usr/libexec/nut/snmp-ups
/V3/usr/libexec/nut/socomec_jbus
/V3/usr/libexec/nut/solis
/V3/usr/libexec/nut/tripplite
/V3/usr/libexec/nut/tripplite_usb
/V3/usr/libexec/nut/tripplitesu
/V3/usr/libexec/nut/upscode2
/V3/usr/libexec/nut/usbhid-ups
/V3/usr/libexec/nut/victronups
/V3/usr/libexec/sockdebug
/usr/libexec/nut-driver-enumerator.sh
/usr/libexec/nut/adelsystem_cbi
/usr/libexec/nut/al175
/usr/libexec/nut/apc_modbus
/usr/libexec/nut/apcsmart
/usr/libexec/nut/apcsmart-old
/usr/libexec/nut/apcupsd-ups
/usr/libexec/nut/asem
/usr/libexec/nut/bcmxcp
/usr/libexec/nut/bcmxcp_usb
/usr/libexec/nut/belkin
/usr/libexec/nut/belkinunv
/usr/libexec/nut/bestfcom
/usr/libexec/nut/bestfortress
/usr/libexec/nut/bestuferrups
/usr/libexec/nut/bestups
/usr/libexec/nut/blazer_ser
/usr/libexec/nut/blazer_usb
/usr/libexec/nut/clone
/usr/libexec/nut/clone-outlet
/usr/libexec/nut/dummy-ups
/usr/libexec/nut/etapro
/usr/libexec/nut/everups
/usr/libexec/nut/gamatronic
/usr/libexec/nut/generic_modbus
/usr/libexec/nut/genericups
/usr/libexec/nut/huawei-ups2000
/usr/libexec/nut/isbmex
/usr/libexec/nut/ivtscd
/usr/libexec/nut/liebert
/usr/libexec/nut/liebert-esp2
/usr/libexec/nut/masterguard
/usr/libexec/nut/metasys
/usr/libexec/nut/mge-shut
/usr/libexec/nut/mge-utalk
/usr/libexec/nut/microdowell
/usr/libexec/nut/microsol-apc
/usr/libexec/nut/netxml-ups
/usr/libexec/nut/nut-ipmipsu
/usr/libexec/nut/nutdrv_atcl_usb
/usr/libexec/nut/nutdrv_qx
/usr/libexec/nut/nutdrv_siemens-sitop
/usr/libexec/nut/oneac
/usr/libexec/nut/optiups
/usr/libexec/nut/phoenixcontact_modbus
/usr/libexec/nut/pijuice
/usr/libexec/nut/powercom
/usr/libexec/nut/powerpanel
/usr/libexec/nut/rhino
/usr/libexec/nut/richcomm_usb
/usr/libexec/nut/riello_ser
/usr/libexec/nut/riello_usb
/usr/libexec/nut/safenet
/usr/libexec/nut/skel
/usr/libexec/nut/sms_ser
/usr/libexec/nut/snmp-ups
/usr/libexec/nut/sockdebug
/usr/libexec/nut/socomec_jbus
/usr/libexec/nut/solis
/usr/libexec/nut/tripplite
/usr/libexec/nut/tripplite_usb
/usr/libexec/nut/tripplitesu
/usr/libexec/nut/upscode2
/usr/libexec/nut/usbhid-ups
/usr/libexec/nut/victronups

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nut/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/nut/842745cb706f8f2126506f544492f7a80dbe29b3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/hosts.conf.5
/usr/share/man/man5/nut.conf.5
/usr/share/man/man5/ups.conf.5
/usr/share/man/man5/upsd.conf.5
/usr/share/man/man5/upsd.users.5
/usr/share/man/man5/upsmon.conf.5
/usr/share/man/man5/upssched.conf.5
/usr/share/man/man5/upsset.conf.5
/usr/share/man/man5/upsstats.html.5
/usr/share/man/man8/adelsystem_cbi.8
/usr/share/man/man8/al175.8
/usr/share/man/man8/apc_modbus.8
/usr/share/man/man8/apcsmart-old.8
/usr/share/man/man8/apcsmart.8
/usr/share/man/man8/apcupsd-ups.8
/usr/share/man/man8/asem.8
/usr/share/man/man8/bcmxcp.8
/usr/share/man/man8/bcmxcp_usb.8
/usr/share/man/man8/belkin.8
/usr/share/man/man8/belkinunv.8
/usr/share/man/man8/bestfcom.8
/usr/share/man/man8/bestfortress.8
/usr/share/man/man8/bestuferrups.8
/usr/share/man/man8/bestups.8
/usr/share/man/man8/blazer_ser.8
/usr/share/man/man8/blazer_usb.8
/usr/share/man/man8/clone.8
/usr/share/man/man8/dummy-ups.8
/usr/share/man/man8/etapro.8
/usr/share/man/man8/everups.8
/usr/share/man/man8/gamatronic.8
/usr/share/man/man8/generic_modbus.8
/usr/share/man/man8/genericups.8
/usr/share/man/man8/huawei-ups2000.8
/usr/share/man/man8/isbmex.8
/usr/share/man/man8/ivtscd.8
/usr/share/man/man8/liebert-esp2.8
/usr/share/man/man8/liebert.8
/usr/share/man/man8/masterguard.8
/usr/share/man/man8/metasys.8
/usr/share/man/man8/mge-shut.8
/usr/share/man/man8/mge-utalk.8
/usr/share/man/man8/microdowell.8
/usr/share/man/man8/microsol-apc.8
/usr/share/man/man8/netxml-ups.8
/usr/share/man/man8/nut-driver-enumerator.8
/usr/share/man/man8/nut-ipmipsu.8
/usr/share/man/man8/nut-recorder.8
/usr/share/man/man8/nut-scanner.8
/usr/share/man/man8/nutdrv_atcl_usb.8
/usr/share/man/man8/nutdrv_qx.8
/usr/share/man/man8/nutdrv_siemens_sitop.8
/usr/share/man/man8/nutupsdrv.8
/usr/share/man/man8/oneac.8
/usr/share/man/man8/optiups.8
/usr/share/man/man8/phoenixcontact_modbus.8
/usr/share/man/man8/pijuice.8
/usr/share/man/man8/powercom.8
/usr/share/man/man8/powerpanel.8
/usr/share/man/man8/rhino.8
/usr/share/man/man8/richcomm_usb.8
/usr/share/man/man8/riello_ser.8
/usr/share/man/man8/riello_usb.8
/usr/share/man/man8/safenet.8
/usr/share/man/man8/sms_ser.8
/usr/share/man/man8/snmp-ups.8
/usr/share/man/man8/sockdebug.8
/usr/share/man/man8/socomec_jbus.8
/usr/share/man/man8/solis.8
/usr/share/man/man8/tripplite.8
/usr/share/man/man8/tripplite_usb.8
/usr/share/man/man8/tripplitesu.8
/usr/share/man/man8/upsc.8
/usr/share/man/man8/upscmd.8
/usr/share/man/man8/upscode2.8
/usr/share/man/man8/upsd.8
/usr/share/man/man8/upsdrvctl.8
/usr/share/man/man8/upsdrvsvcctl.8
/usr/share/man/man8/upsimage.cgi.8
/usr/share/man/man8/upslog.8
/usr/share/man/man8/upsmon.8
/usr/share/man/man8/upsrw.8
/usr/share/man/man8/upssched.8
/usr/share/man/man8/upsset.cgi.8
/usr/share/man/man8/upsstats.cgi.8
/usr/share/man/man8/usbhid-ups.8
/usr/share/man/man8/victronups.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/nut-driver-enumerator.path
/usr/lib/systemd/system/nut-driver-enumerator.service
/usr/lib/systemd/system/nut-driver.target
/usr/lib/systemd/system/nut-driver@.service
/usr/lib/systemd/system/nut-monitor.service
/usr/lib/systemd/system/nut-server.service
/usr/lib/systemd/system/nut.target
